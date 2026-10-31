#!/usr/bin/env python3
"""Sprawdza obrazy w plikach Markdown repozytorium.

Błędy:
- obraz wskazuje na nieistniejący plik,
- obraz nie ma tekstu alternatywnego,
- zdjęcie z assets/foto/ nie ma wpisu w assets/CREDITS.md,
- obraz jest osadzony z zewnętrznego serwera (zdjęcia trzymamy w repozytorium).

Zdjęcie z listy assets/foto/ZDJECIA.tsv, którego jeszcze nie ma, to tylko ostrzeżenie (⏳):
pobiera je workflow „Pobieranie zdjęć z Wikimedia Commons”.

Informacyjnie wypisuje znaczniki „📷 DO ZROBIENIA” i pliki w assets/, których nikt nie używa.

Użycie: python3 tools/check_images.py [--todo]
"""
import re
import sys
import urllib.parse
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FOTO = ROOT / "assets" / "foto"
CREDITS = ROOT / "assets" / "CREDITS.md"
LISTA = FOTO / "ZDJECIA.tsv"
IMG_MD = re.compile(r"!\[([^\]]*)\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
IMG_HTML = re.compile(r"<img\b[^>]*>", re.I)
ATTR = re.compile(r'(\w+)\s*=\s*"([^"]*)"')
FENCE = re.compile(r"^\s*(```|~~~)")
TODO = re.compile(r"📷\s*\**DO ZROBIENIA:?\**:?\s*(.*)")
SKIP = {".git", "node_modules"}


def md_files():
    for p in sorted(ROOT.rglob("*.md")):
        if not SKIP & set(p.relative_to(ROOT).parts):
            yield p


def credited() -> set:
    if not CREDITS.exists():
        return set()
    names = set()
    for line in CREDITS.read_text(encoding="utf-8").splitlines():
        if line.startswith("|") and not line.startswith("|--"):
            cell = line.split("|")[1].strip().strip("`")
            names.add(Path(cell).name)
    return names


def na_liscie() -> set:
    """Zdjęcia z assets/foto/ZDJECIA.tsv — pobiera je GitHub Actions po pushu."""
    if not LISTA.exists():
        return set()
    return {line.split("\t", 1)[0].strip() for line in LISTA.read_text(encoding="utf-8").splitlines()
            if line.strip() and not line.startswith("#")}


def main() -> int:
    errors, waiting, todos, used = [], [], [], set()
    credits = credited()
    lista = na_liscie()
    for f in md_files():
        rel = f.relative_to(ROOT)
        in_fence = False
        for no, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            if FENCE.match(line):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            m = TODO.search(re.sub(r"`[^`]*`", "", line))
            if m:
                todos.append(f"{rel}:{no}: {m.group(1).strip()}")
            imgs = [(a, s) for a, s in IMG_MD.findall(line)]
            for tag in IMG_HTML.findall(line):
                attrs = dict(ATTR.findall(tag))
                imgs.append((attrs.get("alt", ""), attrs.get("src", "")))
            for alt, src in imgs:
                where = f"{rel}:{no}"
                if not alt.strip():
                    errors.append(f"{where}: brak tekstu alternatywnego dla {src}")
                if src.startswith(("http://", "https://")):
                    errors.append(f"{where}: obraz z zewnętrznego serwera ({src}) — pobierz go do assets/")
                    continue
                path = (f.parent / urllib.parse.unquote(src)).resolve()
                used.add(path)
                if not path.exists():
                    if FOTO in path.parents and path.name in lista:
                        waiting.append(f"{where}: {path.name} czeka na pobranie przez GitHub Actions")
                    else:
                        errors.append(f"{where}: brak pliku {src}")
                elif FOTO in path.parents and path.name not in credits:
                    errors.append(f"{where}: {path.name} nie ma wpisu w assets/CREDITS.md")

    unused = [p for p in (ROOT / "assets").rglob("*")
              if p.is_file() and p.suffix.lower() in {".jpg", ".jpeg", ".png", ".svg", ".webp", ".gif"}
              and p.resolve() not in used]

    for e in errors:
        print("❌", e)
    for w in waiting:
        print("⏳", w)
    for p in unused:
        print("ℹ️  nieużywany plik:", p.relative_to(ROOT))
    if "--todo" in sys.argv:
        print(f"\n📷 Zdjęcia do zrobienia ({len(todos)}):")
        for t in todos:
            print("  -", t)
    print(f"Obrazy użyte: {len(used)}, zdjęcia do zrobienia: {len(todos)}, błędy: {len(errors)}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
