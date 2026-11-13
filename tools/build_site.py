#!/usr/bin/env python3
"""Przygotowuje stronę GitHub Pages (MkDocs Material) z plików .md repozytorium.

Pliki źródłowe w repozytorium się nie zmieniają. Skrypt kopiuje je do katalogu _site/src,
zamienia README.md na index.md, poprawia odnośniki (katalogi → index.md, pliki spoza strony →
GitHub), włącza Markdown wewnątrz <details>, kopiuje obrazy (assets/), strony interaktywne (www/)
i PDF-y (pdf/), a na koniec zapisuje _site/mkdocs.yml z menu ułożonym jak mapa modułów w README.
Użycie: python3 tools/build_site.py && mkdocs build -f _site/mkdocs.yml
"""
import glob
import os
import re
import shutil

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUT = os.path.join(ROOT, "_site")
SRC = os.path.join(OUT, "src")
REPO = "https://github.com/kanthakdominik/Elektryka"
LINK = re.compile(r"(\]\()([^)\s]+)(\))")

PLIKI_GLOWNE = ["README.md", "ROADMAP.md", "RESOURCES.md", "NARZEDZIA.md", "SLOWNICZEK.md", "ZADANIA.md",
                "PRZEPISY.md", "LICENSE.md", "docs/SZABLON-TEMATU.md", "docs/GRAFIKI.md", "assets/CREDITS.md",
                "pdf/README.md", "sep/anki/README.md"]
# katalogi kopiowane na stronę bez zmian (obrazy, strony HTML, PDF-y) — odnośniki do nich zostają względne
STATYCZNE = {"assets": (".svg", ".png", ".jpg", ".jpeg", ".gif", ".webp"), "www": (".html",), "pdf": (".pdf",)}


def cel_strony(sciezka_repo):
    """Ścieżka pliku w repozytorium → ścieżka na stronie (README.md → index.md)."""
    katalog, nazwa = os.path.split(sciezka_repo)
    return os.path.join(katalog, "index.md") if nazwa == "README.md" else sciezka_repo


def statyczny(rel_repo):
    gora = rel_repo.split(os.sep, 1)[0]
    return gora in STATYCZNE and rel_repo.lower().endswith(STATYCZNE[gora])


def popraw_link(cel, plik_repo):
    if cel.startswith(("http://", "https://", "mailto:", "#")):
        return cel
    sciezka, _, kotwica = cel.partition("#")
    kotwica = "#" + kotwica if kotwica else ""
    katalog = os.path.dirname(plik_repo)
    pelna = os.path.normpath(os.path.join(ROOT, katalog, sciezka))
    rel_repo = os.path.relpath(pelna, ROOT)
    if os.path.isfile(pelna) and statyczny(rel_repo):
        return os.path.relpath(rel_repo, katalog) + kotwica       # obraz, strona www/, PDF — kopiowane na stronę
    if os.path.isdir(pelna) and os.path.exists(os.path.join(pelna, "README.md")):
        rel_repo = os.path.join(rel_repo, "README.md")
    elif not rel_repo.endswith(".md") or not os.path.exists(pelna):
        rodzaj = "tree" if os.path.isdir(pelna) else "blob"
        return f"{REPO}/{rodzaj}/main/{rel_repo}{kotwica}"       # pliki spoza strony (skrypty, dane, konfiguracja)
    nowy = os.path.relpath(cel_strony(rel_repo), os.path.dirname(cel_strony(plik_repo)))
    return nowy + kotwica


LISTA = re.compile(r"^( *)([-*+]|\d+[.)]) +")


def dostosuj_markdown(tekst):
    """Różnice między Markdownem GitHuba a Python-Markdown (MkDocs): listy, tabele i bloki $$ muszą być
    oddzielone pustą linią od akapitu, a listy zagnieżdżone wymagają wcięcia o 4 spacje."""
    wynik, w_kodzie, w_wzorze = [], False, False
    for linia in tekst.split("\n"):
        poprz = wynik[-1] if wynik else ""
        if linia.lstrip().startswith("```"):
            w_kodzie = not w_kodzie
            wynik.append(linia)
            continue
        if w_kodzie:
            wynik.append(linia)
            continue
        m = LISTA.match(linia)
        if m and 0 < len(m.group(1)) < 4 and LISTA.match(poprz):
            linia = "    " + linia.lstrip()                       # lista zagnieżdżona: wcięcie 4 spacje
            m = LISTA.match(linia)
        pusta_przed = poprz.strip() != "" and not poprz.lstrip().startswith(">")
        if m and pusta_przed and not LISTA.match(poprz) and not poprz.startswith("    ") and not poprz.lstrip().startswith("<"):
            wynik.append("")
        elif linia.startswith("|") and pusta_przed and not poprz.startswith("|"):
            wynik.append("")
        elif linia.strip().startswith("$$"):
            if not w_wzorze and pusta_przed:
                wynik.append("")
            jedna = linia.strip() != "$$" and linia.strip().endswith("$$") and len(linia.strip()) > 4
            if not jedna:
                w_wzorze = not w_wzorze
        elif poprz.strip().endswith("$$") and not w_wzorze and linia.strip() and poprz.strip() != "":
            wynik.append("")
        wynik.append(linia)
    return "\n".join(wynik)


def kopiuj(plik_repo):
    tekst = open(os.path.join(ROOT, plik_repo), encoding="utf-8").read()
    tekst = LINK.sub(lambda m: m.group(1) + popraw_link(m.group(2), plik_repo) + m.group(3), tekst)
    tekst = re.sub(r"(?<!`)<details>", '<details markdown="1">', dostosuj_markdown(tekst))
    cel = os.path.join(SRC, cel_strony(plik_repo))
    os.makedirs(os.path.dirname(cel), exist_ok=True)
    open(cel, "w", encoding="utf-8").write(tekst)


