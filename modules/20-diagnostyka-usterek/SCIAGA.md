# Ściąga — 20 — Diagnostyka usterek

> Zebrane sekcje „Liczby do zapamiętania” ze wszystkich tematów modułu. [Spis modułu](README.md)

## [20.01 Metoda szukania usterek](20.01-metoda-szukania-usterek.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Kroki | bezpieczeństwo → wywiad → oględziny → zawężanie → pomiar i naprawa | każda usterka | praktyka |
| Połowienie | **n** gniazd → ok. **log₂ n** sprawdzeń (8 gniazd → 3) | łańcuch gniazd | — |
| Napięcie w gnieździe | **230 V ± 10 %** (207–253 V) | sieć nN | PN-EN 50160 |
| Ponowne załączenie po zadziałaniu | **raz**, po odłączeniu odbiorników | wyłącznik nadprądowy, RCD | [07.01](../07-zabezpieczenia-nadpradowe/07.01-przeciazenie-i-zwarcie-z-punktu-widzenia.md) |

## [20.02 Nie działa gniazdo albo cały obwód](20.02-nie-dziala-gniazdo-albo-caly-obwod.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| L–N 0, L–PE 0 | **brak fazy** | martwe gniazdo | — |
| L–N 0, L–PE 230 V | **przerwa N** | jw. | — |
| L–N 230, L–PE 0 | **przerwa PE** — groźne | jw. | — |
| Połowienie | 6 gniazd → **2–3** sprawdzenia | — | — |

## [20.03 Wybija wyłącznik różnicowoprądowy](20.03-wybija-wylacznik-roznicowopradowy.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Rezystancja izolacji | ≥ **1 MΩ** przy **500 V DC** | obwody do 500 V | PN-HD 60364-6, tab. 6.1 |
| Upływ za RCD 30 mA | ≤ **0,3 IΔn** ≈ **9 mA** | zalecenie | PN-HD 60364-5-53 |
| Upływ urządzenia z filtrem | **0,5–3 mA** | komputery, RTV, AGD | [08.06](../08-wylaczniki-roznicowopradowe/08.06-dlaczego-roznicowka-wybija-przyczyny-i-szukanie.md) |
| RCD zadziała | między **0,5 IΔn** a **IΔn** (15–30 mA) | RCD 30 mA | PN-EN 61008-1 |

## [20.04 Wybija wyłącznik nadprądowy](20.04-wybija-wylacznik-nadpradowy.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Nie zadziała przez 1 h | **1,13 In** | wyłączniki nadprądowe | PN-EN 60898-1 |
| Zadziała w < 1 h | **1,45 In** | jw. | jw. |
| Natychmiast | B **3–5 In**, C **5–10 In**, D **10–20 In** | jw. | jw. |
| Moc na B16 | ok. **3,7 kW** przy 230 V | cos φ = 1 | $P = U \cdot I$ |
| Ponowne załączenie | **raz**, po odłączeniu odbiorników | — | [07.01](../07-zabezpieczenia-nadpradowe/07.01-przeciazenie-i-zwarcie-z-punktu-widzenia.md) |

## [20.05 Przerwa w przewodzie neutralnym](20.05-przerwa-w-przewodzie-neutralnym.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Napięcie między fazami | **400 V** | sieć 230/400 V | — |
| Przykład 100 W + 1000 W | ok. **364 V / 36 V** | przerwa N, odbiorniki na różnych fazach | obliczenie |
| Dopuszczalne napięcie sieci | **230 V ± 10 %** | normalna praca | PN-EN 50160 |
| Pierwsza czynność | **wyłączyć rozłącznik główny** | podejrzenie przerwy N | — |

## [20.06 Grzejące się zaciski i zapach spalenizny](20.06-grzejace-sie-zaciski-i-zapach-spalenizny.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Moc na styku | $P = I^2 R$; 0,1 Ω przy 16 A → **26 W** | — | [06.04](../06-osprzet-instalacyjny/06.04-zlaczki-i-laczenie-przewodow-dlaczego-nie.md) |
| Temperatura pracy izolacji PVC | **70 °C** | praca ciągła | [05.01](../05-przewody-i-kable/05.01-budowa-przewodu-i-kabla-zyla-izolacja-powloka.md) |
| MCB / RCD | **nie wykrywają** luźnego połączenia | — | — |
| AFDD | wykrywa łuk szeregowy | — | [10.05](../10-aparatura-modulowa/10.05-detektory-iskrzenia-afdd.md) |

## [20.07 Migające i żarzące się LED](20.07-migajace-i-zarzace-sie-led.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Prąd wystarczający do żarzenia LED | rząd **miliamperów** i mniej | — | — |
| Częstotliwość migotania | **100 Hz** (dwa razy częstotliwość sieci) | tanie zasilacze | — |
| Łącznik musi przerywać | **L** | zawsze | [18.02](../18-oswietlenie/18.02-lacznik-jednobiegunowy-i-swiecznikowy-schematy.md) |
