# Lista: przed pomiarami okresowymi

> Dla elektryka (✏️) i zlecającego (🏠). Dobre przygotowanie skraca pomiary i zmniejsza liczbę wyłączeń.
> Tło: [23.08 — protokół i terminy](../modules/23-pomiary-odbiorcze-i-okresowe/23.08-protokol-z-pomiarow-i-terminy-badan-okresowych.md), kolejność badań: [23.01](../modules/23-pomiary-odbiorcze-i-okresowe/23.01-ogledziny-instalacji.md).

**Obiekt:** ______________________________ **Termin:** __________ **Zakres:** ☐ cała instalacja ☐ wybrane obwody ☐ uziemienie / odgromowa

## Zlecający (🏠)

- [ ] Poprzedni **protokół** i schemat rozdzielnicy — do wglądu ([wzór opisu](../wzory/opis-rozdzielnicy.md)).
- [ ] Dostęp do: rozdzielnic, złącza, piwnicy, strychu, **złączy kontrolnych** uziomu i instalacji odgromowej, klucze do szafek.
- [ ] Użytkownicy / lokatorzy **poinformowani** o przerwach w zasilaniu (data, godziny).
- [ ] Lista urządzeń, których **nie wolno** wyłączać bez przygotowania: serwerownia, lodówki z lekami, akwarium, pompy, alarm, windy; plan: UPS, przerwa w ustalonym oknie ([25.03](../modules/25-transformatory-ups-agregaty/25.03-ups-rodzaje-i-zastosowanie.md)).
- [ ] Komputery zapisane i wyłączone przed pomiarem izolacji danego obwodu.
- [ ] Informacja o zmianach od ostatnich pomiarów (nowe obwody, PV, wallbox, pompa ciepła).

## Elektryk (✏️)

- [ ] Świadectwo kwalifikacyjne **z zakresem kontrolno-pomiarowym**, ważne (5 lat) ([32.01](../modules/32-przepisy-i-normy/32.01-prawo-energetyczne-i-swiadectwa-kwalifikacyjne.md)); przy kontroli z art. 62 PB — także **D** ([32.03](../modules/32-przepisy-i-normy/32.03-prawo-budowlane-kontrole-okresowe.md)).
- [ ] Miernik (MPI) z **ważnym świadectwem wzorcowania**, naładowany, przewody i sondy bez uszkodzeń, kategoria CAT odpowiednia do miejsca ([22.01](../modules/22-przyrzady-pomiarowe/22.01-kategorie-pomiarowe-cat-iiiv-i-bezpieczenstwo.md), [22.05](../modules/22-przyrzady-pomiarowe/22.05-miernik-parametrow-instalacji-mpi-przeglad.md)).
- [ ] Wskaźnik napięcia dwubiegunowy, narzędzia 1000 V, kłódki i tablice ([przed pracą](przed-praca.md)).
- [ ] Sondy i przewody do pomiaru uziemienia (metoda techniczna) lub cęgi ([23.06](../modules/23-pomiary-odbiorcze-i-okresowe/23.06-rezystancja-uziemienia.md)).
- [ ] Szablon protokołu z listą obwodów przepisaną ze schematu ([wzór](../wzory/protokol-pomiarow.md)).
- [ ] Wartości dopuszczalne pod ręką: $Z_s$ dla B/C/D i $I_n$ ([12.03](../modules/12-ochrona-przeciwporazeniowa/12.03-warunek-skutecznosci-samoczynnego-wylaczenia.md), [kalkulator](../www/kalkulatory.html)), izolacja ≥ 1 MΩ, RCD ≤ 300 ms.
- [ ] Wiadomo, które **SPD** i urządzenia elektroniczne trzeba odłączyć przed pomiarem izolacji ([23.03](../modules/23-pomiary-odbiorcze-i-okresowe/23.03-rezystancja-izolacji.md)).
- [ ] Przy wielu źródłach (PV, magazyn, agregat) — jak je **odłączyć** i sprawdzić brak napięcia ([26.02](../modules/26-fotowoltaika-pompy-wallboxy/26.02-strona-dc-zagrozenia-i-zabezpieczenia.md)).
- [ ] W zakładzie pracy: polecenie (pisemne lub ustne) i dopuszczenie do pracy zgodnie z instrukcją ([28.01](../modules/28-bhp-przy-urzadzeniach/28.01-organizacja-pracy-i-polecenia.md)).

## Kolejność w dniu pomiarów

- [ ] **1.** Oględziny (bez napięcia, gdzie trzeba — z napięciem tylko patrzymy).
- [ ] **2.** Ciągłość PE i połączeń wyrównawczych ([23.02](../modules/23-pomiary-odbiorcze-i-okresowe/23.02-ciaglosc-przewodow-ochronnych-i-wyrownawczych.md)).
- [ ] **3.** Rezystancja izolacji ([23.03](../modules/23-pomiary-odbiorcze-i-okresowe/23.03-rezystancja-izolacji.md)).
- [ ] **4.** Impedancja pętli zwarcia ([23.04](../modules/23-pomiary-odbiorcze-i-okresowe/23.04-impedancja-petli-zwarcia.md)).
- [ ] **5.** RCD — czas i prąd zadziałania ([23.05](../modules/23-pomiary-odbiorcze-i-okresowe/23.05-badanie-wylacznikow-roznicowopradowych.md)).
- [ ] **6.** Uziemienie, kolejność faz, próby działania ([23.06](../modules/23-pomiary-odbiorcze-i-okresowe/23.06-rezystancja-uziemienia.md), [23.07](../modules/23-pomiary-odbiorcze-i-okresowe/23.07-kolejnosc-faz.md)).
- [ ] **7.** Przywrócenie zasilania, podłączenie odłączonych urządzeń i SPD, informacja dla użytkowników.
- [ ] **8.** Protokół z oceną i terminem następnego badania; wpis do książki obiektu (budynki).
