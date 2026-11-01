# Ściąga — 22 — Przyrządy pomiarowe

> Zebrane sekcje „Liczby do zapamiętania” ze wszystkich tematów modułu. [Spis modułu](README.md)

## [22.01 Kategorie pomiarowe CAT II–IV i bezpieczeństwo przyrządów](22.01-kategorie-pomiarowe-cat-iiiv-i-bezpieczenstwo.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Napięcie udarowe 600 V | CAT II **4 kV**, CAT III **6 kV**, CAT IV **8 kV** | wg napięcia pracy względem ziemi | PN-EN 61010; [Fluke](https://images.a.fluke.com/Web/FlukeCorporation/{ae5c184e-150a-4614-b77b-898cdc214834}_PLPL-safety_pages.pdf) |
| Napięcie udarowe 1000 V | CAT II **6 kV**, CAT III **8 kV** | jw. | jw. |
| Do rozdzielnicy mieszkaniowej | min. **CAT III 300 V** (zwykle CAT III 600/1000 V) | 230/400 V | jw. |
| Przy złączu i liczniku | **CAT IV** | 230/400 V | jw. |
| Rezystancja sprawnych przewodów | ok. **0,1–0,3 Ω** | test zwarcia sond | jw. |

## [22.02 Multimetr — co i jak mierzy](22.02-multimetr-co-i-jak-mierzy.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Rezystancja wewnętrzna przy V | rząd **10 MΩ** | typowe multimetry cyfrowe | instrukcje |
| Rezystancja przy A | bliska **0 Ω** | gniazdo A | — |
| Napięcie w gnieździe | **230 V ± 10 %** (207–253 V) | sieć nN | PN-EN 50160 |
| Pomiar Ω | tylko **bez napięcia** | zawsze | — |

## [22.03 Cęgi prądowe](22.03-cegi-pradowe.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| L + N w cęgach | **≈ 0 A** | sprawny obwód | — |
| Upływ za RCD 30 mA | ≤ **ok. 9 mA** (0,3 IΔn) | zalecenie | PN-HD 60364-5-53 |
| Upływ urządzenia z filtrem | **0,5–3 mA** | typowo | [08.06](../08-wylaczniki-roznicowopradowe/08.06-dlaczego-roznicowka-wybija-przyczyny-i-szukanie.md) |
| Moc z prądu | $P \approx 230 \cdot I \cdot \cos\varphi$ | 1 faza | — |

## [22.04 Wskaźniki napięcia i próbniki](22.04-wskazniki-napiecia-i-probniki.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Pary pomiaru 1-faz. | **3** (L–N, L–PE, N–PE) | sprawdzenie braku napięcia | [00.02](../00-bezpieczenstwo-najpierw/00.02-sprawdzanie-braku-napiecia-probnik-dwubiegunowy.md) |
| Pary pomiaru 3-faz. z N i PE | **10** | jw. | jw. |
| Kolejność | **sprawdź — zmierz — sprawdź** | zawsze | jw. |
| Norma wskaźników dwubiegunowych | **PN-EN 61243-3** | do 1000 V AC / 1500 V DC | PN-EN 61243-3 |

## [22.05 Miernik parametrów instalacji (MPI) — przegląd funkcji](22.05-miernik-parametrow-instalacji-mpi-przeglad.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Ciągłość | źródło **4–24 V**, prąd **≥ 0,2 A** | PE, połączenia wyrównawcze | PN-EN 61557-4 |
| Izolacja | **250 / 500 / 1000 V DC**, prąd znamionowy ≥ 1 mA | wg napięcia obwodu | PN-EN 61557-2 |
| Dopuszczalny błąd przyrządu | **± 30 %** (ciągłość, izolacja, pętla) | wg części 61557 | PN-EN 61557 |
| Wzorcowanie | zwykle co **1–2 lata** | praktyka, zalecenia producentów | — |

## [22.06 Kamera termowizyjna — kiedy się przydaje](22.06-kamera-termowizyjna-kiedy-sie-przydaje.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| ΔT do podobnego elementu | **1–3** możliwa · **4–15** prawdopodobna · **> 15 °C** natychmiast | podobne obciążenie | ANSI/NETA MTS, tab. 100.18 🇬🇧 |
| ΔT do otoczenia | **1–10 · 11–20 · 21–40 · > 40 °C** | brak elementu odniesienia | jw. |
| Emisyjność błyszczącej miedzi | bardzo mała (rzędu **0,1** i mniej) | pomiar „zaniżony” | dane materiałowe |
| Temperatura pracy PVC | **70 °C** | izolacja przewodów | [05.01](../05-przewody-i-kable/05.01-budowa-przewodu-i-kabla-zyla-izolacja-powloka.md) |
