# Wersje PDF do druku

| Plik | Zawartość |
|------|-----------|
| [sciagi-modulow.pdf](sciagi-modulow.pdf) | ściągi wszystkich 35 modułów (liczby, zasady, wzory) |
| [sep-powtorka.pdf](sep-powtorka.pdf) | [powtórka 48 h](../sep/powtorka-48h.md), [pułapki egzaminacyjne](../sep/pulapki.md), [ściąga przepisów dla D](../sep/sciaga-dozor.md) |
| [listy-kontrolne.pdf](listy-kontrolne.pdf) | sześć [list kontrolnych](../listy-kontrolne/README.md) |
| [wzory.pdf](wzory.pdf) | [protokół z pomiarów](../wzory/protokol-pomiarow.md) i [opis rozdzielnicy](../wzory/opis-rozdzielnicy.md) |

**Cała baza w jednym PDF** (wszystkie tematy ze schematami i zdjęciami) powstaje automatycznie w GitHub Actions: zakładka *Actions* → przebieg **pdf** → artefakt **elektryka-pdf**. Lokalnie: `python3 tools/build_pdf.py --ksiazka` (plik `build/elektryka.pdf`).

Odświeżenie plików w tym katalogu: `python3 tools/build_pdf.py` (wymaga `pip install markdown playwright` i `python -m playwright install chromium`).
