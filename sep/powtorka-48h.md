# Powtórka 48 h przed egzaminem

Jedna strona do przeczytania dzień–dwa przed egzaminem: liczby, czasy i wartości graniczne, o które komisja pyta najczęściej. Każda pozycja linkuje do tematu, w którym jest wyjaśniona. Wypełniana na podstawie ściąg z modułów.

[← sep/](README.md)

## Plan na ostatnie dwa dni

| Kiedy | Co |
|-------|----|
| Dzień −2 | Ściągi modułów 04, 07, 08, 11, 12, 13. Pytania z [pytania.md](pytania.md) z tych działów — na głos |
| Dzień −1, rano | Ściągi 23, 24, 28–31. Pozostałe pytania |
| Dzień −1, wieczór | Tylko ta strona. Bez nowego materiału |
| Dzień egzaminu | Dokument tożsamości ze zdjęciem; ta strona w drodze |

## Bezpieczeństwo — bez zawahania

- **Pięć zasad:** wyłącz → zabezpiecz przed załączeniem → sprawdź brak napięcia → uziem i zewrzyj → osłoń sąsiednie części czynne. Po pracy odwrotnie. ([00.01](../modules/00-bezpieczenstwo-najpierw/00.01-piec-zasad-bezpiecznej-pracy-przy-urzadzeniach.md))
- **Brak napięcia:** wskaźnik dwubiegunowy (PN-EN 61243-3), **sprawdź → zmierz → sprawdź**, wszystkie pary: 3 jednofazowo, 10 trójfazowo. Neonówka się nie nadaje. ([00.02](../modules/00-bezpieczenstwo-najpierw/00.02-sprawdzanie-braku-napiecia-probnik-dwubiegunowy.md))
- **Dym z rozdzielnicy:** ludzie z dala, wyłącz zasilanie przed rozdzielnicą, 112, gaśnica do urządzeń elektrycznych, nie woda. ([00.04](../modules/00-bezpieczenstwo-najpierw/00.04-czerwone-flagi-kiedy-przerwac-prace-i-wezwac.md))
- **Numery:** 112 — ratunkowy, 991 — pogotowie energetyczne.

_(uzupełniane z modułów 28, 30, 31)_

## Wartości graniczne ochrony przeciwporażeniowej

- **Progi prądu AC 50 Hz:** odczuwanie 0,5 mA · samouwolnienie ok. 10 mA · migotanie komór od ok. 40–50 mA (> 1 s) lub ok. 500 mA (10 ms). ([04.01](../modules/04-prad-a-czlowiek/04.01-jak-prad-dziala-na-organizm-progi-odczuwania.md))
- **Skutki zależą od:** prądu, czasu, drogi (F: lewa ręka–stopy 1,0; ręka–ręka 0,4; klatka–lewa ręka 1,5; stopa–stopa 0,04), częstotliwości, warunków. ([04.02](../modules/04-prad-a-czlowiek/04.02-droga-przeplywu-czas-i-czestotliwosc.md))
- **$U_L$:** 50 V AC / 120 V DC — warunki normalne; 25 V AC / 60 V DC — zwiększone zagrożenie. Ucieczka ze strefy napięcia krokowego: drobne kroki, stopy razem. ([04.03](../modules/04-prad-a-czlowiek/04.03-napiecie-dotykowe-i-krokowe-napiecia.md))
- **Czasy wyłączenia (230 V):** TN 0,4 s, TT 0,2 s — obwody odbiorcze (gniazda ≤ 63 A, stałe ≤ 32 A); rozdzielcze TN 5 s, TT 1 s. **$Z_s \cdot I_a \le U_0$**; B16 → $Z_s$ ≤ 2,88 Ω, C16 → ≤ 1,44 Ω. ([04.04](../modules/04-prad-a-czlowiek/04.04-maksymalne-czasy-samoczynnego-wylaczenia.md))
- **RCD — zasada:** przekładnik sumujący porównuje prądy L i N; PE omija przekładnik. Nie chroni przed przeciążeniem, zwarciem ani dotykiem L–N; nie działa w TN-C. ([08.01](../modules/08-wylaczniki-roznicowopradowe/08.01-zasada-dzialania-wylacznika-roznicowopradowego.md))
- **RCD — liczby:** zadziała w zakresie 0,5–1 IΔn; ogólny ≤ 300 ms przy IΔn, ≤ 150 ms przy 2 IΔn, ≤ 40 ms przy 5 IΔn; typ S 130–500 ms. ([08.01](../modules/08-wylaczniki-roznicowopradowe/08.01-zasada-dzialania-wylacznika-roznicowopradowego.md))
- **RCD 30 mA obowiązkowo (PN-HD 60364-4-41:2017):** gniazda ≤ 32 A, urządzenia ruchome ≤ 32 A na zewnątrz, oświetlenie w mieszkaniach (411.3.4), łazienki. 300 mA — ochrona przeciwpożarowa. TT: $R_A \cdot I_{\Delta n} \le 50$ V. ([08.02](../modules/08-wylaczniki-roznicowopradowe/08.02-prad-roznicowy-znamionowy-30-ma-100-ma-300-ma.md))
- **Typy RCD:** AC — sinus; A — + pulsujący (DC do 6 mA), standard w domu; F — + mieszane częstotliwości (DC do 10 mA); B — + DC wygładzony (falowniki 3f, EV). ([08.03](../modules/08-wylaczniki-roznicowopradowe/08.03-typy-ac-a-f-i-b-ktory-do-czego.md))
- **TEST** sprawdza mechanizm, nie PE i nie czas — to robi miernik. Selektywność RCD: wyżej typ S i IΔn ≥ 3×. Suma upływu za RCD ≤ 0,3 IΔn. ([08.05](../modules/08-wylaczniki-roznicowopradowe/08.05-przycisk-test-i-okresowe-sprawdzanie.md), [08.07](../modules/08-wylaczniki-roznicowopradowe/08.07-podzial-obwodow-miedzy-wylaczniki.md))
- **Klasy ochronności:** 0 — tylko izolacja podstawowa; I — + PE; II — izolacja podwójna/wzmocniona, bez PE (kwadrat w kwadracie); III — SELV/PELV ≤ 50 V AC. ([06.06](../modules/06-osprzet-instalacyjny/06.06-klasy-ochronnosci-urzadzen-0-i-ii-iii.md))

