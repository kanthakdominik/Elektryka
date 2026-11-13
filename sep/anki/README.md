# Fiszki do Anki

Dwie talie wygenerowane z repozytorium — do nauki metodą powtórek rozłożonych w czasie ([Anki](https://apps.ankiweb.net/) — darmowa aplikacja na komputer i Android; na iOS płatna, ale talie działają też w przeglądarce AnkiWeb).

| Plik | Co zawiera | Liczba kart |
|------|------------|-------------|
| [pytania.tsv](pytania.tsv) | Pytania SEP i „Sprawdź się” ze wszystkich tematów, odpowiedź na odwrocie | ok. 620 |
| [liczby.tsv](liczby.tsv) | Wszystkie „Liczby do zapamiętania”: wielkość i warunek → wartość i źródło | ok. 970 |

[← sep/](../README.md)

## Jak zaimportować

1. Pobierz plik `.tsv` (na GitHubie: otwórz plik → przycisk **Download raw file**).
2. W Anki: **Plik → Importuj** i wskaż pobrany plik.
3. Typ notatki: **Basic** (lub „Podstawowy”), talia: np. „Elektryka — pytania”.
4. Plik ma nagłówek, więc Anki sam rozpozna separator (tabulator), HTML i kolumnę z tagami.
5. Zatwierdź **Importuj**.

Wzory zapisane w LaTeX wyświetlają się dzięki wbudowanemu w Anki MathJax.

## Tagi

Każda karta ma tagi:

- `elektryka::NN` — numer modułu (np. `elektryka::12`),
- `temat::NN_MM` — numer tematu,
- `SEP` — pytanie z sekcji „Pytania SEP” (typowe pytanie komisji),
- `liczby` — karta z talii liczb.

Dzięki temu w przeglądarce kart można zrobić **talię filtrowaną**, np. `tag:SEP` przed egzaminem albo `tag:elektryka::28 OR tag:elektryka::31` na blok BHP i pierwszej pomocy.

## Aktualizacja

Talie generuje skrypt `tools/gen_anki.py` z treści tematów. Po zmianach w repozytorium uruchom go ponownie i zaimportuj plik jeszcze raz — Anki zaktualizuje istniejące karty (pierwsza kolumna jest kluczem), a postęp nauki zostanie zachowany.
