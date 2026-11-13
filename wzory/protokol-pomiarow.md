# Protokół nr ______ ze sprawdzenia instalacji elektrycznej nn

> Wzór na podstawie PN-HD 60364-6 i [23.08](../modules/23-pomiary-odbiorcze-i-okresowe/23.08-protokol-z-pomiarow-i-terminy-badan-okresowych.md). Wiersze *kursywą* to przykłady — usuń je przed wydrukiem.
> Wartości dopuszczalne: [12.03](../modules/12-ochrona-przeciwporazeniowa/12.03-warunek-skutecznosci-samoczynnego-wylaczenia.md), [23.03](../modules/23-pomiary-odbiorcze-i-okresowe/23.03-rezystancja-izolacji.md), [23.05](../modules/23-pomiary-odbiorcze-i-okresowe/23.05-badanie-wylacznikow-roznicowopradowych.md), [kalkulator $Z_s$](../www/kalkulatory.html).

## 1. Obiekt i zakres

| | |
|---|---|
| Zleceniodawca | |
| Adres obiektu | |
| Rodzaj obiektu | ☐ mieszkanie ☐ dom jednorodzinny ☐ budynek wielorodzinny ☐ zakład / inny: ______ |
| Rodzaj sprawdzenia | ☐ odbiorcze ☐ okresowe ☐ po naprawie / zmianie |
| Zakres | ☐ cała instalacja ☐ rozdzielnica: ______ ☐ obwody: ______ |
| Data pomiarów | |
| Warunki (temperatura, wilgotność) | |

## 2. Dane sieci zasilającej

| | |
|---|---|
| Układ sieci | ☐ TN-C ☐ TN-S ☐ TN-C-S ☐ TT ☐ IT ([moduł 11](../modules/11-uklady-sieci/README.md)) |
| Napięcie $U_0$ / $U$ | 230 / 400 V |
| Zabezpieczenie przedlicznikowe | typ ______ $I_n$ ______ A |
| Inne źródła zasilania | ☐ brak ☐ PV ☐ magazyn ☐ agregat ☐ UPS |

## 3. Przyrządy

| Przyrząd | Typ | Nr fabryczny | Świadectwo wzorcowania ważne do |
|----------|-----|--------------|-------------------------------|
| *Miernik parametrów instalacji* | *……* | *……* | *……* |
| | | | |
| | | | |

## 4. Oględziny ([23.01](../modules/23-pomiary-odbiorcze-i-okresowe/23.01-ogledziny-instalacji.md))

| Sprawdzane | Wynik | Uwagi |
|------------|-------|-------|
| Sposób ochrony przed porażeniem (podstawowa, przy uszkodzeniu, uzupełniająca) | ☐ poz. ☐ neg. ☐ n/d | |
| Dobór i oznaczenie przewodów (kolory, przekroje) | ☐ poz. ☐ neg. ☐ n/d | |
| Dobór zabezpieczeń do przewodów | ☐ poz. ☐ neg. ☐ n/d | |
| RCD — obecność i dobór (30 mA, typ) | ☐ poz. ☐ neg. ☐ n/d | |
| Ochrona przeciwprzepięciowa (SPD) | ☐ poz. ☐ neg. ☐ n/d | |
| Połączenia wyrównawcze główne i miejscowe | ☐ poz. ☐ neg. ☐ n/d | |
| Oznaczenie obwodów, schemat w rozdzielnicy | ☐ poz. ☐ neg. ☐ n/d | |
| Stan osprzętu, obudów, IP (łazienka, zewnątrz) | ☐ poz. ☐ neg. ☐ n/d | |
| Dostępność aparatów do obsługi i odłączania | ☐ poz. ☐ neg. ☐ n/d | |
| Ochrona przed skutkami cieplnymi, przegrzania, ślady łuku | ☐ poz. ☐ neg. ☐ n/d | |

## 5. Ciągłość przewodów ochronnych i wyrównawczych ([23.02](../modules/23-pomiary-odbiorcze-i-okresowe/23.02-ciaglosc-przewodow-ochronnych-i-wyrownawczych.md))

| Lp. | Odcinek (od – do) | R [Ω] | Ocena |
|-----|-------------------|-------|-------|
| *1* | *szyna PE – gniazdo kuchnia* | *0,35* | *poz.* |
| | | | |
| | | | |

