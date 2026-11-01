# Ściąga — 16 — Planowanie obwodów

> Zebrane sekcje „Liczby do zapamiętania” ze wszystkich tematów modułu. [Spis modułu](README.md)

## [16.01 Podział instalacji na obwody](16.01-podzial-instalacji-na-obwody.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Minimalna liczba obwodów oświetlenia i gniazd | do 50 m² — **2**; 50–75 m² — **3**; 75–100 m² — **4**; 100–125 m² — **5**; ponad 125 m² — **6** | mieszkanie; obwody wydzielone dochodzą osobno | N SEP-E-002, [Inżynier Budownictwa](https://inzynierbudownictwa.pl/?p=10433) |
| Osobny obwód | odbiornik powyżej ok. **2 kW** | praktyka | [Murator](https://muratordom.pl/instalacje/instalacja-elektryczna/instalacja-elektryczna-w-kuchni-aa-GEzk-fazJ-6PoY.html), N SEP-E-002 |
| Typowe zabezpieczenie | oświetlenie **B10**, gniazda **B16** | przewody 1,5 / 2,5 mm² Cu | [07.06](../07-zabezpieczenia-nadpradowe/07.06-koordynacja-zabezpieczenia-z-przewodem.md) |
| Rezerwa w rozdzielnicy | **20–30 %** miejsca | planowanie | [15.01](../15-rozdzielnica-mieszkaniowa/15.01-budowa-rozdzielnicy-obudowa-szyna-th35-listwy-n.md) |

## [16.02 Dobór przekroju i zabezpieczenia — procedura krok po kroku](16.02-dobor-przekroju-i-zabezpieczenia-procedura-krok.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Prąd 1-fazowy | $I_B = P / (230 \cdot \cos\varphi)$; **1 kW ≈ 4,35 A** | cos φ = 1 | — |
| Prąd 3-fazowy | $I_B = P / (\sqrt{3} \cdot 400 \cdot \cos\varphi)$; **1 kW ≈ 1,44 A** na fazę | odbiornik symetryczny, cos φ = 1 | — |
| Łańcuch doboru | $I_B \le I_n \le I_z$ i $I_2 \le 1{,}45 I_z$ | zawsze | PN-HD 60364-4-43, 433.1 |
| Szereg prądów wyłączników | 6, 10, 13, 16, 20, 25, 32, 40, 50, 63 A | wyłączniki nadprądowe | PN-EN 60898-1 |
| Typowe pary | **1,5 mm² — B10**, **2,5 mm² — B16**, **4 mm² — B20/B25**, **6 mm² — B32** | Cu, PVC, ułożenie C, bez grupowania | tablice obciążalności, praktyka |

## [16.03 Sprawdzanie spadku napięcia](16.03-sprawdzanie-spadku-napiecia.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Spadek 1-faz. | $\Delta U\% = \dfrac{200 P l}{\gamma S U^2}$ | przekroje do ok. 16 mm², U = 230 V | — |
| Spadek 3-faz. | $\Delta U\% = \dfrac{100 P l}{\gamma S U^2}$ | obciążenie symetryczne, U = 400 V | — |
| Konduktywność γ | Cu **56**, Al **34** m/(Ω·mm²) | ok. 20 °C; w temperaturze pracy opór większy o ok. 20 % | dane materiałowe |
| Dopuszczalny spadek od licznika do odbiornika | **3 %** | budynki mieszkalne | N SEP-E-002 |
| Zalecany maks. spadek od złącza | **3 %** oświetlenie, **5 %** inne | instalacje zasilane z sieci publicznej nN | PN-HD 60364-5-52, zał. G |
| Ile to woltów | 3 % z 230 V = **6,9 V**; 5 % = **11,5 V** | — | — |

## [16.04 Strefy instalacyjne i trasy przewodów](16.04-strefy-instalacyjne-i-trasy-przewodow.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Strefa pozioma górna | **15–45 cm** pod sufitem (praktyka PL: ok. **30 cm**) | ściany w pomieszczeniach mieszkalnych | DIN 18015-3 🇩🇪, [ZPE](https://zpe.gov.pl/a/DxddThkId) |
| Strefa pozioma dolna | **15–45 cm** nad podłogą | jw. | DIN 18015-3 🇩🇪 |
| Strefa pozioma środkowa | **100–130 cm** nad podłogą | jw. | jw. |
| Strefa pionowa | **10–30 cm** od drzwi, okien, narożników (praktyka PL: ok. **15 cm** od krawędzi) | jw. | DIN 18015-3 🇩🇪, [ZPE](https://zpe.gov.pl/a/DxddThkId) |
| Strefy w łazience | przewody w strefach 1 i 2 — natynkowo albo na głębokości ≥ **5 cm** | łazienki | [Inżynier Budownictwa](https://inzynierbudownictwa.pl/?p=11855), [17.01](../17-pomieszczenia-szczegolne/17.01-lazienka-strefy-0-1-i-2.md) |

## [16.05 Wysokości montażu i liczba gniazd](16.05-wysokosci-montazu-i-liczba-gniazd.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Łącznik | ok. **105 cm** nad podłogą, ok. **15 cm** od ościeżnicy, po stronie klamki | pomieszczenia mieszkalne | N SEP-E-002, [ZPE](https://zpe.gov.pl/a/DxddThkId) |
| Gniazdo w pokoju | ok. **30 cm** nad podłogą | jw. | jw. |
| Gniazdo nad blatem | **20–30 cm** nad blatem (ok. 110–120 cm nad podłogą) | kuchnia | [Murator](https://muratordom.pl/instalacje/instalacja-elektryczna/instalacja-elektryczna-w-kuchni-aa-GEzk-fazJ-6PoY.html) |
| Gniazda dla urządzeń w zabudowie | **30–50 cm** nad podłogą, w sąsiedniej szafce | kuchnia | jw. |
| Łącznik światła łazienki | **na zewnątrz** łazienki, po stronie klamki | praktyka | [ZPE](https://zpe.gov.pl/a/DxddThkId) |

## [16.06 Obwody wydzielone: płyta, piekarnik, pralka, zmywarka](16.06-obwody-wydzielone-plyta-piekarnik-pralka.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Płyta indukcyjna | **3 × B16**, przewód **5 × 2,5 mm²**, puszka pod blatem | typowa płyta 7–7,5 kW; zawsze wg instrukcji | instrukcje producentów, praktyka |
| Piekarnik, zmywarka, pralka | **B16**, **3 × 2,5 mm²**, każdy osobno | typowo 2–3,6 kW | N SEP-E-002 (osobne obwody) |
| RCD dla obwodów z silnikiem/falownikiem | typ **A** lub **F** (nie AC) | pralki, zmywarki, płyty, pompy ciepła | zalecenia producentów, [08.03](../08-wylaczniki-roznicowopradowe/08.03-typy-ac-a-f-i-b-ktory-do-czego.md) |
| Moc 3-faz. na fazę | **7,2 kW ≈ 3 × 2,4 kW** → ok. **10,4 A** na fazę | płyta na 3 fazach | $I = P / (\sqrt{3} \cdot 400)$ |
