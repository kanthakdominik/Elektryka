"""Buduje strony www/: egzamin.html (trening z bazą pytań i liczb) i kalkulatory.html.

Uruchom: python3 tools/gen_www.py [--fragment KATALOG]
  --fragment — dodatkowo zapisuje wersje bez <!doctype>/<head> (do publikacji jako Artifact).
Szablony i wspólny CSS: tools/www/.
"""
import argparse
import html
import json
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from baza_pytan import ROOT, pytania, liczby, tematy  # noqa: E402

REPO = "https://github.com/kanthakdominik/elektryka/blob/main/"
TPL = Path(__file__).parent / "www"

GREK = {"cdot": "·", "times": "×", "le": "≤", "leq": "≤", "ge": "≥", "geq": "≥", "approx": "≈", "neq": "≠",
        "Omega": "Ω", "Delta": "Δ", "varphi": "φ", "phi": "φ", "mu": "µ", "pi": "π", "rho": "ρ", "gamma": "γ",
        "eta": "η", "alpha": "α", "lambda": "λ", "omega": "ω", "theta": "θ", "sum": "Σ", "pm": "±", "infty": "∞",
        "ldots": "…", "dots": "…", "to": "→", "rightarrow": "→", "Rightarrow": "⇒", "circ": "°", "sim": "~",
        "cos": "cos ", "sin": "sin ", "ln": "ln ", "tg": "tg ", "checkmark": "✓", "quad": "  ", "qquad": "   "}


GREK_SPACJA = {"cdot", "times", "le", "leq", "ge", "geq", "approx", "neq", "to", "rightarrow", "Rightarrow", "pm", "sim", "quad", "qquad"}


def _grupa(s, i):
    """Zwraca (zawartość {…} od pozycji i, indeks za klamrą)."""
    if i < len(s) and s[i] == "{":
        d, j = 0, i
        while j < len(s):
            d += {"{": 1, "}": -1}.get(s[j], 0)
            if d == 0:
                return s[i + 1:j], j + 1
            j += 1
    return (s[i], i + 1) if i < len(s) else ("", i)


def latex(s):
    """Prosty LaTeX → tekst z <sub>/<sup> (wystarcza dla wzorów z tematów)."""
    out, i = [], 0
    while i < len(s):
        c = s[i]
        if c == "\\":
            m = re.match(r"\\([A-Za-z]+)|\\(.)", s[i:])
            if not m:
                i += 1
                continue
            cmd = m.group(1) or m.group(2)
            i += m.end()
            if m.group(1) and cmd not in GREK_SPACJA:
                while i < len(s) and s[i] == " ":
                    i += 1
            if cmd in ("frac", "dfrac", "tfrac"):
                a, i = _grupa(s, i)
                b, i = _grupa(s, i)
                a, b = latex(a), latex(b)
                wrap = lambda x: x if re.fullmatch(r"[\w.,·µΩ]+", re.sub(r"<[^>]+>", "", x)) else f"({x})"
                out.append(f"{wrap(a)}/{wrap(b)}")
            elif cmd == "sqrt":
                a, i = _grupa(s, i)
                out.append(f"√({latex(a)})" if len(a) > 1 else f"√{latex(a)}")
            elif cmd in ("mathrm", "text", "operatorname", "mathbf", "textrm", "mathit"):
                a, i = _grupa(s, i)
                out.append(latex(a) if cmd != "text" else a)
            elif cmd in ("left", "right", "big", "Big"):
                pass
            elif cmd == ",":
                out.append(" ")
            elif cmd == " ":
                out.append(" ")
            elif cmd in ("%", "{", "}", "$", "_", "#", "&"):
                out.append(cmd)
            else:
                out.append(GREK.get(cmd, ""))
        elif c in "_^":
            a, i = _grupa(s, i + 1)
            tag = "sub" if c == "_" else "sup"
            out.append(f"<{tag}>{latex(a)}</{tag}>")
        elif c == "{":
            a, i = _grupa(s, i)
            out.append(latex(a))
        elif c == "}":
            i += 1
        else:
            out.append(c)
            i += 1
    return re.sub(r" {2,}", "  ", "".join(out)).strip()


