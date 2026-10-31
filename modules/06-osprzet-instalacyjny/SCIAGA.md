# Ściąga — 06 — Osprzęt instalacyjny

> Zebrane sekcje „Liczby do zapamiętania” ze wszystkich tematów modułu. [Spis modułu](README.md)

## [06.01 Gniazda wtyczkowe: jednofazowe, z bolcem ochronnym, trójfazowe](06.01-gniazda-wtyczkowe-jednofazowe-z-bolcem.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Gniazdo jednofazowe domowe | **16 A, 250 V** | typ E / F | PN-IEC 60884-1 |
| Typowe zabezpieczenie obwodu gniazd | **B16**, przewód **2,5 mm²** | mieszkania | praktyka, N SEP-E-002 |
| Moc „na obwód” przy B16 | ok. **3,7 kW** | 230 V × 16 A | obliczenie |
| Faza w gnieździe | **lewy otwór** (patrząc od przodu, bolec u góry) | zasada przyjęta w Polsce | praktyka montażowa |
| Gniazdo siłowe niebieskie / czerwone | **230 V / 400 V** | CEE | PN-EN 60309 |
| Ochrona różnicowoprądowa gniazd | RCD **≤ 30 mA** | gniazda do 32 A | PN-HD 60364-4-41, 411.3.3 |

## [06.02 Łączniki: jednobiegunowy, dwubiegunowy, świecznikowy, schodowy, krzyżowy](06.02-laczniki-jednobiegunowy-dwubiegunowy.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Prąd znamionowy łącznika domowego | zwykle **10 A** (10 AX), 250 V | — | PN-EN 60669-1, dane producentów |
| Liczba żył między łącznikami schodowymi | **2** korespondencyjne | + PE, jeśli łącznik jest w obudowie metalowej / dla porządku | — |
| Łącznik krzyżowy | **4** zaciski | — | — |
| Łącznik schodowy | **3** zaciski | — | — |

## [06.03 Puszki instalacyjne i rozgałęźne](06.03-puszki-instalacyjne-i-rozgalezne.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Średnica standardowej puszki osprzętowej | **60 mm** | osprzęt podtynkowy | normy i katalogi producentów |
| Rozstaw puszek w ramce wielokrotnej | **71 mm** | typowy system ramek | katalogi producentów |
| Głębokość puszki płytkiej / głębokiej | ok. **40 / 60 mm** | — | jw. |
| Puszka na zewnątrz, w garażu | zwykle **IP44–IP55** i więcej | wg warunków | PN-EN 60529, projekt |

## [06.04 Złączki i łączenie przewodów — dlaczego nie skręcamy](06.04-zlaczki-i-laczenie-przewodow-dlaczego-nie.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Długość odizolowania | zwykle **9–12 mm** | wg oznaczenia na złączce | instrukcje producentów |
| Żyły w jednym otworze złączki | **1** | złączki sprężynowe | jw. |
| Moc wydzielana na styku | $P = I^2 \cdot R_{styku}$ | — | [01.06](../01-prad-napiecie-opor/01.06-grzanie-przewodow-i-spadek-napiecia.md) |
| Styk 0,1 Ω przy 16 A | ok. **26 W** w jednym punkcie | — | obliczenie |

## [06.05 Stopnie ochrony IP](06.05-stopnie-ochrony-ip.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Pokoje mieszkalne | **IP20** | suche pomieszczenia | praktyka |
| Łazienka, strefy 1 i 2 | **IPX4** (IPX5 przy myciu strumieniem) | — | PN-HD 60364-7-701 |
| Łazienka, strefa 0 | **IPX7** | — | jw. |
| Na zewnątrz | zwykle **≥ IP44** | wg warunków | praktyka, projekt |
| 1. cyfra 2 / 4 | palec **12,5 mm** / drut **1 mm** | — | PN-EN 60529 |
| 2. cyfra 4 / 7 | **bryzgi** / **chwilowe zanurzenie** | — | jw. |

## [06.06 Klasy ochronności urządzeń: 0, I, II, III](06.06-klasy-ochronnosci-urzadzen-0-i-ii-iii.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Klasa 0 | tylko izolacja podstawowa, **brak PE** | nie stosuje się w zwykłych instalacjach | PN-EN 61140 |
| Klasa I | izolacja podstawowa + **PE** | wymaga gniazda z PE | jw. |
| Klasa II | izolacja **podwójna lub wzmocniona**, bez PE | — | jw. |
| Klasa III | zasilanie **SELV/PELV ≤ 50 V AC** (≤ 120 V DC) | — | jw., PN-HD 60364-4-41 |
