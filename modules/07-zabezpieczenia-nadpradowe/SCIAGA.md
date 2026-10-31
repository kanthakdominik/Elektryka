# Ściąga — 07 — Zabezpieczenia nadprądowe

> Zebrane sekcje „Liczby do zapamiętania” ze wszystkich tematów modułu. [Spis modułu](README.md)

## [07.01 Przeciążenie i zwarcie z punktu widzenia zabezpieczenia](07.01-przeciazenie-i-zwarcie-z-punktu-widzenia.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Prąd zwarcia | $I_k = U_0 / Z_s$ | pętla L–N lub L–PE | prawo Ohma |
| Typowe przeciążenie | ok. **1,1–3 × In** | — | — |
| Typowe zwarcie w mieszkaniu | od **~100 A** do **kilku kA** | zależnie od $Z_s$ | — |
| Czas wyłączenia zwarcia przez wyłącznik | **< 0,1 s** (zwykle kilka ms) | powyżej progu wyzwalacza elektromagnetycznego | PN-EN 60898-1 |
| Czas dopuszczalny zwarcia dla przewodu | $t = (k \cdot S / I)^2$ | $t \le 5$ s; Cu/PVC k = 115 | PN-HD 60364-4-43, 434.5.2 |

## [07.02 Bezpieczniki topikowe: wkładki gG, gwintowe i przemysłowe](07.02-bezpieczniki-topikowe-wkladki-gg-gwintowe-i.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| gG: prąd umowny niezadziałania | **1,25 × In** | In ≥ 16 A, czas umowny 1 h (do 63 A) | PN-EN 60269-1 |
| gG: prąd umowny zadziałania $I_2$ | **1,6 × In** | jw. | jw. |
| gG, 4 A < In < 16 A | $I_{nf}$ = **1,5 × In**, $I_2$ = **1,9 × In** | — | jw. |
| Selektywność wkładek gG | stosunek prądów **≥ 1,6** | wkładki tej samej klasy | jw. |
| Kolor wskaźnika D/D0 | 6 A zielony · 10 A czerwony · 16 A szary · 20 A niebieski · 25 A żółty · 35 A czarny · 63 A miedziany | — | normy wkładek |
| Zdolność wyłączania wkładek | **50 kA** (D/D0), **120 kA** (NH) | typowo | dane producentów |

## [07.03 Wyłącznik nadprądowy — budowa i dwa wyzwalacze](07.03-wylacznik-nadpradowy-budowa-i-dwa-wyzwalacze.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Prądy znamionowe (typoszereg) | 6, 10, 13, 16, 20, 25, 32, 40, 50, 63 A | wyłączniki domowe | PN-EN 60898-1 |
| Prąd umowny niezadziałania | **1,13 × In** (≥ 1 h bez zadziałania) | temperatura odniesienia 30 °C | jw. |
| Prąd umowny zadziałania $I_2$ | **1,45 × In** (< 1 h) | jw. | jw. |
| 2,55 × In | **1–60 s** (In ≤ 32 A), 1–120 s (In > 32 A) | jw. | jw. |
| Zdolność zwarciowa | **4500 / 6000 / 10 000 A** | oznaczenie w prostokącie | jw. |

## [07.04 Charakterystyki B, C i D](07.04-charakterystyki-b-c-i-d.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| B — wyłączenie natychmiastowe | **3–5 × In** (< 0,1 s przy 5 × In) | — | PN-EN 60898-1 |
| C — wyłączenie natychmiastowe | **5–10 × In** | — | jw. |
| D — wyłączenie natychmiastowe | **10–20 × In** | — | jw. |
| Część termiczna (wszystkie) | 1,13 × In — nie wyłącza w 1 h; 1,45 × In — wyłącza < 1 h | 30 °C | jw. |
| $Z_s$ max dla B16 / C16 | **2,88 Ω / 1,44 Ω** | TN, 230 V, 0,4 s | PN-HD 60364-4-41 ([04.04](../04-prad-a-czlowiek/04.04-maksymalne-czasy-samoczynnego-wylaczenia.md)) |

## [07.05 Zdolność zwarciowa: 6 kA, 10 kA](07.05-zdolnosc-zwarciowa-6-ka-10-ka.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Typowe Icn wyłączników domowych | **4,5 / 6 / 10 kA** | — | PN-EN 60898-1 |
| Warunek doboru | $I_{cn} \ge I_k$ w miejscu montażu | lub ochrona wsteczna | PN-HD 60364-4-43, 434.5.1 |
| Spodziewany prąd zwarciowy | $I_k = U_0 / Z_s$ | z pomiaru $Z_s$ | — |
| Zdolność wyłączania wkładek | **50 kA** (D/D0), **120 kA** (NH) | typowo | dane producentów |
| Najlepsza klasa ograniczania energii | **3** | — | PN-EN 60898-1 |

## [07.06 Koordynacja zabezpieczenia z przewodem](07.06-koordynacja-zabezpieczenia-z-przewodem.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Warunek przeciążeniowy 1 | $I_B \le I_n \le I_z$ | zawsze | PN-HD 60364-4-43, 433.1 |
| Warunek przeciążeniowy 2 | $I_2 \le 1{,}45 \cdot I_z$ | zawsze | jw. |
| $I_2$ wyłącznika nadprądowego | **1,45 × In** | PN-EN 60898-1 | jw. |
| $I_2$ wkładki gG | **1,6 × In** (In ≥ 16 A) | → $I_n \le 0{,}9 \cdot I_z$ | PN-EN 60269-1 |
| Warunek zwarciowy | $t \le (k S / I)^2$ | t ≤ 5 s | PN-HD 60364-4-43, 434.5.2 |
| k dla żył | Cu/PVC **115**, Cu/XLPE **143**, Al/PVC **76** | przekroje ≤ 300 mm² | jw., tab. 43A |
| Typowo | **1,5 mm² — B10**, **2,5 mm² — B16** | mieszkania, bez niekorzystnych warunków | praktyka |

## [07.07 Selektywność zabezpieczeń](07.07-selektywnosc-zabezpieczen.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Selektywność wkładek gG | stosunek In **≥ 1,6** | wkładki tej samej klasy | PN-EN 60269-1 |
| Wyłącznik nadprądowy za wkładką | selektywność do prądu granicznego $I_s$ | wg tabel producenta | dane producentów |
| Wyłącznik nadprądowy za wyłącznikiem nadprądowym | zwykle **brak** selektywności przy zwarciach | — | jw. |
| Typowe zabezpieczenie przedlicznikowe w mieszkaniu | **gG 20–25 A** | zależnie od mocy przyłączeniowej | warunki przyłączenia OSD |
