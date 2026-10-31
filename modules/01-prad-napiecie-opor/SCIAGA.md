# Ściąga — 01 Prąd, napięcie, opór, moc i energia

> Zebrane sekcje „Liczby do zapamiętania” ze wszystkich tematów modułu. [Spis modułu](README.md)

## [01.01 Ładunek i prąd](01.01-ladunek-i-prad-co-wlasciwie-plynie-w-przewodzie.md)

| Wielkość | Wartość |
|----------|---------|
| Prąd | $I = Q/t$; amper [A] = kulomb na sekundę |
| 1 A | ≈ 6,24·10¹⁸ elektronów na sekundę |
| 1 Ah | 3600 C |
| Prędkość dryfu | ułamki mm/s |
| Pomiar | amperomierz **szeregowo** albo cęgi na **jednym** przewodzie |
| Groźny prąd dla człowieka | już dziesiątki mA |

## [01.02 Napięcie](01.02-napiecie-roznica-cisnien-miedzy-dwoma-punktami.md)

| Wielkość | Wartość |
|----------|---------|
| L–N, L–PE | 230 V |
| L–L | 400 V ≈ 230·√3 |
| N–PE | prawie 0 V |
| Dopuszczalne odchylenie | ±10 % → **207–253 V** (95 % średnich 10-min w tygodniu) — rozporządzenie MKiŚ 2023, § 45 |
| Częstotliwość | 50 Hz ±1 % |
| Pomiar | woltomierz **równolegle**, między dwoma punktami |

## [01.03 Opór i prawo Ohma](01.03-opor-i-prawo-ohma.md)

| Wielkość | Wartość |
|----------|---------|
| Prawo Ohma | $I = U/R$ |
| Opór przewodu | $R = \rho\, l / S$ |
| ρ miedzi | 0,0175 Ω·mm²/m |
| ρ aluminium | 0,0286 Ω·mm²/m (≈ 1,6 × Cu) |
| Temperatura | Cu: +0,4 %/°C, przy 70 °C ok. +20 % |
| 1 m Cu 1,5 mm² / 2,5 mm² | ≈ 0,012 Ω / ≈ 0,007 Ω |
| Ciało człowieka | rzędu 1000 Ω |

## [01.04 Moc i energia](01.04-moc-i-energia-waty-kilowatogodziny-i-rachunek.md)

| Wielkość | Wartość |
|----------|---------|
| Moc | $P = U I = I^2 R = U^2/R$ |
| Energia | $E = P t$; 1 kWh = 3,6 MJ |
| Prąd przy 230 V | ≈ 4,35 A na 1 kW |
| 16 A × 230 V | 3680 W |
| Grzałka przy 207 V | 81 % mocy |
| Moc z licznika | $P = n \cdot 3600 / (C \cdot t)$ [kW] |

## [01.05 Szeregowo i równolegle](01.05-polaczenie-szeregowe-i-rownolegle.md)

| | Szeregowo | Równolegle |
|---|---|---|
| Prąd | ten sam | sumuje się |
| Napięcie | dzieli się | to samo |
| Opór | $R_1 + R_2$ | $1/R = 1/R_1 + 1/R_2$ |

Gniazdo z bolcem: 16 A / 3680 W · wtyczka płaska „euro”: 2,5 A / 575 W · obwód B16: **16 A na cały obwód**.

## [01.06 Grzanie przewodów i spadek napięcia](01.06-grzanie-przewodow-i-spadek-napiecia.md)

| Wielkość | Wartość |
|----------|---------|
| Ciepło | $P = I^2 R$ — 2 × prąd = 4 × ciepło |
| Spadek (1 faza) | $\Delta U = 2 l I \rho / S$ |
| Dopuszczalny spadek licznik → odbiornik | **3 %** (N SEP-E-002) |
| Zalecenie PN-HD 60364-5-52 zał. G | 3 % oświetlenie, 5 % inne |
| Izolacja PVC | 70 °C długotrwale |
| Bęben | rozwijaj — moc dla zwiniętego kilka razy mniejsza |

## [01.07 Przeciążenie a zwarcie](01.07-przeciazenie-a-zwarcie-dwie-rozne-awarie.md)

| Wielkość | Wartość |
|----------|---------|
| Prąd zwarcia | $I_{zw} = U_0 / Z_s$ |
| Nie zadziała przez 1 h | 1,13 $I_n$ |
| Zadziała w < 1 h | 1,45 $I_n$ |
| Natychmiast | B: 3–5 $I_n$ · C: 5–10 $I_n$ · D: 10–20 $I_n$ |
| B16 pewnie natychmiast | ≥ 80 A |
| Przeciążenie | człon **termiczny** (bimetal) |
| Zwarcie | człon **elektromagnetyczny** (cewka) + komora gaszeniowa |
| Luźny zacisk | **żaden** z nich — AFDD (moduł 10) |
