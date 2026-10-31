#!/usr/bin/env python3
"""Sprawdza odnośniki w plikach Markdown repozytorium.

Domyślnie: odnośniki wewnętrzne (czy plik istnieje, czy kotwica #nagłówek istnieje).
Z opcją --external: także linki http(s) (zapytanie HEAD, a przy odmowie GET).

Użycie:
    python3 tools/check_links.py            # tylko wewnętrzne
    python3 tools/check_links.py --external # wewnętrzne i zewnętrzne
"""
import re
import sys
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
AUTOLINK_RE = re.compile(r"<(https?://[^>\s]+)>")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
SKIP_DIRS = {".git", "node_modules"}
UA = "Mozilla/5.0 (compatible; Elektryka-link-checker; +https://github.com/kanthakdominik/Elektryka)"


def md_files():
    for p in sorted(ROOT.rglob("*.md")):
        if not SKIP_DIRS & set(p.relative_to(ROOT).parts):
            yield p


def strip_code(text: str):
    """Zwraca linie poza blokami kodu (z numerami linii)."""
    in_fence = False
    for no, line in enumerate(text.splitlines(), 1):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if not in_fence:
            yield no, re.sub(r"`[^`]*`", "", line)


def github_slug(heading: str) -> str:
    h = re.sub(r"<[^>]+>", "", heading)               # znaczniki HTML
    h = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", h)   # linki -> tekst
    h = h.replace("`", "").replace("*", "").replace("~", "")
    h = h.strip().lower()
    out = []
    for ch in h:
        cat = unicodedata.category(ch)
        if ch in " -_" or cat[0] in "LN" or cat == "Mn":
            out.append("-" if ch == " " else ch)
    return "".join(out)


@lru_cache(maxsize=None)
def anchors(path: Path) -> frozenset:
    seen, result = {}, set()
    for _, line in strip_code(path.read_text(encoding="utf-8")):
        m = HEADING_RE.match(line)
        if not m:
            continue
        s = github_slug(m.group(2))
        n = seen.get(s, 0)
        result.add(s if n == 0 else f"{s}-{n}")
        seen[s] = n + 1
    return frozenset(result)


def check_internal(src: Path, target: str):
    path_part, _, frag = target.partition("#")
    path_part = urllib.parse.unquote(path_part)
    dest = src if not path_part else (src.parent / path_part).resolve()
    if not dest.exists():
        return f"brak pliku: {path_part}"
    if ROOT not in dest.parents and dest != ROOT:
        return f"odnośnik poza repozytorium: {path_part}"
    if frag and dest.suffix == ".md":
        frag = urllib.parse.unquote(frag).lower()
        if frag not in anchors(dest):
            return f"brak kotwicy #{frag} w {dest.relative_to(ROOT)}"
    return None


def check_external(url: str):
    url = urllib.parse.quote(url, safe=":/?#[]@!$&'()*+,;=%~")
    for method in ("HEAD", "GET"):
        req = urllib.request.Request(url, method=method, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=20) as r:
                if r.status < 400:
                    return None
        except urllib.error.HTTPError as e:
            if e.code in (403, 429) and method == "GET":
                return f"ostrzeżenie: HTTP {e.code} (serwer odmawia automatom) — sprawdź ręcznie"
            if method == "GET":
                return f"HTTP {e.code}"
        except Exception as e:  # noqa: BLE001
            if method == "GET":
                return f"błąd połączenia: {e.__class__.__name__}"
    return None


def main() -> int:
    external = "--external" in sys.argv
    errors, warnings, ext_urls = [], [], {}
    for f in md_files():
        rel = f.relative_to(ROOT)
        for no, line in strip_code(f.read_text(encoding="utf-8")):
            targets = LINK_RE.findall(line) + AUTOLINK_RE.findall(line)
            for t in targets:
                t = t.strip("<>")
                if t.startswith(("http://", "https://")):
                    ext_urls.setdefault(t, []).append(f"{rel}:{no}")
                elif t.startswith(("mailto:", "tel:")):
                    continue
                else:
                    msg = check_internal(f, t)
                    if msg:
                        errors.append(f"{rel}:{no}: {msg}")
    if external:
        for url, where in sorted(ext_urls.items()):
            msg = check_external(url)
            if msg:
                (warnings if msg.startswith("ostrzeżenie") else errors).append(
                    f"{where[0]}: {url} — {msg}" + (f" (+{len(where) - 1} innych miejsc)" if len(where) > 1 else ""))
    for w in warnings:
        print("⚠️ ", w)
    for e in errors:
        print("❌", e)
    print(f"Pliki: {sum(1 for _ in md_files())}, linki zewnętrzne: {len(ext_urls)}"
          f"{' (sprawdzone)' if external else ' (pominięte)'}, błędy: {len(errors)}, ostrzeżenia: {len(warnings)}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
