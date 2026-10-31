#!/usr/bin/env python3
"""Pobiera zdjęcie z Wikimedia Commons do assets/foto/ i dopisuje autora i licencję do assets/CREDITS.md.

Użycie:
    python3 tools/commons.py "File:Nazwa pliku.jpg" 07-wylacznik-b16.jpg [--width 1280]

Plik zostaje też dopisany do listy assets/foto/ZDJECIA.tsv, żeby GitHub Actions
(i każdy klon repozytorium) wiedział, skąd pochodzi.

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
LISTA = FOTO / "ZDJECIA.tsv"
API = "https://commons.wikimedia.org/w/api.php"
UA = "Elektryka-repo/1.0 (https://github.com/kanthakdominik/Elektryka)"
ALLOWED = re.compile(r"^(public domain|pd\b|cc0|cc by(-sa)? ?\d|cc-by(-sa)?-\d)", re.I)
FORBIDDEN = re.compile(r"\b(nc|nd)\b", re.I)
SZEROKOSC = 1280  # jeden ze standardowych rozmiarów miniatur Wikimedia


class BladZdjecia(Exception):
    pass


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
        raise BladZdjecia(f"nie znaleziono pliku {title}")
    return page["imageinfo"][0]


def pobierz(title: str, name: str, width: int = SZEROKOSC) -> str:
    """Pobiera plik i dopisuje go do CREDITS.md. Zwraca opis (licencja, autor)."""
    title = title if title.startswith("File:") else f"File:{title}"
    ii = info(title, width)
    meta = ii.get("extmetadata", {})
    lic = plain(meta.get("LicenseShortName", {}).get("value", ""))
    author = plain(meta.get("Artist", {}).get("value", "")) or "nieznany autor"
    if not lic or FORBIDDEN.search(lic) or not ALLOWED.search(lic):
        raise BladZdjecia(f"licencja „{lic or 'brak'}” nie jest dozwolona ({title})")

    dest = FOTO / name
    if dest.exists():
        raise BladZdjecia(f"plik {dest.relative_to(ROOT)} już istnieje")
    if title.lower().endswith(".svg") or ii.get("width", 0) <= width:
        url = ii["url"]
    else:
        url = ii.get("thumburl") or ii["url"]
    FOTO.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(get(url))

    page_url = ii.get("descriptionurl") or f"https://commons.wikimedia.org/wiki/{urllib.parse.quote(title)}"
    author_cell = author.replace("|", "/")[:120]
    row = f"| `{name}` | {author_cell} | {lic} | [Wikimedia Commons]({page_url}) |\n"
    with CREDITS.open("a", encoding="utf-8") as f:
        f.write(row)
    return f"{lic}, {author_cell}"


def dopisz_do_listy(name: str, title: str):
    LISTA.parent.mkdir(parents=True, exist_ok=True)
    istniejace = LISTA.read_text(encoding="utf-8") if LISTA.exists() else ""
    if f"{name}\t" in istniejace:
        return
    with LISTA.open("a", encoding="utf-8") as f:
        if istniejace and not istniejace.endswith("\n"):
            f.write("\n")
        f.write(f"{name}\t{title}\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("title", help='nazwa pliku na Commons, np. "File:MCB B16.jpg"')
    ap.add_argument("name", help="nazwa pliku w assets/foto/, np. 07-wylacznik-b16.jpg")
    ap.add_argument("--width", type=int, default=SZEROKOSC)
    a = ap.parse_args()
    try:
        opis = pobierz(a.title, a.name, a.width)
    except (BladZdjecia, OSError) as e:
        sys.exit(f"Błąd: {e}")
    dopisz_do_listy(a.name, a.title if a.title.startswith("File:") else f"File:{a.title}")
    print(f"Zapisano assets/foto/{a.name} ({opis}) i dopisano do CREDITS.md oraz ZDJECIA.tsv")


if __name__ == "__main__":
    main()