- **Układy sieci:** 1. litera — źródło (T uziemione, I izolowane), 2. — obudowy (T własny uziom, N przez przewód do punktu neutralnego), S/C — osobne N i PE / wspólny PEN. W Polsce zwykle TN-C-S. ([11.01](../modules/11-uklady-sieci/11.01-co-oznaczaja-litery-w-nazwie-ukladu-sieci.md))
- **PEN:** ≥ 10 mm² Cu / 16 mm² Al, nigdy przez łącznik ani RCD; rozdział: PEN → szyna PE → mostek → N, punkt podziału uziemiony, dalej N i PE nigdy razem. Przerwa PEN przed podziałem → do ~400 V na fazie. ([11.04](../modules/11-uklady-sieci/11.04-uklad-tn-c-s-i-punkt-rozdzialu-pen.md))
- **TT:** $R_A \cdot I_{\Delta n} \le 50$ V, czas 0,2 s (odbiorcze) / 1 s, RCD konieczny, N odłączany, bez mostka N–PE. **IT:** pierwsze zwarcie sygnalizowane (IMD), drugie wyłączane. ([11.05](../modules/11-uklady-sieci/11.05-uklad-tt.md), [11.06](../modules/11-uklady-sieci/11.06-uklad-it.md))
- **Trzy poziomy ochrony:** podstawowa (izolacja, obudowy IP2X, góra IP4X; przeszkody i poza zasięgiem — tylko dla wykwalifikowanych), przy uszkodzeniu (PE + połączenia wyrównawcze + samoczynne wyłączenie; izolacja podwójna; separacja), uzupełniająca (RCD ≤ 30 mA, połączenia miejscowe dodatkowe). ([12.01](../modules/12-ochrona-przeciwporazeniowa/12.01-ochrona-podstawowa-izolacja-obudowy-przegrody.md), [12.02](../modules/12-ochrona-przeciwporazeniowa/12.02-ochrona-przy-uszkodzeniu-samoczynne-wylaczenie.md))
- **Ocena pomiaru pętli z zapasem:** $Z_s \le \tfrac{2}{3} U_0/I_a$ — B16 → 1,92 Ω, C16 → 0,96 Ω. ([12.03](../modules/12-ochrona-przeciwporazeniowa/12.03-warunek-skutecznosci-samoczynnego-wylaczenia.md))
- **SELV/PELV:** ≤ 50 V AC / 120 V DC; SELV nieuziemione, PELV może być uziemione, FELV nie chroni; bez ochrony podstawowej do 25 V AC (sucho) / 12 V AC. **Separacja:** transformator separacyjny, 1 odbiornik, bez uziemienia, ≤ 500 V. ([12.04](../modules/12-ochrona-przeciwporazeniowa/12.04-izolacja-podwojna-separacja-elektryczna-selv-i.md))
- **Dawne nazwy:** dotyk bezpośredni → ochrona podstawowa; dotyk pośredni / ochrona dodatkowa → przy uszkodzeniu; zerowanie → wyłączenie w TN; uziemienie ochronne → w TT; sieć ochronna → IT. ([12.06](../modules/12-ochrona-przeciwporazeniowa/12.06-dawne-nazwy-zerowanie-uziemienie-ochronne.md))

