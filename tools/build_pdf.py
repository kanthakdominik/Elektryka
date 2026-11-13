"""Buduje wersje PDF do druku: Markdown → HTML → PDF (Chromium przez Playwright).

Uruchom:
  python3 tools/build_pdf.py            # ściągi, powtórka SEP, listy kontrolne, wzory → pdf/
  python3 tools/build_pdf.py --ksiazka  # cała baza (wszystkie moduły, z obrazami) → build/elektryka.pdf

Wymaga: pip install markdown playwright && python -m playwright install chromium
Linki względne zamieniane są na adresy w repozytorium na GitHubie, wzory LaTeX — na tekst z indeksami.
"""
import argparse
import re
import sys
from datetime import date
from pathlib import Path

import markdown

sys.path.insert(0, str(Path(__file__).parent))
from baza_pytan import ROOT  # noqa: E402
from gen_www import latex, REPO  # noqa: E402

CSS = """
@page { size: A4; margin: 16mm 14mm 18mm 14mm }
body { font: 10.5pt/1.45 "DejaVu Sans", "Liberation Sans", Arial, sans-serif; color: #1a1e23 }
h1 { font-size: 20pt; margin: 0 0 6pt; border-bottom: 2pt solid #1a1e23; padding-bottom: 4pt }
h2 { font-size: 14pt; margin: 14pt 0 4pt; break-after: avoid }
h3 { font-size: 12pt; margin: 10pt 0 3pt; break-after: avoid }
p, li { orphans: 3; widows: 3 }
blockquote { margin: 6pt 0; padding: 4pt 10pt; border-left: 3pt solid #f2c300; background: #f6f6f2; color: #333 }
table { border-collapse: collapse; width: 100%; margin: 6pt 0; font-size: 9pt; break-inside: auto }
tr { break-inside: avoid }
th, td { border: 0.6pt solid #bbb; padding: 3pt 5pt; text-align: left; vertical-align: top }
th { background: #eeeee8 }
code { font-family: "DejaVu Sans Mono", monospace; font-size: 9pt }
.m { font-family: "DejaVu Sans Mono", monospace; font-size: 9.5pt; white-space: nowrap }
a { color: #1a1e23; text-decoration: none; border-bottom: 0.5pt dotted #888 }
img { max-width: 100%; max-height: 120mm; display: block; margin: 6pt auto }
details summary { font-weight: bold }
.doc { break-before: page }
.doc:first-child { break-before: auto }
.okladka { height: 240mm; display: flex; flex-direction: column; justify-content: center; gap: 8pt }
.okladka h1 { font-size: 30pt; border: 0 }
hr { border: 0; border-top: 0.6pt solid #bbb }
.blank { display: inline-block; border-bottom: 0.6pt solid #555; height: 1em; vertical-align: baseline }
td:empty { height: 17pt }
"""


def przygotuj(tekst, src_dir):
    """Matematyka → HTML, linki względne → GitHub, obrazy → file://, checkboxy → ☐/☑, <details> otwarte."""
    tekst = re.sub(r"\$\$(.+?)\$\$", lambda m: f'<span class="m">{latex(m.group(1))}</span>', tekst, flags=re.S)
    tekst = re.sub(r"(?<![\\\w])\$([^$\n]+?)\$", lambda m: f'<span class="m">{latex(m.group(1))}</span>', tekst)

    def obraz(m):
        alt, url = m.group(1), m.group(2)
        if re.match(r"^[a-z]+:", url):
            return m.group(0)
        return f"![{alt}]({(src_dir / url).resolve().as_uri()})"

    def link(m):
        etyk, url = m.group(1), m.group(2)
        if re.match(r"^[a-z]+:", url) or url.startswith("#"):
            return m.group(0)
        path, _, frag = url.partition("#")
        try:
            rel = (src_dir / path).resolve().relative_to(ROOT).as_posix()
        except ValueError:
            return etyk
        return f"[{etyk}]({REPO}{rel}{'#' + frag if frag else ''})"
    tekst = re.sub(r"!\[([^\]]*)\]\(([^)\s]+)\)", obraz, tekst)
    tekst = re.sub(r"(?<!!)\[([^\]]+)\]\(([^)\s]+)\)", link, tekst)
    tekst = re.sub(r"^(\s*[-*]) \[ \] ", r"\1 ☐ ", tekst, flags=re.M)
    tekst = re.sub(r"^(\s*[-*]) \[x\] ", r"\1 ☑ ", tekst, flags=re.M | re.I)
    tekst = re.sub(r"_{3,}", lambda m: f'<span class="blank" style="width:{min(len(m.group(0)), 40) * 0.55}em"></span>', tekst)
    return tekst.replace("<details>", "<details open markdown=\"1\">")


