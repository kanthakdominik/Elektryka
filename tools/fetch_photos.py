#!/usr/bin/env python3
"""Pobiera brakujące zdjęcia z listy assets/foto/ZDJECIA.tsv (format: nazwa<TAB>File:… na Commons).

Uruchamiany automatycznie przez GitHub Actions (.github/workflows/zdjecia.yml) po zmianie listy,
ale działa też lokalnie: python3 tools/fetch_photos.py

Kod wyjścia 1, jeśli któregoś pliku nie udało się pobrać (np. zła nazwa albo niedozwolona licencja).
"""
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from commons import FOTO, LISTA, BladZdjecia, pobierz  # noqa: E402


def wpisy():
    if not LISTA.exists():
        return []
    out = []
    for no, line in enumerate(LISTA.read_text(encoding="utf-8").splitlines(), 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        try:
            name, title = [x.strip() for x in line.split("\t", 1)]
        except ValueError:
            print(f"❌ ZDJECIA.tsv:{no}: oczekiwano „nazwa<TAB>File:…”")
            continue
        out.append((name, title))
    return out


def main() -> int:
    bledy, pobrane = 0, 0
    for name, title in wpisy():
        if (FOTO / name).exists():
            continue
        try:
            opis = pobierz(title, name)
            pobrane += 1
            print(f"✅ {name} ← {title} ({opis})")
        except (BladZdjecia, OSError) as e:
            bledy += 1
            print(f"❌ {name} ← {title}: {e}")
        time.sleep(1)  # uprzejmie wobec serwerów Wikimedia
    print(f"Pobrane: {pobrane}, błędy: {bledy}")
    return 1 if bledy else 0


if __name__ == "__main__":
    sys.exit(main())