## Zabezpieczenia i przewody

- **Prąd zwarcia:** $I_{zw} = U_0 / Z_s$. **Przeciążenie** → człon termiczny (minuty), **zwarcie** → człon elektromagnetyczny (< 0,1 s). ([01.07](../modules/01-prad-napiecie-opor/01.07-przeciazenie-a-zwarcie-dwie-rozne-awarie.md))
- **Prądy umowne:** 1,13 $I_n$ — nie zadziała przez 1 h; 1,45 $I_n$ — zadziała w < 1 h. **Natychmiast:** B 3–5 $I_n$, C 5–10 $I_n$, D 10–20 $I_n$.
- **Opór przewodu:** $R = \rho l / S$; Cu 0,0175, Al 0,0286 Ω·mm²/m. ([01.03](../modules/01-prad-napiecie-opor/01.03-opor-i-prawo-ohma.md))
- **Spadek napięcia:** ≤ 3 % od licznika do odbiornika (N SEP-E-002). ([01.06](../modules/01-prad-napiecie-opor/01.06-grzanie-przewodow-i-spadek-napiecia.md))
- **Napięcie sieci:** 230/400 V (400 = 230·√3), ±10 % (207–253 V), 50 Hz ±1 %, szczyt 230 V ≈ 325 V. Barwy: L1 brązowy, L2 czarny, L3 szary, N niebieski, PE żółto-zielony. ([01.02](../modules/01-prad-napiecie-opor/01.02-napiecie-roznica-cisnien-miedzy-dwoma-punktami.md))

- **Warunki doboru:** $I_B \le I_n \le I_z$ oraz $I_2 \le 1{,}45 \cdot I_z$; wyłącznik $I_2$ = 1,45 $I_n$, wkładka gG $I_2$ = 1,6 $I_n$ → $I_n \le 0{,}9 I_z$. Zwarcie: $t \le (kS/I)^2$, Cu/PVC k = 115. ([07.06](../modules/07-zabezpieczenia-nadpradowe/07.06-koordynacja-zabezpieczenia-z-przewodem.md))
- **Obciążalność Cu 2,5 mm² (PVC, 2 żyły, 30 °C):** A1 19,5 · B1 24 · C 27 · E 30 A; 1,5 mm²: 14,5 / 17,5 / 19,5 / 22 A. Grupowanie: 2 obwody × 0,80, 3 × 0,70. Minimum Cu 1,5 mm². ([05.04](../modules/05-przewody-i-kable/05.04-przekroj-i-obciazalnosc-pradowa.md))
- **Oznaczenia:** YDY — drut, izolacja i powłoka PVC, 450/750 V; YKY — kabel 0,6/1 kV; H07V-K — linka 450/750 V; H05VV-F — giętki 300/500 V. Kabel w ziemi nn: 0,7 m, piasek, folia niebieska. ([05.02](../modules/05-przewody-i-kable/05.02-oznaczenia-literowe-ydy-ydyp-yly-yky-h07v-k.md), [05.06](../modules/05-przewody-i-kable/05.06-przewody-bezhalogenowe-i-kable-ziemne.md))
- **Wkładki:** gG — pełnozakresowe do przewodów, aM — zwarciowe do silników; selektywność gG przy stosunku ≥ 1,6; nie naprawiać, nie zwiększać. ([07.02](../modules/07-zabezpieczenia-nadpradowe/07.02-bezpieczniki-topikowe-wkladki-gg-gwintowe-i.md))
- **Zdolność zwarciowa:** $I_{cn}$ (6000 w prostokącie) ≥ spodziewany prąd zwarcia $U_0/Z_s$ albo ochrona wsteczna; klasa ograniczania energii 3. ([07.05](../modules/07-zabezpieczenia-nadpradowe/07.05-zdolnosc-zwarciowa-6-ka-10-ka.md))
- **IP:** 1. cyfra — ciała stałe (2 palec, 4 drut, 6 pyłoszczelna), 2. cyfra — woda (4 bryzgi, 7 zanurzenie); łazienka strefy 1–2 IPX4, strefa 0 IPX7. ([06.05](../modules/06-osprzet-instalacyjny/06.05-stopnie-ochrony-ip.md))
- **Osprzęt:** łącznik zawsze w fazie L; gniazdo — PE na bolec, L lewy otwór (bolec u góry); połączenia w dostępnych puszkach, złączkami, nie skrętką. ([06.01](../modules/06-osprzet-instalacyjny/06.01-gniazda-wtyczkowe-jednofazowe-z-bolcem.md), [06.02](../modules/06-osprzet-instalacyjny/06.02-laczniki-jednobiegunowy-dwubiegunowy.md), [06.04](../modules/06-osprzet-instalacyjny/06.04-zlaczki-i-laczenie-przewodow-dlaczego-nie.md))

