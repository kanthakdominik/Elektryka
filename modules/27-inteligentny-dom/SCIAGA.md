# Ściąga — 27 — Inteligentny dom

> Zebrane sekcje „Liczby do zapamiętania” ze wszystkich tematów modułu. [Spis modułu](README.md)

## [27.01 Moduły bezprzewodowe w puszce — bezpieczny montaż](27.01-moduly-bezprzewodowe-w-puszce-bezpieczny-montaz.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Głębokość puszki pod moduł | zwykle **≥ 60 mm** | moduł + łącznik w jednej puszce | instrukcje producentów |
| Obciążalność styku | podana w A, dla **LED** zwykle **dużo mniejsza** | dobór do odbiornika | instrukcja modułu |
| Napięcie wejść SW | **230 V** (o ile instrukcja nie mówi inaczej) | moduły zasilane z sieci | instrukcja modułu |
| Zabezpieczenie obwodu | nie większe niż dopuszcza moduł (np. **10 / 16 A**) | wymagania producenta | instrukcja modułu |

## [27.02 Przewód neutralny w puszce łącznika](27.02-przewod-neutralny-w-puszce-lacznika.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Żyły do łącznika (klasycznie) | **2 + PE** (L, L′) | obwód z łącznikiem 1-biegunowym | 18.02 |
| Żyły do łącznika z N | **3 + PE** (L, N, L′) | łączniki elektroniczne, moduły | dobra praktyka |
| Minimalne obciążenie modułu bez N | często **kilka W–kilkanaście W** (wg instrukcji) | moduły 2-przewodowe | instrukcje producentów |

## [27.03 Systemy przewodowe: KNX, Modbus — przegląd](27.03-systemy-przewodowe-knx-modbus-przeglad.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Napięcie KNX | ok. **30 V DC**, SELV | magistrala TP | ABB i-bus KNX |
| Przewód KNX | np. **YCYM 2×2×0,8** | instalacja TP | jw. |
| Linia KNX | do **64** urządzeń, **1000 m** | segment linii | wytyczne KNX |
| Odległości KNX | zasilacz–urządzenie **≤ 350 m**, urządzenie–urządzenie **≤ 700 m** | segment linii | wytyczne KNX |
| Terminator RS-485 | **120 Ω** na obu końcach | Modbus RTU | standard RS-485 |
| DALI | **64** oprawy na linię, ok. **16 V DC** | sterowanie oświetleniem | IEC 62386 |

## [27.04 Automatyka w rozdzielnicy](27.04-automatyka-w-rozdzielnicy.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Rezerwa miejsca | ok. **20 %** wolnych pól | rozdzielnice domowe | dobra praktyka |
| Obwód zasilania automatyki | osobny, np. **B6** | sterownik, zasilacze | dobra praktyka |
| Napięcie zasilaczy automatyki | **12 / 24 V DC** (SELV) | sterowniki, czujniki | katalogi |
| Szerokość modułu | **17,5–18 mm** | aparatura na TH35 | PN-EN 60715 |
