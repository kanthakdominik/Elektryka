# Ściąga — 13 — Uziemienia i połączenia wyrównawcze

> Zebrane sekcje „Liczby do zapamiętania” ze wszystkich tematów modułu. [Spis modułu](README.md)

## [13.01 Uziom: fundamentowy, otokowy, prętowy](13.01-uziom-fundamentowy-otokowy-pretowy.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Taśma stalowa ocynkowana | ≥ **90 mm²**, grubość ≥ **3 mm** | uziom | PN-HD 60364-5-54, tab. 54.1 |
| Pręt stalowy ocynkowany | średnica ≥ **16 mm** | uziom pionowy | jw. |
| Pręt stalowy pokryty miedzią | średnica ≥ **14 mm**, powłoka **250 μm** | jw. | jw. |
| Taśma miedziana | ≥ **50 mm²**, grubość **2 mm** | — | jw. |
| Uziom otokowy | głębokość ≥ **0,5 m**, ok. **1 m** od ścian | — | PN-EN 62305-3 |
| Rury z gazem lub cieczami palnymi | **nie wolno** jako uziom | — | PN-HD 60364-5-54 |

## [13.02 Rezystancja uziemienia — od czego zależy](13.02-rezystancja-uziemienia-od-czego-zalezy.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Uziom prętowy | $R \approx \dfrac{\rho}{2\pi L} \ln\dfrac{4L}{d}$ | grunt jednorodny | wzór teoretyczny |
| Szybkie oszacowanie pręta | $R \approx \rho / L$ | L — długość w m | reguła praktyczna |
| Zalecana rezystancja ogólnie / odgromowa | **< 10 Ω** | — | PN-EN 62305-3, [Inżynier Budownictwa](https://inzynierbudownictwa.pl/?p=9271) |
| Warunek TT | $R_A \le 50\ \mathrm{V} / I_{\Delta n}$ | z RCD | PN-HD 60364-4-41 |
| Rezystywność gruntu (rząd) | glina **kilkadziesiąt**, piasek suchy **setki–tysiące** Ω·m | — | literatura |
| Rozstaw prętów | ≥ **długość pręta** | uziomy wielokrotne | praktyka |

## [13.03 Główna szyna uziemiająca](13.03-glowna-szyna-uziemiajaca.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Przewód uziemiający | ≥ **6 mm² Cu** lub **50 mm² Fe**; bez aluminium | — | PN-HD 60364-5-54, 542.3.1 |
| Przewód uziemiający z instalacją odgromową | ≥ **16 mm² Cu** lub **50 mm² Fe** | — | jw. |
| Przewody wyrównawcze główne | ≥ **6 mm² Cu** (½ największego PE, nie trzeba > 25 mm² Cu) | — | jw., 544.1 |
| Odłączanie przewodów | każdy osobno, **tylko narzędziem** | — | jw., 542.4 |

## [13.04 Połączenia wyrównawcze ochronne główne](13.04-polaczenia-wyrownawcze-ochronne-glowne.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Przekrój przewodu wyrównawczego głównego | ≥ **½ największego PE** instalacji | — | PN-HD 60364-5-54, 544.1 |
| Minimum | **6 mm² Cu**, 16 mm² Al, 50 mm² Fe | — | jw. |
| Maksimum wymagane | **25 mm² Cu** (lub równoważny) | — | jw. |
| Gaz | połączenie **za wstawką izolacyjną** (od strony budynku) | — | wymagania dostawców gazu |

## [13.05 Połączenia wyrównawcze miejscowe](13.05-polaczenia-wyrownawcze-miejscowe.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Warunek skuteczności | $R \le 50\ \mathrm{V} / I_a$ | AC | PN-HD 60364-4-41, 415.2.2 |
| Przewód między dwiema częściami dostępnymi | przewodność ≥ **mniejszego z PE** | — | PN-HD 60364-5-54, 544.2.1 |
| Przewód między częścią dostępną a obcą | przewodność ≥ **½ PE** | — | jw., 544.2.2 |
| Minimalny przekrój | **2,5 mm² Cu** z ochroną mechaniczną, **4 mm² Cu** bez ochrony | — | jw., 544.2.3 |

## [13.06 Przekroje przewodów ochronnych i wyrównawczych](13.06-przekroje-przewodow-ochronnych-i-wyrownawczych.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| PE przy fazowym S ≤ 16 mm² | **S** | ten sam materiał | PN-HD 60364-5-54, tab. 54.2 |
| PE przy 16 < S ≤ 35 mm² | **16 mm²** | jw. | jw. |
| PE przy S > 35 mm² | **S/2** | jw. | jw. |
| PE prowadzony osobno | **2,5 mm² Cu** z ochroną, **4 mm² Cu** bez | — | jw., 543.1.3 |
| PEN | ≥ **10 mm² Cu / 16 mm² Al** | instalacje stałe | jw., 543.4.1 |
| Przewód uziemiający | ≥ **6 mm² Cu / 50 mm² Fe**; z LPS **16 mm² Cu** | bez Al | jw., 542.3.1 |
| Wyrównawczy główny | ≥ ½ PE, min **6 mm² Cu**, max wymagane **25 mm² Cu** | — | jw., 544.1 |
| Wyrównawczy miejscowy | **2,5 / 4 mm² Cu** (z ochroną / bez) | — | jw., 544.2 |
| Prąd upływu > 10 mA | PE ≥ **10 mm² Cu** lub podwójny | — | jw., 543.7 |
| Wzór adiabatyczny | $S = \sqrt{I^2 t}\,/\,k$ | t ≤ 5 s; Cu/PVC k = 115 (żyła w przewodzie) | jw., 543.1.2 |
