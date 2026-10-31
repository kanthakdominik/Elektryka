# Ściąga — 03 — Elektromagnetyzm w praktyce

> Zebrane sekcje „Liczby do zapamiętania” ze wszystkich tematów modułu. [Spis modułu](README.md)

## [03.01 Pole magnetyczne prądu i cewka](03.01-pole-magnetyczne-pradu-i-cewka.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Kierunek pola | reguła prawej dłoni: kciuk — prąd, palce — pole | przewód prostoliniowy | — |
| Reaktancja cewki | $X_L = 2\pi f L$ — rośnie z częstotliwością | prąd przemienny | definicja |
| Przy 50 Hz | $X_L \approx 314 \cdot L$ | sieć 50 Hz | $2\pi \cdot 50 \approx 314$ |
| Cewka przy prądzie stałym | tylko rezystancja drutu (po ustaleniu prądu) | DC | — |
| Wpływ rdzenia stalowego | pole wielokrotnie silniejsze (setki–tysiące razy) | rdzeń nienasycony | — |

## [03.02 Indukcja elektromagnetyczna i transformator](03.02-indukcja-elektromagnetyczna-i-transformator.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Przekładnia napięciowa | $U_1 / U_2 = N_1 / N_2$ | transformator idealny, prąd przemienny | prawo Faradaya |
| Przekładnia prądowa | $I_1 / I_2 = N_2 / N_1$ | jw., pod obciążeniem | bilans mocy |
| Moc | $U_1 I_1 \approx U_2 I_2$ (sprawność dużych transformatorów > 95 %) | — | — |
| Prąd stały | transformator **nie działa** (zwarcie dla źródła) | DC | — |
| Typowe przekładnie | stacja 15 kV / 0,4 kV; zasilacz dzwonka 230 / 8–12 V; transformator bezpieczeństwa 230 / 12–24 V | — | — |

## [03.03 Elektromagnes w pracy: przekaźnik i stycznik](03.03-elektromagnes-w-pracy-przekaznik-i-stycznik.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Zaciski cewki | **A1, A2** | styczniki, przekaźniki | PN-EN 60947, PN-EN 60445 |
| Styki główne | **1-2, 3-4, 5-6** | styczniki | jw. |
| Druga cyfra styku pomocniczego | **3-4 zwierny**, **1-2 rozwierny** | 13-14 NO, 21-22 NC, 31-32 NC, 43-44 NO | jw. |
| Typowe napięcia cewek | **230 V AC**, 24 V AC/DC, 12 V DC | — | tabliczka aparatu |
| Stan rysowany na schemacie | **bez zasilania cewki** | schematy | zasada rysunku |

## [03.04 Jak działa silnik elektryczny — intuicja](03.04-jak-dziala-silnik-elektryczny-intuicja.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Prędkość synchroniczna | $n_s = 60 \cdot f / p$ | $p$ — liczba par biegunów | — |
| Przy 50 Hz | **3000 / 1500 / 1000 / 750** obr/min dla $p$ = 1 / 2 / 3 / 4 | — | — |
| Poślizg znamionowy | ok. **2–6 %** | silniki małej i średniej mocy | typowe wartości |
| Prąd rozruchowy | ok. **5–8 ×** prąd znamionowy | rozruch bezpośredni | katalogi producentów |
| Zmiana kierunku obrotów | zamiana **dwóch** faz | silnik trójfazowy | — |
| Siła na przewód | $F = B I l$ | przewód prostopadły do pola | — |
