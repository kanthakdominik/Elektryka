# Ściąga — 19 — Prace krok po kroku

> Zebrane sekcje „Liczby do zapamiętania” ze wszystkich tematów modułu. [Spis modułu](README.md)

## [19.01 Wymiana gniazda wtyczkowego](19.01-wymiana-gniazda-wtyczkowego.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Kolejność podłączania | **PE → N → L** (odłączanie odwrotnie) | zawsze | praktyka, [15.07](../15-rozdzielnica-mieszkaniowa/15.07-montaz-i-porzadek-przewodow-w-rozdzielnicy.md) |
| Faza w gnieździe | **lewy** otwór przy bolcu u góry | konwencja w Polsce | [06.01](../06-osprzet-instalacyjny/06.01-gniazda-wtyczkowe-jednofazowe-z-bolcem.md) |
| Gniazdo jednofazowe | **16 A, 250 V** | typowe gniazdo domowe | PN-IEC 60884-1 |
| Długość odizolowania | wg oznaczenia na gnieździe, zwykle **8–12 mm** | — | instrukcje producentów |
| Zapas przewodu w puszce | tyle, żeby wyjąć gniazdo przed puszkę (kilka–kilkanaście cm) | — | praktyka |

## [19.02 Wymiana łącznika](19.02-wymiana-lacznika.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Prąd łącznika | typowo **10 A** (10 AX), 250 V | łączniki oświetleniowe | PN-EN 60669-1 |
| Zaciski | 1 → **2**, 5 → **3**, 6 → **3**, 7 → **4** | — | — |
| Wysokość | ok. **105 cm** | — | [16.05](../16-planowanie-obwodow/16.05-wysokosci-montazu-i-liczba-gniazd.md) |
| Moc LED na łączniku/ściemniaczu | wg katalogu (często mniejsza niż dla żarówek) | LED | instrukcje |

## [19.03 Montaż lampy i oprawy](19.03-montaz-lampy-i-oprawy.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Żyły przy lampie | **3** (łącznikowy, N, PE), przy świeczniku **4** | — | [18.02](../18-oswietlenie/18.02-lacznik-jednobiegunowy-i-swiecznikowy-schematy.md) |
| Klasa I | zacisk ⏚ — **musi** być PE | oprawy metalowe | PN-EN 60598-1 |
| Klasa II | symbol ⧈ — **bez** PE | — | jw. |
| Obwód oświetlenia | typowo **B10**, 1,5 mm² | — | [16.02](../16-planowanie-obwodow/16.02-dobor-przekroju-i-zabezpieczenia-procedura-krok.md) |

## [19.04 Podłączenie płyty indukcyjnej](19.04-podlaczenie-plyty-indukcyjnej.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Obwód płyty | **5 × 2,5 mm²**, **3 × B16** | typowa płyta 7–7,5 kW, 3 fazy | instrukcje producentów |
| Prąd przy 1 fazie | ok. **30–32 A** | 7–7,4 kW na 230 V | $I = P/U$ |
| Przewód przyłączeniowy | np. **H05VV-F 5G2,5** | wg instrukcji | jw. |
| Mostki | wg rysunku **na płycie** | zawsze | jw. |

## [19.05 Dodanie nowego obwodu w rozdzielnicy](19.05-dodanie-nowego-obwodu-w-rozdzielnicy.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Kolejność podłączania | **PE → N → L** | rozdzielnica | praktyka |
| N nowego obwodu | listwa N **tej samej** grupy RCD | zawsze | [08.07](../08-wylaczniki-roznicowopradowe/08.07-podzial-obwodow-miedzy-wylaczniki.md) |
| Pod napięciem mimo wyłączenia rozłącznika | **zaciski wejściowe rozłącznika i WLZ** | zawsze | — |
| Po zmianie instalacji | **pomiary** przed oddaniem do użytku | nowy obwód | PN-HD 60364-6 |
| Rezystancja izolacji | ≥ **1 MΩ** przy 500 V DC | obwody do 500 V | PN-HD 60364-6, tab. 6.1 |

## [19.06 Bruzdy, puszki i prowadzenie przewodów w ścianie](19.06-bruzdy-puszki-i-prowadzenie-przewodow-w-scianie.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Bruzda pionowa | głęb. ≤ **30 mm**; szer. **100–200 mm** wg grubości ściany | gotowy mur, bez obliczeń | PN-EN 1996-1-1, tab. 8.2; [IB](https://inzynierbudownictwa.pl/?p=9815) |
| Bruzda pozioma | ściana ≤ 115 mm: **niedozwolona**; 116–175 mm: **15 mm** (do 1,25 m); 176–225 mm: **10/20 mm** | bez obliczeń | PN-EN 1996-1-1, tab. 8.3 |
| Położenie bruzd poziomych | w pasie **1/8 wysokości ściany** przy stropie | — | jw., p. 8.6.3 |
| Odstęp od otworu | ≥ **0,5 m** (bruzda pozioma) | — | jw. |
| Ściana < 85 mm | bez obliczeń bruzd **nie wolno** | — | jw. |

## [19.07 Zakańczanie przewodów: tulejki, zaciski, momenty dokręcania](19.07-zakanczanie-przewodow-tulejki-zaciski-momenty.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Długość odizolowania | zwykle **8–12 mm** (wg zacisku) | osprzęt, aparaty | instrukcje producentów |
| Moment — przykład 1 | **2 N·m** (0,5–25 A), **3,5 N·m** (32–63 A) | wyłączniki jednego producenta | [Schneider Electric](https://www.se.com/pl/pl/faqs/FAQ000269417) |
| Moment — przykład 2 | **2,8 N·m** | wyłącznik B20 innego producenta | [Hager](https://hager.com/pl/katalog/produkt/mbn520e-mcb-6ka-1p-n-b-20a) |
| Tulejki (DIN) | 1,5 mm² **czarna**, 2,5 mm² **niebieska**, 6 mm² **żółta** | system DIN | DIN 46228-4 |
| Przewodów w zacisku | **1**, chyba że producent pozwala na 2 tego samego przekroju | — | instrukcje |
