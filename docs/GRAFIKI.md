# Grafiki: zdjęcia i schematy

Repozytorium ma uczyć „na oko” — rozpoznawania aparatów, przewodów i błędów montażowych. Dlatego obrazy są tak samo ważne jak tekst i obowiązują je stałe zasady.

[← README](../README.md)

## Trzy źródła obrazów

| Źródło | Gdzie | Kiedy |
|--------|-------|-------|
| **Własne schematy SVG** | `assets/schematy/` | Układy połączeń, schematy jednokreskowe, układy sieci, strefy w łazience, drogi prądu — wszędzie, gdzie liczy się czytelność |
| **Zdjęcia z Wikimedia Commons** | `assets/foto/`, pobierane przez [tools/commons.py](../tools/commons.py) | Aparaty, przewody, osprzęt, prawdziwe instalacje |
| **Zdjęcia własne** | `assets/foto/` z wpisem „fot. własna” w CREDITS | Gdy na Commons nie ma dobrego ujęcia; brakujące oznacz `📷 DO ZROBIENIA` |

Zdjęcia producentów (katalogi, karty katalogowe) **tylko jako linki** w sekcji „Źródła” — nie kopiujemy ich do repozytorium.

## Zdjęcia z Wikimedia Commons

1. Znajdź plik na [commons.wikimedia.org](https://commons.wikimedia.org). Dopuszczalne licencje: domena publiczna, CC0, CC BY, CC BY-SA. **Nie używamy** plików z licencjami NC (niekomercyjne) i ND (bez utworów zależnych).
2. Pobierz go skryptem — zapisze plik i dopisze autora, licencję i link do `assets/CREDITS.md`:

   ```bash
   python3 tools/commons.py "File:Nazwa pliku.jpg" 07-wylacznik-b16.jpg
   ```

3. Wstaw do tematu z tekstem alternatywnym i podpisem „Na co patrzeć”.

Skrypt pobiera wersję o szerokości do 1280 px, żeby repozytorium nie puchło, i dopisuje plik do listy `assets/foto/ZDJECIA.tsv`.

**Bez dostępu do Commons na własnym komputerze** wystarczy dopisać wiersz `nazwa-pliku.jpg<TAB>File:Tytuł na Commons.jpg` do `assets/foto/ZDJECIA.tsv` i zrobić push — workflow [zdjecia.yml](../.github/workflows/zdjecia.yml) pobierze brakujące pliki, dopisze autorów do CREDITS i zacommituje wynik. Zdjęcie z listy, którego jeszcze nie ma, `check_images.py` zgłasza jako ⏳, a nie jako błąd.

## Nazwy plików

`NN-opis-po-polsku-bez-ogonkow.ext`, gdzie `NN` to numer modułu, w którym obraz pojawia się pierwszy raz. Przykłady: `07-wylacznik-b16.jpg`, `11-uklad-tn-c-s.svg`, `17-lazienka-strefy.svg`.

## Styl schematów SVG

- Białe tło (`<rect fill="#ffffff">` jako pierwszy element) — schemat musi być czytelny także w ciemnym motywie GitHuba.
- Symbole graficzne wg PN-EN 60617.
- Kolory przewodów jak w rzeczywistości: **L** — brązowy (L1), czarny (L2), szary (L3); **N** — niebieski; **PE** — żółto-zielony (kreskowany zielono-żółty); **PEN** — żółto-zielony z niebieskimi końcami.
- Kolor jest tylko pomocą: każdy przewód ma też etykietę (L, N, PE), żeby schemat był czytelny w druku czarno-białym.
- Czcionka bezszeryfowa, napisy po polsku, rozmiar czytelny przy szerokości 800 px.
- Źródło edytowalne: SVG piszemy ręcznie albo w programie (np. Inkscape, draw.io z eksportem do SVG); plik musi być czytelnym tekstem, bez osadzonych bitmap.

## Tekst alternatywny i podpis

- **Alt** opisuje, *co* jest na obrazie: „Rozdzielnica mieszkaniowa z wyłącznikiem głównym, dwoma wyłącznikami różnicowoprądowymi i dziesięcioma wyłącznikami nadprądowymi”.
- **Podpis** mówi, *na co patrzeć*: „Zwróć uwagę, że listwa N jest podzielona na dwie części — każda różnicówka ma własną”.

Sprawdzanie: [tools/check_images.py](../tools/check_images.py) zgłasza brak pliku, brak tekstu alternatywnego i zdjęcie bez wpisu w CREDITS.
