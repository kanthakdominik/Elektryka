# Ściąga — 09 — Ochrona przeciwprzepięciowa

> Zebrane sekcje „Liczby do zapamiętania” ze wszystkich tematów modułu. [Spis modułu](README.md)

## [09.01 Skąd biorą się przepięcia](09.01-skad-biora-sie-przepiecia.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Prąd pioruna | typowo **kilkadziesiąt kA**, maksymalnie przyjmuje się do **200 kA** | wyładowania doziemne | PN-EN 62305-1 |
| Udar prądu piorunowego | **10/350 μs** | badanie SPD typu 1 | PN-EN 61643-11 |
| Udar przepięć indukowanych | **8/20 μs** | badanie SPD typu 2 | jw. |
| Udar napięciowy | **1,2/50 μs** | badanie wytrzymałości i SPD typu 3 | jw. |
| Zasięg szkodliwych przepięć indukowanych | do ok. **1–2 km** od uderzenia | — | materiały producentów SPD |

## [09.02 Kategorie wytrzymałości udarowej I–IV](09.02-kategorie-wytrzymalosci-udarowej-iiv.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Kategoria IV | $U_W$ = **6 kV** | początek instalacji 230/400 V | PN-HD 60364-4-443, tab. 443.2 |
| Kategoria III | $U_W$ = **4 kV** | instalacja stała | jw. |
| Kategoria II | $U_W$ = **2,5 kV** | odbiorniki | jw. |
| Kategoria I | $U_W$ = **1,5 kV** | wrażliwa elektronika | jw. |
| Warunek doboru SPD | $U_P$ (z połączeniami) < $U_W$ chronionych urządzeń | — | PN-HD 60364-5-534 |
| SPD typu 1 | wymagany przy **instalacji odgromowej** | — | jw., materiały producentów |

## [09.03 Ograniczniki przepięć typu 1, 2 i 3](09.03-ograniczniki-przepiec-typu-1-2-i-3.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Typ 1 — udar probierczy | **10/350 μs**, $I_{imp}$ | — | PN-EN 61643-11 |
| Typ 2 — udar probierczy | **8/20 μs**, $I_n$, $I_{max}$ | — | jw. |
| Typ 3 — udar probierczy | kombinowany **1,2/50 + 8/20 μs** | — | jw. |
| $I_{imp}$ typu 1 bez analizy ryzyka | ≥ **12,5 kA** na biegun | instalacje 230/400 V | PN-HD 60364-5-534 |
| $I_n$ typu 2 | ≥ **5 kA** (typowo 20 kA) | jw. | jw. |
| $U_C$ w sieci 230/400 V | typowo **275 V** (≥ 1,1 × 230 V) | TN | jw., katalogi |
| $U_P$ typu 2 | typowo **1,2–1,5 kV** | — | katalogi producentów |
| Dawne oznaczenia | B = typ 1, C = typ 2, D = typ 3 | — | — |

## [09.04 Montaż ogranicznika: długość połączeń i zabezpieczenie](09.04-montaz-ogranicznika-dlugosc-polaczen-i.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Długość połączeń a + b | ≤ **0,5 m** | każdy SPD | PN-HD 60364-5-534 |
| Spadek na przewodach przy udarze | ok. **1 kV/m** | orientacyjnie | materiały producentów |
| Odległość ochronna | ok. **10 m** | dalej — dodatkowy SPD | PN-HD 60364-5-534 |
| Przekrój przewodu do PE | ≥ **16 mm² Cu** (T1), ≥ **6 mm² Cu** (T2) | — | jw., Hager |
| Układ przed RCD i w TT | **3+1** (CT2) | — | jw. |
| Pomiar izolacji z SPD w obwodzie | napięcie probiercze **250 V DC**, ≥ **1 MΩ** | gdy SPD nie da się odłączyć | PN-HD 60364-6 |

## [09.05 Ochrona odgromowa budynku — podstawy](09.05-ochrona-odgromowa-budynku-podstawy.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Klasy instalacji odgromowej | **I–IV** (I najostrzejsza) | — | PN-EN 62305-3 |
| Typowy odstęp przewodów odprowadzających | I–II **10 m**, III **15 m**, IV **20 m** | wokół obwodu budynku | jw. |
| Wymiar oczek siatki zwodów | I **5×5**, II **10×10**, III **15×15**, IV **20×20 m** | — | jw. |
| Promień toczącej się kuli | I **20 m**, II **30 m**, III **45 m**, IV **60 m** | — | jw. |
| Rezystancja uziemienia | zalecana **< 10 Ω** | pomiar na rozłączonym złączu | jw. |
| Kontrola okresowa | co najmniej **raz na 5 lat** | instalacja elektryczna i piorunochronna | Prawo budowlane, art. 62 ust. 1 pkt 2 |
| Ograniczniki w budynku z LPS | **typ 1** | — | PN-HD 60364-5-534 |
