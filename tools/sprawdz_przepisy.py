"""Sprawdza w API Sejmu (ELI), czy kluczowe akty prawne się zmieniły, i szuka nowych warunków technicznych.

Uruchom: python3 tools/sprawdz_przepisy.py [--stan tools/przepisy-stan.json] [--raport zmiany.md]
Porównuje: status, „w mocy”, datę zmiany i listę powiązanych aktów (zmiany, teksty jednolite, uchylenia).
Gdy coś się zmieniło — zapisuje raport Markdown (do zgłoszenia) i aktualizuje plik stanu.
Pierwsze uruchomienie (brak stanu) zapisuje stan bez raportu.
"""
import argparse
import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from przepisy_lista import AKTY, NOWE_WT, eli_url  # noqa: E402

API = "https://api.sejm.gov.pl/eli"
KLUCZE_REF = ("Akty zmieniające", "Inf. o tekście jednolitym", "Tekst jednolity dla aktu", "Akty uchylające",
              "Uchylenia wynikające z", "Akty wykonawcze", "Akty uznane za uchylone")


def pobierz(url, proby=3):
    ost = None
    for i in range(proby):
        try:
            req = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": "elektryka-alert-przepisow"})
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:  # sieć, 5xx, zły JSON
            ost = e
            time.sleep(2 * (i + 1))
    raise RuntimeError(f"{url}: {ost}")


def odcisk(d):
    refs = []
    for k, v in (d.get("references") or {}).items():
        if any(k.startswith(x) for x in KLUCZE_REF) and isinstance(v, list):
            refs += [f"{k}: {x.get('id', '?')}" for x in v if isinstance(x, dict)]
    return {"tytul": d.get("title", ""), "status": d.get("status", ""), "w_mocy": d.get("inForce", ""),
            "data_zmiany": d.get("changeDate", ""), "powiazane": sorted(set(refs))}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--stan", default=str(Path(__file__).parent / "przepisy-stan.json"))
    ap.add_argument("--raport", default="zmiany.md")
    a = ap.parse_args()
    p_stan = Path(a.stan)
    stary = json.loads(p_stan.read_text(encoding="utf-8")) if p_stan.exists() else None
    nowy, bledy, zmiany = {}, [], []

    for akt in AKTY:
        try:
            d = pobierz(f"{API}/acts/{akt['eli']}")
            nowy[akt["eli"]] = odcisk(d)
            print(f"OK  {akt['eli']}: {nowy[akt['eli']]['status']} · zmiana {nowy[akt['eli']]['data_zmiany']} · powiązań {len(nowy[akt['eli']]['powiazane'])}")
        except Exception as e:
            bledy.append(str(e))
            print("BŁĄD", e)
            if stary and akt["eli"] in stary:
                nowy[akt["eli"]] = stary[akt["eli"]]

    try:
        q = urllib.parse.urlencode({"publisher": "DU", "title": NOWE_WT["title"], "dateFrom": NOWE_WT["od"], "limit": 50})
        wyn = pobierz(f"{API}/acts/search?{q}")
        nowy["_nowe_wt"] = sorted({f"{x.get('ELI', '?')} — {x.get('title', '')}" for x in wyn.get("items", [])})
        print(f"OK  wyszukiwanie WT: {len(nowy['_nowe_wt'])} wyników")
    except Exception as e:
        bledy.append(str(e))
        print("BŁĄD", e)
        if stary and "_nowe_wt" in stary:
            nowy["_nowe_wt"] = stary["_nowe_wt"]

    if len(bledy) > len(AKTY) // 2:
        print(f"Za dużo błędów ({len(bledy)}) — przerywam bez zmian.")
        sys.exit(1)

    if stary is not None:
        for akt in AKTY:
            s, n = stary.get(akt["eli"]), nowy.get(akt["eli"])
            if not s or not n or s == n:
                continue
            linie = [f"### {akt['nazwa']}", f"[{akt['eli']}]({eli_url(akt['eli'])}) · ostatni znany tekst jednolity w bazie: {akt['tj']}", ""]
            for k in ("status", "w_mocy", "data_zmiany"):
                if s.get(k) != n.get(k):
                    linie.append(f"- **{k}**: `{s.get(k)}` → `{n.get(k)}`")
            nowe = sorted(set(n.get("powiazane", [])) - set(s.get("powiazane", [])))
            linie += [f"- nowe powiązanie: {x}" for x in nowe]
            zmiany.append("\n".join(linie))
        nowe_wt = sorted(set(nowy.get("_nowe_wt", [])) - set(stary.get("_nowe_wt", [])))
        if nowe_wt:
            zmiany.append("### Możliwe nowe warunki techniczne\n" + "\n".join(f"- {x}" for x in nowe_wt) +
                          "\n\nSprawdź i zaktualizuj [32.04](../blob/main/modules/32-przepisy-i-normy/32.04-warunki-techniczne-budynkow-instalacja.md).")

    p_stan.write_text(json.dumps(nowy, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    if stary is None:
        print("Pierwsze uruchomienie — zapisano stan, bez raportu.")
    if zmiany:
        tekst = ("Automat wykrył zmiany w aktach prawnych cytowanych w bazie. Do zrobienia: przeczytaj zmiany, popraw tematy "
                 "(lista w [PRZEPISY.md](../blob/main/PRZEPISY.md)), zaktualizuj pole `tj` w `tools/przepisy_lista.py` i uruchom `python3 tools/gen_przepisy.py`.\n\n"
                 + "\n\n".join(zmiany))
        if bledy:
            tekst += "\n\n<details><summary>Błędy pobierania</summary>\n\n" + "\n".join(f"- {b}" for b in bledy) + "\n</details>"
        Path(a.raport).write_text(tekst + "\n", encoding="utf-8")
        print(f"Zmiany: {len(zmiany)} — raport w {a.raport}")
    else:
        print("Bez zmian.")


if __name__ == "__main__":
    main()
