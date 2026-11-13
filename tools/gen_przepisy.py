"""Generuje PRZEPISY.md — indeks aktów prawnych i norm z odnośnikami do tematów, które je cytują.

Uruchom: python3 tools/gen_przepisy.py
Listę aktów prowadzi się w tools/przepisy_lista.py; normy są wyszukiwane automatycznie.
"""
import re
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from baza_pytan import ROOT, tematy  # noqa: E402
from przepisy_lista import AKTY, UE, eli_url  # noqa: E402

NORMA = re.compile(r"\b(PN-(?:HD|EN|IEC|ISO|E|N)(?: IEC| ISO)?[ -]\d+(?:-\d+)*|N SEP-E-\d+)")


def linki(lista):
    return " · ".join(f"[{t['nr']}]({t['plik'].relative_to(ROOT).as_posix()})" for t in sorted(lista, key=lambda t: t["nr"]))


def seria(n):
    m = re.match(r"(PN-HD 60364|PN-EN 6\d{4}|PN-EN 5\d{4}|N SEP)", n)
    if n.startswith("PN-HD 60364"):
        return "PN-HD 60364 — instalacje elektryczne niskiego napięcia"
    if n.startswith("N SEP"):
        return "Normy SEP"
    return "Pozostałe normy" if not m else "Pozostałe normy"


def main():
    T = list(tematy())
    akty = defaultdict(list)
    ue = defaultdict(list)
    normy = defaultdict(set)
    for t in T:
        tx = t["tekst"]
        for a in AKTY:
            if re.search(a["wzor"], tx):
                akty[a["klucz"]].append(t)
        for u in UE:
            if re.search(u["wzor"], tx):
                ue[u["nazwa"]].append(t)
        for n in set(NORMA.findall(tx)):
            normy[n].add(t["nr"])
    po_nr = {t["nr"]: t for t in T}

    L = ["# Przepisy i normy — indeks", "",
         f"> Wszystkie akty prawne i normy cytowane w bazie, z tematami, które z nich korzystają. Stan: **{date.today():%m.%Y}**.",
         "> Teksty aktów sprawdzaj w [ISAP](https://isap.sejm.gov.pl/) lub [ELI](https://eli.gov.pl/). Zmiany kluczowych aktów wykrywa co miesiąc automat ([`.github/workflows/przepisy.yml`](.github/workflows/przepisy.yml)) i zakłada zgłoszenie (issue).",
         "> Ściąga do egzaminu D (paragrafy i liczby): [sep/sciaga-dozor.md](sep/sciaga-dozor.md). Plik generuje [`tools/gen_przepisy.py`](tools/gen_przepisy.py).",
         "", "## Ustawy i rozporządzenia (Polska)", "",
         "| Akt | Aktualny tekst | Co reguluje | Tematy |", "|-----|----------------|-------------|--------|"]
    for a in AKTY:
        L.append(f"| [{a['nazwa']}]({eli_url(a['eli'])}) | {a['tj']} | {a['co']} | {linki(akty[a['klucz']]) or '—'} |")
    L += ["", "## Prawo Unii Europejskiej", "", "| Akt | Tematy |", "|-----|--------|"]
    for u in UE:
        L.append(f"| [{u['nazwa']}]({u['url']}) | {linki(ue[u['nazwa']]) or '—'} |")

    grupy = defaultdict(list)
    for n in normy:
        grupy[seria(n)].append(n)
    klucz = lambda n: [int(x) if x.isdigit() else x for x in re.split(r"(\d+)", n)]
    L += ["", "## Normy", "",
          "> Stosowanie Polskich Norm jest dobrowolne, ale przepisy (np. warunki techniczne) je przywołują, a przy ocenie wypadku traktuje się je jak zasady wiedzy technicznej — [32.06](modules/32-przepisy-i-normy/32.06-normy-pn-hd-60364-i-pozostale.md).",
          f"> Rozpoznano **{len(normy)}** oznaczeń norm (arkusze liczone osobno)."]
    for g in ["PN-HD 60364 — instalacje elektryczne niskiego napięcia", "Normy SEP", "Pozostałe normy"]:
        L += ["", f"### {g}", "", "| Norma | Tematy |", "|-------|--------|"]
        for n in sorted(grupy[g], key=klucz):
            L.append(f"| {n} | {linki([po_nr[x] for x in normy[n]])} |")
    (ROOT / "PRZEPISY.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"PRZEPISY.md: {len(AKTY)} aktów PL, {len(UE)} UE, {len(normy)} norm")
    for a in AKTY:
        if not akty[a["klucz"]]:
            print("  uwaga: brak tematów dla", a["klucz"])


if __name__ == "__main__":
    main()
