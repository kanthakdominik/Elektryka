"""Generuje sep/egzaminy-probne.md — zestawy pytań E, D i SN z odpowiedziami."""
import random
from pathlib import Path
from baza_pytan import pytania, przenies_linki, ROOT
from check_links import github_slug

DST = ROOT / "sep"
random.seed(2026)
P = [p for p in pytania() if p["rodzaj"] == "SEP"]
E = [p for p in P if not p["nr"].startswith(("33", "34"))]
D_EXTRA = [p for p in P if p["nr"].startswith(("33", "32", "29"))]
SN = [p for p in P if p["nr"].startswith("34")]
uzyte = set()


def wez(pula, warunek, n):
    kand = [p for p in pula if warunek(p) and p["pytanie"] not in uzyte]
    if len(kand) < n:
        kand = [p for p in pula if warunek(p)]
    wyb = random.sample(kand, min(n, len(kand)))
    for p in wyb:
        uzyte.add(p["pytanie"])
    return wyb


def blok(nr, q):
    t = przenies_linki(q["odpowiedz"], q["plik"].parent, DST)
    rel = Path("..") / q["plik"].relative_to(ROOT)
    obsz = " ".join(f"({z})" for z in q["zakres"]) or "dozór"
    return (f"{nr}. **{q['pytanie']}**  \n   <sub>obszar {obsz} · temat [{q['nr']}]({rel.as_posix()}#pytania-sep)</sub>\n\n"
            f"<details>\n<summary>Odpowiedź</summary>\n\n{t}\n</details>\n")


out = ["# Egzaminy próbne", "",
       "Zestawy pytań w stylu egzaminu ustnego przed komisją kwalifikacyjną. Każde pytanie pochodzi z sekcji „Pytania SEP” tematów, odpowiedź wzorcowa jest pod rozwinięciem.",
       "", "[← sep/](README.md) · [bank pytań](pytania.md) · [egzamin interaktywny (strona HTML)](../www/egzamin.html)", "",
       "**Jak ćwiczyć:** weź zestaw, odpowiadaj na głos, pełnymi zdaniami (co to jest → do czego służy → jak działa → przepis lub liczba), a dopiero potem rozwiń odpowiedź. Zestaw uznaj za zdany, gdy odpowiesz poprawnie na co najmniej 5 z 6 pytań bez zaglądania.",
       "", "> Zestawy wygenerowano skryptem `tools/gen_egzaminy.py` — po zmianie pytań w tematach uruchom go ponownie.", "",
       "## Spis zestawów", ""]
zestawy = []
for i in range(1, 11):
    q = (wez(E, lambda p: "a" in p["zakres"], 2) + wez(E, lambda p: "b" in p["zakres"] or "c" in p["zakres"], 2)
         + wez(E, lambda p: "d" in p["zakres"], 1) + wez(E, lambda p: "e" in p["zakres"], 1))
    zestawy.append((f"Zestaw E{i} — eksploatacja, G1 do 1 kV", f"e{i}", q))
for i in range(1, 6):
    q = (wez(D_EXTRA, lambda p: p["nr"].startswith("33"), 2) + wez(D_EXTRA, lambda p: p["nr"].startswith(("32", "29")), 2)
         + wez(E, lambda p: "d" in p["zakres"], 1) + wez(E, lambda p: "e" in p["zakres"] or "a" in p["zakres"], 1))
    zestawy.append((f"Zestaw D{i} — dozór, G1", f"d{i}", q))
for i in range(1, 3):
    q = wez(SN, lambda p: True, 4) + wez(E, lambda p: p["nr"].startswith(("28", "31")), 2)
    zestawy.append((f"Zestaw SN{i} — urządzenia powyżej 1 kV (rozszerzenie)", f"sn{i}", q))
for tyt, kot, _ in zestawy:
    out.append(f"- [{tyt}](#{github_slug(tyt)})")
out.append("")
for tyt, kot, q in zestawy:
    out += [f"## {tyt}", ""]
    for j, x in enumerate(q, 1):
        out.append(blok(j, x))
(DST / "egzaminy-probne.md").write_text("\n".join(out).rstrip() + "\n", encoding="utf-8")
print("zestawów:", len(zestawy), "pytań:", sum(len(z[2]) for z in zestawy))
