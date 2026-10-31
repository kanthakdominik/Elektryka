#!/usr/bin/env python3
"""Pobiera zdjęcie z Wikimedia Commons do assets/foto/ i dopisuje autora i licencję do assets/CREDITS.md.

Użycie:
    python3 tools/commons.py "File:Nazwa pliku.jpg" 07-wylacznik-b16.jpg [--width 1200]

Odrzuca pliki na licencjach NC (niekomercyjne) i ND (bez utworów zależnych).
"""
import argparse
import html
import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FOTO = ROOT / "assets" / "foto"
CREDITS = ROOT / "assets" / "CREDITS.md"
API = "https://commons.wikimedia.org/w/api.php"
UA = "Elektryka-repo/1.0 (https://github.com/kanthakdominik/Elektryka)"
ALLOWED = re.compile(r"^(public domain|pd\b|cc0|cc by(-sa)? ?\d|cc-by(-sa)?-\d)", re.I)
FORBIDDEN = re.compile(r"\b(nc|nd)\b", re.I)


def get(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def plain(text: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", text or ""))).strip()


def info(title: str, width: int) -> dict:
    q = urllib.parse.urlencode({
        "action": "query", "format": "json", "titles": title, "prop": "imageinfo",
        "iiprop": "url|extmetadata|size", "iiurlwidth": width,
    })
    pages = json.loads(get(f"{API}?{q}"))["query"]["pages"]
    page = next(iter(pages.values()))
    if "imageinfo" not in page:
        sys.exit(f"Nie znaleziono pliku: {title}")
    return page["imageinfo"][0]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("title", help='nazwa pliku na Commons, np. "File:MCB B16.jpg"')
    ap.add_argument("name", help="nazwa pliku w assets/foto/, np. 07-wylacznik-b16.jpg")
    ap.add_argument("--width", type=int, default=1200)
    a = ap.parse_args()

    title = a.title if a.title.startswith("File:") else f"File:{a.title}"
    ii = info(title, a.width)
    meta = ii.get("extmetadata", {})
    lic = plain(meta.get("LicenseShortName", {}).get("value", ""))
    author = plain(meta.get("Artist", {}).get("value", "")) or "nieznany autor"
    if not lic or FORBIDDEN.search(lic) or not ALLOWED.search(lic):
        sys.exit(f"Licencja „{lic or 'brak'}” nie jest dozwolona (zob. docs/GRAFIKI.md).")

    dest = FOTO / a.name
    if dest.exists():
        sys.exit(f"Plik {dest.relative_to(ROOT)} już istnieje.")
    url = ii.get("thumburl") if ii.get("width", 0) > a.width else ii["url"]
    FOTO.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(get(url))

    page_url = ii.get("descriptionurl") or f"https://commons.wikimedia.org/wiki/{urllib.parse.quote(title)}"
    row = f"| `{a.name}` | {author.replace('|', '/')} | {lic} | [Wikimedia Commons]({page_url}) |\n"
    with CREDITS.open("a", encoding="utf-8") as f:
        f.write(row)
    print(f"Zapisano {dest.relative_to(ROOT)} ({lic}, {author}) i dopisano do CREDITS.md")


if __name__ == "__main__":
    main()
