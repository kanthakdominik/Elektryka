# Elektryka — od podstaw do rozdzielnicy i uprawnień SEP

Otwarta baza wiedzy z elektryki ogólnej, pisana prostym językiem i z dużą liczbą zdjęć i schematów. Ma dwa cele:

- **zrozumieć instalację elektryczną w domu i mieszkaniu** — od gniazdka, przez rozdzielnicę, po przyłącze — na tyle, żeby świadomie planować, oceniać i wykonywać prace,
- **przygotować się do egzaminu kwalifikacyjnego** na świadectwo grupy 1 (urządzenia elektroenergetyczne), stanowisko eksploatacji (E), do 1 kV, razem z czynnościami kontrolno-pomiarowymi.

Repozytorium jest pomyślane jako darmowy materiał dla każdego: osoby remontującej mieszkanie, przyszłego elektryka i inżyniera, który chce uporządkować praktykę.

> ⚠️ **Najpierw bezpieczeństwo.** Repozytorium uczy, jak instalacja działa i jak się przy niej pracuje, ale nie zastępuje uprawnień, pomiarów ani doświadczenia. Zanim wykonasz jakąkolwiek pracę, przeczytaj moduł [00 — Zanim dotkniesz czegokolwiek](modules/00-bezpieczenstwo-najpierw/README.md). Prace przy instalacji wykonuj tylko po wyłączeniu i sprawdzeniu braku napięcia, a nowe obwody i zmiany w rozdzielnicy zawsze kończ pomiarami.

Zasady:

- **Treść jest po polsku** i odnosi się do polskich przepisów i norm.
- **Najpierw intuicja, potem liczby.** Każde pojęcie jest najpierw wyjaśnione „po ludzku”, a dopiero potem podany jest termin normowy i wzór.
- **Dużo obrazów.** Własne schematy SVG oraz zdjęcia na wolnych licencjach z podanym autorem (zasady w [docs/GRAFIKI.md](docs/GRAFIKI.md)).
- **Przepisy z dokładnym odnośnikiem** — akt, paragraf, punkt. Normy z numerem i częścią.
- Linki i obrazy są sprawdzane automatycznie przy każdym pushu.

---

## Jak korzystać z repozytorium

1. Przeczytaj [ROADMAP.md](ROADMAP.md) — kolejność modułów, zależności, trzy ścieżki nauki (SEP, dom, pełna) i szacowany czas.
2. Przejrzyj [RESOURCES.md](RESOURCES.md) — przepisy, normy, książki i poradniki, do których odwołują się moduły.
3. Przygotowujesz się do egzaminu? Zacznij od [sep/](sep/README.md): jak wygląda egzamin, co wpisać we wniosek, [mapa zakresu egzaminu na moduły](sep/zakres.md) i [bank pytań](sep/pytania.md).
4. Sprawdź [NARZEDZIA.md](NARZEDZIA.md) — czego potrzebujesz do bezpiecznej pracy i pomiarów.
5. Przerabiaj moduły. Każdy temat ma ten sam układ (pełny opis w [docs/SZABLON-TEMATU.md](docs/SZABLON-TEMATU.md)):

| Sekcja | Co zawiera |
|--------|------------|
| **Po co to jest** | Gdzie spotkasz to w domu i o co zapyta komisja |
| **Po ludzku** | Wyjaśnienie bez wzorów, z analogią |
| **Jak to wygląda** | Zdjęcia z podpisem „na co patrzeć” |
| **Schemat** | Schemat SVG albo diagram Mermaid |
| **Pojęcia** | Pojęcie — wyjaśnienie — termin normowy |
| **Liczby do zapamiętania** | Wartości i wzory razem z warunkami stosowania |
| **W praktyce** | Procedura krok po kroku |
| **Błędy i zagrożenia** | Typowe błędy, także te groźne dla życia |
| **Przykład** | Obliczenie albo przypadek z życia |
| **Pytania SEP** | Pytania jak na egzaminie ustnym, wzorcowe odpowiedzi pod `<details>` |
| **Sprawdź się** | „Rozpoznaj na zdjęciu”, „znajdź błąd na schemacie” |
| **Źródła** | Konkretne paragrafy, rozdziały norm i poradników |

6. Do powtórki: każdy moduł ma **ściągę** (`SCIAGA.md`), a przed egzaminem jest [powtórka 48 h](sep/powtorka-48h.md). Nieznane słowo sprawdzisz w [słowniczku](SLOWNICZEK.md).
7. Postęp odznaczaj w checklistach (`- [ ]` → `- [x]`) we własnym forku.

### Oznaczenia

| Znak | Znaczenie |
|------|-----------|
| 🟢 | Podstawy — dla każdego, bez wzorów albo z najprostszymi |
| 🏠 | Praktyka w domu i mieszkaniu |
| 📋 | Egzamin SEP — temat pojawia się na egzaminie kwalifikacyjnym |