## 6. Rezystancja izolacji ([23.03](../modules/23-pomiary-odbiorcze-i-okresowe/23.03-rezystancja-izolacji.md))

Napięcie probiercze: ☐ 250 V ☐ **500 V** ☐ 1000 V DC · wymagane ≥ ______ MΩ (dla 230/400 V: **1,0 MΩ** przy 500 V)

| Obwód | L1–PE | L2–PE | L3–PE | N–PE | L–N | Najmniejsza [MΩ] | Ocena |
|-------|-------|-------|-------|------|-----|------------------|-------|
| *F3 gniazda kuchnia* | *> 999* | *—* | *—* | *> 999* | *> 999* | *> 999* | *poz.* |
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |

## 7. Samoczynne wyłączenie — impedancja pętli zwarcia ([23.04](../modules/23-pomiary-odbiorcze-i-okresowe/23.04-impedancja-petli-zwarcia.md))

Warunek: $Z_s \le U_0 / I_a$, ocena pomiaru z zapasem: $Z_s \le \tfrac{2}{3}\, U_0 / I_a$. Czas wyłączenia: ☐ 0,4 s ☐ 5 s ☐ 0,2 s (TT) ☐ 1 s (TT)

| Obwód / punkt | Zabezpieczenie | $I_a$ [A] | $Z_s$ dop. [Ω] | ⅔ $Z_s$ dop. [Ω] | $Z_s$ zmierz. [Ω] | $I_k$ [A] | Ocena |
|---------------|----------------|-------------|------------------|--------------------|---------------------|------------|-------|
| *F3 gniazdo przy oknie* | *B16* | *80* | *2,88* | *1,92* | *0,84* | *274* | *poz.* |
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |

## 8. Wyłączniki różnicowoprądowe ([23.05](../modules/23-pomiary-odbiorcze-i-okresowe/23.05-badanie-wylacznikow-roznicowopradowych.md))

Wymagania (typ ogólny): $I_A$ w zakresie 0,5–1 $I_{\Delta n}$, $t_A$ ≤ 300 ms przy $I_{\Delta n}$ (≤ 40 ms przy 5 $I_{\Delta n}$), $U_B \le U_L$ = 50 V. Przycisk TEST działa.

| RCD | Typ (AC/A/F/B, S) | $I_n$ / $I_{\Delta n}$ | $I_A$ [mA] | $t_A$ przy $I_{\Delta n}$ [ms] | $t_A$ przy 5 $I_{\Delta n}$ [ms] | $U_B$ [V] | TEST | Ocena |
|-----|-------------------|------------------------|-------------|--------------------------|----------------------------|-----------|------|-------|
| *Q2* | *A* | *40 A / 30 mA* | *21* | *24* | *12* | *0,9* | *✓* | *poz.* |
|   |   |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   |   |

## 9. Rezystancja uziemienia ([23.06](../modules/23-pomiary-odbiorcze-i-okresowe/23.06-rezystancja-uziemienia.md))

| Uziom / złącze kontrolne | Metoda | R [Ω] | Wymagane [Ω] | Ocena |
|--------------------------|--------|-------|--------------|-------|
| | ☐ techniczna ☐ cęgowa | | | |
| | ☐ techniczna ☐ cęgowa | | | |

## 10. Kolejność faz i próby działania ([23.07](../modules/23-pomiary-odbiorcze-i-okresowe/23.07-kolejnosc-faz.md))

| Punkt | Kolejność faz | Próba działania (łączniki, blokady, sterowanie) | Ocena |
|-------|---------------|-----------------------------------------------|-------|
| | ☐ zgodna ☐ niezgodna | | |

## 11. Wnioski

☐ Instalacja **nadaje się** do eksploatacji. ☐ Instalacja **nie nadaje się** do eksploatacji do czasu usunięcia usterek.

Usterki i zalecenia:

1. ______________________________________________________________________
2. ______________________________________________________________________

**Termin następnego sprawdzenia:** ____________ (budynek: co najmniej co 5 lat — art. 62 Prawa budowlanego, [32.03](../modules/32-przepisy-i-normy/32.03-prawo-budowlane-kontrole-okresowe.md))

| | Imię i nazwisko | Nr świadectwa kwalifikacyjnego (E / D) | Podpis |
|---|---|---|---|
| Pomiary wykonał | | | |
| Protokół sprawdził | | | |
