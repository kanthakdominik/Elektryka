# Lista: odbiór instalacji od wykonawcy

> Po budowie lub remoncie, **przed** ostatnią płatnością. 🏠 sprawdzisz sam, 🔧 sprawdza lub pokazuje wykonawca.
> Pełne tło: [23.01 — oględziny](../modules/23-pomiary-odbiorcze-i-okresowe/23.01-ogledziny-instalacji.md), [23.08 — protokół](../modules/23-pomiary-odbiorcze-i-okresowe/23.08-protokol-z-pomiarow-i-terminy-badan-okresowych.md).

**Obiekt:** ______________________________ **Wykonawca:** ______________________ **Data:** __________

## Dokumenty (🏠)

- [ ] **Protokół ze sprawdzenia odbiorczego** — każdy obwód z wynikami: ciągłość PE, izolacja, $Z_s$, RCD; przyrządy z datą wzorcowania; podpis i **numer świadectwa kwalifikacyjnego** ([wzór](../wzory/protokol-pomiarow.md)).
- [ ] **Schemat rozdzielnicy** (jednokreskowy) zgodny z tym, co jest w środku ([15.02](../modules/15-rozdzielnica-mieszkaniowa/15.02-schemat-jednokreskowy-jak-czytac-i-jak-rysowac.md)).
- [ ] **Opis obwodów** na maskownicy i tabela na drzwiczkach ([wzór](../wzory/opis-rozdzielnicy.md)).
- [ ] **Zdjęcia tras przewodów** w ścianach przed tynkowaniem (z miarką) — oszczędzą przewiercenie przewodu.
- [ ] Dokumentacja i gwarancje aparatów (RCD typu A/F/B, SPD, AFDD), instrukcje urządzeń (PV, pompa ciepła, wallbox).
- [ ] Oświadczenie wykonawcy, że instalacja jest wykonana zgodnie z projektem i przepisami (przy budowie — do odbioru budynku).

## Rozdzielnica (🏠 oględziny bez zdejmowania osłon)

- [ ] Wyłącznik główny opisany i łatwo dostępny ([10.01](../modules/10-aparatura-modulowa/10.01-rozlacznik-izolacyjny-wylacznik-glowny.md)).
- [ ] RCD **30 mA** chroni gniazda, łazienkę, oświetlenie w mieszkaniu i obwody zewnętrzne ([08.02](../modules/08-wylaczniki-roznicowopradowe/08.02-prad-roznicowy-znamionowy-30-ma-100-ma-300-ma.md)); typ co najmniej **A** ([08.03](../modules/08-wylaczniki-roznicowopradowe/08.03-typy-ac-a-f-i-b-ktory-do-czego.md)).
- [ ] Obwody rozdzielone między kilka RCD — awaria jednego nie gasi całego domu ([08.07](../modules/08-wylaczniki-roznicowopradowe/08.07-podzial-obwodow-miedzy-wylaczniki.md)).
- [ ] Ogranicznik przepięć (SPD) zamontowany i opisany ([09.03](../modules/09-ochrona-przeciwprzepieciowa/09.03-ograniczniki-przepiec-typu-1-2-i-3.md)).
- [ ] Zapas miejsca na szynie (ok. 20 %) na przyszłe obwody.
- [ ] 🔧 Po zdjęciu osłony: porządek przewodów, tulejki, osobne listwy N dla każdego RCD, PE na szynie PE, brak „mostków” N–PE poza punktem rozdziału PEN ([15.07](../modules/15-rozdzielnica-mieszkaniowa/15.07-montaz-i-porzadek-przewodow-w-rozdzielnicy.md), [11.04](../modules/11-uklady-sieci/11.04-uklad-tn-c-s-i-punkt-rozdzialu-pen.md)).
- [ ] 🔧 Przekroje zgodne z zabezpieczeniami (np. 2,5 mm² → B16, 1,5 mm² → B10) ([07.06](../modules/07-zabezpieczenia-nadpradowe/07.06-koordynacja-zabezpieczenia-z-przewodem.md)).

## Instalacja w pomieszczeniach (🏠)

- [ ] Każde gniazdo ma **bolec ochronny** i działa — sprawdź testerem gniazd (L, N, PE na swoich miejscach) ([06.01](../modules/06-osprzet-instalacyjny/06.01-gniazda-wtyczkowe-jednofazowe-z-bolcem.md)).
- [ ] Każdy łącznik włącza właściwą lampę; łącznik przerywa fazę (oprawa bez napięcia po wyłączeniu).
- [ ] Osobne obwody dla płyty, piekarnika, pralki, zmywarki ([16.06](../modules/16-planowanie-obwodow/16.06-obwody-wydzielone-plyta-piekarnik-pralka.md)).
- [ ] Łazienka: strefy 0–2 zachowane, osprzęt IPX4, brak gniazd w strefie 1 ([17.01](../modules/17-pomieszczenia-szczegolne/17.01-lazienka-strefy-0-1-i-2.md)).
- [ ] Połączenia wyrównawcze: główne (rury, zbrojenie) i miejscowe w łazience, jeśli są wymagane ([13.04](../modules/13-uziemienia-i-wyrownanie/13.04-polaczenia-wyrownawcze-ochronne-glowne.md), [13.05](../modules/13-uziemienia-i-wyrownanie/13.05-polaczenia-wyrownawcze-miejscowe.md)).
- [ ] Gniazda zewnętrzne co najmniej IP44, z RCD 30 mA ([17.04](../modules/17-pomieszczenia-szczegolne/17.04-instalacje-zewnetrzne-i-ogrod.md)).
- [ ] Puszki rozgałęźne **dostępne** (nie pod płytkami) ([06.03](../modules/06-osprzet-instalacyjny/06.03-puszki-instalacyjne-i-rozgalezne.md)).
- [ ] Przewody w strefach instalacyjnych — poziomo i pionowo ([16.04](../modules/16-planowanie-obwodow/16.04-strefy-instalacyjne-i-trasy-przewodow.md)).

## Próby przy Tobie (🔧 pokazuje wykonawca)

- [ ] Przycisk **TEST** każdego RCD — wyłącza.
- [ ] Pomiar RCD miernikiem na jednym gnieździe: czas przy IΔn ≤ 300 ms (typ ogólny) ([23.05](../modules/23-pomiary-odbiorcze-i-okresowe/23.05-badanie-wylacznikow-roznicowopradowych.md)).
- [ ] Pomiar $Z_s$ na najdalszym gnieździe: wynik ≤ ⅔ wartości dopuszczalnej (B16: ≤ 1,92 Ω) ([23.04](../modules/23-pomiary-odbiorcze-i-okresowe/23.04-impedancja-petli-zwarcia.md)).
- [ ] Rezystancja izolacji obwodów: ≥ **1,0 MΩ** przy 500 V ([23.03](../modules/23-pomiary-odbiorcze-i-okresowe/23.03-rezystancja-izolacji.md)).
- [ ] Przy zasilaniu 3-fazowym: kolejność faz zgodna (gniazdo 400 V) ([23.07](../modules/23-pomiary-odbiorcze-i-okresowe/23.07-kolejnosc-faz.md)).
- [ ] Przy PV, magazynie, agregacie: ostrzeżenie o **wielu źródłach zasilania** na rozdzielnicy ([26.01](../modules/26-fotowoltaika-pompy-wallboxy/26.01-fotowoltaika-budowa-instalacji.md)).

## Wynik

- [ ] Wszystko OK — odbieram. 
- [ ] Usterki (lista, termin usunięcia): ________________________________________________

Podpis inwestora: ______________________ Podpis wykonawcy: ______________________
