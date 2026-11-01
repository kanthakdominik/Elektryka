# Ściąga — 11 — Układy sieci: TN, TT, IT

> Zebrane sekcje „Liczby do zapamiętania” ze wszystkich tematów modułu. [Spis modułu](README.md)

## [11.01 Co oznaczają litery w nazwie układu sieci](11.01-co-oznaczaja-litery-w-nazwie-ukladu-sieci.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| 1. litera | **T** — źródło uziemione, **I** — izolowane | — | PN-HD 60364-1, 312.2 |
| 2. litera | **T** — obudowy uziemione osobno, **N** — połączone z punktem neutralnym | — | jw. |
| Dopisek | **S** — N i PE osobno, **C** — wspólny PEN | układy TN | jw. |
| Typowo w Polsce | sieć **TN-C**, budynek **TN-S** → **TN-C-S** | — | warunki przyłączenia OSD |

## [11.02 Układ TN-C](11.02-uklad-tn-c.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Minimalny przekrój PEN | **10 mm² Cu / 16 mm² Al** | instalacje stałe | PN-HD 60364-5-54, 543.4.1 |
| RCD w TN-C | **nie stosuje się** | — | PN-HD 60364-4-41 |
| Przewodów w sieci TN-C (3-faz.) | **4** (L1, L2, L3, PEN) | — | — |
| Napięcie na obudowie przy przerwie PEN | do ok. **230 V** | najgorszy przypadek | — |

## [11.03 Układ TN-S](11.03-uklad-tn-s.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Czas wyłączenia obwodów odbiorczych | **0,4 s** (230 V) | TN, gniazda ≤ 63 A, odbiory stałe ≤ 32 A | PN-HD 60364-4-41, tab. 41.1 |
| Czas wyłączenia obwodów rozdzielczych | **5 s** | TN | jw., 411.3.2.3 |
| Warunek ochrony | $Z_s \cdot I_a \le U_0$ | TN | jw., 411.4.4 |
| Przewodów w obwodzie 3-faz. | **5** (L1, L2, L3, N, PE) | — | — |

## [11.04 Układ TN-C-S i punkt rozdziału PEN](11.04-uklad-tn-c-s-i-punkt-rozdzialu-pen.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Punkt podziału | **jeden**, w złączu lub rozdzielnicy głównej | — | PN-HD 60364-5-54, praktyka OSD |
| Kolejność | PEN → **szyna PE** → mostek → szyna N | — | PN-HD 60364-5-54, 543.4.3 |
| Po podziale | N i PE **nigdy** się nie łączą | — | jw. |
| Minimalny przekrój PEN | **10 mm² Cu / 16 mm² Al** | — | jw., 543.4.1 |
| Przerwa PEN — napięcie fazy | do ok. **400 V** | najgorszy przypadek | — |

## [11.05 Układ TT](11.05-uklad-tt.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Warunek ochrony z RCD | $R_A \cdot I_{\Delta n} \le 50\ \mathrm{V}$ | TT | PN-HD 60364-4-41, 411.5.3 |
| Czas wyłączenia obwodów odbiorczych | **0,2 s** (230 V) | TT, gniazda ≤ 63 A, stałe ≤ 32 A | jw., tab. 41.1 |
| Czas wyłączenia obwodów rozdzielczych | **1 s** | TT | jw., 411.3.2.4 |
| $R_A$ max dla RCD 30 / 100 / 300 mA | ok. **1667 / 500 / 167 Ω** | z warunku 50 V | obliczenie |
| Prąd uszkodzenia | kilka–kilkanaście A | typowe uziomy | — |

## [11.06 Układ IT](11.06-uklad-it.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Pierwsze zwarcie | **bez wyłączenia**, sygnalizacja | — | PN-HD 60364-4-41, 411.6 |
| Warunek przy pierwszym zwarciu | $R_A \cdot I_d \le 50\ \mathrm{V}$ | $I_d$ — prąd pierwszego zwarcia | jw., 411.6.2 |
| Drugie zwarcie | **wyłączenie** jak w TN lub TT | — | jw., 411.6.4 |
| Przewód N | zaleca się **nie prowadzić** | — | jw. |
