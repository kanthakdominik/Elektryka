# Ściąga — 08 — Wyłączniki różnicowoprądowe

> Zebrane sekcje „Liczby do zapamiętania” ze wszystkich tematów modułu. [Spis modułu](README.md)

## [08.01 Zasada działania wyłącznika różnicowoprądowego](08.01-zasada-dzialania-wylacznika-roznicowopradowego.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Zakres zadziałania | **0,5 IΔn – IΔn** | prąd sinusoidalny | PN-EN 61008-1 |
| Czas zadziałania przy IΔn | ≤ **300 ms** | RCD ogólnego typu | jw. |
| Czas przy 2 IΔn / 5 IΔn | ≤ **150 ms** / ≤ **40 ms** | jw. | jw. |
| Czas zadziałania typu S przy IΔn | **130–500 ms** | RCD selektywny | jw. |
| Typ S przy 5 IΔn | **50–150 ms** | jw. | jw. |
| Ochrona uzupełniająca | IΔn ≤ **30 mA** | — | PN-HD 60364-4-41, 415.1 |

## [08.02 Prąd różnicowy znamionowy: 30 mA, 100 mA, 300 mA](08.02-prad-roznicowy-znamionowy-30-ma-100-ma-300-ma.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Ochrona uzupełniająca (ludzie) | IΔn ≤ **30 mA** | gniazda ≤ 32 A, oświetlenie w mieszkaniach, łazienki | PN-HD 60364-4-41:2017, 411.3.3, 411.3.4 |
| Ochrona przeciwpożarowa | IΔn ≤ **300 mA** | miejsca z zagrożeniem pożarowym | PN-HD 60364-4-42 |
| Selektywność RCD | wyżej typ **S** i IΔn co najmniej **3×** większy | RCD szeregowo | praktyka, dane producentów |
| Warunek TT | $R_A \cdot I_{\Delta n} \le 50\ \mathrm{V}$ | ochrona przy uszkodzeniu | PN-HD 60364-4-41, 411.5.3 |
| Migotanie komór (długi przepływ) | ok. **40–50 mA** | > 1 s | IEC TS 60479-1 |

## [08.03 Typy AC, A, F i B — który do czego](08.03-typy-ac-a-f-i-b-ktory-do-czego.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Typ A — dopuszczalna składowa stała | do **6 mA** | bez utraty działania | PN-EN 61008-1 |
| Typ F — dopuszczalna składowa stała | do **10 mA** | jw. | PN-EN 62423 |
| Typ B | prąd stały wygładzony | — | jw. |
| W mieszkaniu | co najmniej **typ A** | nowe instalacje | praktyka, zalecenia producentów |
| Ładowarka EV | **typ B** albo typ A + wykrywanie DC **6 mA** | — | PN-HD 60364-7-722 |

## [08.04 RCBO — wyłącznik nadprądowy z członem różnicowoprądowym](08.04-rcbo-wylacznik-nadpradowy-z-czlonem.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Typowe RCBO w mieszkaniu | **B16 / 30 mA / typ A**, 6 kA | obwody gniazd | praktyka |
| Część nadprądowa | jak w wyłączniku nadprądowym (1,13 / 1,45 × In, B/C) | — | PN-EN 61009-1 |
| Część różnicowa | jak w RCD (≤ 300 ms przy IΔn) | — | jw. |
| Szerokość | **1–2 moduły** | 1P+N | katalogi producentów |

## [08.05 Przycisk TEST i okresowe sprawdzanie](08.05-przycisk-test-i-okresowe-sprawdzanie.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Prąd zadziałania (pomiar) | **0,5 IΔn – IΔn** (15–30 mA dla 30 mA) | prąd sinusoidalny | PN-EN 61008-1 |
| Czas zadziałania przy IΔn | ≤ **300 ms** (ogólny), **130–500 ms** (S) | — | jw. |
| Czas przy 5 IΔn | ≤ **40 ms** (ogólny) | — | jw. |
| Naciskanie TEST | wg producenta, zwykle **co 1–6 miesięcy** | użytkownik | instrukcje producentów |

## [08.06 Dlaczego różnicówka wybija — przyczyny i szukanie winnego](08.06-dlaczego-roznicowka-wybija-przyczyny-i-szukanie.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Suma prądów upływowych za RCD | ≤ **0,3 IΔn** (≈ 9 mA dla 30 mA) | zalecenie | PN-HD 60364-5-53 (531.3.2); starsza literatura: 0,33–0,5 IΔn |
| Typowy upływ urządzenia z filtrem | ok. **0,5–3 mA** | komputery, RTV, AGD | dane urządzeń |
| Rezystancja izolacji instalacji | ≥ **1 MΩ** przy napięciu probierczym **500 V DC** | obwody do 500 V | PN-HD 60364-6, tab. 6A |
| Zakres zadziałania RCD | **0,5–1 IΔn** | — | PN-EN 61008-1 |

## [08.07 Podział obwodów między wyłączniki różnicowoprądowe](08.07-podzial-obwodow-miedzy-wylaczniki.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Obwody na jeden RCD | najlepiej **1** (RCBO), zwykle **2–3** | mieszkania | praktyka, [Inżynier Budownictwa](https://inzynierbudownictwa.pl/?p=5443) |
| Suma upływu za RCD | ≤ **0,3 IΔn** | — | PN-HD 60364-5-53 |
| Selektywność RCD szeregowo | wyżej **typ S** i IΔn ≥ **3×** IΔn niższego | — | dane producentów |
| Prąd znamionowy RCD | ≥ prąd zabezpieczenia przed nim lub suma obciążeń wg producenta | — | instrukcje producentów |