Temat może mieć kilka oznaczeń. Przy każdym temacie podany jest też **zakres SEP** — litery (a)–(e) odpowiadają obszarom wiedzy wymaganym na stanowisku eksploatacji (§ 6 ust. 1 pkt 1 rozporządzenia, opis w [sep/zakres.md](sep/zakres.md)).

---

## Mapa modułów

<!-- mapa:start -->
### I. Fundamenty po ludzku

| # | Moduł | Oznaczenia | Tematów | Status |
|---|-------|------------|---------|--------|
| 00 | [Zanim dotkniesz czegokolwiek](modules/00-bezpieczenstwo-najpierw/README.md) | 🟢🏠📋 | 4 | ✅ pełny |
| 01 | [Prąd, napięcie, opór, moc i energia](modules/01-prad-napiecie-opor/README.md) | 🟢 | 7 | ✅ pełny |
| 02 | [Prąd przemienny i sieć 230/400 V](modules/02-prad-przemienny-230-400/README.md) | 🟢📋 | 5 | ✅ pełny |
| 03 | [Elektromagnetyzm w praktyce](modules/03-elektromagnetyzm-w-praktyce/README.md) | 🟢 | 4 | ✅ pełny |
| 04 | [Prąd a człowiek](modules/04-prad-a-czlowiek/README.md) | 🟢📋 | 5 | ✅ pełny |

### II. Elementy instalacji

| # | Moduł | Oznaczenia | Tematów | Status |
|---|-------|------------|---------|--------|
| 05 | [Przewody i kable](modules/05-przewody-i-kable/README.md) | 🏠📋 | 7 | ✅ pełny |
| 06 | [Osprzęt instalacyjny](modules/06-osprzet-instalacyjny/README.md) | 🏠 | 6 | ✅ pełny |
| 07 | [Zabezpieczenia nadprądowe](modules/07-zabezpieczenia-nadpradowe/README.md) | 🏠📋 | 7 | ✅ pełny |
| 08 | [Wyłączniki różnicowoprądowe](modules/08-wylaczniki-roznicowopradowe/README.md) | 🏠📋 | 7 | ✅ pełny |
| 09 | [Ochrona przeciwprzepięciowa](modules/09-ochrona-przeciwprzepieciowa/README.md) | 🏠📋 | 5 | ✅ pełny |
| 10 | [Aparatura modułowa](modules/10-aparatura-modulowa/README.md) | 🏠 | 6 | ✅ pełny |

### III. Systemy ochrony

| # | Moduł | Oznaczenia | Tematów | Status |
|---|-------|------------|---------|--------|
| 11 | [Układy sieci: TN, TT, IT](modules/11-uklady-sieci/README.md) | 🟢📋 | 6 | ✅ pełny |
| 12 | [Ochrona przeciwporażeniowa](modules/12-ochrona-przeciwporazeniowa/README.md) | 📋 | 6 | ✅ pełny |
| 13 | [Uziemienia i połączenia wyrównawcze](modules/13-uziemienia-i-wyrownanie/README.md) | 🏠📋 | 6 | ✅ pełny |

### IV. Dom i mieszkanie

| # | Moduł | Oznaczenia | Tematów | Status |
|---|-------|------------|---------|--------|
| 14 | [Od słupa do gniazdka](modules/14-od-slupa-do-gniazdka/README.md) | 🏠📋 | 5 | ✅ pełny |
| 15 | [Rozdzielnica mieszkaniowa](modules/15-rozdzielnica-mieszkaniowa/README.md) | 🏠📋 | 7 | ✅ pełny |
| 16 | [Planowanie obwodów](modules/16-planowanie-obwodow/README.md) | 🏠📋 | 6 | ✅ pełny |
| 17 | [Pomieszczenia i miejsca szczególne](modules/17-pomieszczenia-szczegolne/README.md) | 🏠📋 | 5 | ✅ pełny |
| 18 | [Oświetlenie](modules/18-oswietlenie/README.md) | 🏠 | 6 | ✅ pełny |
| 19 | [Prace krok po kroku](modules/19-prace-krok-po-kroku/README.md) | 🏠 | 7 | 🔲 szkielet |
| 20 | [Diagnostyka usterek](modules/20-diagnostyka-usterek/README.md) | 🏠📋 | 7 | 🔲 szkielet |
| 21 | [Stare instalacje](modules/21-stare-instalacje/README.md) | 🏠📋 | 5 | 🔲 szkielet |

### V. Pomiary

| # | Moduł | Oznaczenia | Tematów | Status |
|---|-------|------------|---------|--------|
| 22 | [Przyrządy pomiarowe](modules/22-przyrzady-pomiarowe/README.md) | 🏠📋 | 6 | 🔲 szkielet |
| 23 | [Pomiary odbiorcze i okresowe](modules/23-pomiary-odbiorcze-i-okresowe/README.md) | 📋 | 8 | 🔲 szkielet |

### VI. Odbiorniki i nowe technologie

