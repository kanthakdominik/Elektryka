# Ściąga — 15 — Rozdzielnica mieszkaniowa

> Zebrane sekcje „Liczby do zapamiętania” ze wszystkich tematów modułu. [Spis modułu](README.md)

## [15.01 Budowa rozdzielnicy: obudowa, szyna TH35, listwy N i PE, mostki](15.01-budowa-rozdzielnicy-obudowa-szyna-th35-listwy-n.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Szyna montażowa | **35 mm** (TH35) | — | PN-EN 60715 |
| Szerokość modułu | ok. **17,5–18 mm** | — | katalogi |
| Wyłącznik nadprądowy 1P | **1 moduł** | — | jw. |
| RCD 2P / 4P | **2 / 4 moduły** | — | jw. |
| Rezerwa miejsca | **20–30 %** | planowanie | praktyka, N SEP-E-002 |
| Stopień ochrony obudowy | co najmniej **IP2X** od frontu, typowo IP30–IP40 | wnętrza | [06.05](../06-osprzet-instalacyjny/06.05-stopnie-ochrony-ip.md) |

## [15.02 Schemat jednokreskowy — jak czytać i jak rysować](15.02-schemat-jednokreskowy-jak-czytac-i-jak-rysowac.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| 3 kreski | **3 żyły** (L, N, PE) | obwód 1-fazowy | PN-EN 60617 |
| 5 kresek | **5 żył** (L1–L3, N, PE) | obwód 3-fazowy | jw. |
| Opis obwodu | **numer, aparat, przewód, przeznaczenie, faza** | — | praktyka |

## [15.03 Oznaczanie obwodów i opis rozdzielnicy](15.03-oznaczanie-obwodow-i-opis-rozdzielnicy.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Oznaczenie aparatu | **numer + nazwa obwodu** | każdy aparat | PN-HD 60364-5-51, 514 |
| Schemat | **w rozdzielnicy** lub przy niej | — | jw. |
| Wiele źródeł zasilania | **ostrzeżenie** na rozdzielnicy | PV, agregat | PN-HD 60364-7-712, jw. |

## [15.04 Przykład: kawalerka, zasilanie jednofazowe](15.04-przyklad-kawalerka-zasilanie-jednofazowe.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Moc przy 25 A, 1-faz. | ok. **5,75 kW** | teoretycznie | [14.03](../14-od-slupa-do-gniazdka/14.03-licznik-i-zabezpieczenie-przedlicznikowe.md) |
| Oświetlenie | **B10, 3×1,5** | typowo | [07.06](../07-zabezpieczenia-nadpradowe/07.06-koordynacja-zabezpieczenia-z-przewodem.md) |
| Gniazda | **B16, 3×2,5** | typowo | jw. |
| RCD | **30 mA, typ A**, co najmniej **2 grupy** | — | [08.07](../08-wylaczniki-roznicowopradowe/08.07-podzial-obwodow-miedzy-wylaczniki.md) |
| Moduły (przykład) | ok. **20** + rezerwa | — | obliczenie |

## [15.05 Przykład: mieszkanie, zasilanie trójfazowe](15.05-przyklad-mieszkanie-zasilanie-trojfazowe.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Moc przy 3 × 25 A | ok. **17 kW** (teoretycznie, symetrycznie) | — | [14.03](../14-od-slupa-do-gniazdka/14.03-licznik-i-zabezpieczenie-przedlicznikowe.md) |
| Płyta indukcyjna 3-faz. | **B16 3P, 5×2,5** (typowo, wg producenta) | — | instrukcje producentów |
| RCD 4P | **40 A / 30 mA, typ A** (typowo) | — | — |
| Napięcie między fazami | **400 V** | — | [02.03](../02-prad-przemienny-230-400/02.03-uklad-trojfazowy-230-v-i-400-v-kolejnosc-faz.md) |

## [15.06 Przykład: dom jednorodzinny](15.06-przyklad-dom-jednorodzinny.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Czas wyłączenia obwodu rozdzielczego TN | **5 s** | zasilanie podrozdzielnic | PN-HD 60364-4-41, 411.3.2.3 |
| Czas wyłączenia obwodu odbiorczego TN | **0,4 s** | gniazda, odbiory | jw. |
| SPD przy linii napowietrznej / LPS | **typ 1+2** | — | [09.02](../09-ochrona-przeciwprzepieciowa/09.02-kategorie-wytrzymalosci-udarowej-iiv.md) |
| Spadek napięcia od licznika | ≤ **3 %** | do najdalszego odbiornika | N SEP-E-002 |

## [15.07 Montaż i porządek przewodów w rozdzielnicy](15.07-montaz-i-porzadek-przewodow-w-rozdzielnicy.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Przewody pod zaciskiem | **1** (chyba że producent dopuszcza więcej) | — | instrukcje aparatów |
| Moment dokręcenia | wg producenta, typowo **2–3,5 N·m** | aparaty modułowe | katalogi |
| Kolejność podłączania | **PE → N → L** | — | praktyka |
| Kolejność odłączania | **L → N → PE** | — | jw. |
