# Ściąga — 18 — Oświetlenie

> Zebrane sekcje „Liczby do zapamiętania” ze wszystkich tematów modułu. [Spis modułu](README.md)

## [18.01 Źródła światła i zasilacze LED](18.01-zrodla-swiatla-i-zasilacze-led.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Odpowiedniki żarówek | 25 W ≈ **250 lm**; 40 W ≈ **470 lm**; 60 W ≈ **806 lm**; 75 W ≈ **1055 lm**; 100 W ≈ **1521 lm** | żarówki ogólnego przeznaczenia | rozp. (UE) nr 1194/2012 |
| Barwa | **2700–3000 K** ciepła, **4000 K** neutralna, **6500 K** zimna | — | — |
| Ra | ≥ **80** w domu, ≥ **90** przy ocenie kolorów | — | praktyka |
| Typowe napięcia zasilaczy CV | **12 V**, **24 V** DC | taśmy, moduły | katalogi |
| Typowe prądy zasilaczy CC | **350**, **500**, **700** mA | oprawy, panele | katalogi |
| Skala etykiet energetycznych | **A–G**, nowa od **1.09.2021** | źródła światła w UE | rozp. (UE) 2019/2015 |

## [18.02 Łącznik jednobiegunowy i świecznikowy — schematy](18.02-lacznik-jednobiegunowy-i-swiecznikowy-schematy.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Łącznik przerywa | **fazę L** | łącznik jednobiegunowy | PN-HD 60364 (łączniki jednobiegunowe tylko w przewodzie fazowym) |
| Przewód do łącznika 1 | **3 żyły** (L, łącznikowy, PE lub N) | wg układu połączeń | praktyka |
| Przewód do lampy przy łączniku 5 | **4 żyły** (2 × łącznikowy, N, PE) | żyrandol na 2 grupy | praktyka |
| Prąd łączników | zwykle **10 A** (10 AX) | 230 V | katalogi, PN-EN 60669-1 |
| Wysokość łącznika | ok. **105 cm** | [16.05](../16-planowanie-obwodow/16.05-wysokosci-montazu-i-liczba-gniazd.md) | N SEP-E-002 |

## [18.03 Układ schodowy i krzyżowy — schematy](18.03-uklad-schodowy-i-krzyzowy-schematy.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Miejsca sterowania | **2** — dwa łączniki 6; **3** — 6 + 7 + 6; **n** — 6 + (n−2) × 7 + 6 | — | — |
| Zaciski | łącznik 6: **3**; łącznik 7: **4** | — | PN-EN 60669-1 |
| Żyły między łącznikami | **2** korespondencje (+ PE) | — | praktyka |
| Przewód przy 3+ miejscach | rozważ przekaźnik impulsowy | wiele miejsc | [18.04](18.04-przekaznik-impulsowy-zamiast-lacznikow.md) |

## [18.04 Przekaźnik impulsowy zamiast łączników schodowych](18.04-przekaznik-impulsowy-zamiast-lacznikow.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Przewód do przycisku | **2 żyły** (+ PE wg potrzeby) | przekaźnik impulsowy | praktyka |
| Napięcie cewki | typowo **230 V AC**, także **12/24 V** AC/DC | wg wersji | katalogi producentów |
| Prąd styku | typowo **16 A** (obciążalność LED mniejsza — wg katalogu) | — | katalogi, [10.02](../10-aparatura-modulowa/10.02-stycznik-modulowy-i-przekaznik-bistabilny.md) |
| Czas automatu schodowego | typowo **0,5–7 min** (lub więcej) | — | katalogi |
| Kiedy przekaźnik | od **3–4 miejsc** sterowania | praktyka | — |

## [18.05 Ściemniacze i współpraca z LED](18.05-sciemniacze-i-wspolpraca-z-led.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| RL (narastające) | żarówki, halogeny, transformatory żelazne (L) | — | katalogi producentów |
| RC (opadające) | LED, zasilacze elektroniczne (C) | — | jw. |
| Moc dla LED | zwykle **dużo mniejsza** niż dla żarówek (często kilka–kilkanaście razy) | — | instrukcje ściemniaczy |
| Moc minimalna | ≤ moc podłączonych źródeł | — | [Shelly](https://www.shelly.com/pl/pages/dimming-leds) |
| Ściemniacze w ramce wielokrotnej | moc każdego **obniżona** wg instrukcji | — | instrukcje |

## [18.06 Taśmy LED i ich zasilanie](18.06-tasmy-led-i-ich-zasilanie.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Moc zasilacza | moc taśmy × długość + **ok. 20 %** | — | praktyka, [AVSL 🇬🇧](https://avsl.com/support/howtoselectledtapepower) |
| Długość z jednego punktu | **5 m** przy 12 V, **10 m** przy 24 V | typowe taśmy | [AVSL 🇬🇧](https://avsl.com/support/howtoselectledtapepower) |
| Przewód zasilający | **0,75 mm²** do ok. 10 m, **1 mm²** do ok. 20 m | typowe obciążenia | jw. |
| Złączki zaciskowe do taśm | często **max 2 A** | wg katalogu | [Kanlux](https://kanlux.com/download/mat/38472.pdf) |
| IP | **IP20** wnętrza suche, **IP65** kuchnia, łazienka | — | katalogi |
| Prąd taśmy | $I = P / U$: 40 W przy 12 V = **3,3 A**, przy 24 V = **1,7 A** | — | — |
