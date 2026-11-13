"""Wyciąga pytania (Pytania SEP, Sprawdź się) i „Liczby do zapamiętania” z tematów.

Moduł pomocniczy dla generatorów: egzaminów próbnych, fiszek Anki, zbioru zadań i strony egzaminu.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MOD = ROOT / "modules"


def sekcja(text, name):
    m = re.search(r"^## " + re.escape(name) + r"\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    return m.group(1).strip() if m else ""


def tematy():
    for f in sorted(MOD.glob("*/[0-9][0-9].[0-9][0-9]-*.md")):
        tx = f.read_text(encoding="utf-8")
        tytul = tx.splitlines()[0].lstrip("# ").strip()
        meta = tx.splitlines()[2] if len(tx.splitlines()) > 2 else ""
        zakres = re.findall(r"\(([a-e])\)", meta.split("Zakres SEP")[-1]) if "Zakres SEP" in meta else []
        yield {"plik": f, "nr": f.name.split("-")[0], "modul": f.parent.name, "tytul": tytul,
               "zakres": zakres, "dom": "🏠" in meta, "tekst": tx}


def _pary(blok, wzorzec):
    """Zwraca listę (pytanie, odpowiedź) z bloku z <details>."""
    out = []
    czesci = re.split(wzorzec, blok, flags=re.M)
    # czesci: [przed, q1, reszta1, q2, reszta2, ...]
    for i in range(1, len(czesci) - 1, 2):
        q = czesci[i].strip()
        m = re.search(r"<summary>.*?</summary>\s*(.*?)\s*</details>", czesci[i + 1], re.S)
        if m:
            out.append((q, m.group(1).strip()))
    return out


def pytania():
    for t in tematy():
        for q, a in _pary(sekcja(t["tekst"], "Pytania SEP"), r"^\d+\. \*\*(.+?)\*\*\s*$"):
            yield {**t, "rodzaj": "SEP", "pytanie": q, "odpowiedz": a}
        for q, a in _pary(sekcja(t["tekst"], "Sprawdź się"), r"^\d+\. (.+?)\s*$"):
            yield {**t, "rodzaj": "sprawdz", "pytanie": q, "odpowiedz": a}


def liczby():
    """Wiersze tabel „Liczby do zapamiętania”; „jw.” zastępowane wartością z wiersza wyżej."""
    for t in tematy():
        blok = sekcja(t["tekst"], "Liczby do zapamiętania")
        poprz = {"kiedy": "", "zrodlo": ""}
        for line in blok.splitlines():
            if not line.startswith("|") or line.startswith("|--") or line.startswith("| Wielkość") or line.startswith("| Co "):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 2 or set(cells[0]) <= set("-: "):
                continue
            w = {"kiedy": cells[2] if len(cells) > 2 else "", "zrodlo": cells[3] if len(cells) > 3 else ""}
            for k in w:
                if w[k].strip().lower().startswith("jw"):
                    w[k] = poprz[k] + w[k].strip()[3:].rstrip()
                poprz[k] = w[k]
            yield {**t, "wielkosc": cells[0], "wartosc": cells[1], **w}


def przyklady():
    for t in tematy():
        blok = sekcja(t["tekst"], "Przykład")
        m = re.search(r"\*\*Zadanie\.\*\*\s*(.*?)\s*\*\*Rozwiązanie\.\*\*\s*(.*)", blok, re.S)
        if m:
            yield {**t, "zadanie": m.group(1).strip(), "rozwiazanie": m.group(2).strip()}


def link(t, z=ROOT / "sep", kotwica=""):
    rel = Path("..") / t["plik"].relative_to(ROOT) if z != ROOT else t["plik"].relative_to(ROOT)
    return f"[{t['nr']}]({rel.as_posix()}{kotwica})"


if __name__ == "__main__":
    p = list(pytania())
    print("pytania SEP:", sum(1 for x in p if x["rodzaj"] == "SEP"), "sprawdź się:", sum(1 for x in p if x["rodzaj"] == "sprawdz"))
    print("liczby:", len(list(liczby())), "przykłady:", len(list(przyklady())))
    print("bez zakresu:", sorted({x['nr'] for x in p if not x['zakres']})[:20])


def przenies_linki(tekst, src_dir, dst_dir, obrazy=False):
    """Przelicza względne linki Markdown z katalogu src_dir na dst_dir (obrazy=True — także ![...](...))."""
    import os

    def rep(m):
        label, url = m.group(1), m.group(2)
        if re.match(r"^[a-z]+:", url) or url.startswith("#"):
            return m.group(0)
        path, _, frag = url.partition("#")
        absp = (Path(src_dir) / path).resolve()
        rel = os.path.relpath(absp, Path(dst_dir).resolve()).replace(os.sep, "/")
        return f"[{label}]({rel}{'#' + frag if frag else ''})"
    wzor = r"\[([^\]]*)\]\(([^)\s]+)\)" if obrazy else r"(?<!!)\[([^\]]+)\]\(([^)\s]+)\)"
    return re.sub(wzor, rep, tekst)
