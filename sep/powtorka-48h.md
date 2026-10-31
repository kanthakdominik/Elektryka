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
- **RCD 30 mA:** gniazda ≤ 32 A; zadziałanie ≤ 300 ms przy 30 mA, ≤ 40 ms przy 150 mA.

_(uzupełniane z modułów 08 i 12)_

## Zabezpieczenia i przewody

- **Prąd zwarcia:** $I_{zw} = U_0 / Z_s$. **Przeciążenie** → człon termiczny (minuty), **zwarcie** → człon elektromagnetyczny (< 0,1 s). ([01.07](../modules/01-prad-napiecie-opor/01.07-przeciazenie-a-zwarcie-dwie-rozne-awarie.md))
- **Prądy umowne:** 1,13 $I_n$ — nie zadziała przez 1 h; 1,45 $I_n$ — zadziała w < 1 h. **Natychmiast:** B 3–5 $I_n$, C 5–10 $I_n$, D 10–20 $I_n$.
- **Opór przewodu:** $R = \rho l / S$; Cu 0,0175, Al 0,0286 Ω·mm²/m. ([01.03](../modules/01-prad-napiecie-opor/01.03-opor-i-prawo-ohma.md))
- **Spadek napięcia:** ≤ 3 % od licznika do odbiornika (N SEP-E-002). ([01.06](../modules/01-prad-napiecie-opor/01.06-grzanie-przewodow-i-spadek-napiecia.md))
- **Napięcie sieci:** 230/400 V (400 = 230·√3), ±10 % (207–253 V), 50 Hz ±1 %, szczyt 230 V ≈ 325 V. Barwy: L1 brązowy, L2 czarny, L3 szary, N niebieski, PE żółto-zielony. ([01.02](../modules/01-prad-napiecie-opor/01.02-napiecie-roznica-cisnien-miedzy-dwoma-punktami.md))

_(uzupełniane z modułów 05, 07, 16)_

## Pomiary

_(do uzupełnienia z modułu 23)_

## Przepisy w jednym akapicie

Świadectwo kwalifikacyjne wymagane od osób zajmujących się eksploatacją (art. 54 Prawa energetycznego), **ważne 5 lat** (ust. 1aa). Eksploatacja = obsługa, konserwacja, remont/naprawa, montaż/demontaż, czynności kontrolno-pomiarowe (§ 4 rozporządzenia z 2022 r.). **Bez świadectwa** tylko obsługa urządzeń ≤ 1 kV i ≤ 20 kW z instrukcją obsługi oraz cieplnych ≤ 50 kW (§ 5). **Kontrola instalacji w budynku co najmniej raz na 5 lat** (art. 62 ust. 1 pkt 2 Prawa budowlanego), wykonuje ją osoba z kwalifikacjami **dozoru** (art. 62 ust. 5). ([00.03](../modules/00-bezpieczenstwo-najpierw/00.03-co-wolno-zrobic-samemu-a-co-wymaga-uprawnien-i.md))

_(uzupełniane z modułu 32)_
