# Ściąga — 12 — Ochrona przeciwporażeniowa

> Zebrane sekcje „Liczby do zapamiętania” ze wszystkich tematów modułu. [Spis modułu](README.md)

## [12.01 Ochrona podstawowa: izolacja, obudowy, przegrody](12.01-ochrona-podstawowa-izolacja-obudowy-przegrody.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Obudowy i osłony | co najmniej **IP2X / IPXXB** | części czynne | PN-HD 60364-4-41, 416.2 |
| Górne poziome powierzchnie | co najmniej **IP4X / IPXXD** | łatwo dostępne | jw. |
| Zasięg ręki | **2,5 m** w górę, **1,25 m** w bok, **0,75 m** w dół | od miejsca stania | jw., zał. B |
| Przeszkody i poza zasięgiem | tylko przy dostępie **osób wykwalifikowanych lub poinstruowanych** | — | jw., 410.3.5 |

## [12.02 Ochrona przy uszkodzeniu: samoczynne wyłączenie zasilania](12.02-ochrona-przy-uszkodzeniu-samoczynne-wylaczenie.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Czas wyłączenia TN | **0,4 s** (230 V), **5 s** — obwody rozdzielcze | obwody odbiorcze ≤ 63 A gniazd. / ≤ 32 A stałe | PN-HD 60364-4-41, tab. 41.1 |
| Czas wyłączenia TT | **0,2 s** (230 V), **1 s** — obwody rozdzielcze | jw. | jw. |
| Napięcie dotykowe dopuszczalne | $U_L$ = **50 V AC** | warunki normalne | [04.03](../04-prad-a-czlowiek/04.03-napiecie-dotykowe-i-krokowe-napiecia.md) |
| Elementy | **PE + wyrównanie + zabezpieczenie** | wszystkie trzy | 411.3 |

## [12.03 Warunek skuteczności samoczynnego wyłączenia](12.03-warunek-skutecznosci-samoczynnego-wylaczenia.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Warunek TN | $Z_s \cdot I_a \le U_0$ | — | PN-HD 60364-4-41, 411.4.4 |
| Warunek TT | $R_A \cdot I_{\Delta n} \le 50$ V | z RCD | jw., 411.5.3 |
| $I_a$ wyłączników B / C / D | **5 / 10 / 20 × In** | 0,4 s i 5 s | PN-EN 60898-1 |
| $Z_{s,max}$ B10 / B16 / B20 / B25 | **4,60 / 2,88 / 2,30 / 1,84 Ω** | TN, 230 V | obliczenie |
| $Z_{s,max}$ C10 / C16 / C20 | **2,30 / 1,44 / 1,15 Ω** | jw. | obliczenie |
| Ocena pomiaru z zapasem | $Z_s \le \tfrac{2}{3} \cdot U_0 / I_a$ | pomiar „na zimno” | PN-HD 60364-6, zał. informacyjny |

## [12.04 Izolacja podwójna, separacja elektryczna, SELV i PELV](12.04-izolacja-podwojna-separacja-elektryczna-selv-i.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| SELV / PELV | ≤ **50 V AC**, ≤ **120 V DC** (bez tętnień) | — | PN-HD 60364-4-41, 414 |
| Bez ochrony podstawowej | do **25 V AC / 60 V DC** (sucho), do **12 V AC / 30 V DC** (pozostałe) | SELV, PELV | jw., 414.4.5 |
| Separacja — napięcie | do **500 V** | obwód separowany | jw., 413 |
| Separacja — długość | iloczyn **U · L ≤ 100 000 V·m**, **L ≤ 500 m** | zalecenie | jw. |
| Separacja — odbiorniki | zasadniczo **1** na źródło | — | jw., 413.1.2 |

## [12.05 Ochrona uzupełniająca](12.05-ochrona-uzupelniajaca.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| RCD ochrony uzupełniającej | IΔn ≤ **30 mA** | — | PN-HD 60364-4-41, 415.1 |
| Obowiązkowo RCD 30 mA | gniazda ≤ 32 A, urządzenia ruchome na zewnątrz ≤ 32 A, oświetlenie w mieszkaniach | — | jw., 411.3.3, 411.3.4 |
| Warunek połączeń dodatkowych | $R \le 50\ \mathrm{V} / I_a$ (AC) | między częściami jednocześnie dostępnymi | jw., 415.2.2 |

## [12.06 Dawne nazwy: zerowanie, uziemienie ochronne — słownik przejściowy](12.06-dawne-nazwy-zerowanie-uziemienie-ochronne.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Zerowanie | = samoczynne wyłączenie w **TN** | dawna nazwa | PN-HD 60364-4-41 (nazwy obecne) |
| Uziemienie ochronne | = samoczynne wyłączenie w **TT** | jw. | jw. |
| Dotyk bezpośredni / pośredni | = ochrona **podstawowa / przy uszkodzeniu** | jw. | jw. |
| Napięcie bezpieczne | = **SELV/PELV**, ≤ 50 V AC | jw. | jw. |
