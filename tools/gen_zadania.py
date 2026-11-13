"""Generuje ZADANIA.md — zbiór zadań i sytuacji z sekcji „Przykład” wszystkich tematów.

Uruchom: python3 tools/gen_zadania.py
Rozwiązania są schowane w <details>, żeby najpierw spróbować samemu.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from baza_pytan import ROOT, MOD, tematy, sekcja, przenies_linki  # noqa: E402
from check_links import github_slug  # noqa: E402

START = re.compile(r"^\*\*(Zadanie|Sytuacja)[^*]*\*\*", re.M)
LICZ = re.compile(r"\$|\d\s*[=·×/]\s*\d|=\s*\d|\d\s*(?:A|V|W|Ω|kW|mm²|m)\b\s*[·×/]")


def bloki(sekcja_txt):
    """Dzieli sekcję Przykład na zadania: (treść, rozwiązanie)."""
    starty = [m.start() for m in START.finditer(sekcja_txt)] or [0]
    out = []
    for i, s in enumerate(starty):
        kawalek = sekcja_txt[s: starty[i + 1] if i + 1 < len(starty) else len(sekcja_txt)].strip()
        akapity = re.split(r"\n\s*\n", kawalek, maxsplit=1)
        tresc = akapity[0].strip()
        rozw = akapity[1].strip() if len(akapity) > 1 else ""
        # format „**Zadanie.** … **Rozwiązanie.** …” w jednym akapicie
        if not rozw and "**Rozwiązanie" in tresc:
            tresc, _, rozw = tresc.partition("**Rozwiązanie")
            rozw = "**Rozwiązanie" + rozw
        out.append((tresc.strip(), rozw.strip()))
    return out


def tytul_modulu(katalog):
    readme = MOD / katalog / "README.md"
    if readme.exists():
        return readme.read_text(encoding="utf-8").splitlines()[0].lstrip("# ").strip()
    return katalog


def main():
    wpisy = {}
    licz = {"obl": 0, "syt": 0}
    for t in tematy():
        s = sekcja(t["tekst"], "Przykład")
        if not s:
            continue
        for tresc, rozw in bloki(s):
            obl = bool(LICZ.search(tresc + rozw))
            licz["obl" if obl else "syt"] += 1
            tresc = przenies_linki(tresc, t["plik"].parent, ROOT, obrazy=True)
            rozw = przenies_linki(rozw, t["plik"].parent, ROOT, obrazy=True)
            wpisy.setdefault(t["modul"], []).append((t, obl, tresc, rozw))

    razem = licz["obl"] + licz["syt"]
    L = ["# Zbiór zadań i sytuacji", "",
         "> Wszystkie przykłady z tematów w jednym miejscu: najpierw spróbuj sam, potem rozwiń **Rozwiązanie**.",
         f"> **{razem}** pozycji: 🧮 **{licz['obl']}** obliczeniowych (wzór, liczby, wynik) i 🔎 **{licz['syt']}** sytuacji do oceny (co jest źle, co zrobić).",
         "> Plik jest generowany skryptem [`tools/gen_zadania.py`](tools/gen_zadania.py) — poprawki rób w tematach, nie tutaj.",
         "", "**Tylko obliczeniowe?** Szukaj znaczka 🧮 (Ctrl+F). Kalkulatory do sprawdzenia wyników: [www/kalkulatory.html](www/kalkulatory.html).",
         "", "## Spis", ""]
    naglowki = []
    for kat in sorted(wpisy):
        nr = kat[:2]
        h = f"{nr} — {tytul_modulu(kat).split('—', 1)[-1].strip()}"
        naglowki.append((kat, h))
        n_obl = sum(1 for w in wpisy[kat] if w[1])
        L.append(f"- [{h}](#{github_slug(h)}) · {len(wpisy[kat])} ({n_obl} 🧮)")
    L.append("")
    for kat, h in naglowki:
        L += ["---", "", f"## {h}", ""]
        for i, (t, obl, tresc, rozw) in enumerate(wpisy[kat], 1):
            rel = t["plik"].relative_to(ROOT).as_posix()
            znak = "🧮" if obl else "🔎"
            L.append(f"{znak} **[{t['nr']}]({rel}#przykład)** · {t['tytul'].split('—', 1)[-1].strip()}")
            L.append("")
            L.append(tresc)
            L.append("")
            if rozw:
                L += ["<details><summary>Rozwiązanie</summary>", "", rozw, "", "</details>", ""]
    (ROOT / "ZADANIA.md").write_text("\n".join(L).rstrip() + "\n", encoding="utf-8")
    print(f"ZADANIA.md: {razem} pozycji ({licz['obl']} obliczeniowych, {licz['syt']} sytuacji)")


if __name__ == "__main__":
    main()