| # | Moduł | Oznaczenia | Tematów | Status |
|---|-------|------------|---------|--------|
| 24 | [Silniki i napędy](modules/24-silniki-i-napedy/README.md) | 📋 | 8 | 🔲 szkielet |
| 25 | [Transformatory, zasilacze, UPS i agregaty](modules/25-transformatory-ups-agregaty/README.md) | 🏠📋 | 5 | 🔲 szkielet |
| 26 | [Fotowoltaika, pompy ciepła, wallboxy i magazyny energii](modules/26-fotowoltaika-pompy-wallboxy/README.md) | 🏠📋 | 6 | 🔲 szkielet |
| 27 | [Inteligentny dom](modules/27-inteligentny-dom/README.md) | 🏠 | 4 | 🔲 szkielet |

### VII. BHP, eksploatacja i egzamin

| # | Moduł | Oznaczenia | Tematów | Status |
|---|-------|------------|---------|--------|
| 28 | [BHP przy urządzeniach elektrycznych](modules/28-bhp-przy-urzadzeniach/README.md) | 📋 | 6 | 🔲 szkielet |
| 29 | [Eksploatacja urządzeń i instalacji](modules/29-eksploatacja/README.md) | 📋 | 5 | 🔲 szkielet |
| 30 | [Pożar i awaria](modules/30-pozar-i-awaria/README.md) | 📋 | 5 | 🔲 szkielet |
| 31 | [Pierwsza pomoc przy porażeniu](modules/31-pierwsza-pomoc/README.md) | 📋 | 5 | 🔲 szkielet |
| 32 | [Przepisy i normy](modules/32-przepisy-i-normy/README.md) | 📋 | 6 | 🔲 szkielet |

### VIII. Rozszerzenia (opcjonalne)

| # | Moduł | Oznaczenia | Tematów | Status |
|---|-------|------------|---------|--------|
| 33 | [Dozór (D)](modules/33-dozor/README.md) | 📋 | 6 | 🔲 szkielet |
| 34 | [Sieci SN i stacje transformatorowe](modules/34-sieci-sn-i-stacje/README.md) | 📋 | 5 | 🔲 szkielet |
<!-- mapa:end -->

🔲 szkielet — lista tematów i układ sekcji · 🟡 w trakcie — część tematów wypełniona · ✅ pełny — wyjaśnienia, zdjęcia, schematy, pytania z odpowiedziami, źródła

Numeracja prowadzi od fizyki zjawisk, przez elementy instalacji i ochronę, do praktyki i przepisów, ale nie jest sztywną kolejnością nauki — zależności między modułami są w [ROADMAP.md](ROADMAP.md). Moduły **33–34** są rozszerzeniami: dozór (D) oraz sieci powyżej 1 kV.

---

## Sprawdzanie materiałów

- **Odnośniki** sprawdza [tools/check_links.py](tools/check_links.py): przy każdym pushu odnośniki wewnętrzne (pliki i kotwice), raz w tygodniu także linki zewnętrzne.
- **Obrazy** sprawdza [tools/check_images.py](tools/check_images.py): czy plik istnieje, czy ma tekst alternatywny i czy każde zdjęcie z `assets/foto/` ma wpis w [assets/CREDITS.md](assets/CREDITS.md). Skrypt wypisuje też listę zdjęć oznaczonych jako `📷 DO ZROBIENIA`.
- Zdjęcia z Wikimedia Commons pobiera [tools/commons.py](tools/commons.py) — razem z autorem i licencją. Lista źródeł zdjęć jest w [assets/foto/ZDJECIA.tsv](assets/foto/ZDJECIA.tsv); po jej zmianie brakujące pliki pobiera automatycznie GitHub Actions ([zdjecia.yml](.github/workflows/zdjecia.yml)).
- Wzory są pisane pod renderer GitHuba (MathJax): przecinek dziesiętny jako `{,}` (np. `0{,}4\ \mathrm{s}`), jednostki pismem prostym.

---

## Zasady pracy, które naprawdę działają

- **Wyłącz, zabezpiecz, sprawdź — zawsze.** Każda praca zaczyna się od pięciu zasad bezpieczeństwa, także „tylko wymiana gniazdka”.
- **Najpierw schemat, potem śrubokręt.** Zanim coś odłączysz, narysuj albo sfotografuj, jak było podłączone.
- **Rozumiej, nie zapamiętuj.** Komisja pyta „dlaczego”, a nie tylko „ile”. Każdą liczbę wiąż z jej uzasadnieniem.
- **Oglądaj prawdziwe instalacje.** Otwórz (bezpiecznie, z zachowaniem zasad) własną rozdzielnicę i opisz każdy aparat.
- **Mów na głos.** Egzamin jest ustny — odpowiadaj na pytania z `sep/pytania.md` głośno, pełnymi zdaniami.

---

## Licencja

Treść własna repozytorium (teksty, schematy, pytania): **CC BY-SA 4.0** — szczegóły w [LICENSE.md](LICENSE.md). Zdjęcia zewnętrzne zachowują swoje licencje, wymienione w [assets/CREDITS.md](assets/CREDITS.md). Przepisy i normy są tylko przywoływane z numerem jednostki redakcyjnej; normy nie są tu kopiowane.
