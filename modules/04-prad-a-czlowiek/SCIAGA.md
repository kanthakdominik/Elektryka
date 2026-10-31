# Ściąga — 04 — Prąd a człowiek

> Zebrane sekcje „Liczby do zapamiętania” ze wszystkich tematów modułu. [Spis modułu](README.md)

## [04.01 Jak prąd działa na organizm — progi odczuwania, samouwolnienia i migotania komór](04.01-jak-prad-dziala-na-organizm-progi-odczuwania.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Próg odczuwania AC | **0,5 mA** | 50 Hz, niezależnie od czasu | IEC TS 60479-1 |
| Próg odczuwania DC | ok. **2 mA** | prąd stały | jw. |
| Próg samouwolnienia AC | ok. **10 mA** (u części osób ok. 5 mA) | 50 Hz, dorośli | jw. |
| Migotanie komór — długi przepływ | od ok. **40–50 mA** | czas powyżej ok. 1–3 s | jw., krzywa c₁ |
| Migotanie komór — krótki przepływ | ok. **400–500 mA** | 10–100 ms | jw. |
| Różnicówka ochrony uzupełniającej | **30 mA** | obwody gniazd, łazienki itd. | PN-HD 60364-4-41 (moduł 08) |
| Czas zadziałania RCD 30 mA | ≤ **300 ms** przy 30 mA, ≤ **40 ms** przy 150 mA | wyłączniki ogólnego typu | PN-EN 61008-1 (moduł 08) |

## [04.02 Droga przepływu, czas i częstotliwość](04.02-droga-przeplywu-czas-i-czestotliwosc.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| F: lewa ręka → stopy | **1,0** (droga odniesienia) | — | IEC TS 60479-1, tab. 12 |
| F: obie ręce → stopy | **1,0** | — | jw. |
| F: prawa ręka → stopy | **0,8** | — | jw. |
| F: ręka → ręka | **0,4** | — | jw. |
| F: klatka piersiowa → lewa ręka | **1,5** | — | jw. |
| F: stopa → stopa | **0,04** | — | jw. |
| Prąd równoważny | $I_{ref} = F \cdot I_h$ | porównanie z drogą lewa ręka → stopy | jw. |
| Impedancja ciała przy 230 V | rząd **1000–2000 Ω** (sucha skóra, duży styk); mniej przy wilgoci | ręka → ręka | jw. |
| Impedancja ręka → stopy | ok. **70–90 %** wartości ręka → ręka | — | jw. |
| Najgroźniejsze częstotliwości | **15–100 Hz** | — | jw. |

## [04.03 Napięcie dotykowe i krokowe, napięcia dopuszczalne długotrwale](04.03-napiecie-dotykowe-i-krokowe-napiecia.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| $U_L$ — warunki normalne | **50 V AC**, **120 V DC** | instalacje w budynkach | PN-HD 60364-4-41; dawne przepisy ochrony przeciwporażeniowej |
| $U_L$ — warunki zwiększonego zagrożenia | **25 V AC**, **60 V DC** | wilgoć, przewodzące otoczenie, np. obiekty rolnicze | PN-HD 60364-7-705 i in. |
| Granica SELV/PELV | **50 V AC**, **120 V DC** (bez tętnień) | obwody bardzo niskiego napięcia | PN-HD 60364-4-41 (moduł 12) |
| Krok (do obliczeń napięcia krokowego) | **1 m** | — | konwencja |
| Ucieczka ze strefy | drobne kroki, stopy złączone, lub skoki obunóż | zerwany przewód, uziom w czasie zwarcia | dobra praktyka |

## [04.04 Maksymalne czasy samoczynnego wyłączenia](04.04-maksymalne-czasy-samoczynnego-wylaczenia.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| TN, 230 V, obwody odbiorcze | **0,4 s** | gniazda ≤ 63 A, odbiorniki stałe ≤ 32 A | PN-HD 60364-4-41, tabl. 41.1 |
| TT, 230 V, obwody odbiorcze | **0,2 s** | jw. | jw. |
| TN, obwody rozdzielcze i pozostałe | **5 s** | — | PN-HD 60364-4-41, 411.3.2.3 |
| TT, obwody rozdzielcze i pozostałe | **1 s** | — | PN-HD 60364-4-41, 411.3.2.4 |
| Warunek skuteczności (TN) | $Z_s \cdot I_a \le U_0$ | — | PN-HD 60364-4-41, 411.4.4 (moduł 12) |
| $I_a$ dla wyłączników B / C / D | **5 / 10 / 20 × $I_n$** (zadziałanie < 0,1 s) | wyłączniki wg PN-EN 60898-1 | moduł 07 |
| RCD 30 mA w obwodach gniazd | wymagany dla gniazd ≤ 32 A dla laików | ochrona uzupełniająca | PN-HD 60364-4-41, 411.3.3 |

## [04.05 Łuk elektryczny i oparzenia](04.05-luk-elektryczny-i-oparzenia.md)

| Wielkość | Wartość | Kiedy obowiązuje | Źródło |
|----------|---------|------------------|--------|
| Temperatura plazmy łuku | **kilka–kilkanaście tysięcy °C** | łuk w powietrzu | fizyka łuku |
| Prąd zwarcia w gnieździe | **setki A** | koniec obwodu odbiorczego | [01.07](../01-prad-napiecie-opor/01.07-przeciazenie-a-zwarcie-dwie-rozne-awarie.md) |
| Prąd zwarcia przy złączu / rozdzielnicy głównej | **kilka–kilkanaście kA** | blisko transformatora | zdolność zwarciowa aparatów 6–10 kA (moduł 07) |
| Konsultacja lekarska | **po każdym porażeniu** napięciem sieciowym | — | moduł 31 |