def tytul(plik_repo):
    pierwsza = open(os.path.join(ROOT, plik_repo), encoding="utf-8").readline().lstrip("# ").strip()
    return pierwsza.replace('"', "'")


def czesci_modulow():
    """Części I–VIII z mapy modułów w README: [(nazwa części, [katalogi modułów])]."""
    readme = open(os.path.join(ROOT, "README.md"), encoding="utf-8").read()
    mapa = readme.split("## Mapa modułów", 1)[1].split("<!-- mapa:end -->", 1)[0]
    wynik = []
    for blok in re.split(r"^### ", mapa, flags=re.M)[1:]:
        nazwa = blok.splitlines()[0].strip()
        moduly = re.findall(r"\]\((modules/[^/)]+)/README\.md\)", blok)
        if moduly:
            wynik.append((nazwa, moduly))
    return wynik


def glob_md(wzor):
    return sorted(glob.glob(wzor, root_dir=ROOT))


shutil.rmtree(OUT, ignore_errors=True)
pliki = (PLIKI_GLOWNE + glob_md("sep/*.md") + glob_md("listy-kontrolne/*.md") + glob_md("wzory/*.md")
         + glob_md("modules/*/*.md"))
pliki = [p for p in dict.fromkeys(pliki) if os.path.exists(os.path.join(ROOT, p))]
for p in pliki:
    kopiuj(p)

for katalog, rozszerzenia in STATYCZNE.items():
    for f in glob.glob(f"{katalog}/**/*", root_dir=ROOT, recursive=True):
        if f.lower().endswith(rozszerzenia):
            os.makedirs(os.path.dirname(os.path.join(SRC, f)), exist_ok=True)
            shutil.copy(os.path.join(ROOT, f), os.path.join(SRC, f))


def pozycje(lista, wciecie):
    return [f'{" " * wciecie}- "{t}": {p}' for t, p in lista if os.path.exists(os.path.join(SRC, p))]


# menu
nav = ["nav:", "  - Start: index.md", "  - Roadmapa: ROADMAP.md", "  - Egzamin SEP:", "    - sep/index.md"]
nav += pozycje([("Zakres → moduły", "sep/zakres.md"), ("Bank pytań", "sep/pytania.md"),
                ("Egzaminy próbne", "sep/egzaminy-probne.md"), ("Pułapki egzaminacyjne", "sep/pulapki.md"),
                ("Ściąga przepisów — dozór (D)", "sep/sciaga-dozor.md"), ("Powtórka 48 h", "sep/powtorka-48h.md"),
                ("Fiszki Anki", "sep/anki/index.md")], 4)
nav += ['    - "Trening online ↗": https://kanthakdominik.github.io/Elektryka/www/egzamin.html']
for nazwa, moduly in czesci_modulow():
    nav.append(f'  - "{nazwa.replace(chr(34), chr(39))}":')
    for d in moduly:
        nav.append(f'    - "{tytul(d + "/README.md")}":')
        nav.append(f"      - {d}/index.md")
        if os.path.exists(os.path.join(ROOT, d, "SCIAGA.md")):
            nav.append(f'      - "Ściąga": {d}/SCIAGA.md')
        for t in glob_md(f"{d}/[0-9][0-9].[0-9][0-9]-*.md"):
            nav.append(f'      - "{tytul(t)}": {t}')
nav += ["  - Praktyka:"]
nav += pozycje([("Zbiór zadań", "ZADANIA.md"), ("Listy kontrolne", "listy-kontrolne/index.md")], 4)
nav += pozycje([(tytul(p).replace("Lista: ", ""), p) for p in glob_md("listy-kontrolne/*.md") if not p.endswith("README.md")], 4)
nav += pozycje([("Wzory dokumentów", "wzory/index.md")], 4)
nav += pozycje([(tytul(p), p) for p in glob_md("wzory/*.md") if not p.endswith("README.md")], 4)
nav += ['    - "Kalkulatory ↗": https://kanthakdominik.github.io/Elektryka/www/kalkulatory.html']
nav += ["  - Materiały:"]
nav += pozycje([("Przepisy i normy — indeks", "PRZEPISY.md"), ("Źródła", "RESOURCES.md"), ("Narzędzia i przyrządy", "NARZEDZIA.md"),
                ("Słowniczek", "SLOWNICZEK.md"), ("PDF do druku", "pdf/index.md"), ("Zasady grafik", "docs/GRAFIKI.md"),
                ("Szablon tematu", "docs/SZABLON-TEMATU.md"), ("Autorzy zdjęć", "assets/CREDITS.md"), ("Licencja", "LICENSE.md")], 4)

os.makedirs(os.path.join(SRC, "javascripts"), exist_ok=True)
shutil.copy(os.path.join(ROOT, "tools", "site", "mathjax.js"), os.path.join(SRC, "javascripts", "mathjax.js"))
shutil.copy(os.path.join(ROOT, "tools", "site", "extra.css"), os.path.join(SRC, "javascripts", "extra.css"))
konfig = open(os.path.join(ROOT, "tools", "site", "mkdocs.base.yml"), encoding="utf-8").read()
open(os.path.join(OUT, "mkdocs.yml"), "w", encoding="utf-8").write(konfig.rstrip() + "\n\n" + "\n".join(nav) + "\n")
print(f"stron: {len(pliki)}, katalog: {SRC}")
