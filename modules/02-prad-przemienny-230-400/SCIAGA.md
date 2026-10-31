# Ściąga — 02 — Prąd przemienny i sieć 230/400 V

> Zebrane sekcje „Liczby do zapamiętania” ze wszystkich tematów modułu. [Spis modułu](README.md)

## [02.01 Sinusoida, 50 Hz i wartość skuteczna](02.01-sinusoida-50-hz-i-wartosc-skuteczna.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Częstotliwość sieci | **50 Hz** (±1 % przez 99,5 % tygodnia) | sieć połączona z systemem | rozporządzenie MKiŚ z 2023 r., § 45 ust. 5 pkt 1 |
| Okres | **20 ms** | 50 Hz | $T = 1/f$ |
| Przejścia przez zero | **100 na sekundę** | 50 Hz | dwa na okres |
| Wartość szczytowa 230 V | **≈ 325 V** | przebieg sinusoidalny | $U_{max} = \sqrt{2} \cdot U$ |
| Międzyszczytowa 230 V | **≈ 650 V** | jw. | $2 \sqrt{2} \cdot U$ |
| Wartość szczytowa 400 V | **≈ 566 V** | jw. | jw. |
| Wartość skuteczna z szczytowej | $U = U_{max} / \sqrt{2} \approx 0{,}707\, U_{max}$ | tylko sinusoida | — |

## [02.02 Faza, przewód neutralny i przewód ochronny — L, N, PE](02.02-faza-przewod-neutralny-i-przewod-ochronny-l-n-pe.md)

| Przewód | Barwa | Napięcie względem ziemi (sprawna instalacja) | Prąd w normalnej pracy | Źródło |
|---------|-------|----------------------------------------------|------------------------|--------|
| L (L1, L2, L3) | brązowy, czarny, szary | 230 V | prąd roboczy | PN-EN 60445 |
| N | niebieski | ≈ 0 V | prąd roboczy (taki jak w L) | jw. |
| PE | żółto-zielony | 0 V | **brak** (tylko prąd upływu, mA) | jw. |
| PEN | żółto-zielony + niebieskie oznaczenie końców (lub odwrotnie) | ≈ 0 V | prąd roboczy | jw. |

## [02.03 Układ trójfazowy: 230 V i 400 V, kolejność faz](02.03-uklad-trojfazowy-230-v-i-400-v-kolejnosc-faz.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Napięcie fazowe | **230 V** | sieć nN | PN-EN 60038 |
| Napięcie międzyfazowe | **400 V** = $\sqrt{3} \cdot 230$ | jw. | jw. |
| Przesunięcie faz | **120°** = 6,67 ms | 50 Hz | — |
| Moc trójfazowa | $P = \sqrt{3} \cdot U \cdot I \cdot \cos\varphi$ | $U$ = 400 V, $I$ — prąd fazowy | [02.04](02.04-moc-czynna-bierna-i-pozorna-wspolczynnik-mocy.md) |
| Prąd na 1 kW (trójfazowo, cos φ = 1) | ok. **1,44 A** na fazę | odbiornik symetryczny | $1000 / (\sqrt{3} \cdot 400)$ |
| Barwy faz | L1 **brązowy**, L2 **czarny**, L3 **szary** | nowe instalacje | PN-EN 60445 |
| Gniazdo CEE | czerwone **400 V**, niebieskie **230 V**; 16 A, 32 A, 63 A… | gniazda przemysłowe | PN-EN 60309 |

## [02.04 Moc czynna, bierna i pozorna, współczynnik mocy](02.04-moc-czynna-bierna-i-pozorna-wspolczynnik-mocy.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Moc pozorna | $S = U \cdot I$ (1f), $S = \sqrt{3}\, U I$ (3f) | zawsze | definicja |
| Moc czynna | $P = S \cos\varphi$ | przebiegi sinusoidalne | jw. |
| Moc bierna | $Q = S \sin\varphi$ | jw. | jw. |
| Trójkąt mocy | $S^2 = P^2 + Q^2$ | jw. | jw. |
| Typowe cos φ | grzałka, żarówka **1** · silnik **0,7–0,9** · świetlówka bez kompensacji **≈ 0,5** | wartości orientacyjne | tabliczki znamionowe |
| Próg opłat za energię bierną | zwykle **tg φ = 0,4** (cos φ ≈ 0,93) | odbiorcy biznesowi w niektórych grupach taryfowych; **nie dotyczy** gospodarstw domowych (grupa G) | taryfy operatorów |

## [02.05 Odbiorniki nieliniowe i wyższe harmoniczne — podstawy](02.05-odbiorniki-nieliniowe-i-wyzsze-harmoniczne.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Częstotliwości harmonicznych | 3. — **150 Hz**, 5. — **250 Hz**, 7. — **350 Hz** | sieć 50 Hz | $f_n = n \cdot 50\ \mathrm{Hz}$ |
| Dopuszczalny THD napięcia | **≤ 8 %** (maks. ze średnich 10-min w tygodniu) | odbiorcy w grupach przyłączeniowych III–V | rozporządzenie MKiŚ z 2023 r., § 45 ust. 5 |
| Prąd w N przy odbiornikach nieliniowych | może **przekroczyć prąd fazowy** (do ok. 1,7 ×) | sieć trójfazowa, dużo zasilaczy impulsowych | — |
| Harmoniczne sumujące się w N | **3., 9., 15.** (wielokrotności 3) | układ trójfazowy | — |
