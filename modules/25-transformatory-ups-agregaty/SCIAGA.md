# Ściąga — 25 — Transformatory, zasilacze, UPS i agregaty

> Zebrane sekcje „Liczby do zapamiętania” ze wszystkich tematów modułu. [Spis modułu](README.md)

## [25.01 Transformator separacyjny i bezpieczeństwa](25.01-transformator-separacyjny-i-bezpieczenstwa.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Górna granica ELV (SELV/PELV) | **50 V AC**, **120 V DC** (nietętniące) | obwody bardzo niskiego napięcia | PN-HD 60364-4-41 |
| Napięcie obwodu separowanego | **≤ 500 V** | separacja elektryczna | jw., 413 |
| Długość oprzewodowania separowanego | iloczyn **U · l ≤ 100 000 V·m**, maks. **500 m** | separacja, zalecenie normy | jw. |
| Odbiorniki na jedno uzwojenie | **1** (przy kilku — nieuziemione połączenia wyrównawcze) | separacja | jw. |
| Typowe napięcia trafo bezpieczeństwa | **12 V, 24 V** | lampy, dzwonki, sterowanie | katalogi |

## [25.02 Zasilacze impulsowe](25.02-zasilacze-impulsowe.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Napięcie kondensatora wejściowego | ok. **325 V DC** (z PFC ok. **400 V**) | zasilanie 230 V | √2 · 230 V |
| Częstotliwość kluczowania | **dziesiątki–setki kHz** | typowe zasilacze | katalogi |
| Sprawność | **85–95 %** | zasilacze dobrej jakości | katalogi |
| Suma prądów upływu za RCD | najlepiej **≤ 0,3 · IΔn** (≈ 9 mA dla 30 mA) | podział obwodów | PN-HD 60364-5-53 |
| Prąd upływu urządzenia klasy I | do ok. **3,5 mA** (typowo mniej) | sprzęt IT | PN-EN 62368-1 |

## [25.03 UPS — rodzaje i zastosowanie](25.03-ups-rodzaje-i-zastosowanie.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Czas przełączenia offline / line-interactive | ok. **2–10 ms** | zanik sieci | katalogi |
| Czas przełączenia online | **0 ms** | praca normalna → bateryjna | PN-EN 62040-3 (VFI) |
| Moc UPS | **VA i W** — np. 1000 VA / 600 W | dobór | katalogi |
| Żywotność akumulatora VRLA | ok. **3–5 lat** | temperatura ok. 20–25 °C | katalogi |
| Energia akumulatora | **U · Ah** — 12 V · 9 Ah = **108 Wh** | obliczenie orientacyjne | — |
| Realnie użyteczna energia | ok. **60–70 %** nominalnej | małe UPS-y, szybkie rozładowanie | szacunek |

## [25.04 Agregat prądotwórczy i przełącznik zasilania](25.04-agregat-pradotworczy-i-przelacznik-zasilania.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Zapas mocy agregatu | ok. **25 %** ponad sumę odbiorników | dobór | TAURON Dystrybucja |
| Rozruch silników | kilka razy **In** | pompy, sprężarki | 24.01 |
| Pozycje przełącznika | **I – 0 – II** (sieć – wyłączone – agregat) | podłączenie do domu | TAURON Dystrybucja |
| Miejsce przełącznika | **za licznikiem** | instalacja odbiorcy | jw. |
| Napięcie po stronie SN transformatora | ok. **15 kV** (typowo 15–20 kV) | sieć rozdzielcza | 14.01 |

## [25.05 Dlaczego nie zasila się domu przez gniazdo](25.05-dlaczego-nie-zasila-sie-domu-przez-gniazdo.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Przekładnia stacji SN/nn | ok. **15 000 / 400 V** | typowa sieć rozdzielcza | 14.01 |
| Napięcie po stronie SN przy 230 V „wepchniętym” od dołu | **tysiące V** (do ok. 15 kV) | zasilanie zwrotne | prawo transformacji |
| Obwód gniazdowy | **B16, 2,5 mm²** — nie do zasilania domu | typowa instalacja | 16.01 |
