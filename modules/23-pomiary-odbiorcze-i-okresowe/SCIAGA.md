# Ściąga — 23 — Pomiary odbiorcze i okresowe

> Zebrane sekcje „Liczby do zapamiętania” ze wszystkich tematów modułu. [Spis modułu](README.md)

## [23.01 Oględziny instalacji](23.01-ogledziny-instalacji.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Kolejność | **oględziny przed próbami** | każde sprawdzenie | PN-HD 60364-6 |
| Zasilanie przy oględzinach | zwykle **wyłączone** | — | jw. |
| Barwy | N **niebieski**, PE **żółto-zielony** | instalacje | PN-EN 60445 |
| Kontrola instalacji w budynku | co najmniej co **5 lat** | budynki | art. 62 Prawa budowlanego |

## [23.02 Ciągłość przewodów ochronnych i wyrównawczych](23.02-ciaglosc-przewodow-ochronnych-i-wyrownawczych.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Źródło pomiarowe | **4–24 V**, prąd **≥ 0,2 A** | ciągłość PE | PN-EN 61557-4 |
| Błąd przyrządu | ≤ **± 30 %** w zakresie 0,2–2 Ω | — | jw. |
| Rezystancja Cu (20 °C) | 1,5 mm² **12,1 mΩ/m**, 2,5 mm² **7,41**, 4 mm² **4,61**, 6 mm² **3,08** | — | PN-EN 60228 |
| Połączenia wyrównawcze dodatkowe | $R \le 50\ \mathrm{V} / I_a$ | — | PN-HD 60364-4-41, 415.2 |

## [23.03 Rezystancja izolacji](23.03-rezystancja-izolacji.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Obwody 230/400 V | **500 V DC**, ≥ **1,0 MΩ** | do 500 V | PN-HD 60364-6, tab. 6.1 |
| SELV / PELV | **250 V DC**, ≥ **0,5 MΩ** | — | jw. |
| Powyżej 500 V | **1000 V DC**, ≥ **1,0 MΩ** | — | jw. |
| Z SPD, którego nie da się odłączyć | **250 V DC**, ≥ **1 MΩ** | — | jw., 6.4.3.3 |
| Przyrząd | prąd znamionowy ≥ **1 mA**, napięcie jałowe ≤ **1,5 U_N** | — | PN-EN 61557-2 |
| Dawne wymaganie (dla porównania) | 0,5 MΩ przy 500 V | wcześniejsze wydanie | [SEP](https://sep.com.pl/opracowania/Kontrola%20stanu%20instalacji%20elektrycznych%20niskiego%20napiecia.pdf) |

## [23.04 Impedancja pętli zwarcia](23.04-impedancja-petli-zwarcia.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Warunek | $Z_s \cdot I_a \le U_0$ | TN | PN-HD 60364-4-41, 411.4.4 |
| $I_a$ wyłącznika | B **5 × In**, C **10 × In**, D **20 × In** | 0,4 s | PN-EN 60898-1 |
| $Z_{s,max}$ B10 / B16 / B20 | **4,60 / 2,88 / 2,30 Ω** | TN, 230 V | obliczenie |
| $Z_{s,max}$ C10 / C16 | **2,30 / 1,44 Ω** | jw. | jw. |
| Ocena z zapasem | $Z_s \le \tfrac{2}{3} \cdot U_0 / I_a$ | pomiar „na zimno” | PN-HD 60364-6, zał. informacyjny |
| Błąd przyrządu | ≤ **± 30 %** | — | PN-EN 61557-3 |

## [23.05 Badanie wyłączników różnicowoprądowych](23.05-badanie-wylacznikow-roznicowopradowych.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Czas przy IΔn / 2 IΔn / 5 IΔn | ≤ **300 / 150 / 40 ms** | RCD ogólnego typu | PN-EN 61008-1, 61009-1 |
| RCD typu S | **130–500 / 60–200 / 50–150 ms** | selektywne | jw. |
| Prąd zadziałania (AC) | **0,5–1,0 IΔn** | — | jw. |
| Napięcie dotykowe | $U_B \le$ **50 V** | przy IΔn | PN-HD 60364-4-41 |
| Błąd przyrządu (prąd) | ≤ **± 10 %** IΔn | — | PN-EN 61557-6 |
| Przycisk TEST | regularnie (np. co miesiąc–kwartał wg producenta) | użytkownik | [08.05](../08-wylaczniki-roznicowopradowe/08.05-przycisk-test-i-okresowe-sprawdzanie.md) |

## [23.06 Rezystancja uziemienia](23.06-rezystancja-uziemienia.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Sonda prądowa | ≥ **40 m** (≥ ok. 5 × długość uziomu) | metoda techniczna | instrukcje mierników |
| Sonda napięciowa | ok. **62 %** odległości E–H | jw. | jw. |
| Sprawdzenie | przesunięcie S o **±10 %** | jw. | jw. |
| Warunek TT | $R_A \cdot I_{\Delta n} \le 50$ V (30 mA → do **1667 Ω**) | TT z RCD | PN-HD 60364-4-41, 411.5.3 |
| Zalecane uziemienie (LPS, ogólnie) | < **10 Ω** | zalecenie | [13.02](../13-uziemienia-i-wyrownanie/13.02-rezystancja-uziemienia-od-czego-zalezy.md) |
| Błąd przyrządu | ≤ **± 30 %** | — | PN-EN 61557-5 |

## [23.07 Kolejność faz](23.07-kolejnosc-faz.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Prawidłowa kolejność | **L1 → L2 → L3** (prawa) | instalacje wielofazowe | PN-HD 60364-6, 6.4.3.9 |
| Przesunięcie faz | **120°** | sieć 3-faz. | [02.03](../02-prad-przemienny-230-400/02.03-uklad-trojfazowy-230-v-i-400-v-kolejnosc-faz.md) |
| Zmiana kierunku | zamiana **dwóch** faz | — | — |

## [23.08 Protokół z pomiarów i terminy badań okresowych](23.08-protokol-z-pomiarow-i-terminy-badan-okresowych.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Kontrola instalacji elektrycznej i piorunochronnej | co najmniej co **5 lat** | budynki | art. 62 ust. 1 pkt 2 Prawa budowlanego |
| Przegląd elementów narażonych na czynniki atmosferyczne | co najmniej **raz w roku** | budynki | art. 62 ust. 1 pkt 1 |
| Duże obiekty | **2 razy w roku** (do 31.05 i 30.11) | zabudowa > 2000 m², dach > 1000 m² | art. 62 ust. 1 pkt 3 |
| Zalecenie normy — mieszkania | co **10 lat** + zmiana użytkownika | informacyjne | PN-HD 60364-6 |
| Zalecenie normy — inne budynki | co **4 lata** | informacyjne | jw. |
| Ważność świadectwa kwalifikacyjnego | **5 lat** | — | art. 54 Prawa energetycznego |
