# Ściąga — 24 — Silniki i napędy

> Zebrane sekcje „Liczby do zapamiętania” ze wszystkich tematów modułu. [Spis modułu](README.md)

## [24.01 Silnik indukcyjny trójfazowy](24.01-silnik-indukcyjny-trojfazowy.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Prędkość synchroniczna | $n_s = 60 f / p$: **3000 / 1500 / 1000 / 750** obr/min | 50 Hz, p = 1…4 | — |
| Poślizg | **2–6 %** | znamionowo, silniki małe i średnie | katalogi |
| Prąd rozruchowy | **5–8 × In** | rozruch bezpośredni | katalogi |
| Moment rozruchowy | ok. **1,5–3 × Mn** | silniki klatkowe | katalogi |
| Wymóg IE3 | **0,75–1000 kW** od 1.07.2021 | silniki 3-faz. w UE | rozp. (UE) 2019/1781 |
| Wymóg IE4 | **75–200 kW** od 1.07.2023 | 2, 4, 6 biegunów | jw. |

## [24.02 Tabliczka znamionowa silnika](24.02-tabliczka-znamionowa-silnika.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Klasy izolacji | B **130 °C**, F **155 °C**, H **180 °C** | uzwojenia | PN-EN 60085 |
| Rodzaj pracy | **S1** ciągła, **S2** dorywcza, **S3** przerywana | — | PN-EN 60034-1 |
| Prąd 3-faz. | $I = P / (\sqrt{3} \cdot U \cdot \cos\varphi \cdot \eta)$ | P — moc na wale | — |
| Szybki szacunek | ok. **2 A na 1 kW** przy 400 V | silniki kilku kW | praktyka |
| Nastawa termika | **= prąd znamionowy** dla danego połączenia | — | [24.05](24.05-uklad-start-stop-ze-stycznikiem-i-przekaznikiem.md) |

## [24.03 Połączenie w gwiazdę i w trójkąt](24.03-polaczenie-w-gwiazde-i-w-trojkat.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Napięcie uzwojenia w Y | $U / \sqrt{3}$ = **230 V** | sieć 400 V | — |
| Napięcie uzwojenia w Δ | $U$ = **400 V** | jw. | — |
| Prąd przewodu w Δ | **√3 ×** prąd uzwojenia | — | — |
| Oznaczenia zacisków | **U1 V1 W1 / W2 U2 V2** | PN-EN 60034-8 | PN-EN 60034-8 |
| 230/400 V w sieci 400 V | **Y** | — | — |
| 400/690 V w sieci 400 V | **Δ** | — | — |

## [24.04 Rozruch: bezpośredni, gwiazda-trójkąt, softstart](24.04-rozruch-bezposredni-gwiazda-trojkat-softstart.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Prąd rozruchu bezpośredniego | **5–8 × In** | silniki klatkowe | katalogi |
| Y-Δ: prąd i moment | **⅓** wartości przy rozruchu bezpośrednim | silnik pracujący w Δ | — |
| Softstart: moment | ∝ **U²** | — | — |
| Falownik: prąd rozruchowy | ok. **1–1,5 × In** | pełny moment | katalogi |
| Warunek Y-Δ | tabliczka **400/690 V Δ/Y** w sieci 400 V | — | [24.03](24.03-polaczenie-w-gwiazde-i-w-trojkat.md) |

## [24.05 Układ start-stop ze stycznikiem i przekaźnikiem termicznym](24.05-uklad-start-stop-ze-stycznikiem-i-przekaznikiem.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Styk termika | **95-96** rozwierny (97-98 zwierny — sygnalizacja) | przekaźniki termiczne | PN-EN 60947 |
| Podtrzymanie | **13-14** | styk zwierny stycznika | jw. |
| Cewka | **A1-A2** | jw. | jw. |
| Nastawa termika | **= In silnika** | dla danego połączenia Y/Δ | instrukcje |
| Klasa 10 | zadziała w **≤ 10 s** przy **7,2 ×** prąd nastawy | rozruch normalny | PN-EN 60947-4-1 |
| Kolory przycisków | **STOP czerwony**, START zielony/biały/czarny | — | PN-EN 60204-1 |

## [24.06 Zmiana kierunku obrotów](24.06-zmiana-kierunku-obrotow.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Zmiana kierunku | zamiana **dwóch** faz | silnik 3-faz. | — |
| Styk blokady | **21-22** (rozwierny) | styczniki | PN-EN 60947 |
| Liczba blokad | **elektryczna + mechaniczna** (zalecane obie) | układy nawrotne | praktyka |

## [24.07 Przemienniki częstotliwości](24.07-przemienniki-czestotliwosci.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Napięcie DC | ok. **560 V** ($400 \cdot \sqrt{2}$) | zasilanie 3 × 400 V | — |
| Moc pompy / wentylatora | ∝ **n³** (80 % obrotów → **51 %** mocy) | prawa podobieństwa | — |
| RCD | typ **B** (lub F wg producenta) | falowniki | instrukcje producentów, [08.03](../08-wylaczniki-roznicowopradowe/08.03-typy-ac-a-f-i-b-ktory-do-czego.md) |
| Klasa sprawności przemienników | **IE2** od 1.07.2021 | 0,12–1000 kW | rozp. (UE) 2019/1781 |
| Czas rozładowania DC | wg tabliczki, często **kilka minut** | po wyłączeniu | instrukcje |

## [24.08 Silniki jednofazowe](24.08-silniki-jednofazowe.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Kondensator w układzie Steinmetza | ok. **70 µF / kW** | silnik 230/400 V w Δ na 230 V | reguła praktyczna |
| Moc w układzie Steinmetza | ok. **⅔** mocy znamionowej | jw. | jw. |
| Napięcie kondensatorów silnikowych | typowo **400–450 V AC** | — | katalogi |
| Objaw uszkodzonego kondensatora | **buczy, nie rusza** (rusza „popchnięty”) | silniki kondensatorowe | — |
