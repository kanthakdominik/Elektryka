# Ściąga — 26 — Fotowoltaika, pompy ciepła, wallboxy i magazyny energii

> Zebrane sekcje „Liczby do zapamiętania” ze wszystkich tematów modułu. [Spis modułu](README.md)

## [26.01 Fotowoltaika — budowa instalacji](26.01-fotowoltaika-budowa-instalacji.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Mikroinstalacja | **≤ 50 kW**, sieć **< 110 kV** | definicja | ustawa o OZE |
| Uzgodnienie ppoż. + zawiadomienie PSP | **> 6,5 kW** | instalacje PV | Prawo budowlane; KM PSP |
| Napięcie łańcucha | do ok. **1000 V DC** (typowo 1000 V, czasem 1500 V w farmach) | domy, firmy | katalogi falowników |
| Uzysk roczny | ok. **900–1100 kWh/kWp** | Polska | dane branżowe |
| Panel | ok. **400–500 W**, Voc ok. **35–50 V** | typowe moduły | katalogi |
| Norma instalacji PV | **PN-HD 60364-7-712** | zasilanie PV | — |

## [26.02 Strona DC — zagrożenia i zabezpieczenia](26.02-strona-dc-zagrozenia-i-zabezpieczenia.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Wzrost Voc na mrozie | do ok. **15–20 %** | niska temperatura, słońce | ETI Polam |
| Dobór Ucpv ogranicznika DC | **≥ 1,2 × Uoc łańcucha** (STC) | SPD po stronie DC | ETI Polam |
| SPD przy panelach | gdy trasa DC **> 10 m** | ochrona falownika i modułów | jw. |
| Bezpieczniki gPV | zwykle przy **≥ 3** łańcuchach równoległych | ochrona przed prądem wstecznym | dane producentów |
| Przekroje przewodów DC | typowo **4–6 mm²** | domowe łańcuchy | katalogi |

## [26.03 Falownik i przyłączenie mikroinstalacji](26.03-falownik-i-przylaczenie-mikroinstalacji.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Górna granica napięcia | **253 V** (230 V + 10 %) — falownik się odłącza | sieć nn | Globenergia; PN-EN 50160 |
| Napięcie znamionowe | **230 V ± 10 %** | sieć nn | PN-EN 50160 |
| Rozliczenie nowych prosumentów | **net-billing** od **1.04.2022** | mikroinstalacje | ustawa o OZE |
| RCD falownika | **typ A** gdy producent dopuszcza (RCMU), inaczej **typ B** | strona AC | instrukcja falownika; PN-HD 60364-7-712 |
| Moc instalacji | **≤ moc przyłączeniowa** | przyłączenie na zgłoszenie | ustawa o OZE |

## [26.04 Pompa ciepła — zasilanie i zabezpieczenia](26.04-pompa-ciepla-zasilanie-i-zabezpieczenia.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| SCOP | ok. **3–4** (zależnie od pompy i domu) | pompy powietrze–woda | katalogi |
| Grzałka wspomagająca | ok. **3–9 kW** | typowe pompy domowe | katalogi |
| Moc elektryczna sprężarki | ok. **2–5 kW** przy maksimum | domy jednorodzinne | katalogi |
| Typ RCD | **wg instrukcji** (A, F lub B) | obwody pompy | instrukcja producenta |
| Typowa moc przyłączeniowa domu | **11–14 kW** — sprawdź bilans | przed zakupem | 14.05 |

## [26.05 Wallbox i ładowanie samochodu](26.05-wallbox-i-ladowanie-samochodu.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Typowa moc domowa | **11 kW = 3 × 16 A** | ładowanie AC | 🇬🇧 NEN guide |
| RCD | **30 mA typ B** lub **typ A + 6 mA DC** w wallboxie | każdy punkt ładowania | PN-HD 60364-7-722 |
| Wykrycie przerwy PEN | odłączenie w ciągu ok. **5 s** | TN-C-S, ładowanie na zewnątrz | jw. |
| Wysokość złącza | ok. **0,5–1,5 m** | montaż | 🇬🇧 NEN guide |
| Mode 2 z gniazda 230 V | ok. **8–10 A** | ładowanie awaryjne | instrukcje ładowarek |
| Zasięg z 1 h ładowania 11 kW | ok. **50–70 km** (przy 15–20 kWh/100 km) | szacunek | — |

## [26.06 Magazyn energii](26.06-magazyn-energii.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Pojemność domowa | ok. **5–15 kWh** | typowe magazyny | katalogi |
| Chemia | najczęściej **LFP** | domowe magazyny | katalogi |
| Trwałość LFP | ok. **3000–6000 cykli** | według producenta | katalogi |
| Sprawność cyklu | ok. **85–95 %** | ładowanie + rozładowanie | katalogi |
| Czas przełączenia na backup | **ms – kilka s** | zależnie od modelu | instrukcje |