def html_z(pliki, tytul, okladka=None):
    sekcje = []
    if okladka:
        sekcje.append(f'<section class="okladka"><h1>{tytul}</h1><p>{okladka}</p><p>Stan: {date.today():%d.%m.%Y} · {REPO.split("/blob")[0]}</p></section>')
    for p in pliki:
        md = przygotuj(p.read_text(encoding="utf-8"), p.parent)
        body = markdown.markdown(md, extensions=["tables", "fenced_code", "sane_lists", "md_in_html"])
        sekcje.append(f'<section class="doc">{body}</section>')
    return f'<!doctype html><html lang="pl"><head><meta charset="utf-8"><title>{tytul}</title><style>{CSS}</style></head><body>{"".join(sekcje)}</body></html>'


def do_pdf(strony, przegladarka):
    for wyj, (pliki, tytul, okl) in strony.items():
        wyj.parent.mkdir(parents=True, exist_ok=True)
        tmp = wyj.with_suffix(".html")
        tmp.write_text(html_z(pliki, tytul, okl), encoding="utf-8")
        pg = przegladarka.new_page()
        pg.goto(tmp.as_uri(), wait_until="load")
        pg.pdf(path=str(wyj), format="A4", print_background=True, display_header_footer=True,
               header_template="<span></span>",
               footer_template=f'<div style="font:7pt sans-serif;color:#777;width:100%;padding:0 14mm;display:flex;justify-content:space-between">'
                               f'<span>{tytul}</span><span><span class="pageNumber"></span>/<span class="totalPages"></span></span></div>',
               margin={"top": "16mm", "bottom": "18mm", "left": "14mm", "right": "14mm"})
        pg.close()
        tmp.unlink()
        print(f"{wyj.relative_to(ROOT)}: {wyj.stat().st_size // 1024} KB")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ksiazka", action="store_true", help="cała baza w jednym PDF (build/elektryka.pdf)")
    a = ap.parse_args()
    M = sorted(p for p in (ROOT / "modules").iterdir() if p.is_dir())
    if a.ksiazka:
        pliki = [ROOT / "README.md"]
        for m in M:
            pliki += [m / "README.md"] + sorted(m.glob("[0-9][0-9].[0-9][0-9]-*.md"))
        pliki += [ROOT / "SLOWNICZEK.md"]
        strony = {ROOT / "build" / "elektryka.pdf": ([p for p in pliki if p.exists()], "Elektryka — baza wiedzy",
                                                    "Wszystkie moduły: od bezpieczeństwa i podstaw po dozór i sieci SN.")}
    else:
        P = ROOT / "pdf"
        strony = {
            P / "sciagi-modulow.pdf": ([m / "SCIAGA.md" for m in M if (m / "SCIAGA.md").exists()], "Elektryka — ściągi modułów",
                                       "Jedna strona na moduł: najważniejsze liczby, zasady i wzory."),
            P / "sep-powtorka.pdf": ([ROOT / "sep" / f for f in ("powtorka-48h.md", "pulapki.md", "sciaga-dozor.md")],
                                     "Egzamin SEP — powtórka", "Powtórka 48 h, pułapki egzaminacyjne i ściąga przepisów dla D."),
            P / "listy-kontrolne.pdf": ([ROOT / "listy-kontrolne" / f for f in ("przed-praca.md", "odbior-instalacji.md", "kupno-domu-mieszkania.md",
                                         "przeglad-rozdzielnicy.md", "po-burzy-lub-zalaniu.md", "przed-pomiarami.md")], "Listy kontrolne", None),
            P / "wzory.pdf": ([ROOT / "wzory" / f for f in ("protokol-pomiarow.md", "opis-rozdzielnicy.md")], "Wzory dokumentów", None),
        }
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        b = pw.chromium.launch()
        do_pdf(strony, b)
        b.close()


if __name__ == "__main__":
    main()