- **Aparatura:** odłącznik — przerwa izolacyjna bez obciążenia; rozłącznik — prąd roboczy; wyłącznik — także zwarcia. Stycznik trzyma, dopóki cewka zasilona; bistabilny zmienia stan po impulsie. Zgaszona kontrolka ≠ brak napięcia. AFDD wykrywa łuk szeregowy, którego nie widzi MCB ani RCD. Moc z licznika: $P = 3600 n/(C t)$. ([10.01](../modules/10-aparatura-modulowa/10.01-rozlacznik-izolacyjny-wylacznik-glowny.md), [10.05](../modules/10-aparatura-modulowa/10.05-detektory-iskrzenia-afdd.md), [10.06](../modules/10-aparatura-modulowa/10.06-podliczniki-energii.md))

_(uzupełniane z modułu 16)_

## Przepięcia i ochrona odgromowa

- **Źródła:** uderzenie w budynek, w linię, w pobliżu (indukcja), przełączenia. Udary: **10/350 μs** — piorun (typ 1, $I_{imp}$), **8/20 μs** — indukowane (typ 2, $I_n$). ([09.01](../modules/09-ochrona-przeciwprzepieciowa/09.01-skad-biora-sie-przepiecia.md))
- **Kategorie (230/400 V):** IV 6 kV · III 4 kV · II 2,5 kV · I 1,5 kV. Ochrona wymagana przy zagrożeniu życia, usługach publicznych, działalności, wielu osobach; poza tym ocena ryzyka — bez niej ochrona obowiązkowa. ([09.02](../modules/09-ochrona-przeciwprzepieciowa/09.02-kategorie-wytrzymalosci-udarowej-iiv.md))
- **SPD:** typ 1 przy instalacji odgromowej (≥ 12,5 kA/biegun), typ 2 w rozdzielnicy (In ≥ 5 kA), typ 3 przy odbiorniku; $U_C$ 275 V; czerwony wskaźnik = wymiana. ([09.03](../modules/09-ochrona-przeciwprzepieciowa/09.03-ograniczniki-przepiec-typu-1-2-i-3.md))
- **Montaż:** a + b ≤ 0,5 m (≈ 1 kV/m), przed RCD, 3+1 w TT i przed RCD, PE ≥ 6 mm² (T2) / 16 mm² (T1), ochrona do ok. 10 m. ([09.04](../modules/09-ochrona-przeciwprzepieciowa/09.04-montaz-ogranicznika-dlugosc-polaczen-i.md))
- **Instalacja odgromowa:** zwody, przewody odprowadzające, złącza kontrolne, uziom; klasy I–IV; kontrola co 5 lat (art. 62 Prawa budowlanego). ([09.05](../modules/09-ochrona-przeciwprzepieciowa/09.05-ochrona-odgromowa-budynku-podstawy.md))

## Pomiary

_(do uzupełnienia z modułu 23)_

## Przepisy w jednym akapicie

Świadectwo kwalifikacyjne wymagane od osób zajmujących się eksploatacją (art. 54 Prawa energetycznego), **ważne 5 lat** (ust. 1aa). Eksploatacja = obsługa, konserwacja, remont/naprawa, montaż/demontaż, czynności kontrolno-pomiarowe (§ 4 rozporządzenia z 2022 r.). **Bez świadectwa** tylko obsługa urządzeń ≤ 1 kV i ≤ 20 kW z instrukcją obsługi oraz cieplnych ≤ 50 kW (§ 5). **Kontrola instalacji w budynku co najmniej raz na 5 lat** (art. 62 ust. 1 pkt 2 Prawa budowlanego), wykonuje ją osoba z kwalifikacjami **dozoru** (art. 62 ust. 5). ([00.03](../modules/00-bezpieczenstwo-najpierw/00.03-co-wolno-zrobic-samemu-a-co-wymaga-uprawnien-i.md))

_(uzupełniane z modułu 32)_
