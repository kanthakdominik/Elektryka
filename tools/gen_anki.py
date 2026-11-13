"""Generuje talie fiszek Anki (TSV) z pytań i „Liczb do zapamiętania”: sep/anki/*.tsv."""
import re
from baza_pytan import pytania, liczby, ROOT

DST = ROOT / "sep" / "anki"
DST.mkdir(parents=True, exist_ok=True)


def html(s):
    s = re.sub(r"(?<!!)\[([^\]]+)\]\([^)]+\)", r"\1", s)          # linki → sam tekst
    s = re.sub(r"\$\$(.+?)\$\$", r"\\[\1\\]", s, flags=re.S)       # LaTeX → MathJax Anki
    s = re.sub(r"\$(.+?)\$", r"\\(\1\\)", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<![*\w])\*(?!\s)(.+?)(?<!\s)\*(?![*\w])", r"<i>\1</i>", s)
    s = s.replace("\t", " ").replace("\r", "")
    s = re.sub(r"\n{2,}", "<br><br>", s.strip())
    return s.replace("\n", "<br>")


def tag(p):
    return f"elektryka::{p['modul'][:2]} temat::{p['nr'].replace('.', '_')}" + (" SEP" if p.get("rodzaj") == "SEP" else "")


naglowek = "#separator:tab\n#html:true\n#tags column:3\n"
with open(DST / "pytania.tsv", "w", encoding="utf-8") as f:
    f.write(naglowek)
    n = 0
    for p in pytania():
        front = html(p["pytanie"]) + f"<br><small>{html(p['tytul'])}</small>"
        f.write(f"{front}\t{html(p['odpowiedz'])}\t{tag(p)}\n"); n += 1
with open(DST / "liczby.tsv", "w", encoding="utf-8") as f:
    f.write(naglowek)
    m = 0
    for l in liczby():
        front = f"{html(l['wielkosc'])}" + (f"<br><small>{html(l['kiedy'])}</small>" if l["kiedy"] else "") + f"<br><small>{l['nr']}</small>"
        back = html(l["wartosc"]) + (f"<br><small>źródło: {html(l['zrodlo'])}</small>" if l["zrodlo"] and l["zrodlo"] not in "—-" else "")
        f.write(f"{front}\t{back}\t{tag(l)} liczby\n"); m += 1
print("pytania:", n, "liczby:", m)