def inline(t, src_dir):
    """Markdown w linii → HTML. Matematyka i linki najpierw zamieniane na znaczniki."""
    schowek = []

    def chowaj(h):
        schowek.append(h)
        return f"\x00{len(schowek) - 1}\x00"
    t = re.sub(r"\$\$(.+?)\$\$", lambda m: chowaj(f'<span class="m">{latex(html.unescape(m.group(1)))}</span>'), t, flags=re.S)
    t = re.sub(r"\$(.+?)\$", lambda m: chowaj(f'<span class="m">{latex(html.unescape(m.group(1)))}</span>'), t)

    def link(m):
        etyk, url = m.group(1), m.group(2)
        if not re.match(r"^[a-z]+:", url):
            path, _, frag = url.partition("#")
            absp = (src_dir / path).resolve()
            try:
                url = REPO + absp.relative_to(ROOT).as_posix() + ("#" + frag if frag else "")
            except ValueError:
                return etyk
        return chowaj(f'<a href="{html.escape(url)}" target="_blank" rel="noopener">') + etyk + chowaj("</a>")
    t = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", t)
    t = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link, t)
    t = html.escape(t, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<i>\1</i>", t)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    return re.sub(r"\x00(\d+)\x00", lambda m: schowek[int(m.group(1))], t)


def blok(t, src_dir):
    """Markdown blokowy (akapity, listy) → HTML."""
    out = []
    for akap in re.split(r"\n\s*\n", t.strip()):
        linie = akap.splitlines()
        if all(re.match(r"\s*([-*]|\d+\.)\s", l) for l in linie if l.strip()):
            tag = "ol" if re.match(r"\s*\d+\.", linie[0]) else "ul"
            pozycje = [inline(re.sub(r"^\s*([-*]|\d+\.)\s+", "", l), src_dir) for l in linie if l.strip()]
            out.append(f"<{tag}>" + "".join(f"<li>{p}</li>" for p in pozycje) + f"</{tag}>")
        else:
            out.append("<p>" + inline(" ".join(l.strip() for l in linie), src_dir) + "</p>")
    return "".join(out)


def grupy(t):
    g = list(t["zakres"])
    nr = int(t["nr"][:2])
    if nr in (32, 33):
        g.append("D")
    if nr == 34:
        g.append("SN")
    return g or ["c"]


def dane():
    P, L = [], []
    licz = {}
    for x in pytania():
        k = (x["nr"], x["rodzaj"])
        licz[k] = licz.get(k, 0) + 1
        d = x["plik"].parent
        P.append({"id": f"{x['nr']}{'S' if x['rodzaj'] == 'SEP' else 'P'}{licz[k]}",
                  "n": x["nr"], "t": x["tytul"].split("—", 1)[-1].strip(),
                  "u": REPO + x["plik"].relative_to(ROOT).as_posix(), "z": grupy(x),
                  "r": "S" if x["rodzaj"] == "SEP" else "P",
                  "q": inline(x["pytanie"], d), "a": blok(x["odpowiedz"], d)})
    licz = {}
    for x in liczby():
        licz[x["nr"]] = licz.get(x["nr"], 0) + 1
        d = x["plik"].parent
        L.append({"id": f"{x['nr']}L{licz[x['nr']]}", "n": x["nr"], "t": x["tytul"].split("—", 1)[-1].strip(),
                  "u": REPO + x["plik"].relative_to(ROOT).as_posix() + "#liczby-do-zapamiętania", "z": grupy(x),
                  "w": inline(x["wielkosc"], d), "v": inline(x["wartosc"], d),
                  "k": inline(x["kiedy"], d) if x["kiedy"] not in ("—", "-", "jw.") else "",
                  "s": inline(x["zrodlo"], d) if x["zrodlo"] not in ("—", "-") else ""})
    return {"pytania": P, "liczby": L,
            "meta": {"data": date.today().isoformat(), "tematy": sum(1 for _ in tematy())}}


def pelny(fragment, tytul_lang="pl"):
    """Fragment strony → pełny dokument do otwarcia z dysku."""
    return ('<!doctype html>\n<html lang="pl">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            + fragment.replace("<div class=\"wrap\">", "</head>\n<body>\n<div class=\"wrap\">", 1)
            + "\n</body>\n</html>\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fragment", help="katalog na wersje-fragmenty (Artifact)")
    a = ap.parse_args()
    css = (TPL / "wspolne.css").read_text(encoding="utf-8")
    d = dane()
    js = json.dumps(d, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    strony = {
        "egzamin.html": (TPL / "egzamin.tpl.html").read_text(encoding="utf-8").replace("/*CSS*/", css).replace("/*DANE*/", js),
        "kalkulatory.html": (TPL / "kalkulatory.tpl.html").read_text(encoding="utf-8").replace("/*CSS*/", css),
    }
    (ROOT / "www").mkdir(exist_ok=True)
    for nazwa, frag in strony.items():
        (ROOT / "www" / nazwa).write_text(pelny(frag), encoding="utf-8")
        if a.fragment:
            Path(a.fragment).mkdir(parents=True, exist_ok=True)
            (Path(a.fragment) / nazwa).write_text(frag, encoding="utf-8")
    print(f"www/: egzamin.html ({len(d['pytania'])} pytań, {len(d['liczby'])} liczb), kalkulatory.html")


if __name__ == "__main__":
    main()
