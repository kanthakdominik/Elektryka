# Zbiór zadań i sytuacji

> Wszystkie przykłady z tematów w jednym miejscu: najpierw spróbuj sam, potem rozwiń **Rozwiązanie**.
> **206** pozycji: 🧮 **113** obliczeniowych (wzór, liczby, wynik) i 🔎 **93** sytuacji do oceny (co jest źle, co zrobić).
> Plik jest generowany skryptem [`tools/gen_zadania.py`](tools/gen_zadania.py) — poprawki rób w tematach, nie tutaj.

**Tylko obliczeniowe?** Szukaj znaczka 🧮 (Ctrl+F). Kalkulatory do sprawdzenia wyników: [www/kalkulatory.html](www/kalkulatory.html).

## Spis

- [00 — Zanim dotkniesz czegokolwiek](#00--zanim-dotkniesz-czegokolwiek) · 4 (0 🧮)
- [01 — Prąd, napięcie, opór, moc i energia](#01--prąd-napięcie-opór-moc-i-energia) · 9 (9 🧮)
- [02 — Prąd przemienny i sieć 230/400 V](#02--prąd-przemienny-i-sieć-230400-v) · 5 (5 🧮)
- [03 — Elektromagnetyzm w praktyce](#03--elektromagnetyzm-w-praktyce) · 4 (4 🧮)
- [04 — Prąd a człowiek](#04--prąd-a-człowiek) · 5 (4 🧮)
- [05 — Przewody i kable](#05--przewody-i-kable) · 7 (5 🧮)
- [06 — Osprzęt instalacyjny](#06--osprzęt-instalacyjny) · 6 (2 🧮)
- [07 — Zabezpieczenia nadprądowe](#07--zabezpieczenia-nadprądowe) · 7 (7 🧮)
- [08 — Wyłączniki różnicowoprądowe](#08--wyłączniki-różnicowoprądowe) · 7 (5 🧮)
- [09 — Ochrona przeciwprzepięciowa](#09--ochrona-przeciwprzepięciowa) · 5 (4 🧮)
- [10 — Aparatura modułowa](#10--aparatura-modułowa) · 6 (2 🧮)
- [11 — Układy sieci: TN, TT, IT](#11--układy-sieci-tn-tt-it) · 6 (2 🧮)
- [12 — Ochrona przeciwporażeniowa](#12--ochrona-przeciwporażeniowa) · 6 (3 🧮)
- [13 — Uziemienia i połączenia wyrównawcze](#13--uziemienia-i-połączenia-wyrównawcze) · 6 (5 🧮)
- [14 — Od słupa do gniazdka](#14--od-słupa-do-gniazdka) · 5 (3 🧮)
- [15 — Rozdzielnica mieszkaniowa](#15--rozdzielnica-mieszkaniowa) · 7 (5 🧮)
- [16 — Planowanie obwodów](#16--planowanie-obwodów) · 6 (4 🧮)
- [17 — Pomieszczenia i miejsca szczególne](#17--pomieszczenia-i-miejsca-szczególne) · 5 (3 🧮)
- [18 — Oświetlenie](#18--oświetlenie) · 6 (5 🧮)
- [19 — Prace krok po kroku](#19--prace-krok-po-kroku) · 7 (3 🧮)
- [20 — Diagnostyka usterek](#20--diagnostyka-usterek) · 7 (1 🧮)
- [21 — Stare instalacje](#21--stare-instalacje) · 5 (2 🧮)
- [22 — Przyrządy pomiarowe](#22--przyrządy-pomiarowe) · 6 (2 🧮)
- [23 — Pomiary odbiorcze i okresowe](#23--pomiary-odbiorcze-i-okresowe) · 8 (4 🧮)
- [24 — Silniki i napędy](#24--silniki-i-napędy) · 8 (7 🧮)
- [25 — Transformatory, zasilacze, UPS i agregaty](#25--transformatory-zasilacze-ups-i-agregaty) · 5 (3 🧮)
- [26 — Fotowoltaika, pompy ciepła, wallboxy i magazyny energii](#26--fotowoltaika-pompy-ciepła-wallboxy-i-magazyny-energii) · 6 (5 🧮)
- [27 — Inteligentny dom](#27--inteligentny-dom) · 4 (2 🧮)
- [28 — BHP przy urządzeniach elektrycznych](#28--bhp-przy-urządzeniach-elektrycznych) · 6 (1 🧮)
- [29 — Eksploatacja urządzeń i instalacji](#29--eksploatacja-urządzeń-i-instalacji) · 5 (0 🧮)
- [30 — Pożar i awaria](#30--pożar-i-awaria) · 5 (1 🧮)
- [31 — Pierwsza pomoc przy porażeniu](#31--pierwsza-pomoc-przy-porażeniu) · 5 (1 🧮)
- [32 — Przepisy i normy](#32--przepisy-i-normy) · 6 (1 🧮)
- [33 — Dozór (D)](#33--dozór-d) · 6 (2 🧮)
- [34 — Sieci SN i stacje transformatorowe](#34--sieci-sn-i-stacje-transformatorowe) · 5 (1 🧮)

---

## 00 — Zanim dotkniesz czegokolwiek

🔎 **[00.01](modules/00-bezpieczenstwo-najpierw/00.01-piec-zasad-bezpiecznej-pracy-przy-urzadzeniach.md#przykład)** · Pięć zasad bezpiecznej pracy przy urządzeniach elektrycznych

**Sytuacja.** Wymieniasz lampę sufitową w przedpokoju. Wyłączyłeś łącznik na ścianie i wyłącznik opisany jako „Oświetlenie przedpokój”. Wskaźnik dwubiegunowy między dwoma przewodami w suficie (brązowym i niebieskim) pokazuje 0 V. Między brązowym a żółto-zielonym pokazuje 230 V.

<details><summary>Rozwiązanie</summary>

**Co to znaczy?** Brązowy przewód jest pod napięciem względem ziemi. Wyłącznik z opisu nie zasila tej lampy albo zasila ją tylko częściowo. Brak napięcia między L i N wynika z tego, że przewód niebieski w tej puszce nie jest przewodem neutralnym tego obwodu albo jest przerwany. Gdybyś sprawdził tylko jedną parę przewodów, uznałbyś, że możesz pracować.

**Wniosek.** Brak napięcia sprawdza się **między wszystkimi parami przewodów**, także względem PE. Tu trzeba znaleźć właściwy wyłącznik (albo wyłączyć główny) i powtórzyć pomiar. Opis w rozdzielnicy trzeba poprawić.

</details>

🔎 **[00.02](modules/00-bezpieczenstwo-najpierw/00.02-sprawdzanie-braku-napiecia-probnik-dwubiegunowy.md#przykład)** · Sprawdzanie braku napięcia: próbnik dwubiegunowy a śrubokręt z neonówką

**Sytuacja.** W puszce rozgałęźnej wyłączonego obwodu oświetlenia multimetr pokazuje między brązowym przewodem a PE **63 V**. Wskaźnik dwubiegunowy z obciążeniem między tymi samymi przewodami nie pokazuje napięcia, a po teście na gnieździe działa poprawnie.

<details><summary>Rozwiązanie</summary>

**Analiza.** Brązowy przewód biegnie w jednej rurce z przewodem innego obwodu, który jest pod napięciem. Między przewodami jest niewielka pojemność. Przez nią na odłączony przewód „przecieka” trochę napięcia, ale za tym napięciem nie stoi prawie żaden prąd. Multimetr ma impedancję wejściową około 10 MΩ i nie obciąża przewodu, więc pokazuje sporą wartość. Wskaźnik z obciążeniem pobiera prąd i napięcie „siada” do zera.

**Wniosek.** To napięcie indukowane, a nie zasilanie. Gdyby jednak wskaźnik z obciążeniem pokazał około 230 V, przewód byłby zasilany i pracy nie wolno zaczynać.

</details>

🔎 **[00.03](modules/00-bezpieczenstwo-najpierw/00.03-co-wolno-zrobic-samemu-a-co-wymaga-uprawnien-i.md#przykład)** · Co wolno zrobić samemu, a co wymaga uprawnień i pomiarów

**Sytuacja.** Remontujesz mieszkanie. Plan: (a) wymienić wszystkie stare gniazda i łączniki na nowe w tych samych miejscach, (b) dołożyć dwa gniazda nad blatem w kuchni z istniejącego obwodu gniazd, (c) poprowadzić nowy obwód do piekarnika z nowym wyłącznikiem w rozdzielnicy, (d) przenieść kinkiet w łazience.

<details><summary>Rozwiązanie</summary>

**Klasyfikacja.**

- (a) **naprawa 1:1** 🟡: możliwa samodzielnie z pięcioma zasadami, ale przy wymianie wszystkiego warto zamówić pomiary. Przy okazji wyjdą na jaw stare błędy (brak PE, zamienione L/N).
- (b) **zmiana instalacji** 🔴: zwiększasz obciążenie obwodu i dokładasz punkty w kuchni, gdzie pracują urządzenia dużej mocy. Trzeba sprawdzić przekrój, zabezpieczenie i ochronę różnicowoprądową.
- (c) **zmiana instalacji** 🔴: praca w rozdzielnicy. Obowiązkowe pomiary odbiorcze i protokół.
- (d) **zmiana instalacji w pomieszczeniu szczególnym** 🔴: w łazience obowiązują strefy ([moduł 17](modules/17-pomieszczenia-szczegolne/README.md)). To zadanie dla osoby z kwalifikacjami.

**Wniosek.** Najrozsądniej przygotować bruzdy i puszki samemu, a podłączenia, rozdzielnicę i pomiary zlecić jednej osobie ze świadectwem, która zrobi dokumentację całości.

</details>

🔎 **[00.04](modules/00-bezpieczenstwo-najpierw/00.04-czerwone-flagi-kiedy-przerwac-prace-i-wezwac.md#przykład)** · Czerwone flagi — kiedy przerwać pracę i wezwać elektryka

**Sytuacja.** Wieczorem w mieszkaniu zasilanym trójfazowo żarówki w kuchni zaczynają świecić bardzo jasno, a w pokoju przygasają. Po chwili wyłącza się router, a z zasilacza telewizora czuć spaleniznę.

<details><summary>Rozwiązanie</summary>

**Co się dzieje?** Najbardziej prawdopodobna jest przerwa w przewodzie neutralnym przed rozdzielnicą mieszkania. Bez wspólnego N odbiorniki z różnych faz łączą się szeregowo między fazami, czyli na napięciu do 400 V. Faza, na której jest mniejsze obciążenie (większa rezystancja), dostaje wyższe napięcie. Sprzęt na tej fazie przegrzewa się i psuje (podział napięcia na połączeniu szeregowym — [01.05](modules/01-prad-napiecie-opor/01.05-polaczenie-szeregowe-i-rownolegle.md)).

**Co robisz?** Natychmiast wyłączasz wyłącznik główny mieszkania. Nie włączasz go ponownie, żeby sprawdzić, czy przeszło. Dzwonisz do elektryka, a jeśli problem dotyczy całego budynku albo sąsiadów, także do pogotowia energetycznego (991). Uszkodzenia sprzętu dokumentujesz zdjęciami.

</details>

---

## 01 — Prąd, napięcie, opór, moc i energia

🧮 **[01.01](modules/01-prad-napiecie-opor/01.01-ladunek-i-prad-co-wlasciwie-plynie-w-przewodzie.md#przykład)** · Ładunek i prąd — co właściwie płynie w przewodzie

**Zadanie.** Czajnik pobiera 8,7 A. Ile elektronów przepływa przez jego grzałkę w ciągu sekundy? Jak szybko przesuwają się elektrony w przewodzie 1,5 mm², gdy płynie 10 A?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.**

Liczba elektronów na sekundę:

$$N = \frac{I}{e} = \frac{8{,}7\ \mathrm{A}}{1{,}602 \cdot 10^{-19}\ \mathrm{C}} \approx 5{,}4 \cdot 10^{19}\ \text{elektronów na sekundę}$$

Prędkość dryfu:

$$v = \frac{I}{n\,e\,S} = \frac{10}{8{,}5 \cdot 10^{28} \cdot 1{,}602 \cdot 10^{-19} \cdot 1{,}5 \cdot 10^{-6}}\ \mathrm{\frac{m}{s}} \approx 4{,}9 \cdot 10^{-4}\ \mathrm{\frac{m}{s}} \approx 0{,}5\ \mathrm{\frac{mm}{s}}$$

**Sprawdzenie.** Jednostki: $\mathrm{A} / (\mathrm{m^{-3}} \cdot \mathrm{C} \cdot \mathrm{m^2}) = \mathrm{(C/s)} / (\mathrm{C/m}) = \mathrm{m/s}$ ✓. Przy prądzie stałym elektron w godzinę przesunąłby się o niecałe 2 metry, a przy przemiennym tylko drga wokół jednego miejsca.

**Wniosek.** Liczba elektronów jest ogromna, a ich ruch powolny. Energia nie „jedzie” razem z elektronami, tylko jest przekazywana przez pole elektryczne wzdłuż przewodu.

</details>

🧮 **[01.02](modules/01-prad-napiecie-opor/01.02-napiecie-roznica-cisnien-miedzy-dwoma-punktami.md#przykład)** · Napięcie — różnica „ciśnień” między dwoma punktami

**Sytuacja.** W domu na końcu wsi wieczorem miernik w gniazdku pokazuje 203 V, a w południe 236 V. Czy operator sieci dotrzymuje wymagań?

<details><summary>Rozwiązanie</summary>

**Analiza.** Dopuszczalne pasmo to 230 V ±10 %:

$$230 \cdot 0{,}9 = 207\ \mathrm{V} \qquad 230 \cdot 1{,}1 = 253\ \mathrm{V}$$

Wartość 236 V mieści się w paśmie, a 203 V jest poniżej. Wymaganie dotyczy jednak 95 % średnich 10-minutowych w ciągu tygodnia. Pojedynczy odczyt nie wystarczy, żeby stwierdzić naruszenie. Trzeba rejestrować napięcie przez tydzień rejestratorem albo zgłosić problem operatorowi, który zrobi taki pomiar.

**Wniosek.** Napięcie w gniazdku nie jest stałe: spada przy dużym obciążeniu sieci (wieczór) i rośnie przy małym albo przy pracy fotowoltaiki (południe). Pasmo ±10 % to norma, a nie awaria.

</details>

🧮 **[01.03](modules/01-prad-napiecie-opor/01.03-opor-i-prawo-ohma.md#przykład)** · Opór i prawo Ohma

**Zadanie 1.** Czajnik ma moc 2000 W przy 230 V. Jaki ma opór i jaki pobiera prąd?

<details><summary>Rozwiązanie</summary>

Z wzorów na moc ([01.04](modules/01-prad-napiecie-opor/01.04-moc-i-energia-waty-kilowatogodziny-i-rachunek.md)): $P = U^2 / R$, więc

$$R = \frac{U^2}{P} = \frac{230^2}{2000}\ \Omega = 26{,}45\ \Omega \qquad I = \frac{U}{R} = \frac{230}{26{,}45}\ \mathrm{A} \approx 8{,}7\ \mathrm{A}$$

Sprawdzenie: $P = U \cdot I = 230 \cdot 8{,}7 \approx 2000\ \mathrm{W}$ ✓.

</details>

🧮 **[01.03](modules/01-prad-napiecie-opor/01.03-opor-i-prawo-ohma.md#przykład)** · Opór i prawo Ohma

**Zadanie 2.** Obwód gniazd w pokoju to przewód YDYp 3×1,5 mm², odległość od rozdzielnicy do gniazda 20 m. Jaki opór ma pętla L + N?

<details><summary>Rozwiązanie</summary>

Prąd płynie do gniazda żyłą L i wraca żyłą N, więc długość drogi to $2 \cdot 20\ \mathrm{m} = 40\ \mathrm{m}$:

$$R = 0{,}0175 \cdot \frac{40}{1{,}5}\ \Omega \approx 0{,}47\ \Omega$$

Przy przewodzie 2,5 mm² byłoby to $0{,}28\ \Omega$. Ta wartość wróci w [01.06](modules/01-prad-napiecie-opor/01.06-grzanie-przewodow-i-spadek-napiecia.md) przy spadku napięcia i w [01.07](modules/01-prad-napiecie-opor/01.07-przeciazenie-a-zwarcie-dwie-rozne-awarie.md) przy prądzie zwarcia.

</details>

🧮 **[01.04](modules/01-prad-napiecie-opor/01.04-moc-i-energia-waty-kilowatogodziny-i-rachunek.md#przykład)** · Moc i energia — waty, kilowatogodziny i rachunek za prąd

**Zadanie 1 — rachunek.** Czajnik 2 kW pracuje średnio 3 minuty dziennie. Ile energii zużywa w roku i ile to kosztuje przy łącznej cenie 1,10 zł za kWh? (Cena jest przykładowa, swoją sprawdź na rachunku.)

<details><summary>Rozwiązanie</summary>

$$E_{\text{dzień}} = 2\ \mathrm{kW} \cdot \tfrac{3}{60}\ \mathrm{h} = 0{,}1\ \mathrm{kWh} \qquad E_{\text{rok}} = 0{,}1 \cdot 365 = 36{,}5\ \mathrm{kWh} \qquad 36{,}5 \cdot 1{,}10 \approx 40\ \text{zł}$$

Dla porównania telewizor w czuwaniu (5 W, całą dobę) zużywa w roku $5\ \mathrm{W} \cdot 8760\ \mathrm{h} = 43{,}8\ \mathrm{kWh}$, czyli więcej niż czajnik.

</details>

🧮 **[01.04](modules/01-prad-napiecie-opor/01.04-moc-i-energia-waty-kilowatogodziny-i-rachunek.md#przykład)** · Moc i energia — waty, kilowatogodziny i rachunek za prąd

**Zadanie 2 — moc z licznika.** Licznik ma stałą 250 obr/kWh. Gdy działa piekarnik, tarcza robi 8 obrotów w ciągu minuty. Jaką moc pobiera mieszkanie?

<details><summary>Rozwiązanie</summary>

$$P = \frac{8 \cdot 3600}{250 \cdot 60}\ \mathrm{kW} = 1{,}92\ \mathrm{kW}$$

**Sprawdzenie.** 8 obrotów to $8/250 = 0{,}032\ \mathrm{kWh}$ w ciągu minuty, czyli $0{,}032 \cdot 60 = 1{,}92\ \mathrm{kWh}$ w ciągu godziny. Moc wynosi więc 1,92 kW ✓.

</details>

🧮 **[01.05](modules/01-prad-napiecie-opor/01.05-polaczenie-szeregowe-i-rownolegle.md#przykład)** · Połączenie szeregowe i równoległe

**Sytuacja.** W kuchni z jednego obwodu (wyłącznik B16) jednocześnie pracują czajnik 2000 W, grzejnik olejowy 2000 W i mikrofalówka 1200 W. Jaki prąd płynie przewodem z rozdzielnicy i jaki jest opór zastępczy?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Każde urządzenie jest podłączone równolegle i ma 230 V. Prądy:

$$I_{cz} = \frac{2000}{230} \approx 8{,}7\ \mathrm{A} \qquad I_{gr} \approx 8{,}7\ \mathrm{A} \qquad I_{mf} = \frac{1200}{230} \approx 5{,}2\ \mathrm{A}$$

$$I = 8{,}7 + 8{,}7 + 5{,}2 = 22{,}6\ \mathrm{A}$$

Opory: czajnik i grzejnik po 26,45 Ω, mikrofalówka (traktowana jak opór) $230^2 / 1200 \approx 44{,}1\ \Omega$:

$$\frac{1}{R_z} = \frac{1}{26{,}45} + \frac{1}{26{,}45} + \frac{1}{44{,}1} \approx 0{,}0983\ \frac{1}{\Omega} \qquad R_z \approx 10{,}2\ \Omega$$

**Sprawdzenie.** $230 / 10{,}2 \approx 22{,}6\ \mathrm{A}$ ✓, a $5200\ \mathrm{W} / 230\ \mathrm{V} \approx 22{,}6\ \mathrm{A}$ ✓. Opór zastępczy (10,2 Ω) jest mniejszy niż najmniejszy z oporów (26,45 Ω), tak jak powinien.

**Wniosek.** 22,6 A to 1,41 raza więcej niż 16 A, czyli przeciążenie. Wyłącznik zadziała członem termicznym, ale nie od razu, a nawet po kilkudziesięciu minutach ([01.07](modules/01-prad-napiecie-opor/01.07-przeciazenie-a-zwarcie-dwie-rozne-awarie.md)). Przez ten czas przewód pracuje w podwyższonej temperaturze.

</details>

🧮 **[01.06](modules/01-prad-napiecie-opor/01.06-grzanie-przewodow-i-spadek-napiecia.md#przykład)** · Grzanie przewodów i spadek napięcia

**Zadanie.** Kosiarka elektryczna 2000 W na końcu przedłużacza o długości 50 m z przewodem 3×1,5 mm². Jaki jest spadek napięcia i ile ciepła wydziela się w przedłużaczu?

<details><summary>Rozwiązanie</summary>

**Dane.** $P = 2000\ \mathrm{W}$, $U = 230\ \mathrm{V}$, $l = 50\ \mathrm{m}$, $S = 1{,}5\ \mathrm{mm^2}$, $\rho = 0{,}0175\ \Omega \cdot \mathrm{mm^2/m}$.

**Prąd:** $I = 2000 / 230 \approx 8{,}7\ \mathrm{A}$.

**Opór pętli L + N:**

$$R = 0{,}0175 \cdot \frac{2 \cdot 50}{1{,}5}\ \Omega \approx 1{,}17\ \Omega$$

**Spadek napięcia:**

$$\Delta U = I \cdot R = 8{,}7 \cdot 1{,}17 \approx 10{,}1\ \mathrm{V} \qquad \Delta U\% = \frac{10{,}1}{230} \cdot 100\% \approx 4{,}4\ \%$$

**Ciepło w przedłużaczu:**

$$P_{\text{straty}} = I^2 R = 8{,}7^2 \cdot 1{,}17 \approx 88\ \mathrm{W}$$

**Sprawdzenie.** $\Delta U \cdot I = 10{,}1 \cdot 8{,}7 \approx 88\ \mathrm{W}$ ✓. Te same 88 W liczone na dwa sposoby.

**Wniosek.** Rozłożone na 50 m rozwiniętego przewodu 88 W to niecałe 2 W na metr i nie stanowi problemu. Te same 88 W w ciasno zwiniętym bębnie podgrzeje środek zwoju do niebezpiecznej temperatury. Przy przewodzie 2,5 mm² spadek wyniósłby około 2,6 %, a straty około 53 W.

</details>

🧮 **[01.07](modules/01-prad-napiecie-opor/01.07-przeciazenie-a-zwarcie-dwie-rozne-awarie.md#przykład)** · Przeciążenie a zwarcie — dwie różne awarie

**Zadanie.** Gniazdo zabezpieczone wyłącznikiem B16. W gnieździe nastąpiło zwarcie L–N. Ile wyniesie prąd zwarcia i czy wyłącznik zadziała natychmiast, jeśli impedancja pętli wynosi (a) 0,8 Ω, (b) 3 Ω? A gdyby zamiast B16 był C16?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.**

(a) $I_{zw} = 230 / 0{,}8 \approx 288\ \mathrm{A}$, czyli $288 / 16 \approx 18$ razy więcej niż $I_n$. B16 zadziała natychmiast, bo próg pewnego zadziałania to 5 × 16 = 80 A. C16 też, bo jego próg to 10 × 16 = 160 A.

(b) $I_{zw} = 230 / 3 \approx 77\ \mathrm{A}$, czyli $77/16 \approx 4{,}8\ I_n$. B16: wartość leży między 3 a 5 $I_n$, więc wyłącznik **może, ale nie musi** zadziałać natychmiast. Pewnego zadziałania norma gwarantuje dopiero od 80 A. C16 (próg 160 A) **nie zadziała** natychmiast i wyłączy dopiero członem termicznym, po sekundach. Przez ten czas przewody się grzeją, a przy zwarciu do obudowy na obudowie byłoby niebezpieczne napięcie.

**Sprawdzenie.** Jednostki: V / Ω = A ✓. Wynik (b) jest mniejszy, bo impedancja większa ✓.

**Wniosek.** O skuteczności wyłącznika decyduje nie tylko jego prąd znamionowy, ale też impedancja pętli zwarcia, czyli długość i przekrój przewodów oraz parametry sieci. Dlatego mierzy się ją przy pomiarach odbiorczych i okresowych ([moduł 23](modules/23-pomiary-odbiorcze-i-okresowe/README.md)), a w module 12 poznasz warunek skuteczności samoczynnego wyłączenia.

</details>

---

## 02 — Prąd przemienny i sieć 230/400 V

🧮 **[02.01](modules/02-prad-przemienny-230-400/02.01-sinusoida-50-hz-i-wartosc-skuteczna.md#przykład)** · Sinusoida, 50 Hz i wartość skuteczna

**Zadanie.** Kondensator w zasilaczu ładuje się do szczytowej wartości napięcia sieci. Do jakiego napięcia naładuje się przy 230 V i przy górnej granicy normy (253 V)? Czy kondensator na 350 V wystarczy?

<details><summary>Rozwiązanie</summary>

$$U_{max} = 230 \cdot \sqrt{2} \approx 325\ \mathrm{V} \qquad U_{max,253} = 253 \cdot \sqrt{2} \approx 358\ \mathrm{V}$$

**Wniosek.** Przy górnej dopuszczalnej wartości napięcia (230 V + 10 %) szczyt przekracza 350 V. Dlatego kondensatory wejściowe zasilaczy sieciowych mają napięcie znamionowe co najmniej 400 V. To samo dotyczy izolacji: przewody instalacyjne mają napięcie znamionowe 450/750 V lub wyższe.

</details>

🧮 **[02.02](modules/02-prad-przemienny-230-400/02.02-faza-przewod-neutralny-i-przewod-ochronny-l-n-pe.md#przykład)** · Faza, przewód neutralny i przewód ochronny — L, N, PE

**Sytuacja.** W łazience pralka „kopie” przy dotknięciu obudowy. Pomiar wskaźnikiem w gnieździe: L–N 230 V, L–PE 0 V, N–PE 230 V. W rozdzielnicy nie ma wyłącznika różnicowoprądowego.

<details><summary>Rozwiązanie</summary>

**Analiza.** Zacisk PE w gnieździe ma potencjał fazy (L–PE = 0 V, N–PE = 230 V). Przewód ochronny tego obwodu został gdzieś połączony z fazą, na przykład w puszce żyłę żółto-zieloną podłączono do zacisku L. Przez przewód PE napięcie fazy trafia prosto na obudowę pralki. Pralka działa normalnie, bo między L a N jest 230 V. Wyłącznik nadprądowy nic nie widzi, bo nie płynie żaden nadmierny prąd.

**Wniosek.** Natychmiast wyłączyć obwód i nie używać pralki do czasu poprawienia połączeń i pomiarów. W łazience obowiązkowa jest też ochrona różnicowoprądowa 30 mA ([moduł 17](modules/17-pomieszczenia-szczegolne/README.md)). Gdyby była zainstalowana, prawdopodobnie zadziałałaby przy pierwszym dotknięciu, zanim prąd stałby się groźny.

</details>

🧮 **[02.03](modules/02-prad-przemienny-230-400/02.03-uklad-trojfazowy-230-v-i-400-v-kolejnosc-faz.md#przykład)** · Układ trójfazowy: 230 V i 400 V, kolejność faz

**Zadanie.** Grzejnik elektryczny trójfazowy 9 kW (rezystancyjny, cos φ = 1). Jaki prąd pobiera z każdej fazy? Jaki pobierałby jednofazowy grzejnik 9 kW?

<details><summary>Rozwiązanie</summary>

$$I_{3f} = \frac{P}{\sqrt{3} \cdot U} = \frac{9000}{1{,}732 \cdot 400}\ \mathrm{A} \approx 13\ \mathrm{A} \qquad I_{1f} = \frac{9000}{230}\ \mathrm{A} \approx 39\ \mathrm{A}$$

**Sprawdzenie.** Każda faza dostarcza jedną trzecią mocy: $3000\ \mathrm{W} / 230\ \mathrm{V} \approx 13\ \mathrm{A}$ ✓.

**Wniosek.** Trójfazowo grzejnik pracuje na zwykłym przewodzie 2,5 mm² z zabezpieczeniem 16 A. Jednofazowo potrzebowałby zabezpieczenia 40 A i przewodu 6–10 mm², zależnie od sposobu ułożenia ([moduł 16](modules/16-planowanie-obwodow/README.md)).

</details>

🧮 **[02.04](modules/02-prad-przemienny-230-400/02.04-moc-czynna-bierna-i-pozorna-wspolczynnik-mocy.md#przykład)** · Moc czynna, bierna i pozorna, współczynnik mocy

**Zadanie.** Silnik jednofazowy: tabliczka 230 V, 5 A, cos φ = 0,8. Oblicz S, P i Q. Ile prądu pobierałby, gdyby cos φ podnieść do 1 przy tej samej mocy czynnej?

<details><summary>Rozwiązanie</summary>

$$S = 230 \cdot 5 = 1150\ \mathrm{VA} \qquad P = 1150 \cdot 0{,}8 = 920\ \mathrm{W} \qquad Q = 1150 \cdot \sin\varphi = 1150 \cdot 0{,}6 = 690\ \mathrm{var}$$

($\sin\varphi = \sqrt{1 - 0{,}8^2} = 0{,}6$.)

**Sprawdzenie:** $\sqrt{920^2 + 690^2} = 1150$ ✓.

Przy cos φ = 1: $I = 920 / 230 = 4\ \mathrm{A}$ zamiast 5 A.

**Wniosek.** Moc bierna zwiększa prąd o 25 %, choć silnik nie wykonuje przez to więcej pracy. Ten „nadmiarowy” prąd grzeje przewody, transformatory i obciąża sieć. Dlatego duże zakłady kompensują moc bierną.

</details>

🧮 **[02.05](modules/02-prad-przemienny-230-400/02.05-odbiorniki-nieliniowe-i-wyzsze-harmoniczne.md#przykład)** · Odbiorniki nieliniowe i wyższe harmoniczne — podstawy

**Sytuacja.** W biurze zasilanym trójfazowo każda faza obciążona jest równo prądem 20 A, pobieranym głównie przez komputery i oświetlenie LED. W każdej fazie trzecia harmoniczna stanowi ok. 12 A. Jaki prąd płynie w przewodzie N?

<details><summary>Rozwiązanie</summary>

**Analiza.** Składowe 50 Hz trzech faz przy równym obciążeniu znoszą się w N. Trzecie harmoniczne z trzech faz są ze sobą w fazie, więc się dodają:

$$I_N \approx 3 \cdot I_3 = 3 \cdot 12\ \mathrm{A} = 36\ \mathrm{A}$$

**Wniosek.** W przewodzie N płynie ok. 36 A, czyli więcej niż w którejkolwiek fazie (20 A). Przewód N dobrany „tak jak fazy, a nawet cieńszy, bo przy równym obciążeniu nic nie płynie” będzie się przegrzewał. Taki problem wykrywa pomiar cęgami True RMS na przewodzie N.

</details>

---

## 03 — Elektromagnetyzm w praktyce

🧮 **[03.01](modules/03-elektromagnetyzm-w-praktyce/03.01-pole-magnetyczne-pradu-i-cewka.md#przykład)** · Pole magnetyczne prądu i cewka

**Zadanie.** Cewka stycznika ma indukcyjność 1 H i rezystancję drutu 100 Ω. Jaki prąd popłynie przy 230 V prądu przemiennego 50 Hz, a jaki płynąłby przy 230 V prądu stałego?

<details><summary>Rozwiązanie</summary>

Reaktancja: $X_L = 2\pi \cdot 50 \cdot 1 \approx 314\ \Omega$. Impedancja: $Z = \sqrt{R^2 + X_L^2} = \sqrt{100^2 + 314^2} \approx 330\ \Omega$.

$$I_{AC} = \frac{230}{330} \approx 0{,}7\ \mathrm{A} \qquad I_{DC} = \frac{230}{100} = 2{,}3\ \mathrm{A}$$

**Wniosek.** Przy prądzie stałym ta sama cewka pobiera ponad trzy razy większy prąd i się przegrzewa. Dlatego cewek na napięcie przemienne nie podłącza się do napięcia stałego tej samej wartości, a na tabliczce cewki zawsze jest rodzaj napięcia (np. „230 V AC” albo „24 V DC”). W rzeczywistych stycznikach indukcyjność zmienia się jeszcze po przyciągnięciu zwory, ale wniosek jest ten sam.

</details>

🧮 **[03.02](modules/03-elektromagnetyzm-w-praktyce/03.02-indukcja-elektromagnetyczna-i-transformator.md#przykład)** · Indukcja elektromagnetyczna i transformator

**Zadanie.** Transformator bezpieczeństwa 230/12 V zasila oświetlenie o mocy 60 W. Ile wynosi przekładnia, prąd po stronie 12 V i prąd pobierany z sieci (pomijając straty)?

<details><summary>Rozwiązanie</summary>

$$\vartheta = \frac{230}{12} \approx 19{,}2 \qquad I_2 = \frac{60}{12} = 5\ \mathrm{A} \qquad I_1 = \frac{I_2}{\vartheta} = \frac{5}{19{,}2} \approx 0{,}26\ \mathrm{A}$$

**Sprawdzenie:** $230 \cdot 0{,}26 \approx 60\ \mathrm{W}$ ✓.

**Wniosek.** Po stronie 12 V płynie prąd 19 razy większy niż po stronie 230 V. Dlatego przewody niskonapięciowe muszą mieć **większy** przekrój niż przewód zasilający transformator, a spadek napięcia na nich jest procentowo dużo groźniejszy: 1 V to ponad 8 % z 12 V.

</details>

🧮 **[03.03](modules/03-elektromagnetyzm-w-praktyce/03.03-elektromagnes-w-pracy-przekaznik-i-stycznik.md#przykład)** · Elektromagnes w pracy: przekaźnik i stycznik

**Zadanie.** Bojler elektryczny 3 kW ma grzać tylko w nocy (tańsza taryfa). Programator czasowy w rozdzielnicy ma styk 16 A. Czy można zasilić bojler bezpośrednio przez styk programatora, czy lepiej przez stycznik?

<details><summary>Rozwiązanie</summary>

**Analiza.** Prąd bojlera: $3000/230 \approx 13\ \mathrm{A}$. Mieści się w 16 A, ale styk programatora pracuje wtedy blisko granicy, codziennie, przy dużym prądzie. Typowe rozwiązanie: programator steruje tylko cewką stycznika modułowego (prąd cewki to ułamek ampera), a stycznik z kategorią AC-1 20 A lub 25 A łączy bojler.

**Wniosek.** Stycznik oddziela „rozum” (programator) od „mięśni” (styki mocy). Programator i jego styk żyją dłużej, a przy awarii wymienia się tani stycznik. Szczegóły doboru w [module 10](modules/10-aparatura-modulowa/README.md).

</details>

🧮 **[03.04](modules/03-elektromagnetyzm-w-praktyce/03.04-jak-dziala-silnik-elektryczny-intuicja.md#przykład)** · Jak działa silnik elektryczny — intuicja

**Zadanie.** Na tabliczce silnika trójfazowego: 400 V, 50 Hz, 2,2 kW, 4,8 A, 1430 obr/min. Ile ma par biegunów, jaki jest poślizg i jakiego prądu rozruchowego można się spodziewać?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Najbliższa wyższa prędkość synchroniczna to 1500 obr/min, więc $p = 2$.

$$s = \frac{1500 - 1430}{1500} \approx 0{,}047 = 4{,}7\ \%$$

Prąd rozruchowy (przyjmując 6–7 × $I_n$): $6 \cdot 4{,}8 \approx 29\ \mathrm{A}$ do $7 \cdot 4{,}8 \approx 34\ \mathrm{A}$.

**Wniosek.** Wyłącznik B10 (próg natychmiastowego zadziałania 30–50 A) może zadziałać przy rozruchu. Do takiego silnika stosuje się wyłącznik silnikowy albo charakterystykę C lub D, dobraną w module 24.

</details>

---

## 04 — Prąd a człowiek

🧮 **[04.01](modules/04-prad-a-czlowiek/04.01-jak-prad-dziala-na-organizm-progi-odczuwania.md#przykład)** · Jak prąd działa na organizm — progi odczuwania, samouwolnienia i migotania komór

**Zadanie.** Człowiek stojący na wilgotnej posadzce dotyka obudowy pralki, na którą przez uszkodzenie dostało się napięcie fazowe. Impedancja drogi ręka–stopy przy tych warunkach wynosi ok. 1000 Ω. Jaki prąd popłynie i do której strefy należy, jeśli (a) zadziała różnicówka 30 mA w 40 ms, (b) nie ma różnicówki, a wyłącznik nadprądowy nie zadziała?

<details><summary>Rozwiązanie</summary>

$$I = \frac{230\ \mathrm{V}}{1000\ \Omega} = 0{,}23\ \mathrm{A} = 230\ \mathrm{mA}$$

(a) 230 mA przez 40 ms: na [wykresie stref](assets/schematy/04-strefy-skutkow-pradu.svg) to strefa AC-3, wyraźnie poniżej krzywej c₁. Silny, bolesny skurcz, ale bez migotania komór.

(b) 230 mA bez ograniczenia czasu: po kilkuset milisekundach głęboko w strefie AC-4 — duże ryzyko migotania komór i śmierci.

**Wniosek.** Te same 230 mA mogą zakończyć się nieprzyjemnym szarpnięciem albo śmiercią. Różnicę robi **czas przepływu**, który skraca ochrona przeciwporażeniowa ([moduł 12](modules/12-ochrona-przeciwporazeniowa/README.md)).

</details>

🧮 **[04.02](modules/04-prad-a-czlowiek/04.02-droga-przeplywu-czas-i-czestotliwosc.md#przykład)** · Droga przepływu, czas i częstotliwość

**Zadanie.** Elektryk dotyka jedną ręką fazy, a drugą metalowej obudowy połączonej z PE. Płynie prąd 100 mA. Jak groźne jest to w porównaniu z prądem płynącym drogą lewa ręka → stopy?

<details><summary>Rozwiązanie</summary>

$$I_{ref} = F \cdot I_h = 0{,}4 \cdot 100\ \mathrm{mA} = 40\ \mathrm{mA}$$

**Wniosek.** Dla serca to tak, jakby drogą lewa ręka → stopy płynęło 40 mA. Przy przepływie dłuższym niż ok. 1 s to już okolice progu migotania komór. Droga ręka → ręka jest „łagodniejsza”, ale przy 100 mA wcale nie bezpieczna.

</details>

🧮 **[04.03](modules/04-prad-a-czlowiek/04.03-napiecie-dotykowe-i-krokowe-napiecia.md#przykład)** · Napięcie dotykowe i krokowe, napięcia dopuszczalne długotrwale

**Sytuacja.** W piwnicy przez uszkodzenie izolacji faza dotknęła obudowy pompy. Prąd uszkodzenia 200 A płynie przewodem PE o rezystancji 0,25 Ω (od pompy do szyny wyrównawczej). Jakie napięcie dotykowe pojawi się między obudową pompy a metalową rurą wodną połączoną z szyną wyrównawczą?

<details><summary>Rozwiązanie</summary>

$$U_T = I \cdot R_{PE} = 200\ \mathrm{A} \cdot 0{,}25\ \Omega = 50\ \mathrm{V}$$

**Analiza.** Obudowa ma względem rury 50 V, czyli dokładnie granicę $U_L$ dla warunków normalnych. W wilgotnej piwnicy to już powyżej 25 V. Dlatego obwód musi zostać wyłączony szybko: przy 200 A wyłącznik B16 zadziała natychmiast ([01.07](modules/01-prad-napiecie-opor/01.07-przeciazenie-a-zwarcie-dwie-rozne-awarie.md)). Gdyby przewód PE był dłuższy lub cieńszy, napięcie dotykowe byłoby wyższe.

**Wniosek.** Napięcie dotykowe zależy od prądu uszkodzenia i rezystancji przewodu ochronnego. Pomaga je ograniczyć dodatkowe połączenie wyrównawcze miejscowe, czyli pompa i rura połączone krótkim przewodem bezpośrednio ([moduł 13](modules/13-uziemienia-i-wyrownanie/README.md)).

</details>

🧮 **[04.04](modules/04-prad-a-czlowiek/04.04-maksymalne-czasy-samoczynnego-wylaczenia.md#przykład)** · Maksymalne czasy samoczynnego wyłączenia

**Zadanie.** Obwód gniazd w garażu chroniony wyłącznikiem B16, układ TN, 230 V. Zmierzona impedancja pętli zwarcia w najdalszym gnieździe: 2,1 Ω. Czy samoczynne wyłączenie jest skuteczne? A gdyby zamontowano C16?

<details><summary>Rozwiązanie</summary>

**B16:** $I_a = 5 \cdot 16 = 80\ \mathrm{A}$, więc $Z_{s,max} = 230/80 = 2{,}88\ \Omega$. Zmierzone 2,1 Ω < 2,88 Ω, więc ochrona jest skuteczna. Prąd zwarcia $230/2{,}1 \approx 110\ \mathrm{A}$ wyłączy B16 w czasie poniżej 0,1 s.

**C16:** $I_a = 10 \cdot 16 = 160\ \mathrm{A}$, więc $Z_{s,max} = 1{,}44\ \Omega$. Zmierzone 2,1 Ω > 1,44 Ω, więc ochrona **nie jest** skuteczna. Prąd 110 A nie wywoła natychmiastowego zadziałania C16, a człon termiczny wyłączy obwód dopiero po kilku sekundach, więc 0,4 s nie zostanie dotrzymane.

**Wniosek.** Ten sam obwód jest bezpieczny z B16 i niebezpieczny z C16. Ratunkiem byłby wyłącznik różnicowoprądowy, który zadziała przy prądzie uszkodzenia do PE niezależnie od impedancji pętli ([moduł 08](modules/08-wylaczniki-roznicowopradowe/README.md)).

</details>

🔎 **[04.05](modules/04-prad-a-czlowiek/04.05-luk-elektryczny-i-oparzenia.md#przykład)** · Łuk elektryczny i oparzenia

**Sytuacja.** Przy wymianie wyłącznika w rozdzielnicy mieszkaniowej elektryk wyłączył wyłącznik główny, ale nie osłonił jego zacisków górnych. Wkrętak ześlizgnął się z zacisku wyłącznika obwodu i dotknął jednocześnie zacisku górnego wyłącznika głównego (faza) i szyny PE.

<details><summary>Rozwiązanie</summary>

**Co się stało?** Zacisk górny wyłącznika głównego był pod napięciem (przed wyłącznikiem). Powstało zwarcie faza–PE przez wkrętak. Prąd zwarcia ograniczała tylko impedancja WLZ, przyłącza i sieci, czyli setki amperów albo kilka kiloamperów. Zadziałało zabezpieczenie przedlicznikowe, ale przez kilka–kilkadziesiąt milisekund trwał łuk. Końcówka wkrętaka się stopiła, a rozprysk metalu i błysk poparzyły dłoń i twarz.

**Czego zabrakło:** osłony części pozostających pod napięciem (zasada 5), okularów lub osłony twarzy i narzędzia izolowanego z izolacją prawie do samego grotu.

</details>

---

## 05 — Przewody i kable

🔎 **[05.01](modules/05-przewody-i-kable/05.01-budowa-przewodu-i-kabla-zyla-izolacja-powloka.md#przykład)** · Budowa przewodu i kabla: żyła, izolacja, powłoka

**Sytuacja.** W puszce znajdujesz przewód, z którego przy lekkim zgięciu odpada kawałek twardej, pękającej izolacji. Przewód zasila obwód gniazd w kuchni, w której stoi czajnik, mikrofalówka i ekspres.

<details><summary>Rozwiązanie</summary>

**Co się stało?** Izolacja PVC przegrzewała się latami: obwód był przeciążany albo połączenie w puszce było luźne i grzało miejscowo. Gdy izolacja kruszeje, przewód traci podstawową ochronę przed porażeniem i zwarciem.

**Co zrobić?** Wyłączyć obwód, sprawdzić brak napięcia. Wymienić uszkodzony odcinek (albo cały przewód, jeśli kruszeje na długości) i poprawić połączenie. Sprawdzić, czy zabezpieczenie pasuje do przekroju ([07.06](modules/07-zabezpieczenia-nadpradowe/07.06-koordynacja-zabezpieczenia-z-przewodem.md)) i rozważyć podział obciążenia na dwa obwody.

</details>

🧮 **[05.02](modules/05-przewody-i-kable/05.02-oznaczenia-literowe-ydy-ydyp-yly-yky-h07v-k.md#przykład)** · Oznaczenia literowe: YDY, YDYp, YLY, YKY, H07V-K, H05VV-F, N2XH

**Zadanie.** Rozszyfruj: **YDYżo 5×4 450/750 V**.

<details><summary>Rozwiązanie</summary>

- Y — izolacja żył z PVC,
- D — żyły jednodrutowe,
- Y — powłoka z PVC,
- żo — z żyłą ochronną żółto-zieloną, przewód okrągły,
- 5×4 — pięć żył po 4 mm²,
- 450/750 V — napięcie znamionowe.

**Wniosek.** To przewód instalacyjny do obwodu trójfazowego (L1, L2, L3, N, PE), np. do płyty indukcyjnej z dłuższym odcinkiem albo podlicznikowej linii zasilającej rozdzielnicę w domu.

</details>

🔎 **[05.03](modules/05-przewody-i-kable/05.03-kolory-zyl-i-ich-znaczenie.md#przykład)** · Kolory żył i ich znaczenie

**Sytuacja.** Podłączasz lampę sufitową w pokoju. Z sufitu wychodzi przewód z żyłami: czarną, brązową i żółto-zieloną. Nie ma niebieskiej.

<details><summary>Rozwiązanie</summary>

**Co to może znaczyć?** Najczęściej to obwód z łącznikiem świecznikowym ([06.02](modules/06-osprzet-instalacyjny/06.02-laczniki-jednobiegunowy-dwubiegunowy.md)): brązowa i czarna to dwie łączone fazy dla dwóch grup żarówek, a N… jest gdzie indziej albo go nie ma. Albo jest to stara instalacja, w której żółto-zielona pełni funkcję N lub PEN.

**Co zrobić?** Nie zgadywać. Wyłączyć obwód, sprawdzić, które żyły dochodzą do łącznika, a które do puszki rozgałęźnej. Po załączeniu zmierzyć napięcia między żyłami przy różnych położeniach łącznika. Jeśli żółto-zielona okazuje się N, instalacja wymaga poprawienia, a nie „dopasowania” lampy.

</details>

🧮 **[05.04](modules/05-przewody-i-kable/05.04-przekroj-i-obciazalnosc-pradowa.md#przykład)** · Przekrój i obciążalność prądowa

**Zadanie.** Trzy obwody gniazd (YDY 3×2,5) biegną obok siebie w jednej bruździe w tynku (sposób C). Każdy ma być zabezpieczony wyłącznikiem B16. Czy to dopuszczalne? A gdyby ta sama trójka biegła w ścianie z ociepleniem (sposób A1)?

<details><summary>Rozwiązanie</summary>

**Sposób C:**

$$I_z = 27\ \mathrm{A} \cdot 0{,}70 = 18{,}9\ \mathrm{A} \ge 16\ \mathrm{A}$$

Warunek In ≤ Iz spełniony.

**Sposób A1:**

$$I_z = 19{,}5\ \mathrm{A} \cdot 0{,}70 = 13{,}7\ \mathrm{A} < 16\ \mathrm{A}$$

Warunek niespełniony. Trzeba rozdzielić trasy, zastosować 4 mm² albo zmniejszyć zabezpieczenie (B13, o ile wystarczy dla odbiorników).

**Wniosek.** Ten sam przewód z tym samym wyłącznikiem może być poprawny albo nie — zależnie od tego, jak i z czym go ułożysz.

</details>

🧮 **[05.05](modules/05-przewody-i-kable/05.05-sposoby-ukladania-przewodow-a1-b1-c-e-i-ich.md#przykład)** · Sposoby układania przewodów (A1, B1, C, E…) i ich wpływ na obciążalność

**Zadanie.** Obwód gniazd w łazience na poddaszu: YDY 3×2,5, pierwsze 3 m w tynku (C), potem 4 m przez ocieploną ścianę kolankową w peszlu (A2: 18,5 A). Zabezpieczenie B16. Czy dobór jest poprawny?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Liczy się najgorszy odcinek, czyli A2:

$$I_z = 18{,}5\ \mathrm{A} \ge I_n = 16\ \mathrm{A}$$

Warunek jest spełniony, ale z niewielkim zapasem. Gdyby przewód leżał bezpośrednio w wełnie bez rurki na długości ponad 0,5 m, obciążalność mogłaby spaść do ok. 13,5 A (27 A × 0,5) i B16 byłby za duży.

</details>

🧮 **[05.06](modules/05-przewody-i-kable/05.06-przewody-bezhalogenowe-i-kable-ziemne.md#przykład)** · Przewody bezhalogenowe i kable ziemne

**Sytuacja.** Kolega zakopał w ogrodzie przewód YDY 3×2,5 na głębokości 30 cm do lampy przy furtce, bez rurki i bez folii. Po roku lampa zaczęła wybijać różnicówkę po deszczu.

<details><summary>Rozwiązanie</summary>

**Diagnoza.** Powłoka przewodu instalacyjnego nie jest przeznaczona do pracy w wilgotnym gruncie. Po roku nawilgła izolacja ma upływ, który przy deszczu przekracza próg różnicówki. Na płytko zakopanym przewodzie wystarczy też jeden ruch szpadla.

**Naprawa.** Wymiana na kabel ziemny (YKY 3×2,5 0,6/1 kV), ułożony na 0,7 m w piasku, z folią ostrzegawczą i rurą osłonową na wyjściu z ziemi.

</details>

🧮 **[05.07](modules/05-przewody-i-kable/05.07-miedz-a-aluminium.md#przykład)** · Miedź a aluminium

**Zadanie.** Stara instalacja: przewód aluminiowy 2,5 mm², długość obwodu 20 m. Nowa: przewód miedziany 2,5 mm² tej samej długości. Porównaj rezystancję pętli L–N (2 × 20 m).

<details><summary>Rozwiązanie</summary>

$$R_{Al} = \frac{0{,}0286 \cdot 40}{2{,}5} \approx 0{,}46\ \Omega \qquad R_{Cu} = \frac{0{,}0175 \cdot 40}{2{,}5} = 0{,}28\ \Omega$$

Przy prądzie 16 A moc tracona w przewodach: Al $16^2 \cdot 0{,}46 \approx 117\ \mathrm{W}$, Cu $16^2 \cdot 0{,}28 \approx 72\ \mathrm{W}$.

**Wniosek.** Aluminium grzeje się wyraźniej, a do tego dochodzą straty na każdym gorszym połączeniu. W puszce z kilkoma takimi stykami potrafi się zrobić naprawdę gorąco.

</details>

---

## 06 — Osprzęt instalacyjny

🧮 **[06.01](modules/06-osprzet-instalacyjny/06.01-gniazda-wtyczkowe-jednofazowe-z-bolcem.md#przykład)** · Gniazda wtyczkowe: jednofazowe, z bolcem ochronnym, trójfazowe

**Sytuacja.** W kuchni na jednym gnieździe podwójnym pracują czajnik 2,2 kW i mikrofalówka 1,2 kW. Gniazdo jest ciepłe w dotyku, a plastik wokół jednego otworu zmienił kolor.

<details><summary>Rozwiązanie</summary>

**Obliczenie.**

$$I = \frac{2200 + 1200}{230} \approx 14{,}8\ \mathrm{A}$$

To mieści się w 16 A gniazda i nie wyłącza B16. Gniazdo nie powinno się grzać. Jeśli się grzeje, przyczyną jest **połączenie**: luźny zacisk, zużyte sprężyny styków albo wypalona miedź.

**Co zrobić.** Wymienić gniazdo, sprawdzić stan żył (obciąć przegrzane końce). Na przyszłość rozdzielić mocne odbiorniki kuchenne na osobne obwody ([moduł 16](modules/16-planowanie-obwodow/README.md)).

</details>

🔎 **[06.02](modules/06-osprzet-instalacyjny/06.02-laczniki-jednobiegunowy-dwubiegunowy.md#przykład)** · Łączniki: jednobiegunowy, dwubiegunowy, świecznikowy, schodowy, krzyżowy

**Sytuacja.** Po wymianie łączników w korytarzu światło zapala się z dolnego łącznika tylko wtedy, gdy górny jest w jednym położeniu.

<details><summary>Rozwiązanie</summary>

**Diagnoza.** W jednym z łączników schodowych na zacisku wspólnym jest żyła korespondencyjna, a na zacisku korespondencyjnym — zasilanie (albo przewód do lampy). Taki łącznik nie przełącza między korespondencjami, tylko przerywa jedną z nich.

**Naprawa.** Wyłączyć obwód. W puszce przy łączniku znaleźć żyłę zasilającą (dolny łącznik) lub żyłę do lampy (górny łącznik) i podłączyć ją na zacisk wspólny. Dwie pozostałe żyły to korespondencja.

</details>

🔎 **[06.03](modules/06-osprzet-instalacyjny/06.03-puszki-instalacyjne-i-rozgalezne.md#przykład)** · Puszki instalacyjne i rozgałęźne

**Sytuacja.** Po remoncie łazienki przestały działać dwa gniazda w przedpokoju. Elektryk znajduje przewód przerwany… nigdzie, bo wszystko jest pod płytkami i tynkiem.

<details><summary>Rozwiązanie</summary>

**Prawdopodobna przyczyna.** Puszka rozgałęźna, przez którą szło zasilanie gniazd w przedpokoju, została zakryta płytkami. Przy wierceniu albo przez wilgoć połączenie w niej się rozłączyło.

**Lekcja.** Puszki rozgałęźne muszą zostać dostępne. Jeśli przeszkadzają w projekcie, połączenia przenosi się do puszek osprzętowych albo w miejsce, które zostanie dostępne. Przy remoncie dobrze jest mieć zdjęcia ścian z naniesionymi trasami.

</details>

🧮 **[06.04](modules/06-osprzet-instalacyjny/06.04-zlaczki-i-laczenie-przewodow-dlaczego-nie.md#przykład)** · Złączki i łączenie przewodów — dlaczego nie skręcamy

**Zadanie.** W puszce jest skrętka, która ma rezystancję styku 0,05 Ω. Obwód zasila grzejnik olejowy 2 kW. Ile mocy grzeje samą skrętkę?

<details><summary>Rozwiązanie</summary>

$$I = \frac{2000}{230} \approx 8{,}7\ \mathrm{A} \qquad P = I^2 \cdot R = 8{,}7^2 \cdot 0{,}05 \approx 3{,}8\ \mathrm{W}$$

Wygląda niewiele, ale to moc skupiona w punkcie o wielkości ziarenka ryżu, zamkniętym w puszce bez chłodzenia. Gdy rezystancja wzrośnie dziesięciokrotnie (utlenienie), moc rośnie do ok. 38 W — tyle co lutownica.

**Wniosek.** Dobre połączenie ma rezystancję rzędu miliomów i grzeje się niezauważalnie. Złe może grzać jak lutownica, a zabezpieczenie nadprądowe go nie wykryje, bo prąd w obwodzie jest normalny.

</details>

🔎 **[06.05](modules/06-osprzet-instalacyjny/06.05-stopnie-ochrony-ip.md#przykład)** · Stopnie ochrony IP

**Zadanie.** Dobierz minimalny stopień ochrony oprawy:

<details><summary>Rozwiązanie</summary>

1. nad lustrem w łazience, w strefie 2,
2. pod daszkiem nad wejściem do domu,
3. w myjni samochodowej w garażu, myta myjką ciśnieniową.

**Rozwiązanie.**

1. **IPX4** — strefa 2 łazienki.
2. **IP44** — deszcz i bryzgi, owady i pył (pierwsza cyfra 4 chroni przed drobnymi owadami wchodzącymi do oprawy).
3. Co najmniej **IPX5**, a przy myciu wysokociśnieniowym oprawa o stopniu odpowiednim do strumienia (np. IP65, IP66 lub IPX9K według producenta).

</details>

🔎 **[06.06](modules/06-osprzet-instalacyjny/06.06-klasy-ochronnosci-urzadzen-0-i-ii-iii.md#przykład)** · Klasy ochronności urządzeń: 0, I, II, III

**Sytuacja.** W starym mieszkaniu z instalacją dwuprzewodową (L i N, bez PE) lokator chce podłączyć nową pralkę (klasa I) w łazience.

<details><summary>Rozwiązanie</summary>

**Ocena.** Pralka klasy I bez PE nie ma ochrony przy uszkodzeniu. W łazience (mokro, przewodzące podłoże) to sytuacja szczególnie groźna.

**Rozwiązanie.** Doprowadzić do gniazda pralki przewód z żyłą PE z rozdzielnicy i objąć obwód ochroną różnicowoprądową 30 mA ([moduł 21](modules/21-stare-instalacje/README.md), [moduł 17](modules/17-pomieszczenia-szczegolne/README.md)). Różnicówka w instalacji bez PE to tylko część rozwiązania — wyłączy dopiero wtedy, gdy prąd popłynie przez człowieka.

</details>

---

## 07 — Zabezpieczenia nadprądowe

🧮 **[07.01](modules/07-zabezpieczenia-nadpradowe/07.01-przeciazenie-i-zwarcie-z-punktu-widzenia.md#przykład)** · Przeciążenie i zwarcie z punktu widzenia zabezpieczenia

**Zadanie.** Zmierzona impedancja pętli zwarcia w gnieździe wynosi 0,8 Ω. Jaki prąd popłynie przy zwarciu L–PE w tym gnieździe i który wyzwalacz B16 zadziała?

<details><summary>Rozwiązanie</summary>

$$I_k = \frac{230\ \mathrm{V}}{0{,}8\ \Omega} \approx 290\ \mathrm{A}$$

To ok. 18 × In. Próg zadziałania natychmiastowego B16 to 3–5 × In (48–80 A), więc zadziała wyzwalacz elektromagnetyczny w czasie rzędu milisekund.

**Wniosek.** Gdyby impedancja wynosiła 4 Ω, prąd zwarcia miałby tylko 57 A. To mniej niż gwarantowane 80 A, więc wyzwalacz elektromagnetyczny mógłby nie zadziałać, a termiczny wyłączyłby po kilku sekundach. Ochrona przeciwporażeniowa nie byłaby skuteczna.

</details>

🧮 **[07.02](modules/07-zabezpieczenia-nadpradowe/07.02-bezpieczniki-topikowe-wkladki-gg-gwintowe-i.md#przykład)** · Bezpieczniki topikowe: wkładki gG, gwintowe i przemysłowe

**Zadanie.** Przewód o obciążalności Iz = 27 A (2,5 mm², sposób C). Jaką największą wkładkę gG można zastosować, żeby chroniła przewód przed przeciążeniem?

<details><summary>Rozwiązanie</summary>

Warunek: $I_2 \le 1{,}45 \cdot I_z$, a dla gG $I_2 = 1{,}6 \cdot I_n$:

$$1{,}6 \cdot I_n \le 1{,}45 \cdot 27 \Rightarrow I_n \le 24{,}5\ \mathrm{A}$$

**Odpowiedź.** gG 20 A. Wkładka 25 A nie spełnia warunku, choć 25 < 27. Ten sam przewód z wyłącznikiem nadprądowym może mieć B25 ([07.06](modules/07-zabezpieczenia-nadpradowe/07.06-koordynacja-zabezpieczenia-z-przewodem.md)).

</details>

🧮 **[07.03](modules/07-zabezpieczenia-nadpradowe/07.03-wylacznik-nadpradowy-budowa-i-dwa-wyzwalacze.md#przykład)** · Wyłącznik nadprądowy — budowa i dwa wyzwalacze

**Sytuacja.** Wyłącznik B16 obwodu kuchennego wyłącza się po 20–30 minutach pracy piekarnika (2,5 kW) i zmywarki (2 kW). Po kilku minutach daje się załączyć ponownie.

<details><summary>Rozwiązanie</summary>

**Obliczenie.**

$$I = \frac{4500}{230} \approx 19{,}6\ \mathrm{A} \approx 1{,}22 \cdot I_n$$

To przeciążenie. 1,22 × In leży między 1,13 a 1,45, więc wyłącznik może zadziałać po kilkunastu–kilkudziesięciu minutach. Właśnie to się dzieje. Po wyłączeniu bimetal stygnie i pozwala załączyć.

**Wniosek.** Wyłącznik działa prawidłowo i chroni przewód. Rozwiązaniem jest rozdzielenie odbiorników na dwa obwody, a nie większy wyłącznik.

</details>

🧮 **[07.04](modules/07-zabezpieczenia-nadpradowe/07.04-charakterystyki-b-c-i-d.md#przykład)** · Charakterystyki B, C i D

**Zadanie.** Obwód zasila sprężarkę o prądzie znamionowym 8 A i prądzie rozruchowym 6 × In silnika (48 A). Czy B10 wystarczy? A C10?

<details><summary>Rozwiązanie</summary>

**B10:** próg natychmiastowy 30–50 A. Rozruch 48 A leży w paśmie, więc B10 może wyłączać przy części rozruchów.

**C10:** próg 50–100 A. Rozruch 48 A jest poniżej progu, więc wyłącznik nie zadziała przy rozruchu.

**Wniosek.** C10, pod warunkiem że impedancja pętli w gnieździe sprężarki ≤ 230 / 100 = 2,3 Ω. Jeśli jest większa, trzeba zwiększyć przekrój albo zastosować różnicówkę jako ochronę przy uszkodzeniu ([moduł 12](modules/12-ochrona-przeciwporazeniowa/README.md)).

</details>

🧮 **[07.05](modules/07-zabezpieczenia-nadpradowe/07.05-zdolnosc-zwarciowa-6-ka-10-ka.md#przykład)** · Zdolność zwarciowa: 6 kA, 10 kA

**Zadanie.** W rozdzielnicy domu jednorodzinnego zmierzono impedancję pętli L–PE 0,35 Ω. Czy wystarczą wyłączniki 6 kA?

<details><summary>Rozwiązanie</summary>

$$I_k = \frac{230}{0{,}35} \approx 660\ \mathrm{A}$$

660 A ≪ 6000 A. Wyłączniki 6 kA wystarczą z dużym zapasem.

**Dla porównania:** rozdzielnica w budynku przy stacji, $Z_s$ = 0,03 Ω → $I_k$ ≈ 7,7 kA. Wyłączniki 6 kA nie wystarczą — potrzebne 10 kA albo ochrona wsteczna z tabel producenta.

</details>

🧮 **[07.06](modules/07-zabezpieczenia-nadpradowe/07.06-koordynacja-zabezpieczenia-z-przewodem.md#przykład)** · Koordynacja zabezpieczenia z przewodem

**Zadanie.** Obwód gniazd w kuchni: czajnik 2,2 kW i ekspres 1,3 kW mogą pracować jednocześnie. Przewód YDY 3×2,5 w tynku (C), obok jeszcze jeden obwód (2 obwody, k₂ = 0,80). Dobierz wyłącznik.

<details><summary>Rozwiązanie</summary>

1. $I_B = 3500 / 230 \approx 15{,}2\ \mathrm{A}$.
2. $I_z = 27 \cdot 0{,}80 = 21{,}6\ \mathrm{A}$.
3. Wyłącznik: In ≥ 15,2 A i In ≤ 21,6 A → **B16** (albo B20).
4. Warunek 2: $1{,}45 \cdot 16 = 23{,}2 \le 1{,}45 \cdot 21{,}6 = 31{,}3$ — spełniony.

**Wniosek.** B16. B20 też spełnia oba warunki, ale zostawia mniejszy zapas dla przewodu i przy kolejnym dołożonym obwodzie w bruździe przestanie je spełniać. Przy prądzie 15,2 A B16 pracuje blisko granicy — lepiej rozdzielić odbiorniki kuchenne na dwa obwody.

</details>

🧮 **[07.07](modules/07-zabezpieczenia-nadpradowe/07.07-selektywnosc-zabezpieczen.md#przykład)** · Selektywność zabezpieczeń

**Zadanie.** Wkładki gG w rozdzielnicy budynku: 63 A na wlz, 25 A przedlicznikowe w mieszkaniu, potem wyłączniki B10 i B16. Czy wkładki 63 A i 25 A są wzajemnie selektywne? A gdyby przedlicznikowa miała 50 A?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** 63 / 25 = 2,52 ≥ 1,6 — selektywne. 63 / 50 = 1,26 < 1,6 — selektywność niezapewniona: przy zwarciu w mieszkaniu może się przepalić wkładka wlz i zgasną inne mieszkania.

</details>

---

## 08 — Wyłączniki różnicowoprądowe

🧮 **[08.01](modules/08-wylaczniki-roznicowopradowe/08.01-zasada-dzialania-wylacznika-roznicowopradowego.md#przykład)** · Zasada działania wyłącznika różnicowoprądowego

**Zadanie.** Pralka ma uszkodzoną grzałkę: z fazy do obudowy (z PE) płynie 40 mA. Ile wynosi prąd w L i w N, jeśli pralka pobiera 9 A? Co zrobi różnicówka 30 mA?

<details><summary>Rozwiązanie</summary>

- $I_L = 9{,}000 + 0{,}040 = 9{,}040\ \mathrm{A}$
- $I_N = 9{,}000\ \mathrm{A}$
- $I_\Delta = I_L - I_N = 40\ \mathrm{mA} \ge I_{\Delta n} = 30\ \mathrm{mA}$

**Wynik.** Różnicówka wyłączy, i to w czasie poniżej 300 ms. Wyłącznik nadprądowy B16 nie widzi żadnej różnicy: 9,04 A to dla niego normalna praca.

</details>

🧮 **[08.02](modules/08-wylaczniki-roznicowopradowe/08.02-prad-roznicowy-znamionowy-30-ma-100-ma-300-ma.md#przykład)** · Prąd różnicowy znamionowy: 30 mA, 100 mA, 300 mA

**Zadanie.** Dom w układzie TT, rezystancja uziomu 120 Ω. Czy różnicówka 300 mA zapewni ochronę przy uszkodzeniu? A 30 mA?

<details><summary>Rozwiązanie</summary>

**300 mA:** $120 \cdot 0{,}3 = 36\ \mathrm{V} \le 50\ \mathrm{V}$ — spełnione.

**30 mA:** $120 \cdot 0{,}03 = 3{,}6\ \mathrm{V}$ — spełnione z dużym zapasem.

**Wniosek.** Obie spełniają warunek ochrony przy uszkodzeniu, ale ochronę uzupełniającą ludzi (gniazda, oświetlenie) zapewni tylko 30 mA. Typowe rozwiązanie: 300 mA S na początku, 30 mA na obwodach odbiorczych.

</details>

🧮 **[08.03](modules/08-wylaczniki-roznicowopradowe/08.03-typy-ac-a-f-i-b-ktory-do-czego.md#przykład)** · Typy AC, A, F i B — który do czego

**Sytuacja.** W domu jest jedna różnicówka 40 A / 30 mA typu AC. Właściciel montuje pompę ciepła z trójfazowym falownikiem, której instrukcja wymaga RCD typu B.

<details><summary>Rozwiązanie</summary>

**Ocena.** Pompy nie wolno podłączyć za istniejącym RCD AC. Prąd stały upływu z falownika mógłby nasycić rdzeń AC i wyłączyć ochronę różnicową dla całego domu.

**Rozwiązanie.** Osobny obwód pompy z własnym RCD typu B, zasilany przed RCD AC (równolegle, nie za nim). Pozostałe obwody — przy okazji wymiana RCD AC na typ A.

</details>

🧮 **[08.04](modules/08-wylaczniki-roznicowopradowe/08.04-rcbo-wylacznik-nadpradowy-z-czlonem.md#przykład)** · RCBO — wyłącznik nadprądowy z członem różnicowoprądowym

**Zadanie.** Lodówka i zamrażarka w kuchni są na wspólnej różnicówce z gniazdami kuchennymi i oświetleniem. W czasie urlopu czajnik z zawilgoconą grzałką, zostawiony w gnieździe, wybił różnicówkę i jedzenie się rozmroziło. Jak to zmienić?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Wydzielić osobny obwód dla lodówki i zamrażarki zabezpieczony RCBO B16 / 30 mA typu A. Zadziałanie różnicówki gniazd kuchennych nie odetnie wtedy chłodzenia.

</details>

🔎 **[08.05](modules/08-wylaczniki-roznicowopradowe/08.05-przycisk-test-i-okresowe-sprawdzanie.md#przykład)** · Przycisk TEST i okresowe sprawdzanie

**Sytuacja.** Podczas pomiarów okresowych miernik pokazuje dla RCD 30 mA: prąd zadziałania 27 mA, czas przy IΔn 420 ms.

<details><summary>Rozwiązanie</summary>

**Ocena.** Prąd zadziałania jest w zakresie 15–30 mA, ale czas 420 ms przekracza 300 ms dopuszczalne dla RCD ogólnego typu. Aparat działa za wolno.

**Działanie.** Sprawdzić, czy to na pewno RCD ogólnego typu (nie S). Jeśli tak — do wymiany. Wpisać wynik negatywny do protokołu.

</details>

🔎 **[08.06](modules/08-wylaczniki-roznicowopradowe/08.06-dlaczego-roznicowka-wybija-przyczyny-i-szukanie.md#przykład)** · Dlaczego różnicówka wybija — przyczyny i szukanie winnego

**Sytuacja.** RCD w mieszkaniu wybija mniej więcej raz na tydzień, losowo. Nie ma związku z deszczem. Za tym RCD jest: biuro domowe (2 komputery, 2 monitory, drukarka, router), salon (telewizor, soundbar, konsola, dekoder) i oświetlenie LED w trzech pokojach.

<details><summary>Rozwiązanie</summary>

**Oszacowanie upływu.** Kilkanaście urządzeń z zasilaczami impulsowymi, po ok. 0,5–1,5 mA każde — razem ok. 10–15 mA. To 30–50 % IΔn, czyli powyżej zalecanego 0,3 IΔn. Chwilowe impulsy przy włączaniu urządzeń albo przepięcia w sieci dokładają resztę.

**Rozwiązanie.** Podzielić obwody biura i salonu między dwie różnicówki (albo RCBO), sprawdzić rezystancję izolacji obwodów i działanie ochrony przeciwprzepięciowej. Ewentualnie RCD typu A o zwiększonej odporności na zakłócenia.

</details>

🧮 **[08.07](modules/08-wylaczniki-roznicowopradowe/08.07-podzial-obwodow-miedzy-wylaczniki.md#przykład)** · Podział obwodów między wyłączniki różnicowoprądowe

**Zadanie.** Dom jednorodzinny: obwody oświetlenia parteru i piętra, gniazda w 6 pomieszczeniach, kuchnia (2 obwody gniazd), łazienka, pralka, lodówka, kotłownia, gniazda zewnętrzne. Zaproponuj podział na RCD.

<details><summary>Rozwiązanie</summary>

**Propozycja:**

- **RCD 1 (40 A / 30 mA, A):** oświetlenie parteru, gniazda pokoi na piętrze, gniazda łazienki.
- **RCD 2 (40 A / 30 mA, A):** oświetlenie piętra, gniazda pokoi na parterze, kuchnia — obwód 1.
- **RCD 3 (40 A / 30 mA, A):** kuchnia — obwód 2, kotłownia, oświetlenie zewnętrzne.
- **RCBO:** pralka; lodówka; gniazda zewnętrzne (często mokre — niech nie wyłączają niczego innego).

Sprawdzenie: w każdym pomieszczeniu światło i gniazda są pod różnymi aparatami, a urządzenia krytyczne i obwody narażone na wilgoć mają własne RCBO.

</details>

---

## 09 — Ochrona przeciwprzepięciowa

🔎 **[09.01](modules/09-ochrona-przeciwprzepieciowa/09.01-skad-biora-sie-przepiecia.md#przykład)** · Skąd biorą się przepięcia

**Sytuacja.** Dom na wsi zasilany linią napowietrzną. Po burzy, w czasie której nie było widać uderzenia w dom, przestały działać: sterownik pieca, router i brama wjazdowa. Bezpieczniki i różnicówki nie zadziałały.

<details><summary>Rozwiązanie</summary>

**Wyjaśnienie.** Uderzenie w pobliżu linii lub w samą linię wywołało falę przepięciową w przewodach zasilających (źródło 2) i indukowało napięcia w długich przewodach do bramy (źródło 3). Impuls trwał mikrosekundy — za krótko dla zabezpieczeń nadprądowych. Najbardziej podatne były urządzenia z elektroniką i długimi przewodami sygnałowymi.

**Wniosek.** Taki dom potrzebuje ograniczników przepięć w rozdzielnicy (przy linii napowietrznej — typu 1+2), a długie przewody zewnętrzne — ochrony na obu końcach ([09.04](modules/09-ochrona-przeciwprzepieciowa/09.04-montaz-ogranicznika-dlugosc-polaczen-i.md)).

</details>

🧮 **[09.02](modules/09-ochrona-przeciwprzepieciowa/09.02-kategorie-wytrzymalosci-udarowej-iiv.md#przykład)** · Kategorie wytrzymałości udarowej I–IV

**Zadanie.** W rozdzielnicy domu jest SPD typu 2 o $U_P$ = 1,5 kV, połączony przewodami o łącznej długości 0,5 m. Sterownik pieca (kategoria I, 1,5 kV) jest 25 m dalej. Czy jest chroniony?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Napięcie na zaciskach instalacji przy SPD: ok. $1{,}5 + 0{,}5 \cdot 1 = 2{,}0\ \mathrm{kV}$. To mniej niż 2,5 kV — odbiorniki kategorii II w pobliżu rozdzielnicy są chronione. Sterownik kategorii I (1,5 kV) — nie. Do tego jest dalej niż ok. 10 m od SPD, więc przepięcie na końcu przewodu może być jeszcze wyższe.

**Wniosek.** Przy sterowniku potrzebny jest SPD typu 3 (np. moduł w puszce lub gniazdo z ochroną).

</details>

🧮 **[09.03](modules/09-ochrona-przeciwprzepieciowa/09.03-ograniczniki-przepiec-typu-1-2-i-3.md#przykład)** · Ograniczniki przepięć typu 1, 2 i 3

**Zadanie.** Odczytaj parametry ogranicznika: „T2, Uc 275 V, Up ≤ 1,3 kV, In 20 kA, Imax 40 kA, 3+1”. Czy nadaje się do domu w układzie TN-S, bez instalacji odgromowej, zasilanego kablem?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.**

- T2 — przepięcia indukowane i łączeniowe; budynek bez instalacji odgromowej i z zasilaniem kablowym — typ 2 wystarcza.
- $U_C$ = 275 V ≥ 253 V — poprawne dla sieci 230 V.
- $U_P$ ≤ 1,3 kV — z przewodami ≤ 0,5 m ok. 1,8 kV, poniżej 2,5 kV — chroni odbiorniki kategorii II.
- $I_n$ = 20 kA ≥ 5 kA — z zapasem.
- 3+1 — poprawny układ dla TN-S i do montażu przed różnicówką ([09.04](modules/09-ochrona-przeciwprzepieciowa/09.04-montaz-ogranicznika-dlugosc-polaczen-i.md)).

**Wniosek.** Nadaje się.

</details>

🧮 **[09.04](modules/09-ochrona-przeciwprzepieciowa/09.04-montaz-ogranicznika-dlugosc-polaczen-i.md#przykład)** · Montaż ogranicznika: długość połączeń i zabezpieczenie

**Zadanie.** SPD typu 2 o $U_P$ = 1,3 kV podłączono przewodem 0,6 m do fazy i 0,9 m do szyny PE. Jakie napięcie dostanie instalacja przy udarze? Co poprawić?

<details><summary>Rozwiązanie</summary>

$$U \approx U_P + (a + b) \cdot 1\ \mathrm{kV/m} = 1{,}3 + 1{,}5 = 2{,}8\ \mathrm{kV}$$

To więcej niż 2,5 kV dla odbiorników kategorii II — ochrona jest nieskuteczna.

**Poprawka.** Przenieść SPD bliżej szyny PE i wprowadzić fazy z grzebienia lub połączeniem „V”. Przy a + b = 0,4 m: $1{,}3 + 0{,}4 = 1{,}7\ \mathrm{kV}$.

</details>

🧮 **[09.05](modules/09-ochrona-przeciwprzepieciowa/09.05-ochrona-odgromowa-budynku-podstawy.md#przykład)** · Ochrona odgromowa budynku — podstawy

**Zadanie.** Dom jednorodzinny o obwodzie ścian 48 m, instalacja odgromowa klasy III. Ile przewodów odprowadzających trzeba przewidzieć?

<details><summary>Rozwiązanie</summary>

$$n = \frac{48\ \mathrm{m}}{15\ \mathrm{m}} = 3{,}2 \Rightarrow 4$$

Przewody rozmieszcza się możliwie równomiernie, zwykle w narożnikach, przy czym norma wymaga co najmniej dwóch.

**Wniosek.** Cztery przewody odprowadzające w narożnikach budynku, każdy ze złączem kontrolnym, połączone z uziomem otokowym.

</details>

---

## 10 — Aparatura modułowa

🔎 **[10.01](modules/10-aparatura-modulowa/10.01-rozlacznik-izolacyjny-wylacznik-glowny.md#przykład)** · Rozłącznik izolacyjny — wyłącznik główny

**Sytuacja.** Elektryk ma wymienić wyłącznik nadprądowy w rozdzielnicy mieszkania. Wyłącza rozłącznik główny, ale nie sprawdza braku napięcia, bo „przecież wszystko zgasło”.

<details><summary>Rozwiązanie</summary>

**Co mogło pójść źle?** Rozłącznik mógł być podłączony odwrotnie (zasilanie na dolnych zaciskach), mógł mieć sklejony styk w jednym biegunie albo w rozdzielnicy mógł być obwód zasilany sprzed rozłącznika (np. dzwonek, SPD, osobny podlicznik). Bez sprawdzenia braku napięcia każda z tych sytuacji kończy się dotknięciem części pod napięciem.

**Wniosek.** Wyłączenie rozłącznika to dopiero pierwszy krok. Kolejne: zabezpieczenie przed załączeniem i sprawdzenie braku napięcia na każdym przewodzie, którego się dotyka.

</details>

🧮 **[10.02](modules/10-aparatura-modulowa/10.02-stycznik-modulowy-i-przekaznik-bistabilny.md#przykład)** · Stycznik modułowy i przekaźnik bistabilny

**Zadanie.** Podgrzewacz wody 2 kW ma się włączać tylko w taryfie nocnej. Masz zegar sterujący ze stykiem 16 A i stycznik 25 A. Jak to połączyć?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.**

1. Obwód główny: wyłącznik B16 → styk stycznika (1–2) → podgrzewacz → N. Prąd $2000/230 \approx 8{,}7$ A — styk 25 A ma duży zapas.
2. Obwód sterowania: faza (np. z tego samego B16) → styk zegara → A1 cewki → A2 → N.
3. Zegar ustawiony na godziny taryfy nocnej. Stycznik przejmuje prąd grzałki, a styk zegara przełącza tylko cewkę.

**Dlaczego nie bezpośrednio przez zegar?** Styk zegara 16 A by wystarczył, ale przy codziennym łączeniu grzałki zużywa się szybciej, a jego wymiana jest droższa. Stycznik jest tańszy i łatwiej wymienialny. Przy większych mocach (np. 3 × 3 kW) zegar w ogóle nie dałby rady.

</details>

🔎 **[10.03](modules/10-aparatura-modulowa/10.03-programatory-czasowe-i-wylaczniki-zmierzchowe.md#przykład)** · Programatory czasowe i wyłączniki zmierzchowe

**Zadanie.** Oświetlenie ogrodu: 12 opraw LED po 10 W. Ma się zapalać o zmierzchu i gasnąć o 23:00. Jak to zrobić?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Wyłącznik zmierzchowy (zapala) i zegar (wyłącza) połączone szeregowo w obwodzie cewki stycznika albo jeden zegar astronomiczny z programem „zachód słońca – 23:00”. Moc 120 W to mało, ale 12 zasilaczy LED ma duży prąd załączania, więc sprawdź, czy styk zegara jest do tego przeznaczony, albo daj stycznik z oznaczeniem do LED.

</details>

🔎 **[10.04](modules/10-aparatura-modulowa/10.04-kontrolki-faz-przekazniki-zaniku-fazy-i.md#przykład)** · Kontrolki faz, przekaźniki zaniku fazy i ograniczniki mocy

**Sytuacja.** W domu jednocześnie przepaliły się zasilacze telewizora i routera (na L1), a lodówka i lampy na L3 działały słabo. Licznik i bezpieczniki są w porządku.

<details><summary>Rozwiązanie</summary>

**Diagnoza.** Objawy typowe dla przerwy w przewodzie PEN (lub N) przed punktem podziału: na mało obciążonej fazie napięcie wzrosło do ok. 300–400 V, a na mocno obciążonej spadło. Pomiar: napięcia L–N bardzo różne, napięcie N–PE kilkadziesiąt–kilkaset woltów.

**Działanie.** Wyłączyć zasilanie, zgłosić awarię operatorowi sieci (przerwa PEN w sieci lub złączu to jego obszar), sprawdzić połączenia PEN w złączu i rozdzielnicy. Na przyszłość: przekaźnik napięciowy wyłączający wrażliwe obwody.

</details>

🔎 **[10.05](modules/10-aparatura-modulowa/10.05-detektory-iskrzenia-afdd.md#przykład)** · Detektory iskrzenia AFDD

**Sytuacja.** W sypialni z gniazdem za łóżkiem AFDD wyłącza obwód raz na kilka dni, zawsze wieczorem. Odbiorniki: lampka nocna i ładowarka telefonu, razem kilkanaście watów.

<details><summary>Rozwiązanie</summary>

**Diagnoza.** Przy tak małym prądzie przeciążenie nie wchodzi w grę. Wskaźnik na AFDD pokazuje łuk szeregowy. Przy oględzinach okazuje się, że przedłużacz za łóżkiem jest przygnieciony nogą łóżka i jedna żyła jest w środku prawie przerwana. Wieczorem, przy przesuwaniu łóżka, żyła iskrzy.

**Wniosek.** Bez AFDD przedłużacz iskrzyłby dalej, nagrzewając izolację tuż przy materacu. Przedłużacz do wymiany.

</details>

🧮 **[10.06](modules/10-aparatura-modulowa/10.06-podliczniki-energii.md#przykład)** · Podliczniki energii

**Zadanie.** Tarcza starego licznika o stałej C = 375 obr/kWh wykonała 25 obrotów w ciągu 60 s. Jaka jest moc pobierana przez instalację?

<details><summary>Rozwiązanie</summary>

$$P = \frac{3600 \cdot n}{C \cdot t} = \frac{3600 \cdot 25}{375 \cdot 60} = 4\ \mathrm{kW}$$

**Sprawdzenie sensu.** 25 obrotów to $25/375 \approx 0{,}067$ kWh w ciągu minuty, a w ciągu godziny 60 razy więcej, czyli 4 kWh — średnio 4 kW. Ta sama metoda działa z diodą licznika elektronicznego: liczysz mignięcia zamiast obrotów.

</details>

---

## 11 — Układy sieci: TN, TT, IT

🔎 **[11.01](modules/11-uklady-sieci/11.01-co-oznaczaja-litery-w-nazwie-ukladu-sieci.md#przykład)** · Co oznaczają litery w nazwie układu sieci

**Zadanie.** Odczytaj układ: źródło uziemione, obudowy połączone z punktem neutralnym, do budynku przychodzą cztery przewody L1, L2, L3, PEN, a w rozdzielnicy głównej PEN jest rozdzielony na N i PE.

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Źródło uziemione → T. Obudowy przez przewód do punktu neutralnego → N. Do budynku PEN, potem osobno → C-S. Układ **TN-C-S**.

</details>

🔎 **[11.02](modules/11-uklady-sieci/11.02-uklad-tn-c.md#przykład)** · Układ TN-C

**Sytuacja.** W starym bloku w obwodzie dwuprzewodowym poluzowało się połączenie N (PEN) w puszce. W gnieździe za puszką bolec jest połączony z N. Podłączona jest pralka (klasa I, 2 kW).

<details><summary>Rozwiązanie</summary>

**Co się dzieje?** Za przerwą przewód N gniazda nie jest już połączony z punktem neutralnym. Przez grzałkę pralki łączy się z fazą. Bolec gniazda, a więc obudowa pralki, ma prawie 230 V względem ziemi. Pralka nie pracuje (nie ma obwodu), ale jej obudowa jest „pod prądem”. Dotknięcie obudowy i kranu — porażenie. Zabezpieczenie nie zadziała, bo nie ma zwarcia.

**Wniosek.** Właśnie dlatego w nowych instalacjach PE jest osobnym przewodem, a w starych mostek bolec–N jest jednym z najgroźniejszych rozwiązań.

</details>

🔎 **[11.03](modules/11-uklady-sieci/11.03-uklad-tn-s.md#przykład)** · Układ TN-S

**Zadanie.** Garaż zasilany z domu przewodem 5-żyłowym. W rozdzielnicy garażu elektryk połączył N i PE na jednej szynie „dla pewności”. Co się stanie?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Od tego miejsca prąd roboczy obwodów garażu płynie częściowo przez PE do domu. Różnicówka w domu chroniąca obwód garażu zobaczy różnicę prądów i będzie wybijać przy obciążeniu. Jeśli różnicówka jest w garażu za tym mostkiem — będzie działać, ale prąd N popłynie przez PE i wszystkie metalowe elementy połączone z PE w domu. To błąd: N i PE muszą być na osobnych szynach.

</details>

🧮 **[11.04](modules/11-uklady-sieci/11.04-uklad-tn-c-s-i-punkt-rozdzialu-pen.md#przykład)** · Układ TN-C-S i punkt rozdziału PEN

**Zadanie.** Dom: PEN rozdzielony w złączu. W rozdzielnicy głównej domu są osobne szyny N i PE. Do rozdzielnicy w garażu idzie przewód 5×4. Czy w garażu wolno połączyć N i PE?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Nie. Punkt podziału jest jeden — w złączu. Od niego w całej instalacji N i PE są rozdzielone. W rozdzielnicy garażu N i PE na osobnych szynach, a PE garażu można dodatkowo połączyć z lokalnym uziomem i połączeniami wyrównawczymi garażu ([moduł 13](modules/13-uziemienia-i-wyrownanie/README.md)).

</details>

🧮 **[11.05](modules/11-uklady-sieci/11.05-uklad-tt.md#przykład)** · Układ TT

**Zadanie.** Dom w układzie TT, zmierzona rezystancja uziomu $R_A$ = 95 Ω. Obwody gniazd za RCD 30 mA, a obwód pompy w studni — za RCD 300 mA. Czy warunek ochrony jest spełniony?

<details><summary>Rozwiązanie</summary>

- RCD 30 mA: $95 \cdot 0{,}03 = 2{,}85\ \mathrm{V} \le 50\ \mathrm{V}$ — tak.
- RCD 300 mA: $95 \cdot 0{,}3 = 28{,}5\ \mathrm{V} \le 50\ \mathrm{V}$ — tak.

**Uwaga.** Pompa w studni to urządzenie w miejscu wilgotnym — ochrona uzupełniająca 30 mA byłaby lepsza ([moduł 17](modules/17-pomieszczenia-szczegolne/README.md)).

</details>

🔎 **[11.06](modules/11-uklady-sieci/11.06-uklad-it.md#przykład)** · Układ IT

**Sytuacja.** Na sali operacyjnej zapala się lampka i słychać sygnał kontroli izolacji. Trwa zabieg.

<details><summary>Rozwiązanie</summary>

**Co to znaczy?** Rezystancja izolacji sieci IT spadła poniżej progu — prawdopodobnie jedno z urządzeń ma doziemienie. Zasilanie działa, zabieg może trwać. Sygnał akustyczny można wyciszyć, ale służba techniczna musi zlokalizować uszkodzenie (np. odłączając kolejno urządzenia po zabiegu) i usunąć je, zanim wystąpi drugie.

</details>

---

## 12 — Ochrona przeciwporażeniowa

🔎 **[12.01](modules/12-ochrona-przeciwporazeniowa/12.01-ochrona-podstawowa-izolacja-obudowy-przegrody.md#przykład)** · Ochrona podstawowa: izolacja, obudowy, przegrody

**Sytuacja.** W rozdzielnicy mieszkaniowej po wymianie aparatów zostały trzy puste miejsca na szynie, nieosłonięte. Maskownica jest założona.

<details><summary>Rozwiązanie</summary>

**Ocena.** Przez puste miejsca w maskownicy można sięgnąć palcem do szyny grzebieniowej lub zacisków sąsiednich aparatów. Stopień ochrony spada poniżej IP2X — ochrona podstawowa jest niewystarczająca.

**Naprawa.** Zaślepki w puste miejsca maskownicy. Kosztują grosze.

</details>

🧮 **[12.02](modules/12-ochrona-przeciwporazeniowa/12.02-ochrona-przy-uszkodzeniu-samoczynne-wylaczenie.md#przykład)** · Ochrona przy uszkodzeniu: samoczynne wyłączenie zasilania

**Sytuacja.** W piekarniku (klasa I) przetarł się przewód wewnątrz i faza dotyka obudowy. Obwód: TN-C-S, B16, impedancja pętli 0,9 Ω.

<details><summary>Rozwiązanie</summary>

**Co się dzieje?** Prąd zwarcia $230 / 0{,}9 \approx 255\ \mathrm{A}$ — ponad 5 × 16 = 80 A, więc B16 wyłącza natychmiast (milisekundy). Przez ten czas napięcie na obudowie względem rury z wodą jest ograniczone połączeniami wyrównawczymi. Piekarnik jest wyłączony, użytkownik widzi zadziałany wyłącznik.

**Bez PE:** zwarcia nie ma, piekarnik działa dalej, a jego obudowa ma 230 V względem ziemi — aż ktoś jej dotknie, opierając się o zlew.

</details>

🧮 **[12.03](modules/12-ochrona-przeciwporazeniowa/12.03-warunek-skutecznosci-samoczynnego-wylaczenia.md#przykład)** · Warunek skuteczności samoczynnego wyłączenia

**Zadanie.** Obwód gniazd w garażu: B16, przewód 2,5 mm² Cu, długość 45 m, impedancja w rozdzielnicy (od strony sieci) 0,35 Ω. Czy warunek samoczynnego wyłączenia jest spełniony? Ocenić z zapasem 2/3.

<details><summary>Rozwiązanie</summary>

**Rezystancja przewodów (L + PE, 2 × 45 m):**

$$R = \frac{0{,}0175 \cdot 90}{2{,}5} = 0{,}63\ \Omega$$

$$Z_s \approx 0{,}35 + 0{,}63 = 0{,}98\ \Omega$$

**Dopuszczalne:** $230 / 80 = 2{,}88\ \Omega$; z zapasem $\tfrac{2}{3} \cdot 2{,}88 = 1{,}92\ \Omega$.

**Wniosek.** 0,98 Ω < 1,92 Ω — warunek spełniony z dużym zapasem. Dla C16: $\tfrac{2}{3} \cdot 1{,}44 = 0{,}96\ \Omega$ — wynik 0,98 Ω jest już na granicy, więc C16 nie byłby dobrym wyborem.

</details>

🔎 **[12.04](modules/12-ochrona-przeciwporazeniowa/12.04-izolacja-podwojna-separacja-elektryczna-selv-i.md#przykład)** · Izolacja podwójna, separacja elektryczna, SELV i PELV

**Zadanie.** Do pracy wewnątrz metalowego zbiornika potrzebna jest lampa ręczna. Masz: lampę 230 V klasy I, lampę 230 V klasy II i lampę 24 V z transformatorem bezpieczeństwa. Którą wybrać?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Wewnątrz zbiornika (przestrzeń ograniczona, przewodzące ściany, często wilgoć) stosuje się SELV — **lampę 24 V z transformatorem bezpieczeństwa**, a transformator umieszcza się **poza zbiornikiem**. Lampa klasy II jest lepsza od klasy I, ale uszkodzenie obudowy przy uderzeniu o ścianę zbiornika odsłoni 230 V, a człowiek ma doskonały kontakt z „ziemią”. Szczegółowe wymagania — [moduł 17](modules/17-pomieszczenia-szczegolne/README.md).

</details>

🔎 **[12.05](modules/12-ochrona-przeciwporazeniowa/12.05-ochrona-uzupelniajaca.md#przykład)** · Ochrona uzupełniająca

**Sytuacja.** Dziecko wkłada metalowy klucz do otworu fazy w gnieździe i dotyka drugą ręką grzejnika.

<details><summary>Rozwiązanie</summary>

**Co chroni?** Ochrona podstawowa została obejściona. Ochrona przy uszkodzeniu nie ma tu zastosowania — nie ma uszkodzenia izolacji, jest dotyk bezpośredni. Prąd płynie: faza → klucz → ręka → ciało → grzejnik → PE / ziemia. Różnicówka 30 mA widzi różnicę i wyłącza w ułamku sekundy. Wyłącznik nadprądowy nic by nie zrobił — kilkadziesiąt miliamperów to dla niego nic.

**Wniosek.** Właśnie dlatego RCD 30 mA jest obowiązkowy w obwodach gniazd. A przesłony torów prądowych w gniazdach ([06.01](modules/06-osprzet-instalacyjny/06.01-gniazda-wtyczkowe-jednofazowe-z-bolcem.md)) wzmacniają ochronę podstawową tam, gdzie są dzieci.

</details>

🧮 **[12.06](modules/12-ochrona-przeciwporazeniowa/12.06-dawne-nazwy-zerowanie-uziemienie-ochronne.md#przykład)** · Dawne nazwy: zerowanie, uziemienie ochronne — słownik przejściowy

**Zadanie.** W starym protokole z 1995 r. zapisano: „Ochrona przeciwporażeniowa dodatkowa: zerowanie. Skuteczność: spełniona, Zs = 1,2 Ω, zabezpieczenie 10 A (wkładka)”. Co to znaczy dziś?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Ochrona przy uszkodzeniu przez samoczynne wyłączenie zasilania w układzie TN (prawdopodobnie TN-C). Zmierzono impedancję pętli 1,2 Ω przy wkładce 10 A. Dziś trzeba sprawdzić, czy warunek $Z_s \cdot I_a \le U_0$ jest spełniony dla obecnego zabezpieczenia — jeśli wkładkę zamieniono na B16, $Z_{s,max}$ = 2,88 Ω (z zapasem 1,92 Ω), więc 1,2 Ω jest w porządku. Ale układ TN-C w obwodach odbiorczych i brak RCD — instalacja wymaga modernizacji.

</details>

---

## 13 — Uziemienia i połączenia wyrównawcze

🧮 **[13.01](modules/13-uziemienia-i-wyrownanie/13.01-uziom-fundamentowy-otokowy-pretowy.md#przykład)** · Uziom: fundamentowy, otokowy, prętowy

**Sytuacja.** Budowa domu w stanie fundamentów. Inwestor pyta, czy uziom „zrobi się później, przy instalacji elektrycznej”.

<details><summary>Rozwiązanie</summary>

**Odpowiedź.** Uziom fundamentowy wykonuje się teraz: bednarka 30×4 mm (stal ocynkowana) ułożona w ławach, połączona ze zbrojeniem co kilka metrów, z wyprowadzeniami w miejscu przyszłej GSU (np. pomieszczenie techniczne) i w narożnikach dla instalacji odgromowej. Koszt — materiał i godzina pracy. Później zostaje tylko uziom otokowy lub prętowy: więcej pracy, wykopy, często gorsza rezystancja.

</details>

🧮 **[13.02](modules/13-uziemienia-i-wyrownanie/13.02-rezystancja-uziemienia-od-czego-zalezy.md#przykład)** · Rezystancja uziemienia — od czego zależy

**Zadanie.** Dom w układzie TT, grunt piaszczysty ρ ≈ 300 Ω·m. Ile mniej więcej da pręt 6 m i czy wystarczy dla RCD 30 mA? A dla 300 mA?

<details><summary>Rozwiązanie</summary>

$$R \approx \frac{300}{2\pi \cdot 6} \ln\frac{4 \cdot 6}{0{,}016} \approx 7{,}96 \cdot 7{,}31 \approx 58\ \Omega$$

**Warunek:** RCD 30 mA: $58 \cdot 0{,}03 = 1{,}7$ V ≤ 50 V — tak. RCD 300 mA: $58 \cdot 0{,}3 = 17{,}4$ V ≤ 50 V — tak.

**Wniosek.** Dla ochrony przeciwporażeniowej wystarczy. Dla instalacji odgromowej (zalecane < 10 Ω) trzeba dużo więcej: uziomu otokowego lub kilku dłuższych prętów.

</details>

🔎 **[13.03](modules/13-uziemienia-i-wyrownanie/13.03-glowna-szyna-uziemiajaca.md#przykład)** · Główna szyna uziemiająca

**Sytuacja.** W piwnicy bloku przy rozdzielnicy głównej jest szyna z czterema przewodami żółto-zielonymi i jednym zaciskiem wolnym. Brak opisów.

<details><summary>Rozwiązanie</summary>

**Co zrobić przed pracami?** Ustalić, co jest czym: przewód do uziomu, PE z rozdzielnicy, woda, ogrzewanie. Zmierzyć ciągłość każdego połączenia do jego drugiego końca. Opisać przewody trwałymi oznacznikami. Brak połączenia z instalacją gazową lub z metalowymi kanałami — dopisać do listy usterek do usunięcia.

</details>

🧮 **[13.04](modules/13-uziemienia-i-wyrownanie/13.04-polaczenia-wyrownawcze-ochronne-glowne.md#przykład)** · Połączenia wyrównawcze ochronne główne

**Zadanie.** W domu zmierzono przy zwarciu w piekarniku impedancję pętli tak, że prąd zwarcia wynosi 300 A. Przewód PE od rozdzielnicy do piekarnika (2,5 mm², 15 m) ma rezystancję $0{,}0175 \cdot 15 / 2{,}5 = 0{,}105\ \Omega$. Jakie napięcie pojawi się na obudowie piekarnika względem PE rozdzielnicy?

<details><summary>Rozwiązanie</summary>

$$U = I \cdot R_{PE} = 300 \cdot 0{,}105 \approx 32\ \mathrm{V}$$

**A względem kranu?** Jeśli rura wodna jest połączona z GSU (a GSU z PE rozdzielnicy) — ok. 32 V przez ułamek sekundy, dopóki wyłącznik nie zadziała. Jeśli rura nie jest połączona i ma potencjał dalekiej ziemi — napięcie może być znacznie większe, bo dochodzi spadek na przewodach zasilających i PEN.

</details>

🧮 **[13.05](modules/13-uziemienia-i-wyrownanie/13.05-polaczenia-wyrownawcze-miejscowe.md#przykład)** · Połączenia wyrównawcze miejscowe

**Zadanie.** Łazienka: obwód zabezpieczony B16 ($I_a$ = 80 A) bez RCD (stara instalacja). Jaka może być największa rezystancja połączenia wyrównawczego między obudową pralki a grzejnikiem?

<details><summary>Rozwiązanie</summary>

$$R \le \frac{50}{80} = 0{,}625\ \Omega$$

Z RCD 30 mA: $R \le 50 / 0{,}03 \approx 1667\ \Omega$ — warunek praktycznie zawsze spełniony. Dlatego w łazience obwody i tak muszą mieć RCD 30 mA ([moduł 17](modules/17-pomieszczenia-szczegolne/README.md)).

</details>

🧮 **[13.06](modules/13-uziemienia-i-wyrownanie/13.06-przekroje-przewodow-ochronnych-i-wyrownawczych.md#przykład)** · Przekroje przewodów ochronnych i wyrównawczych

**Zadanie.** Dobierz minimalny PE: (a) obwód gniazd 3×2,5; (b) WLZ z żyłami fazowymi 25 mm² Cu; (c) WLZ 70 mm² Cu; (d) osobny przewód PE w korytku w piwnicy.

<details><summary>Rozwiązanie</summary>

- (a) 2,5 mm² (= S);
- (b) 16 mm² (16 < S ≤ 35);
- (c) 35 mm² (S/2);
- (d) 2,5 mm² Cu, jeśli korytko chroni go mechanicznie; 4 mm² Cu, jeśli nie.

</details>

---

## 14 — Od słupa do gniazdka

🔎 **[14.01](modules/14-od-slupa-do-gniazdka/14.01-przylacze-napowietrzne-i-kablowe.md#przykład)** · Przyłącze napowietrzne i kablowe

**Sytuacja.** Działka z istniejącą linią napowietrzną wzdłuż drogi. Inwestor chce zasilić dom kablem, „żeby nie było drutów nad podwórkiem”.

<details><summary>Rozwiązanie</summary>

**Odpowiedź.** W warunkach przyłączenia operator określi, czy możliwe jest przyłącze kablowe ze słupa (kabel ze słupa w rurze osłonowej, w ziemi do złącza ZKP w ogrodzeniu). Często jest to standardowe rozwiązanie. Złącze ZKP z licznikiem w ogrodzeniu, dalej WLZ kablem do domu — to już po stronie inwestora.

</details>

🔎 **[14.02](modules/14-od-slupa-do-gniazdka/14.02-zlacze-i-granica-wlasnosci.md#przykład)** · Złącze i granica własności

**Sytuacja.** Wieczorem w całym domu zgasło światło. W rozdzielnicy wszystkie wyłączniki są załączone, rozłącznik główny też. W złączu ZKP w ogrodzeniu wyświetlacz licznika jest wygaszony.

<details><summary>Rozwiązanie</summary>

**Diagnoza.** Licznik nie ma zasilania — problem jest przed nim: przepalona wkładka w złączu albo awaria sieci. Sprawdź, czy sąsiedzi mają prąd. Jeśli tak — prawdopodobnie zabezpieczenie przyłączowe; zgłoś awarię operatorowi. Nie otwieraj zaplombowanej części złącza.

</details>

🧮 **[14.03](modules/14-od-slupa-do-gniazdka/14.03-licznik-i-zabezpieczenie-przedlicznikowe.md#przykład)** · Licznik i zabezpieczenie przedlicznikowe

**Zadanie.** Dom: zabezpieczenie przedlicznikowe 3 × 20 A. Chcesz włączyć jednocześnie płytę indukcyjną 7,2 kW (3-faz., równo rozłożoną), czajnik 2,2 kW na L1 i pralkę 2 kW na L1. Czy L1 wytrzyma?

<details><summary>Rozwiązanie</summary>

- płyta: $7200 / 3 = 2400$ W na fazę → $2400/230 \approx 10{,}4$ A na L1;
- czajnik: $2200/230 \approx 9{,}6$ A;
- pralka (grzanie): $2000/230 \approx 8{,}7$ A.

Razem na L1 ok. **28,7 A** > 20 A. To przeciążenie ok. 1,4 × In — wkładka gG zadziała po pewnym czasie (od kilku do kilkudziesięciu minut, zależnie od charakterystyki), a przy dłuższej pracy na pewno. Na L2 i L3 jest tylko po 10,4 A.

**Wniosek.** Pralkę przenieść na L2, czajnik zostawić na L1 — wtedy L1 ≈ 20 A, L2 ≈ 19 A. Przy takich mocach i tak blisko granicy — warto rozważyć zwiększenie mocy przyłączeniowej.

</details>

🧮 **[14.04](modules/14-od-slupa-do-gniazdka/14.04-wewnetrzna-linia-zasilajaca-wlz.md#przykład)** · Wewnętrzna linia zasilająca (WLZ)

**Zadanie.** WLZ domu: 25 m, YKY 5×10 Cu, prąd obliczeniowy 25 A na fazę (symetrycznie). Oblicz spadek napięcia.

<details><summary>Rozwiązanie</summary>

Dla obwodu trójfazowego symetrycznego (bez N), w przybliżeniu:

$$\Delta U = \sqrt{3} \cdot I \cdot R = \sqrt{3} \cdot 25 \cdot \frac{0{,}0175 \cdot 25}{10} \approx 1{,}89\ \mathrm{V}$$

$$\Delta U\% = \frac{1{,}89}{400} \cdot 100\% \approx 0{,}47\ \%$$

**Wniosek.** Mieści się w ok. 0,5 % dla WLZ. Zostaje ok. 2,5 % dla obwodów w domu.

</details>

🧮 **[14.05](modules/14-od-slupa-do-gniazdka/14.05-moc-przylaczeniowa-i-taryfy.md#przykład)** · Moc przyłączeniowa i taryfy

**Zadanie.** Dom z G12: podgrzewacz wody 3 kW pracuje 2 h dziennie. Różnica cen między strefą droższą a tańszą wynosi 0,40 zł/kWh (przykład). Ile zaoszczędzisz rocznie, przenosząc grzanie na noc?

<details><summary>Rozwiązanie</summary>

$$E = 3\ \mathrm{kW} \cdot 2\ \mathrm{h} \cdot 365 = 2190\ \mathrm{kWh}$$

$$\text{oszczędność} \approx 2190 \cdot 0{,}40 \approx 876\ \mathrm{zł}$$

**Wniosek.** Stycznik z zegarem za kilkadziesiąt złotych zwraca się w kilka tygodni — pod warunkiem, że zbiornik jest wystarczający na dzienne zużycie.

</details>

---

## 15 — Rozdzielnica mieszkaniowa

🧮 **[15.01](modules/15-rozdzielnica-mieszkaniowa/15.01-budowa-rozdzielnicy-obudowa-szyna-th35-listwy-n.md#przykład)** · Budowa rozdzielnicy: obudowa, szyna TH35, listwy N i PE, mostki

**Zadanie.** Policz moduły dla mieszkania: rozłącznik 3P, SPD 3+1, 2 × RCD 4P, 8 wyłączników 1P, 1 wyłącznik 3P (płyta), 3 RCBO (po 2 moduły), kontrolki faz (1 moduł). Jaką rozdzielnicę wybrać?

<details><summary>Rozwiązanie</summary>

$$3 + 4 + 2 \cdot 4 + 8 + 3 + 3 \cdot 2 + 1 = 33\ \text{moduły}$$

Z rezerwą ok. 25 %: $33 \cdot 1{,}25 \approx 41$ modułów. Wybór: rozdzielnica **3 × 14 = 42** albo **4 × 12 = 48** moduły (wygodniej przy listwach N dla kilku grup).

</details>

🧮 **[15.02](modules/15-rozdzielnica-mieszkaniowa/15.02-schemat-jednokreskowy-jak-czytac-i-jak-rysowac.md#przykład)** · Schemat jednokreskowy — jak czytać i jak rysować

**Zadanie.** Odczytaj z przykładowego schematu kawalerki: ile jest obwodów, które są chronione wspólną różnicówką i jakim przewodem zasilane są gniazda w łazience.

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** 7 obwodów odbiorczych. RCD 1: oświetlenie pokoju (B10, 3×1,5) i gniazda pokoju (B16, 3×2,5). RCD 2: oświetlenie kuchni i łazienki, gniazda kuchni, gniazda łazienki. Osobne RCBO: pralka i lodówka. Gniazda w łazience: B16, przewód 3×2,5, za RCD 2.

</details>

🧮 **[15.03](modules/15-rozdzielnica-mieszkaniowa/15.03-oznaczanie-obwodow-i-opis-rozdzielnicy.md#przykład)** · Oznaczanie obwodów i opis rozdzielnicy

**Zadanie.** Zaproponuj opis dla obwodu: wyłącznik B16, faza L2, za RCD 1, zasila gniazda w kuchni przy blacie po lewej stronie zlewu.

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Na maskownicy: **„F7 · L2 · gniazda kuchnia blat lewy”**, z kolorem lub znacznikiem grupy RCD 1. Na przewodach w rozdzielnicy: **„F7”** na żyle L, N i PE. W tabeli na drzwiczkach: F7, B16, YDY 3×2,5, L2, RCD 1, gniazda kuchnia blat (lewa strona zlewu).

</details>

🧮 **[15.04](modules/15-rozdzielnica-mieszkaniowa/15.04-przyklad-kawalerka-zasilanie-jednofazowe.md#przykład)** · Przykład: kawalerka, zasilanie jednofazowe

**Zadanie.** W kawalerce wieczorem pracują: płyta ograniczona do 3,5 kW, piekarnik 2,5 kW, czajnik 2 kW, oświetlenie 0,2 kW, TV i komputer 0,3 kW. Czy zabezpieczenie przedlicznikowe 25 A wytrzyma?

<details><summary>Rozwiązanie</summary>

$$P = 3{,}5 + 2{,}5 + 2 + 0{,}2 + 0{,}3 = 8{,}5\ \mathrm{kW} \qquad I = \frac{8500}{230} \approx 37\ \mathrm{A}$$

37 A > 25 A — zabezpieczenie zadziała po krótkim czasie.

**Rozwiązanie.** Nie włączać wszystkiego naraz (czajnik po zakończeniu gotowania), zastosować przekaźnik priorytetowy (płyta odcina piekarnik) albo wystąpić o zwiększenie mocy (często trójfazowe zasilanie).

</details>

🔎 **[15.05](modules/15-rozdzielnica-mieszkaniowa/15.05-przyklad-mieszkanie-zasilanie-trojfazowe.md#przykład)** · Przykład: mieszkanie, zasilanie trójfazowe

**Zadanie.** Sprawdź rozkład na fazy dla mieszkania z tabeli przy jednoczesnej pracy: płyta 6 kW (po 2 kW na fazę), pralka 2 kW (L2), zmywarka 2 kW (L3), czajnik 2 kW (gniazda kuchnia, L1), lodówka 0,15 kW (L1), oświetlenie 0,3 kW (L1 i L2).

<details><summary>Rozwiązanie</summary>

- L1: 2 + 2 + 0,15 + 0,15 = **4,3 kW** → 18,7 A,
- L2: 2 + 2 + 0,15 = **4,15 kW** → 18 A,
- L3: 2 + 2 = **4 kW** → 17,4 A.

**Wniosek.** Fazy obciążone równo, każda poniżej 25 A. Przy pracy piekarnika (2,5 kW, np. na L3) L3 wzrośnie do ok. 28 A — warto przewidzieć piekarnik na fazie z największym zapasem albo zaplanować moc przyłączeniową z zapasem.

</details>

🧮 **[15.06](modules/15-rozdzielnica-mieszkaniowa/15.06-przyklad-dom-jednorodzinny.md#przykład)** · Przykład: dom jednorodzinny

**Zadanie.** Garaż 30 m od domu, w nim: gniazda 230 V, gniazdo siłowe 400 V do sprężarki (C16), oświetlenie. Jak zasilić?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie (szkic).** Z RG: wyłącznik C25 3P (selektywny względem C16 w garażu tylko częściowo — sprawdzić w tabelach), kabel YKY 5×6 w ziemi (spadek napięcia i warunek samoczynnego wyłączenia do sprawdzenia, [12.03](modules/12-ochrona-przeciwporazeniowa/12.03-warunek-skutecznosci-samoczynnego-wylaczenia.md)). W garażu podrozdzielnica: rozłącznik 3P, RCD 4P 40 A / 30 mA typu A, wyłączniki: B10 oświetlenie, B16 gniazda, C16 3P gniazdo siłowe. PE garażu połączony z lokalnymi połączeniami wyrównawczymi (brama metalowa, instalacje). N i PE na osobnych szynach.

</details>

🔎 **[15.07](modules/15-rozdzielnica-mieszkaniowa/15.07-montaz-i-porzadek-przewodow-w-rozdzielnicy.md#przykład)** · Montaż i porządek przewodów w rozdzielnicy

**Sytuacja.** Nowa rozdzielnica. Po załączeniu RCD 2 wybija od razu przy załączeniu obwodu F5 (gniazda kuchnia), mimo że w kuchni nic nie jest podłączone.

<details><summary>Rozwiązanie</summary>

**Diagnoza.** Najczęstsza przyczyna w świeżo zmontowanej rozdzielnicy: N obwodu F5 trafił do listwy N grupy RCD 1 (albo do PE). Sprawdź: L obwodu F5 jest pod RCD 2 — więc jego N musi być na listwie „N RCD2”. Po przełożeniu przewodu RCD działa ([08.06](modules/08-wylaczniki-roznicowopradowe/08.06-dlaczego-roznicowka-wybija-przyczyny-i-szukanie.md)).

</details>

---

## 16 — Planowanie obwodów

🧮 **[16.01](modules/16-planowanie-obwodow/16.01-podzial-instalacji-na-obwody.md#przykład)** · Podział instalacji na obwody

**Zadanie.** Mieszkanie 62 m²: pokój dzienny z aneksem kuchennym, sypialnia, pokój dziecka, łazienka, przedpokój. Odbiorniki: płyta indukcyjna 7,2 kW (trójfazowa), piekarnik 3,5 kW, zmywarka, pralka. Zasilanie trójfazowe. Zaproponuj podział.

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.**

- Oświetlenie: **2 obwody** (strefa dzienna; strefa nocna + łazienka + przedpokój) — B10, 1,5 mm².
- Gniazda ogólne: **3 obwody** (pokój dzienny; sypialnia + pokój dziecka; przedpokój) — B16, 2,5 mm². Razem z oświetleniem 5 obwodów — więcej niż minimum 3 z tabeli dla 50–75 m².
- Gniazda kuchenne nad blatem: **1 obwód**, B16, 2,5 mm².
- Łazienka (gniazda): **1 obwód**, B16, 2,5 mm².
- Wydzielone: płyta (3 × B16, 5 × 2,5 mm²), piekarnik, zmywarka, pralka — **4 obwody**.
- Razem **11 obwodów**. Rozłożenie na fazy: L1 — piekarnik, gniazda pokoju dziennego, oświetlenie 1; L2 — zmywarka, gniazda kuchenne, oświetlenie 2, przedpokój; L3 — pralka, gniazda sypialni, łazienka; płyta — na trzech fazach.
- Różnicówki: dwie, każda z oświetleniem i częścią gniazd, albo RCBO dla każdego obwodu.

</details>

🧮 **[16.02](modules/16-planowanie-obwodow/16.02-dobor-przekroju-i-zabezpieczenia-procedura-krok.md#przykład)** · Dobór przekroju i zabezpieczenia — procedura krok po kroku

**Zadanie.** Obwód gniazd w warsztacie: piła 1,8 kW i odkurzacz 1,2 kW mogą pracować razem, cos φ ≈ 0,9. Przewód YDYp 3 × 2,5 mm² pod tynkiem (sposób C), ale 3 m trasy przechodzi w peszlu przez ocieploną ścianę (A2, obciążalność ok. 18,5 A). Długość 22 m. Dobierz zabezpieczenie.

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.**

1. $I_B = \dfrac{1800 + 1200}{230 \cdot 0{,}9} \approx 14{,}5$ A.
2. I_n ≥ 14,5 A → **16 A**. Silnik piły ma prąd rozruchu — rozważ charakterystykę C.
3. Najgorszy odcinek: A2, $I_z \approx 18{,}5$ A ≥ 16 A — **spełnione**.
4. I₂ = 1,45 · 16 = 23,2 A ≤ 1,45 · 18,5 = 26,8 A — **spełnione**.
5. ΔU przy 14,5 A: $\Delta U = \dfrac{2 \cdot 22 \cdot 14{,}5}{56 \cdot 2{,}5} \approx 4{,}6$ V, czyli **2,0 %** — w normie.
6. Dla C16: $Z_{s,max} = 230 / 160 = 1{,}44\ \Omega$; dla B16: 2,88 Ω. Jeśli pomiar pokaże np. 1,1 Ω — C16 formalnie przejdzie, ale nie spełni oceny z zapasem ⅔ (0,96 Ω, [12.03](modules/12-ochrona-przeciwporazeniowa/12.03-warunek-skutecznosci-samoczynnego-wylaczenia.md)); B16 przejdzie z dużym zapasem. Wybór: **B16**, a jeśli przy rozruchu piły wybija — **C16** po sprawdzeniu pętli.

</details>

🧮 **[16.03](modules/16-planowanie-obwodow/16.03-sprawdzanie-spadku-napiecia.md#przykład)** · Sprawdzanie spadku napięcia

**Zadanie.** Obwód do garażu wolnostojącego: długość 40 m, odbiorniki do 3,5 kW (cos φ = 1), przewód miedziany. Sprawdź 2,5 mm² i 4 mm². Spadek na WLZ wynosi 0,5 %.

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** $I = 3500 / 230 \approx 15{,}2$ A.

- 2,5 mm²: $\Delta U = \dfrac{2 \cdot 40 \cdot 15{,}2}{56 \cdot 2{,}5} \approx 8{,}7$ V → **3,8 %**; razem z WLZ **4,3 %** — za dużo (dopuszczalne 3 %).
- 4 mm²: $\Delta U = \dfrac{2 \cdot 40 \cdot 15{,}2}{56 \cdot 4} \approx 5{,}4$ V → **2,4 %**; razem z WLZ **2,9 %** — mieści się, ale na styk.
- Wybór: **4 mm²** (albo 6 mm², jeśli w garażu planowane są większe odbiorniki lub ładowanie samochodu).

</details>

🔎 **[16.04](modules/16-planowanie-obwodow/16.04-strefy-instalacyjne-i-trasy-przewodow.md#przykład)** · Strefy instalacyjne i trasy przewodów

**Zadanie.** Gniazdo na wysokości 30 cm stoi 80 cm od narożnika pokoju. Chcesz powiesić półkę 50 cm nad nim i 20 cm w bok. Czy wiercenie jest bezpieczne?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Jeśli instalację wykonano zgodnie ze strefami, przewód do gniazda schodzi **pionowo nad gniazdem** z pasa górnego (albo biegnie poziomo w pasie dolnym). Punkt 50 cm nad gniazdem i 20 cm w bok jest poza pionem gniazda i poza pasem dolnym — wiercenie powinno być bezpieczne. Ale w starych budynkach przewody bywały prowadzone dowolnie — przed wierceniem sprawdź wykrywaczem, a obwód warto wyłączyć.

</details>

🔎 **[16.05](modules/16-planowanie-obwodow/16.05-wysokosci-montazu-i-liczba-gniazd.md#przykład)** · Wysokości montażu i liczba gniazd

**Zadanie.** Sypialnia 14 m²: łóżko podwójne pod jedną ścianą, biurko pod oknem, szafa przy drzwiach, telewizor naprzeciwko łóżka. Rozplanuj gniazda.

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.**

- Przy łóżku: **2 × gniazdo podwójne** (po obu stronach, ok. 30 cm albo nad szafkami nocnymi).
- Przy biurku: **gniazdo potrójne lub 2 × podwójne** nad blatem biurka (np. 80–90 cm), w pionie w strefie przy oknie.
- Telewizor: **gniazdo podwójne** + gniazdo antenowe/sieciowe, na wysokości zawieszenia lub za szafką RTV.
- Przy drzwiach: **gniazdo pojedyncze** do odkurzacza (nie za szafą).
- Łącznik: przy drzwiach po stronie klamki, 105 cm; opcjonalnie łącznik schodowy przy łóżku ([18.03](modules/18-oswietlenie/18.03-uklad-schodowy-i-krzyzowy-schematy.md)).
- Razem ok. **11–12 gniazd** w kilku punktach — wszystkie na jednym obwodzie gniazd sypialni (B16, 2,5 mm²), bo nie ma tu dużych odbiorników.

</details>

🧮 **[16.06](modules/16-planowanie-obwodow/16.06-obwody-wydzielone-plyta-piekarnik-pralka.md#przykład)** · Obwody wydzielone: płyta, piekarnik, pralka, zmywarka

**Zadanie.** Kuchnia w mieszkaniu z zasilaniem trójfazowym: płyta 7,4 kW, piekarnik 3,5 kW, zmywarka 2,1 kW. Dobierz obwody i rozłóż na fazy.

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.**

- Płyta: $I = 7400 / (\sqrt{3} \cdot 400) \approx 10{,}7$ A na fazę (przy pełnej mocy rozłożonej na 3 fazy) → **3 × B16**, przewód **5 × 2,5 mm²**.
- Piekarnik: $I = 3500 / 230 \approx 15{,}2$ A → **B16**, **3 × 2,5 mm²**, np. faza L1.
- Zmywarka: $I = 2100 / 230 \approx 9{,}1$ A → **B16**, **3 × 2,5 mm²**, faza L2.
- Gniazda nad blatem → faza L3, żeby najcięższe obciążenia jednofazowe były na różnych fazach.
- RCD: typ A, 30 mA — najlepiej RCBO dla piekarnika i zmywarki.

</details>

---

## 17 — Pomieszczenia i miejsca szczególne

🔎 **[17.01](modules/17-pomieszczenia-szczegolne/17.01-lazienka-strefy-0-1-i-2.md#przykład)** · Łazienka: strefy 0, 1 i 2

**Zadanie.** W łazience wanna stoi wzdłuż ściany, a umywalka na tej samej ścianie — jej krawędź jest 75 cm od krawędzi wanny. Gdzie przy umywalce można powiesić gniazdo: 40 cm od umywalki w stronę wanny czy 40 cm od umywalki po jej drugiej stronie?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Strefa 2 kończy się 60 cm od krawędzi wanny.

- Gniazdo 40 cm od umywalki **w stronę wanny** jest 75 − 40 = **35 cm** od wanny — **w strefie 2**. Niedopuszczalne.
- Gniazdo po **drugiej stronie** umywalki jest co najmniej 75 + szerokość umywalki + 40 cm od wanny — **poza strefami**. Dopuszczalne: IP44, za RCD 30 mA.

</details>

🧮 **[17.02](modules/17-pomieszczenia-szczegolne/17.02-kuchnia.md#przykład)** · Kuchnia

**Zadanie.** Kuchnia z blatem 3 m: zlew w środku, płyta na prawym końcu. Na blacie pracują czajnik (2,2 kW), ekspres (1,5 kW), toster (0,9 kW) i robot (1,0 kW). Ile obwodów nad blatem?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Wszystko naraz: $2{,}2 + 1{,}5 + 0{,}9 + 1{,}0 = 5{,}6$ kW, czyli ok. 24 A — za dużo na jeden B16. Realnie razem pracują 2–3 urządzenia (ok. 4 kW, 17 A). Rozwiązanie: **dwa obwody nad blatem** po B16 — gniazda po lewej stronie zlewu na jednym, po prawej (między zlewem a płytą) na drugim. Czajnik i ekspres podłącza się wtedy do różnych obwodów.

</details>

🧮 **[17.03](modules/17-pomieszczenia-szczegolne/17.03-garaz-i-warsztat.md#przykład)** · Garaż i warsztat

**Zadanie.** Wolnostojący garaż 30 m od domu. Planowane: oświetlenie, 4 gniazda 230 V, gniazdo CEE 16 A dla kompresora 2,2 kW (3-faz.) i w przyszłości wallbox 11 kW. Jak to zasilić?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Kabel ziemny **YKY 5 × 10 mm²** (lub 5 × 6 mm² po sprawdzeniu spadku i pętli) z rozdzielnicy domu do **podrozdzielnicy w garażu** ([17.04](modules/17-pomieszczenia-szczegolne/17.04-instalacje-zewnetrzne-i-ogrod.md)). W domu zabezpieczenie linii, np. C32 lub bezpieczniki, z selektywnością wobec przedlicznikowego. W garażu: rozłącznik, RCD 30 mA typ A dla oświetlenia i gniazd, B10 oświetlenie, B16 gniazda, C16 3P dla gniazda CEE, oraz miejsce na obwód wallboxa (B16 3P lub C16 3P wg instrukcji, z RCD typu A + RDC-DD lub typ B). Spadek napięcia dla 11 kW na 30 m, 6 mm² Cu: $\Delta U\% = 100 \cdot 11000 \cdot 30 / (56 \cdot 6 \cdot 400^2) \approx 0{,}6$ % — w porządku.

</details>

🧮 **[17.04](modules/17-pomieszczenia-szczegolne/17.04-instalacje-zewnetrzne-i-ogrod.md#przykład)** · Instalacje zewnętrzne i ogród

**Zadanie.** Oświetlenie ścieżki: 8 lamp po 5 W LED, ścieżka 25 m. Dwie opcje: 230 V albo 24 V z zasilacza w garażu. Porównaj.

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.**

- **230 V:** kabel YKY 3 × 1,5 mm² na 0,7 m, lampy klasy I z PE lub klasy II, obwód B10 za RCD 30 mA. Prąd mały (40 W ≈ 0,2 A), spadek pomijalny. Wymaga starannego wykonania połączeń w gruncie lub w słupkach.
- **24 V SELV:** zasilacz 60 W w garażu, przewód do ziemi dla systemów niskonapięciowych; 40 W / 24 V ≈ 1,7 A; dla 25 m przewodu 1,5 mm²: $\Delta U = 2 \cdot 25 \cdot 1{,}7 / (56 \cdot 1{,}5) \approx 1{,}0$ V (ok. 4 %) — do przyjęcia dla LED; przy uszkodzeniu kabla brak zagrożenia porażeniem.
- Wybór: dla oświetlenia ogrodowego **24 V** jest bezpieczniejsze i prostsze w eksploatacji.

</details>

🔎 **[17.05](modules/17-pomieszczenia-szczegolne/17.05-tymczasowa-instalacja-na-budowie.md#przykład)** · Tymczasowa instalacja na budowie

**Zadanie.** Na budowie domu potrzebne są: betoniarka 230 V 0,8 kW, piła stołowa 400 V 3 kW, nagrzewnica 400 V 9 kW (gniazdo CEE 32 A), elektronarzędzia i oświetlenie. Jakie RCD?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.**

- Gniazda 230 V (betoniarka, elektronarzędzia, oświetlenie) — **RCD 30 mA**.
- Gniazdo CEE 16 A (piła) — gniazdo do 32 A, więc też **RCD 30 mA**.
- Gniazdo CEE 32 A (nagrzewnica) — prąd znamionowy 32 A, czyli „do 32 A włącznie” — **RCD 30 mA**. RCD ≤ 500 mA wystarcza dopiero dla gniazd powyżej 32 A (np. CEE 63 A).
- Wniosek: w typowej rozdzielnicy budowy domu wszystkie gniazda mają RCD 30 mA (najlepiej kilka, żeby jedna usterka nie zatrzymywała całej budowy).

</details>

---

## 18 — Oświetlenie

🧮 **[18.01](modules/18-oswietlenie/18.01-zrodla-swiatla-i-zasilacze-led.md#przykład)** · Źródła światła i zasilacze LED

**Zadanie.** W salonie było 6 halogenów GU10 po 50 W (ok. 350 lm każdy). Na co je wymienić i ile energii się zaoszczędzi przy 4 h świecenia dziennie?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** LED GU10 ok. 350–400 lm to typowo **4–5 W**. Barwa 2700–3000 K (salon), Ra ≥ 80. Moc: 6 × 50 = 300 W → 6 × 5 = 30 W. Oszczędność 270 W × 4 h × 365 = **ok. 394 kWh rocznie**. Jeśli halogeny były na ściemniaczu — kupić LED ściemnialne i sprawdzić zgodność ściemniacza ([18.05](modules/18-oswietlenie/18.05-sciemniacze-i-wspolpraca-z-led.md)).

</details>

🧮 **[18.02](modules/18-oswietlenie/18.02-lacznik-jednobiegunowy-i-swiecznikowy-schematy.md#przykład)** · Łącznik jednobiegunowy i świecznikowy — schematy

**Zadanie.** Żyrandol z 5 żarówkami: chcesz włączać osobno 2 i 3 żarówki oraz wszystkie razem. Narysuj, jak to podłączyć, i jakie przewody położyć.

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Łącznik **świecznikowy (5)**: klawisz I zasila grupę 2 żarówek, klawisz II — grupę 3 żarówek, oba klawisze — wszystkie 5. Do łącznika: **L** (z puszki), z łącznika do lampy **dwa przewody łącznikowe**. Do lampy: dwa łącznikowe + **N** + **PE** → przewód **4 × 1,5 mm²** (np. YDYp 4 × 1,5 z PE). W żyrandolu: N wspólny dla obu grup, PE do zacisku oprawy (klasa I).

</details>

🧮 **[18.03](modules/18-oswietlenie/18.03-uklad-schodowy-i-krzyzowy-schematy.md#przykład)** · Układ schodowy i krzyżowy — schematy

**Zadanie.** Sypialnia: światło sufitowe ma się włączać przy drzwiach i przy obu stronach łóżka. Jakie łączniki i ile żył?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Trzy miejsca: **6 (drzwi) – 7 (łóżko lewe) – 6 (łóżko prawe)**. Połączenia:

- faza L → zacisk wspólny łącznika przy drzwiach;
- łącznik przy drzwiach → łącznik krzyżowy: 2 korespondencje (przewód 3 × 1,5 z PE lub 4 × 1,5);
- łącznik krzyżowy → łącznik przy prawej stronie łóżka: 2 korespondencje;
- zacisk wspólny ostatniego łącznika → lampa; N i PE do lampy.

Alternatywa: trzy przyciski i przekaźnik impulsowy — wtedy do każdego przycisku wystarczy przewód 2-żyłowy (+ PE) ([18.04](modules/18-oswietlenie/18.04-przekaznik-impulsowy-zamiast-lacznikow.md)).

</details>

🔎 **[18.04](modules/18-oswietlenie/18.04-przekaznik-impulsowy-zamiast-lacznikow.md#przykład)** · Przekaźnik impulsowy zamiast łączników schodowych

**Zadanie.** Długi korytarz z 4 wejściami w domu jednorodzinnym. Porównaj: łączniki 6–7–7–6 i przekaźnik impulsowy.

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.**

- **Łączniki:** 2 schodowe + 2 krzyżowe; między łącznikami 3 odcinki przewodu z dwiema korespondencjami (+ PE); prąd lampy przez wszystkie 4 łączniki; dodanie piątego miejsca = kolejny krzyżowy i przekładanie przewodów.
- **Przekaźnik:** 4 przyciski zwierne, przekaźnik w rozdzielnicy lub puszce, do każdego przycisku przewód 2-żyłowy (+ PE); dodanie piątego miejsca = jeden przycisk podłączony równolegle; można dodać zmierzchówkę lub „wyłącz wszystko” przy wyjściu z domu.
- Wybór: **przekaźnik impulsowy** — prostsza i elastyczniejsza instalacja.

</details>

🧮 **[18.05](modules/18-oswietlenie/18.05-sciemniacze-i-wspolpraca-z-led.md#przykład)** · Ściemniacze i współpraca z LED

**Zadanie.** Ściemniacz uniwersalny: „R, L 20–400 W; C 20–300 W; LED 3–100 W”. Chcesz podłączyć 8 ściemnialnych LED GU10 po 5 W. Czy to zadziała?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Łączna moc LED: 8 × 5 = 40 W. Mieści się w zakresie **LED 3–100 W** — tak. Gdybyś patrzył na zakres dla żarówek (do 400 W), uznałbyś, że zmieści się 80 takich żarówek — a dla LED producent dopuszcza maksymalnie 100 W, czyli 20 sztuk. Zanim kupisz — sprawdź, czy żarówki są na liście zgodności ściemniacza.

</details>

🧮 **[18.06](modules/18-oswietlenie/18.06-tasmy-led-i-ich-zasilanie.md#przykład)** · Taśmy LED i ich zasilanie

**Zadanie.** Podświetlenie blatu kuchennego: 3,6 m taśmy 9,6 W/m. Zasilacz w szafce nad lodówką, 2 m od początku taśmy. Dobierz zasilacz i przewód.

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.**

- Moc: $9{,}6 \cdot 3{,}6 \approx 34{,}6$ W; z zapasem 20 % → **≥ 41,5 W** → zasilacz **50 W**.
- Napięcie: odcinek 3,6 m — wystarczy 12 V, ale 24 V daje mniejszy prąd; wybierz **24 V**.
- Prąd: $34{,}6 / 24 \approx 1{,}44$ A.
- Przewód 2 m, 0,75 mm²: $\Delta U = 2 \cdot 2 \cdot 1{,}44 / (56 \cdot 0{,}75) \approx 0{,}14$ V — pomijalne.
- Profil aluminiowy z kloszem (taśma pod szafkami, 9,6 W/m), taśma IP65 lub w profilu z kloszem (para znad płyty).
- Zasilacz z oznaczeniem SELV, w obudowie, w wentylowanej szafce; zasilanie 230 V z obwodu oświetlenia kuchni przez łącznik.

</details>

---

## 19 — Prace krok po kroku

🔎 **[19.01](modules/19-prace-krok-po-kroku/19.01-wymiana-gniazda-wtyczkowego.md#przykład)** · Wymiana gniazda wtyczkowego

**Zadanie.** Po zdjęciu starego gniazda widzisz: brązową żyłę na lewym zacisku, niebieską na prawym i kawałek drutu od prawego zacisku do bolca. Żółto-zielonej żyły w puszce nie ma. Co robisz?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** To mostek N–bolec — instalacja dwuprzewodowa. Nowe gniazdo z bolcem **bez mostka** pozostawiłoby bolec bez ochrony, a **z mostkiem** odtworzyłoby zagrożenie. Właściwe rozwiązanie to doprowadzenie PE (nowy przewód z rozdzielnicy). Rozwiązanie przejściowe: gniazdo **bez bolca** i obwód za RCD 30 mA — oraz informacja dla domowników, że urządzenia klasy I (pralka, czajnik z metalową obudową) nie mają tu ochrony. Zaplanuj modernizację ([21.04](modules/21-stare-instalacje/21.04-modernizacja-czesciowa.md)).

</details>

🔎 **[19.02](modules/19-prace-krok-po-kroku/19.02-wymiana-lacznika.md#przykład)** · Wymiana łącznika

**Zadanie.** Wymieniasz podwójny klawisz w przedpokoju. W puszce są 3 żyły: brązowa, czarna, szara. Klawisze sterują dwiema różnymi lampami. Co to za łącznik i jak go podłączyć?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** 3 żyły, 2 klawisze, dwie lampy — **świecznikowy (5)**. Brązowa to najpewniej L (sprawdź: po załączeniu obwodu tylko ona ma napięcie przy wyłączonych klawiszach — pomiar wykonujesz ostrożnie, przed wyjęciem mechanizmu, albo zanotuj, który zacisk był wspólny). Brązowa → zacisk wspólny L, czarna i szara → wyjścia 1 i 2. Jeśli klawisze sterują lampami „na odwrót” — zamień czarną z szarą.

</details>

🔎 **[19.03](modules/19-prace-krok-po-kroku/19.03-montaz-lampy-i-oprawy.md#przykład)** · Montaż lampy i oprawy

**Zadanie.** W suficie są 3 żyły: czarna, niebieska, żółto-zielona. Nowa lampa ma metalową obudowę, zacisk ⏚ i kostkę z oznaczeniami L, N. Jak podłączyć?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Czarna (przewód łącznikowy) → **L**, niebieska → **N**, żółto-zielona → **⏚**. Oprawa klasy I — PE jest konieczny. Po montażu: łącznikiem wyłącz lampę i sprawdź wskaźnikiem, że na zacisku L oprawy nie ma napięcia względem PE (czyli łącznik przerywa fazę).

</details>

🧮 **[19.04](modules/19-prace-krok-po-kroku/19.04-podlaczenie-plyty-indukcyjnej.md#przykład)** · Podłączenie płyty indukcyjnej

**Zadanie.** Na tabliczce płyty: „400 V 2N~ 50 Hz, 7,4 kW”. W kuchni jest obwód 5 × 2,5 mm² z 3 × B16. Jak podłączyć?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Płyta przewiduje **dwie fazy** (2N~). Z pięciożyłowego przewodu wykorzystujesz **L1, L2, N, PE**; trzecią fazę (szarą) zaizoluj w puszce. Mostki — wg rysunku dla 2N~. Prąd: $7400 / (2 \cdot 230) \approx 16$ A na fazę — przy pełnej mocy B16 jest na granicy, ale płyty mają zarządzanie mocą, które to uwzględnia; wartości zabezpieczeń podaje instrukcja. Wyłącznik trójfazowy B16 może zostać — trzecia faza będzie po prostu nieobciążona.

</details>

🧮 **[19.05](modules/19-prace-krok-po-kroku/19.05-dodanie-nowego-obwodu-w-rozdzielnicy.md#przykład)** · Dodanie nowego obwodu w rozdzielnicy

**Zadanie.** Chcesz dodać obwód klimatyzatora 1,2 kW (B16, 3 × 2,5 mm²). W rozdzielnicy są: RCD 1 (oświetlenie, gniazda pokoi), RCD 2 (kuchnia, łazienka), jedno wolne miejsce w rzędzie z RCD 2. Listwa N grupy RCD 2 ma jeden wolny zacisk. Gdzie podłączyć?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Wyłącznik w wolnym miejscu rzędu RCD 2, zasilany z grzebienia za RCD 2. N → **wolny zacisk listwy N grupy RCD 2**. PE → listwa PE. Sprawdź jeszcze, czy RCD 2 nie ma już zbyt wielu obwodów z prądami upływu (klimatyzator z falownikiem ma swój upływ) — alternatywą jest RCBO dla klimatyzatora z N na jego zacisku ([08.04](modules/08-wylaczniki-roznicowopradowe/08.04-rcbo-wylacznik-nadpradowy-z-czlonem.md)).

</details>

🧮 **[19.06](modules/19-prace-krok-po-kroku/19.06-bruzdy-puszki-i-prowadzenie-przewodow-w-scianie.md#przykład)** · Bruzdy, puszki i prowadzenie przewodów w ścianie

**Zadanie.** Ściana działowa z cegły pełnej, grubość 12 cm (120 mm), wysokość 2,6 m. Chcesz poprowadzić przewód poziomo 1,2 m nad podłogą od gniazda do gniazda (2 m). Czy możesz?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Grubość 120 mm mieści się w przedziale 116–175 mm: bruzdy poziome są dopuszczalne tylko **do 1,25 m długości** i **15 mm** głębokości, i tylko w pasie **1/8 wysokości** przy stropie lub podłodze ($2{,}6 / 8 \approx 0{,}33$ m). Wysokość 1,2 m to środek ściany, a bruzda ma 2 m — **nie wolno** bez obliczeń. Rozwiązanie: przewód poziomo w pasie przy suficie (albo przy podłodze, do 33 cm), a do gniazd pionowo w dół.

</details>

🔎 **[19.07](modules/19-prace-krok-po-kroku/19.07-zakanczanie-przewodow-tulejki-zaciski-momenty.md#przykład)** · Zakańczanie przewodów: tulejki, zaciski, momenty dokręcania

**Zadanie.** Podłączasz przewód H05VV-F 3G2,5 (linka) do zacisku śrubowego wyłącznika B16. Co przygotować?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Zdejmij powłokę, odizoluj żyły na długość tulejki (dla tulejki izolowanej 2,5 mm² z częścią metalową 10 mm — ok. 10 mm), nałóż tulejki **2,5 mm²** (w systemie DIN niebieskie), zaciśnij zaciskarką. Włóż do zacisku do oporu, dokręć momentem z instrukcji wyłącznika (np. 2 N·m), pociągnij przewód. PE i N — tak samo, do listew.

</details>

---

## 20 — Diagnostyka usterek

🔎 **[20.01](modules/20-diagnostyka-usterek/20.01-metoda-szukania-usterek.md#przykład)** · Metoda szukania usterek

**Zadanie.** Zgłoszenie: „W kuchni wybija prąd, zwykle rano”. Jak to rozpisać na kroki?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.**

1. **Wywiad:** co wybija — różnicówka czy wyłącznik? „Rano” — czyli przy czajniku, ekspresie, tosterze naraz? Od kiedy — po zakupie nowego ekspresu?
2. **Oględziny rozdzielnicy:** w dole jest B16 gniazd kuchennych, RCD załączona → **przeciążenie** lub zwarcie w obwodzie, nie upływ.
3. **Zawężanie:** jeśli wybija po kilku minutach jednoczesnej pracy czajnika i ekspresu → przeciążenie (2,2 + 1,5 + 0,9 kW ≈ 20 A na B16). Jeśli od razu przy włączeniu jednego urządzenia → zwarcie w urządzeniu.
4. **Naprawa:** rozdzielenie urządzeń na dwa obwody ([17.02](modules/17-pomieszczenia-szczegolne/17.02-kuchnia.md)) albo — jeśli zwarcie — naprawa urządzenia. **Nie** wymiana B16 na B20.

</details>

🔎 **[20.02](modules/20-diagnostyka-usterek/20.02-nie-dziala-gniazdo-albo-caly-obwod.md#przykład)** · Nie działa gniazdo albo cały obwód

**Zadanie.** W sypialni nie działają dwa gniazda przy łóżku, działa gniazdo przy drzwiach i przy biurku. Pomiar w martwym: L–N 0 V, L–PE 0 V, N–PE 0 V. Wyłącznik załączony. Co dalej?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Brak fazy w martwych gniazdach przy załączonym wyłączniku → **przerwa L** przed nimi. Gniazda przy łóżku są dalej w łańcuchu niż te przy drzwiach i biurku. Ostatnie działające (przy biurku, jeśli jest bliżej łóżka) — wyłącz obwód, otwórz je i sprawdź zacisk L z przelotem do gniazd przy łóżku. Jeśli tam wszystko jest dobrze — szukaj puszki rozgałęźnej na trasie.

</details>

🔎 **[20.03](modules/20-diagnostyka-usterek/20.03-wybija-wylacznik-roznicowopradowy.md#przykład)** · Wybija wyłącznik różnicowoprądowy

**Zadanie.** Różnicówka grupy łazienka + kuchnia wybija od razu. Po wyłączeniu wszystkich wyłączników za nią — **dalej wybija**. Co to oznacza?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Wyłączniki 1P odcięły L, ale nie N. Wybijanie przy wyłączonych obwodach oznacza, że **prąd ucieka przez N**: połączenie N–PE w którymś obwodzie grupy (np. zalana puszka, gwóźdź przebijający N i PE, oprawa z mostkiem) albo N tej grupy połączony z N innej grupy, przez który płynie prąd odbiorników z drugiej różnicówki. Szukanie: odłączaj kolejno przewody N obwodów od listwy N grupy (po wyłączeniu napięcia) i próbuj załączyć — obwód, po odłączeniu którego RCD trzyma, jest winny. Potem pomiar izolacji N–PE w tym obwodzie.

</details>

🧮 **[20.04](modules/20-diagnostyka-usterek/20.04-wybija-wylacznik-nadpradowy.md#przykład)** · Wybija wyłącznik nadprądowy

**Zadanie.** B16 obwodu gniazd w pokoju wybija po ok. 20 minutach, kiedy pracują grzejnik olejowy 2,5 kW i suszarka do ubrań 2 kW. Co to jest i co zrobić?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** $I = 4500/230 \approx 19{,}6$ A — więcej niż 1,13 × 16 ≈ 18 A, więc wyłącznik **ma prawo** zadziałać po kilkunastu minutach. Zadziałanie **po czasie** → **przeciążenie** (wyzwalacz termiczny). Potwierdź cęgami prądowymi. Rozwiązanie: grzejnik na innym obwodzie, nie większy wyłącznik. Gdyby cęgi pokazały np. 12 A, a wyłącznik był ciepły — przyczyną byłby luźny zacisk lub zużyty aparat.

</details>

🔎 **[20.05](modules/20-diagnostyka-usterek/20.05-przerwa-w-przewodzie-neutralnym.md#przykład)** · Przerwa w przewodzie neutralnym

**Zadanie.** W domu z zasilaniem trójfazowym nagle: w kuchni żarówki świecą bardzo jasno, w salonie ledwo, lodówka buczy. Pomiar w gnieździe kuchni: L–N 290 V, L–PE 232 V. Co się stało?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** L–PE prawidłowe, L–N za duże → **przerwa N** (lub bardzo słaby styk) w części wspólnej — prawdopodobnie na głównej listwie N, w WLZ albo w złączu. Natychmiast **wyłączyć rozłącznik główny**. Sprawdzić (elektryk) zaciski N w rozdzielnicy głównej; jeśli są w porządku — zgłosić do OSD (przerwa przed licznikiem lub w sieci).

</details>

🔎 **[20.06](modules/20-diagnostyka-usterek/20.06-grzejace-sie-zaciski-i-zapach-spalenizny.md#przykład)** · Grzejące się zaciski i zapach spalenizny

**Zadanie.** Wtyczka czajnika jest gorąca po zagotowaniu wody, a wokół jednego otworu gniazda widać brązowy ślad. Co robisz?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Wyłącz obwód. Wymień **gniazdo** (styk przegrzany, sprężyna osłabiona). Obejrzyj żyły w puszce — przebarwione końcówki odetnij. Obejrzyj **wtyczkę czajnika** — przebarwiony kołek lub nalot → wymiana wtyczki (lub przewodu) przez serwis. Sprawdź, czy czajnik nie był podłączony przez rozgałęźnik. Po naprawie wtyczka po zagotowaniu powinna być co najwyżej lekko ciepła.

</details>

🔎 **[20.07](modules/20-diagnostyka-usterek/20.07-migajace-i-zarzace-sie-led.md#przykład)** · Migające i żarzące się LED

**Zadanie.** W przedpokoju układ schodowy z dwoma łącznikami, przewody między nimi po 8 m. Po wymianie żarówek na LED lampa po wyłączeniu słabo świeci. Łączniki bez podświetlenia. Co robisz?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Najpierw sprawdź, czy przy wyłączonej lampie na oprawie nie ma fazy (łącznik w N) — to byłoby groźne. Jeśli faza jest prawidłowo przerywana, przyczyną jest **pojemność długich korespondencji**: przewód fazowy i korespondencja leżą obok siebie na kilkunastu metrach. Rozwiązania: element obciążający przy lampie (dedykowany kompensator LED / kondensator X2), żarówka mniej czuła na mały prąd albo przebudowa na przekaźnik impulsowy przy lampie.

</details>

---

## 21 — Stare instalacje

🔎 **[21.01](modules/21-stare-instalacje/21.01-jak-rozpoznac-stara-instalacje.md#przykład)** · Jak rozpoznać starą instalację

**Zadanie.** Mieszkanie z 1978 r. W przedpokoju tablica z czterema bezpiecznikami wkręcanymi 10 A, w gnieździe dwie srebrne żyły i mostek do bolca. Oceń i zaproponuj kolejne kroki.

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Cechy starej instalacji: **aluminium, dwie żyły, zerowanie, bezpieczniki topikowe, brak RCD**. Kroki: (1) pomiary przez elektryka (izolacja, pętla, stan połączeń), (2) sprawdzenie WLZ (czy jest PEN o przekroju pozwalającym na rozdział), (3) decyzja: przy remoncie — **wymiana całej instalacji** ([21.05](modules/21-stare-instalacje/21.05-wymiana-instalacji-plan-prac.md)); bez remontu — modernizacja częściowa: nowa rozdzielnica, nowe obwody dla kuchni i łazienki, usunięcie mostków ([21.04](modules/21-stare-instalacje/21.04-modernizacja-czesciowa.md)).

</details>

🧮 **[21.02](modules/21-stare-instalacje/21.02-przewody-aluminiowe-zagrozenia-i-postepowanie.md#przykład)** · Przewody aluminiowe — zagrożenia i postępowanie

**Zadanie.** W kuchni z instalacją Al 2,5 mm² (2 żyły) chcesz podłączyć zmywarkę 2,2 kW. Czy wystarczy wymienić gniazdo?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Nie. Obwód aluminiowy 2,5 mm² obsługuje zwykle kilka gniazd; dodanie zmywarki (ok. 10 A przez dłuższy czas) obciąży stare połączenia, które najłatwiej się grzeją. Do tego brak PE — zmywarka z metalowymi częściami w wilgotnym otoczeniu. Właściwie: **nowy obwód miedziany 3 × 2,5 mm²** z rozdzielnicy (z punktu rozdziału PEN, [21.04](modules/21-stare-instalacje/21.04-modernizacja-czesciowa.md)), B16, RCD 30 mA typ A.

</details>

🔎 **[21.03](modules/21-stare-instalacje/21.03-mostkowanie-bolca-ochronnego-w-gniazdku.md#przykład)** · Mostkowanie bolca ochronnego w gniazdku — dlaczego zabija

**Zadanie.** Pralka w łazience w bloku z lat 70. podłączona do gniazda z mostkiem. Sąsiad zgłosił, że „kopie” przy dotknięciu pralki i wanny jednocześnie, ale tylko czasem. Co się dzieje?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Najpewniej **słaby styk N** (utleniony zacisk aluminiowy w puszce) przed gniazdem: przy pracy pralki na rezystancji styku odkłada się kilkanaście–kilkadziesiąt woltów, które przez mostek trafiają na obudowę pralki. Wanna ma potencjał ziemi (rury) → napięcie między pralką a wanną. Przy całkowitej przerwie N byłoby ok. 230 V. **Natychmiast**: odłączyć pralkę, wyłączyć obwód, usunąć mostek, naprawić połączenia N; docelowo nowy obwód z PE i RCD 30 mA dla łazienki ([17.01](modules/17-pomieszczenia-szczegolne/17.01-lazienka-strefy-0-1-i-2.md)).

</details>

🧮 **[21.04](modules/21-stare-instalacje/21.04-modernizacja-czesciowa.md#przykład)** · Modernizacja częściowa

**Zadanie.** Mieszkanie w bloku: WLZ 4 × 16 mm² Al (L1, L2, L3, PEN), tablica z bezpiecznikami, instalacja dwuprzewodowa Al. Planujesz remont tylko łazienki i kuchni. Co zrobić?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.**

1. PEN 16 mm² Al — **można** rozdzielić w rozdzielnicy mieszkania (≥ 16 mm² Al).
2. Nowa rozdzielnica: rozłącznik, SPD, listwy PE i N z jednym mostkiem (punkt rozdziału), 2 × RCD 30 mA typ A, wyłączniki.
3. Nowe obwody 3-żyłowe Cu: łazienka (gniazda, oświetlenie), kuchnia (gniazda nad blatem, płyta 3-faz., zmywarka), pralka.
4. Stare obwody pokoi: przegląd, **usunięcie mostków**, podłączenie do listwy N; jeśli N obwodów nie są wspólne — za RCD.
5. Pomiary i protokół; w opisie rozdzielnicy — które obwody są stare.

</details>

🔎 **[21.05](modules/21-stare-instalacje/21.05-wymiana-instalacji-plan-prac.md#przykład)** · Wymiana instalacji — plan prac

**Zadanie.** Kawalerka 32 m² w bloku, instalacja Al dwuprzewodowa, WLZ 1-faz. 10 mm² Cu (L, PEN). Kolejność i zakres wymiany?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.**

1. Pomiary i projekt: PEN 10 mm² Cu — rozdział możliwy; obwody: oświetlenie (2), gniazda pokój, gniazda kuchnia, łazienka, płyta (1-faz. — ograniczenie mocy płyty lub uzgodnienie zwiększenia mocy), pralka, rezerwa.
2. Zarządca — zgoda na prace, informacja o stanie WLZ.
3. Zasilanie tymczasowe, demontaż starej instalacji.
4. Bruzdy, puszki, przewody Cu 3-żyłowe, zdjęcia.
5. Rozdzielnica: rozłącznik, SPD, 2 × RCD 30 mA typ A, wyłączniki, punkt rozdziału PEN ([15.04](modules/15-rozdzielnica-mieszkaniowa/15.04-przyklad-kawalerka-zasilanie-jednofazowe.md)).
6. Pomiar izolacji, tynki, malowanie, osprzęt.
7. Pomiary odbiorcze, protokół, schemat w rozdzielnicy.

</details>

---

## 22 — Przyrządy pomiarowe

🧮 **[22.01](modules/22-przyrzady-pomiarowe/22.01-kategorie-pomiarowe-cat-iiiv-i-bezpieczenstwo.md#przykład)** · Kategorie pomiarowe CAT II–IV i bezpieczeństwo przyrządów

**Zadanie.** Masz multimetr „CAT III 600 V / CAT IV 300 V” z przewodami „CAT II 1000 V”. Czy możesz zmierzyć napięcie na zaciskach wyjściowych licznika w złączu 230/400 V?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Miernik — tak (CAT IV 300 V wystarcza, bo napięcie względem ziemi to 230 V). Ale **zestaw** ma kategorię najsłabszego elementu — przewody to tylko **CAT II**. Do złącza potrzebne są przewody co najmniej CAT IV 300 V (najlepiej z osłonkami ostrzy). Do tego: licznik i złącze należą do operatora — pomiar wykonuje się tylko z uprawnieniami i bez ingerencji w plomby.

</details>

🔎 **[22.02](modules/22-przyrzady-pomiarowe/22.02-multimetr-co-i-jak-mierzy.md#przykład)** · Multimetr — co i jak mierzy

**Zadanie.** Odłączony przewód w puszce (żyła czarna) — multimetr pokazuje między nim a PE 87 V. Wskaźnik dwubiegunowy nic nie pokazuje. Co to jest?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** To **napięcie indukowane** (sprzężenie pojemnościowe z żyłą pod napięciem biegnącą obok). Multimetr ma wejście ok. 10 MΩ i „widzi” bardzo mały prąd, wskaźnik z obciążeniem — nie. Żyła nie jest podłączona do fazy, ale **zanim jej dotkniesz**, i tak sprawdź pomiar ponownie po wyłączeniu obwodów, z którymi biegnie, i traktuj ją jak będącą pod napięciem, dopóki nie wiesz, skąd pochodzi.

</details>

🔎 **[22.03](modules/22-przyrzady-pomiarowe/22.03-cegi-pradowe.md#przykład)** · Cęgi prądowe

**Zadanie.** Różnicówka 30 mA w kuchni wybija losowo. Cęgami upływowymi mierzysz przewody obwodów (L i N razem): gniazda blat 1,2 mA, zmywarka 9,5 mA, lodówka 0,8 mA, piekarnik 1,0 mA. Wniosek?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Suma ok. 12,5 mA — powyżej zalecanych ~9 mA dla RCD 30 mA, a sama **zmywarka 9,5 mA** to dużo jak na jedno urządzenie. Najpierw sprawdź zmywarkę (grzałka, pompa, zawilgocenie). Jeśli jest sprawna (upływ wynika z filtrów), daj jej osobne RCBO ([08.07](modules/08-wylaczniki-roznicowopradowe/08.07-podzial-obwodow-miedzy-wylaczniki.md)).

</details>

🔎 **[22.04](modules/22-przyrzady-pomiarowe/22.04-wskazniki-napiecia-i-probniki.md#przykład)** · Wskaźniki napięcia i próbniki

**Zadanie.** Elektryk wyłączył obwód, długopis bezdotykowy „milczy”, neonówka nie świeci. Czy może dotknąć przewodów w puszce?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** **Nie.** Ani długopis, ani neonówka nie stwierdzają braku napięcia. Potrzebny jest **wskaźnik dwubiegunowy**: sprawdzony na znanym źródle, pomiar L–N, L–PE, N–PE w puszce (także na przewodach przelotowych), ponowne sprawdzenie wskaźnika. Dopiero wtedy — praca.

</details>

🔎 **[22.05](modules/22-przyrzady-pomiarowe/22.05-miernik-parametrow-instalacji-mpi-przeglad.md#przykład)** · Miernik parametrów instalacji (MPI) — przegląd funkcji

**Zadanie.** Dostajesz zlecenie: pomiary okresowe w mieszkaniu (TN-S, 10 obwodów, 2 RCD). Jakie funkcje MPI wykorzystasz?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Ciągłość PE (bolce gniazd, oprawy klasy I, połączenia wyrównawcze w łazience), rezystancja izolacji każdego obwodu (500 V, po odłączeniu odbiorników), impedancja pętli zwarcia w każdym obwodzie (najdalszy punkt; tryb bez wyzwalania RCD), badanie obu RCD (czas przy IΔn, prąd zadziałania, napięcie dotykowe). Uziemienie — jeśli instalacja ma własny uziom do oceny (dom, TT). Wyniki w pamięci → protokół.

</details>

🧮 **[22.06](modules/22-przyrzady-pomiarowe/22.06-kamera-termowizyjna-kiedy-sie-przydaje.md#przykład)** · Kamera termowizyjna — kiedy się przydaje

**Zadanie.** W rozdzielnicy trójfazowej kamera pokazuje zaciski: L1 42 °C, L2 44 °C, L3 63 °C przy podobnych prądach (cęgi: 18, 19, 18 A). Otoczenie 25 °C. Co robić?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Porównanie z podobnymi elementami: ΔT = 63 − 44 = **19 °C > 15 °C** → **poważna usterka, naprawa natychmiast**. Prądy są podobne, więc przyczyną nie jest przeciążenie, tylko zacisk L3 (luźny, utleniony). Po wyłączeniu napięcia: sprawdzenie i dokręcenie, ocena przebarwień, ewentualnie wymiana aparatu i końcówki przewodu. Potem ponowny pomiar pod obciążeniem.

</details>

---

## 23 — Pomiary odbiorcze i okresowe

🔎 **[23.01](modules/23-pomiary-odbiorcze-i-okresowe/23.01-ogledziny-instalacji.md#przykład)** · Oględziny instalacji

**Zadanie.** Oględziny mieszkania: w rozdzielnicy brak dwóch zaślepek, B20 na przewodzie 1,5 mm² (oświetlenie), gniazdo w łazience 40 cm od wanny, przewody opisane. Jaki wynik?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** **Negatywny** — trzy usterki: (1) brak zaślepek → dostęp do części czynnych (ochrona podstawowa), (2) B20 na 1,5 mm² → przewód nie chroniony przed przeciążeniem, (3) gniazdo w strefie 2 łazienki. Każdą wpisuje się do protokołu z zaleceniem usunięcia; pomiary wykonuje się, ale instalacja nie nadaje się do eksploatacji do czasu poprawek.

</details>

🧮 **[23.02](modules/23-pomiary-odbiorcze-i-okresowe/23.02-ciaglosc-przewodow-ochronnych-i-wyrownawczych.md#przykład)** · Ciągłość przewodów ochronnych i wyrównawczych

**Zadanie.** Obwód gniazd: przewód 3 × 2,5 mm², długość do ostatniego gniazda 24 m. Wynik ciągłości PE do tego gniazda: 0,95 Ω. Ocena?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Spodziewana rezystancja PE: $24 \cdot 0{,}00741 \approx 0{,}18\ \Omega$ (plus kilka setnych na zaciskach). Wynik **0,95 Ω** to ok. pięć razy więcej → **złe połączenie** gdzieś na drodze PE (luźny zacisk w gnieździe przelotowym, utleniona złączka). Mierz kolejne gniazda od rozdzielnicy — skok wyniku wskaże miejsce.

</details>

🔎 **[23.03](modules/23-pomiary-odbiorcze-i-okresowe/23.03-rezystancja-izolacji.md#przykład)** · Rezystancja izolacji

**Zadanie.** Obwód gniazd w starym mieszkaniu: L+N względem PE — 0,6 MΩ przy 500 V. Ocena?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Wymagane **≥ 1,0 MΩ** → wynik **negatywny**. Kroki: sprawdź, czy wszystko jest odłączone (np. zapomniana listwa z filtrem), zmierz osobno L–PE i N–PE, dziel obwód na odcinki (rozłączenie w puszkach), szukaj zawilgocenia (gniazdo przy oknie, zewnętrzne, w łazience). Po naprawie — powtórzenie pomiaru.

</details>

🧮 **[23.04](modules/23-pomiary-odbiorcze-i-okresowe/23.04-impedancja-petli-zwarcia.md#przykład)** · Impedancja pętli zwarcia

**Zadanie.** Gniazdo na końcu obwodu B16: $Z_s = 1{,}75\ \Omega$. Spełniony warunek? A dla C16?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.**

- B16: $Z_{s,max} = 230 / 80 = 2{,}88\ \Omega$; z zapasem ⅔: 1,92 Ω. $1{,}75 \le 1{,}92$ → **spełniony** (z zapasem). $I_k = 230/1{,}75 \approx 131$ A — wyłącznik B16 zadziała natychmiast (> 80 A).
- C16: $Z_{s,max} = 230 / 160 = 1{,}44\ \Omega$ → **niespełniony** (1,75 > 1,44). Zmiana B16 na C16 „bo wybija przy rozruchu” byłaby w tym obwodzie błędem — chyba że obwód chroni RCD 30 mA.

</details>

🧮 **[23.05](modules/23-pomiary-odbiorcze-i-okresowe/23.05-badanie-wylacznikow-roznicowopradowych.md#przykład)** · Badanie wyłączników różnicowoprądowych

**Zadanie.** RCD 30 mA typ A (ogólny). Wyniki: $I_A$ = 22 mA, $t_A$ przy IΔn = 28 ms, $U_B$ = 0,9 V. Ocena?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Prąd zadziałania 22 mA mieści się w 15–30 mA → **dobrze**. Czas 28 ms ≤ 300 ms → **dobrze**. Napięcie dotykowe 0,9 V ≤ 50 V → **dobrze** (bardzo mała rezystancja pętli PE). RCD sprawny.

</details>

🧮 **[23.06](modules/23-pomiary-odbiorcze-i-okresowe/23.06-rezystancja-uziemienia.md#przykład)** · Rezystancja uziemienia

**Zadanie.** Dom w układzie TT, RCD 30 mA (ogólny) jako ochrona przy uszkodzeniu. Zmierzona rezystancja uziemienia $R_A = 85\ \Omega$. Ocena?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Warunek: $R_A \cdot I_{\Delta n} = 85 \cdot 0{,}03 = 2{,}55$ V ≤ 50 V → **spełniony**. Mimo to 85 Ω to dużo jak na uziom budynku — przy różnicówce 300 mA na przyłączu: $85 \cdot 0{,}3 = 25{,}5$ V — też spełnione. Warto rozważyć poprawę uziomu (dodatkowe pręty), zwłaszcza jeśli dom ma instalację odgromową i SPD typu 1.

</details>

🔎 **[23.07](modules/23-pomiary-odbiorcze-i-okresowe/23.07-kolejnosc-faz.md#przykład)** · Kolejność faz

**Zadanie.** Po wymianie rozdzielnicy w warsztacie kompresor tłokowy (silnik 3-faz.) kręci się w drugą stronę. Co zrobić?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Wskaźnikiem kolejności faz zbadaj gniazdo kompresora i inne gniazda trójfazowe. Jeśli wszystkie mają odwrotną kolejność — zamień dwie fazy na **zasilaniu rozdzielnicy** (po wyłączeniu). Jeśli tylko jedno — popraw podłączenie tego gniazda. Sprawdź ponownie wskaźnikiem i kierunek obrotów kompresora.

</details>

🔎 **[23.08](modules/23-pomiary-odbiorcze-i-okresowe/23.08-protokol-z-pomiarow-i-terminy-badan-okresowych.md#przykład)** · Protokół z pomiarów i terminy badań okresowych

**Zadanie.** Właściciel domu jednorodzinnego (2015 r.) pyta, czy musi „robić pomiary”. Co mu odpowiesz?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Prawo budowlane (art. 62) wymaga kontroli stanu technicznego, w tym **instalacji elektrycznej i piorunochronnej, co najmniej raz na 5 lat** — także w domach jednorodzinnych. Kontrola obejmuje m.in. skuteczność ochrony przeciwporażeniowej, rezystancję izolacji i uziemień, czyli pomiary. Wykonuje ją osoba z odpowiednimi kwalifikacjami; wynikiem jest protokół. Niezależnie od przepisu — protokół przydaje się przy szkodzie i sprzedaży domu.

</details>

---

## 24 — Silniki i napędy

🧮 **[24.01](modules/24-silniki-i-napedy/24.01-silnik-indukcyjny-trojfazowy.md#przykład)** · Silnik indukcyjny trójfazowy

**Zadanie.** Na tabliczce: 1440 obr/min, 50 Hz. Ile biegunów i jaki poślizg?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Najbliższa wyższa prędkość synchroniczna to **1500 obr/min** → $p = 60 \cdot 50 / 1500 = 2$ pary, czyli **4 bieguny**. Poślizg: $s = (1500 - 1440)/1500 = 0{,}04$ → **4 %**.

</details>

🧮 **[24.02](modules/24-silniki-i-napedy/24.02-tabliczka-znamionowa-silnika.md#przykład)** · Tabliczka znamionowa silnika

**Zadanie.** Tabliczka: 4 kW, 400/690 V Δ/Y, 8,1/4,7 A, cos φ 0,82, 2900 obr/min. Jak podłączyć w sieci 400 V i jaka nastawa termika?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** 400 V odpowiada połączeniu **Δ** (trójkąt). Prąd w Δ: **8,1 A** → nastawa przekaźnika termicznego **8,1 A**. Silnik 2-biegunowy (synchronicznie 3000 obr/min, poślizg ok. 3,3 %). Ten silnik nadaje się do rozruchu gwiazda-trójkąt.

</details>

🧮 **[24.03](modules/24-silniki-i-napedy/24.03-polaczenie-w-gwiazde-i-w-trojkat.md#przykład)** · Połączenie w gwiazdę i w trójkąt

**Zadanie.** Silnik: „Δ 230 V / Y 400 V, 6,4/3,7 A”. Sieć 3 × 400 V. Jak połączyć, jaki prąd pobiera i czy można go rozruszać metodą gwiazda-trójkąt?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Uzwojenie na 230 V → w sieci 400 V **gwiazda**. Prąd: **3,7 A**. Rozruch gwiazda-trójkąt **nie** — po przełączeniu na trójkąt uzwojenia dostałyby 400 V. Do łagodnego rozruchu — softstart albo falownik.

</details>

🧮 **[24.04](modules/24-silniki-i-napedy/24.04-rozruch-bezposredni-gwiazda-trojkat-softstart.md#przykład)** · Rozruch: bezpośredni, gwiazda-trójkąt, softstart

**Zadanie.** Wentylator 11 kW, silnik 400/690 V Δ/Y, In(Δ) = 21 A. Ile wyniesie prąd rozruchowy bezpośrednio i w Y-Δ (zakładając 7 × In)?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Bezpośrednio: $7 \cdot 21 = 147$ A. W gwieździe: ok. $147 / 3 \approx 49$ A. Wentylator ma lekki rozruch (moment rośnie z prędkością), więc Y-Δ się nada. Softstart dałby podobne ograniczenie prądu z łagodniejszym przejściem, falownik — dodatkowo regulację wydajności.

</details>

🧮 **[24.05](modules/24-silniki-i-napedy/24.05-uklad-start-stop-ze-stycznikiem-i-przekaznikiem.md#przykład)** · Układ start-stop ze stycznikiem i przekaźnikiem termicznym

**Zadanie.** Silnik pompy 2,2 kW, 400 V Y, In = 4,7 A, rozruch bezpośredni. Dobierz elementy układu start-stop.

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Q1 — wyłącznik silnikowy z zakresem nastawy np. 4–6,3 A, ustawiony na **4,7 A** (wtedy osobny termik nie jest potrzebny) albo wyłącznik C10/C16 + przekaźnik termiczny 4–6 A ustawiony na **4,7 A**, klasa 10. K1 — stycznik w kategorii AC-3 o prądzie ≥ 4,7 A (np. 9 A), cewka 230 V, z zestykiem pomocniczym 13-14. S0 STOP (rozwierny), S1 START (zwierny). Przewód zasilający silnik 4 × 1,5 mm² + PE (5 żył) zależnie od długości.

</details>

🔎 **[24.06](modules/24-silniki-i-napedy/24.06-zmiana-kierunku-obrotow.md#przykład)** · Zmiana kierunku obrotów

**Zadanie.** Brama przesuwna z silnikiem 3-faz.: otwieranie, zamykanie, krańcówki w obu pozycjach. Jak zbudować sterowanie?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Dwa styczniki K1 (otwieranie) i K2 (zamykanie, zamiana L1↔L3) z blokadą mechaniczną. Obwód cewki K1: STOP → START „otwórz” (z podtrzymaniem K1) → krańcówka „otwarta” (rozwierna) → rozwierny K2 → cewka K1. Analogicznie K2 z krańcówką „zamknięta” i rozwiernym K1. Termik wspólny w obu obwodach. Do tego zatrzymanie awaryjne i — przy bramach — fotokomórki bezpieczeństwa.

</details>

🧮 **[24.07](modules/24-silniki-i-napedy/24.07-przemienniki-czestotliwosci.md#przykład)** · Przemienniki częstotliwości

**Zadanie.** Wentylator wyciągowy 7,5 kW pracuje zwykle z 70 % wydajności, regulowanej przepustnicą. Ile mocy zaoszczędzi falownik?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Z prawa sześcianu: przy 70 % obrotów potrzeba ok. $0{,}7^3 \approx 34\ \%$ mocy, czyli ok. **2,6 kW** zamiast prawie pełnych 7,5 kW (przepustnica zmniejsza moc tylko nieznacznie). Oszczędność rzędu kilku kW przy każdej godzinie pracy — falownik zwraca się zwykle w krótkim czasie.

</details>

🧮 **[24.08](modules/24-silniki-i-napedy/24.08-silniki-jednofazowe.md#przykład)** · Silniki jednofazowe

**Zadanie.** Masz silnik 3~ 0,75 kW, 230/400 V Δ/Y, i tylko gniazdo 230 V. Jak go uruchomić awaryjnie i co lepiej zrobić?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Awaryjnie: połączyć w **trójkąt** (230 V na uzwojenie), kondensator pracy ok. $0{,}75 \cdot 70 \approx 50\ \mu\mathrm{F}$, 450 V AC, między jeden zacisk a trzeci (wg schematu). Moc spadnie do ok. 0,5 kW, rozruch będzie słaby. Lepiej: **falownik 1 × 230 V → 3 × 230 V** 0,75 kW — pełna moc, łagodny rozruch, regulacja prędkości. W obu przypadkach obudowa silnika — do PE, obwód za RCD.

</details>

---

## 25 — Transformatory, zasilacze, UPS i agregaty

🧮 **[25.01](modules/25-transformatory-ups-agregaty/25.01-transformator-separacyjny-i-bezpieczenstwa.md#przykład)** · Transformator separacyjny i bezpieczeństwa

**Zadanie.** Serwisant chce zasilić przez jeden transformator separacyjny 230/230 V 400 VA lutownicę (60 W) i otwarty zasilacz komputerowy (pobór 200 W). Czy tak można?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Moc wystarcza (260 W < 400 VA), ale to **dwa odbiorniki** na jednym uzwojeniu. Jeśli w lutownicy przebije się izolacja do obudowy na jednym przewodzie, a w zasilaczu na drugim, między obudową lutownicy a elementami zasilacza pojawi się 230 V. Poprawnie: **osobny transformator dla każdego odbiornika** albo lutownica z normalnego gniazda z RCD.

</details>

🧮 **[25.02](modules/25-transformatory-ups-agregaty/25.02-zasilacze-impulsowe.md#przykład)** · Zasilacze impulsowe

**Zadanie.** W biurze na jednym obwodzie z RCD 30 mA pracuje 8 komputerów, każdy z prądem upływu ok. 1 mA, i drukarka (ok. 1,5 mA). Czy to rozsądny podział?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Suma upływów: 8 · 1 + 1,5 = **9,5 mA**, czyli ok. **0,32 · IΔn**. To już granica zalecenia (0,3 · IΔn ≈ 9 mA), a RCD może zadziałać przy prądzie od 0,5 · IΔn = 15 mA — wystarczy kilka mA więcej przy włączaniu, by zaczął wybijać. Lepiej podzielić na **dwa obwody z osobnymi RCD**.

</details>

🧮 **[25.03](modules/25-transformatory-ups-agregaty/25.03-ups-rodzaje-i-zastosowanie.md#przykład)** · UPS — rodzaje i zastosowanie

**Zadanie.** Pompa obiegowa pieca pobiera 60 W, sterownik 10 W. UPS ma dwa akumulatory 12 V 9 Ah połączone szeregowo (24 V). Jak długo podtrzyma zasilanie?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Energia nominalna: 24 V · 9 Ah = **216 Wh**. Realnie użyteczne ok. 65 % → ok. **140 Wh**. Obciążenie 70 W → czas ok. 140 / 70 = **2 h**. Na dłuższą awarię potrzebny jest większy akumulator zewnętrzny albo agregat ([25.04](modules/25-transformatory-ups-agregaty/25.04-agregat-pradotworczy-i-przelacznik-zasilania.md)).

</details>

🔎 **[25.04](modules/25-transformatory-ups-agregaty/25.04-agregat-pradotworczy-i-przelacznik-zasilania.md#przykład)** · Agregat prądotwórczy i przełącznik zasilania

**Zadanie.** Na czas awarii chcesz zasilić: piec gazowy z pompą (120 W), lodówkę (150 W, rozruch sprężarki ok. 3×), oświetlenie LED (100 W), router i laptop (80 W), pompę studni (900 W, rozruch ok. 3×). Jaki agregat?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Suma pracy ciągłej: 120 + 150 + 100 + 80 + 900 = **1350 W**. Z zapasem 25 %: ok. **1,7 kW** mocy ciągłej. Najgorszy moment to rozruch pompy studni przy pracującej reszcie: 450 + 2700 ≈ **3,2 kW chwilowo**. Wybierz agregat **ok. 2 kW ciągłej / 3+ kW maksymalnej** (dla pieca najlepiej inwerterowy) albo nie uruchamiaj pompy studni razem z lodówką.

</details>

🔎 **[25.05](modules/25-transformatory-ups-agregaty/25.05-dlaczego-nie-zasila-sie-domu-przez-gniazdo.md#przykład)** · Dlaczego nie zasila się domu przez gniazdo

**Zadanie.** Sąsiad mówi: „Wyłączam główny w RG, potem wtykam agregat do gniazdka w garażu, więc nic do sieci nie idzie”. Co jest źle?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Bezpieczeństwo zależy wyłącznie od pamięci i uwagi jednej osoby — nie ma blokady wykluczającej jednoczesne podłączenie. Wtyczka na końcu przewodu ma odsłonięte bolce pod napięciem przy wpinaniu i wypinaniu. Gniazdo w garażu i jego obwód nie są przewidziane do zasilania całej instalacji (przekrój, zabezpieczenie), a ochrona przeciwporażeniowa nie jest sprawdzona dla takiego zasilania. Poprawnie: przełącznik I-0-II za licznikiem montowany przez elektryka z uprawnieniami.

</details>

---

## 26 — Fotowoltaika, pompy ciepła, wallboxy i magazyny energii

🧮 **[26.01](modules/26-fotowoltaika-pompy-wallboxy/26.01-fotowoltaika-budowa-instalacji.md#przykład)** · Fotowoltaika — budowa instalacji

**Zadanie.** Dom ma moc przyłączeniową 14 kW. Właściciel chce 10 kWp paneli. Jakie formalności?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** 10 kW ≤ 50 kW i ≤ 14 kW mocy przyłączeniowej → to **mikroinstalacja** przyłączana na **zgłoszenie do OSD**. Ponieważ 10 kW > 6,5 kW, potrzebne jest **uzgodnienie projektu z rzeczoznawcą ds. zabezpieczeń przeciwpożarowych** i **zawiadomienie PSP** po zakończeniu montażu. Szacunkowa produkcja: ok. 10 · 1000 = **10 000 kWh rocznie**.

</details>

🧮 **[26.02](modules/26-fotowoltaika-pompy-wallboxy/26.02-strona-dc-zagrozenia-i-zabezpieczenia.md#przykład)** · Strona DC — zagrożenia i zabezpieczenia

**Zadanie.** Panel ma Voc = 45 V (STC). Falownik przyjmuje maks. 1000 V DC. Ile paneli w łańcuchu i jaki ogranicznik DC?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Z zapasem na mróz: $n \le 1000 / (1{,}2 \cdot 45) = 1000 / 54 \approx 18{,}5$ → **maks. 18 paneli**. Voc łańcucha (STC): 18 · 45 = 810 V. Ogranicznik: Ucpv ≥ 1,2 · 810 = **972 V** → dobierz **SPD DC o Ucpv = 1000 V** (lub wyższym, np. 1100 V). Dla 20 paneli wyszłoby 20 · 54 = 1080 V > 1000 V — za dużo.

</details>

🧮 **[26.03](modules/26-fotowoltaika-pompy-wallboxy/26.03-falownik-i-przylaczenie-mikroinstalacji.md#przykład)** · Falownik i przyłączenie mikroinstalacji

**Zadanie.** Napięcie w RG w południe: 249 V. Falownik 10 kW trójfazowy jest podłączony przewodem 5 × 2,5 mm² o długości 30 m. Prąd na fazę ok. 14,5 A. Czy przewód przyczynia się do wyłączeń?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Spadek napięcia na fazie (Cu, ρ ≈ 0,0175): $\Delta U \approx I \cdot \rho \cdot l / S = 14{,}5 \cdot 0{,}0175 \cdot 30 / 2{,}5 \approx 3{,}0$ V. Falownik „widzi” ok. 249 + 3 = **252 V** — tuż pod granicą. Przewód 5 × 6 mm² zmniejszy spadek do ok. 1,3 V. Pomoże też autokonsumpcja; jeśli napięcie w RG stale przekracza 250 V, warto zgłosić to do OSD.

</details>

🔎 **[26.04](modules/26-fotowoltaika-pompy-wallboxy/26.04-pompa-ciepla-zasilanie-i-zabezpieczenia.md#przykład)** · Pompa ciepła — zasilanie i zabezpieczenia

**Zadanie.** Dom: moc przyłączeniowa 14 kW. Pompa ciepła: sprężarka maks. 3,5 kW + grzałka 6 kW. Płyta indukcyjna 7,4 kW, wallbox 11 kW. Co z mocą?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Najgorszy zimowy wieczór: 3,5 + 6 + 7,4 + 11 = **27,9 kW** (plus reszta domu) — dwukrotnie ponad moc przyłączeniową. Rozwiązania: **dynamiczne zarządzanie mocą** wallboxa ([26.05](modules/26-fotowoltaika-pompy-wallboxy/26.05-wallbox-i-ladowanie-samochodu.md)), blokada grzałki przy ładowaniu, ładowanie nocą, a jeśli to nie wystarczy — **wniosek o zwiększenie mocy przyłączeniowej**.

</details>

🧮 **[26.05](modules/26-fotowoltaika-pompy-wallboxy/26.05-wallbox-i-ladowanie-samochodu.md#przykład)** · Wallbox i ładowanie samochodu

**Zadanie.** Wallbox 11 kW, trasa od RG do garażu 35 m, przewód ułożony w rurce w ścianie. Dobierz zabezpieczenie i sprawdź spadek napięcia dla 5 × 2,5 mm² i 5 × 4 mm² (Cu, ρ ≈ 0,0175 Ω·mm²/m).

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Prąd: 11 000 / (√3 · 400) ≈ **16 A** → **C16 3P** + RCD (B lub A + RDC-DD). Spadek trójfazowy: $\Delta U\% = \frac{\sqrt{3} \cdot I \cdot \rho \cdot l}{S \cdot 400} \cdot 100$.
Dla 2,5 mm²: $\sqrt{3} \cdot 16 \cdot 0{,}0175 \cdot 35 / 2{,}5 \approx 6{,}8$ V → **1,7 %**. Dla 4 mm²: ok. 4,2 V → **1,1 %**. Oba mieszczą się w typowych 3 %, ale przy długotrwałym obciążeniu i ułożeniu w ścianie z innymi przewodami **5 × 4 mm²** daje zapas obciążalności i mniejsze grzanie — dobry wybór.

</details>

🧮 **[26.06](modules/26-fotowoltaika-pompy-wallboxy/26.06-magazyn-energii.md#przykład)** · Magazyn energii

**Zadanie.** Dom zużywa wieczorem i w nocy (18:00–7:00) ok. 6 kWh. Magazyn ma 10 kWh pojemności nominalnej i 90 % pojemności użytecznej. Czy wystarczy na noc i ile zostanie na awarię?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Pojemność użyteczna: 10 · 0,9 = **9 kWh**. Po nocy zostaje ok. 9 − 6 = **3 kWh**, jeśli w dzień bateria się naładowała. Gdy rano wystąpi awaria, 3 kWh wystarczy na kilka godzin zasilania lodówki, pieca, routera i oświetlenia (razem ok. 300–400 W). Część pojemności można zarezerwować w ustawieniach na backup (np. 20 %).

</details>

---

## 27 — Inteligentny dom

🧮 **[27.01](modules/27-inteligentny-dom/27.01-moduly-bezprzewodowe-w-puszce-bezpieczny-montaz.md#przykład)** · Moduły bezprzewodowe w puszce — bezpieczny montaż

**Zadanie.** Lampa LED 8 × 7 W w salonie, moduł o styku „16 A”, ale w instrukcji: „LED — maks. 200 W”. Czy wystarczy? Co, jeśli właściciel chce też podłączyć do modułu grzejnik konwektorowy 2000 W?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Oświetlenie: 8 · 7 = **56 W** < 200 W — w porządku. Grzejnik 2000 W to ok. **8,7 A** — w granicy styku, ale długotrwałe obciążenie w ciasnej puszce grzeje moduł. Rozsądniej: moduł steruje **stycznikiem modułowym** w rozdzielnicy, a grzejnik jest na osobnym obwodzie ([10.02](modules/10-aparatura-modulowa/10.02-stycznik-modulowy-i-przekaznik-bistabilny.md)).

</details>

🔎 **[27.02](modules/27-inteligentny-dom/27.02-przewod-neutralny-w-puszce-lacznika.md#przykład)** · Przewód neutralny w puszce łącznika

**Zadanie.** W puszce łącznika są dwie żyły: brązowa i czarna, plus żółto-zielona. Właściciel chce łącznik dotykowy wymagający N. Co proponujesz?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Brązowa to zapewne L, czarna — przewód do lampy (sprawdź pomiarem). N w puszce nie ma, **PE nie może go zastąpić**. Możliwości: łącznik dotykowy w wersji **bez N** (z bypassem przy LED), **moduł przy lampie** z łącznikiem zwykłym/przyciskiem, albo — jeśli przewody są w rurce — **przeciągnięcie przewodu z dodatkową żyłą**.

</details>

🔎 **[27.03](modules/27-inteligentny-dom/27.03-systemy-przewodowe-knx-modbus-przeglad.md#przykład)** · Systemy przewodowe: KNX, Modbus — przegląd

**Zadanie.** Do sterownika domowego (master Modbus) w rozdzielnicy podłączasz licznik energii (w rozdzielnicy), falownik PV (garaż, 25 m) i pompę ciepła (kotłownia, 15 m dalej). Jak ułożyć magistralę?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Łańcuchowo: **sterownik → licznik → falownik → pompa**, jednym przewodem skrętkowym z parą A/B i żyłą masy (np. przewód do RS-485 lub skrętka). **Terminatory 120 Ω** na pierwszym (sterownik) i ostatnim (pompa) urządzeniu — wiele urządzeń ma je wbudowane do włączenia przełącznikiem. Przewód magistrali w osobnej rurce lub z odpowiednią izolacją, oddzielony od przewodów 230 V.

</details>

🧮 **[27.04](modules/27-inteligentny-dom/27.04-automatyka-w-rozdzielnicy.md#przykład)** · Automatyka w rozdzielnicy

**Zadanie.** Dom z KNX: 12 aktorów przekaźnikowych 4-kanałowych (po 4 moduły szerokości), 4 aktory ściemniające (po 4 moduły), zasilacz KNX (4 moduły), zasilacz 24 V (2 moduły), sterownik/serwer (4 moduły), router IP (2 moduły). Ile pól potrzeba na automatykę?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** 12 · 4 + 4 · 4 + 4 + 2 + 4 + 2 = 48 + 16 + 12 = **76 modułów**. Z rezerwą ok. 20 %: **ok. 92 moduły** — czyli osobna obudowa automatyki (np. 4 rzędy po 24 moduły) obok rozdzielnicy obwodów.

</details>

---

## 28 — BHP przy urządzeniach elektrycznych

🔎 **[28.01](modules/28-bhp-przy-urzadzeniach/28.01-organizacja-pracy-i-polecenia.md#przykład)** · Organizacja pracy i polecenia

**Zadanie.** Monter z świadectwem E (eksploatacja) dostaje telefon od kierownika: „wymień uszkodzoną głowicę kablową w stacji, polecenie przyślę jutro”. Co jest źle?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Praca przy urządzeniach w stacji (w pobliżu nieosłoniętych części pod napięciem, identyfikacja i przecinanie kabli) to praca w warunkach **szczególnego zagrożenia** — wymaga **polecenia pisemnego** przed rozpoczęciem, **zespołu** (min. 2 osoby), przygotowania strefy przez **dopuszczającego** i kierującego zespołem. „Polecenie jutro” nie istnieje — bez niego praca nie może się zacząć (chyba że to ratowanie życia lub mienia).

</details>

🔎 **[28.02](modules/28-bhp-przy-urzadzeniach/28.02-prace-w-warunkach-szczegolnego-zagrozenia.md#przykład)** · Prace w warunkach szczególnego zagrożenia

**Zadanie.** Elektryk ma wymienić oprawę w hali na wysokości 6 m z podnośnika, obok przebiega nieosłonięty szynoprzewód 400 V pod napięciem (odległość ok. 40 cm). Czy to praca w warunkach szczególnego zagrożenia?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Tak, z dwóch powodów: **praca na wysokości** i **w pobliżu nieosłoniętych urządzeń pod napięciem**. Wymaga **polecenia pisemnego** i **zespołu**. Najlepiej wyłączyć szynoprzewód; jeśli nie można — osłonić go i pilnować, by ani ręka, ani narzędzie nie przekroczyły odstępu (dla ≤ 1 kV — 300 mm granicy strefy w pobliżu, bez dotyku części czynnych).

</details>

🔎 **[28.03](modules/28-bhp-przy-urzadzeniach/28.03-przygotowanie-miejsca-pracy-i-dopuszczenie-do.md#przykład)** · Przygotowanie miejsca pracy i dopuszczenie do pracy

**Zadanie.** Wymiana wyłącznika w polu odpływowym rozdzielnicy nn w zakładzie. Podaj kolejność czynności dopuszczającego.

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Zgoda na łączenia → wyłączenie odpływu i rozłącznika, wyjęcie wkładek (widoczna przerwa) → kłódka i tablica „Nie załączać — pracują ludzie” → oznaczenie miejsc wyłączenia → sprawdzenie braku napięcia wskaźnikiem w miejscu pracy na wszystkich fazach i N → uziemienie i zwarcie (jeśli wymaga instrukcja; zawsze, gdy odpływ może dostać napięcie zwrotne) → osłony na sąsiednich polach pod napięciem i oznaczenie strefy → instruktaż kierującego → **wskazanie strefy, pisemne dopuszczenie**.

</details>

🔎 **[28.04](modules/28-bhp-przy-urzadzeniach/28.04-sprzet-ochronny-izolacyjny-i-ochrony-osobistej.md#przykład)** · Sprzęt ochronny izolacyjny i ochrony osobistej

**Zadanie.** Na rękawicach elektroizolacyjnych jest nadruk „Class 0”, data ostatniego badania sprzed 8 miesięcy, a producent wymaga badań co 6 miesięcy. W rękawicy jest drobne przetarcie. Czy można w nich pracować w rozdzielnicy 400 V?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** **Nie**, z dwóch powodów: minął termin badania okresowego wymagany przez producenta, a przetarcie dyskwalifikuje rękawice niezależnie od daty. Klasa 0 (1000 V) byłaby odpowiednia do 400 V — ale tylko sprawne i aktualnie zbadane rękawice.

</details>

🔎 **[28.05](modules/28-bhp-przy-urzadzeniach/28.05-prace-pod-napieciem-dlaczego-nie.md#przykład)** · Prace pod napięciem — dlaczego nie

**Zadanie.** Klient prosi o dołożenie obwodu w rozdzielnicy mieszkania „bez wyłączania prądu, bo pracuje serwer”. Co robisz?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Odmawiasz pracy pod napięciem. Proponujesz: zasilić serwer na czas pracy z UPS-a lub przedłużacza z innego, niewyłączanego źródła, uzgodnić krótkie okno serwisowe i pracować na wyłączonej rozdzielnicy (pięć zasad, blokada, sprawdzenie braku napięcia). Praca pod napięciem w rozdzielnicy mieszkaniowej to ryzyko łuku i porażenia — przy braku technologii PPN i zespołu niedopuszczalne.

</details>

🧮 **[28.06](modules/28-bhp-przy-urzadzeniach/28.06-narzedzia-drabiny-i-praca-na-wysokosci.md#przykład)** · Narzędzia, drabiny i praca na wysokości

**Zadanie.** Drabina przystawna ma 4 m długości i ma sięgać do krawędzi podestu na wysokości 3,2 m, wystając 0,75 m ponad niego. Czy jest wystarczająca, przy kącie ok. 75°?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Potrzebna długość wzdłuż drabiny do krawędzi: $3{,}2 / \sin 75° \approx 3{,}2 / 0{,}966 \approx 3{,}31$ m, plus 0,75 m wysunięcia → ok. **4,06 m**. Drabina 4 m jest **za krótka** — trzeba dłuższej (lub innego środka dostępu).

</details>

---

## 29 — Eksploatacja urządzeń i instalacji

🔎 **[29.01](modules/29-eksploatacja/29.01-rodzaje-prac-eksploatacyjnych.md#przykład)** · Rodzaje prac eksploatacyjnych

**Zadanie.** Elektryk z świadectwem E (G1, do 1 kV, obsługa, konserwacja, naprawa, montaż, demontaż) chce wykonać okresowe pomiary instalacji w bloku i podpisać protokół kontroli okresowej z art. 62 Prawa budowlanego. Może?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** **Nie.** Brakuje mu zakresu **czynności kontrolno-pomiarowych** — więc nie może wykonywać pomiarów. A kontrolę okresową instalacji z art. 62 przeprowadzają osoby z kwalifikacjami wymaganymi przy **dozorze** (D). Potrzebne jest świadectwo E z zakresem pomiarowym do wykonania pomiarów i osoba z D do przeprowadzenia kontroli.

</details>

🔎 **[29.02](modules/29-eksploatacja/29.02-instrukcja-eksploatacji.md#przykład)** · Instrukcja eksploatacji

**Zadanie.** Wymień, co powinna zawierać instrukcja eksploatacji rozdzielnicy głównej budynku biurowego zasilanego z sieci i z agregatu przez SZR.

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Charakterystyka rozdzielnicy, agregatu i SZR; opis automatyki SZR, pomiarów, sygnalizacji i zabezpieczeń; schemat jednokreskowy i opis pól po polsku; czynności przy normalnej pracy (załączanie, przełączanie ręczne, testy agregatu); postępowanie przy zaniku sieci, awarii SZR, pożarze; terminy oględzin, przeglądów, pomiarów i prób agregatu; wymagania BHP i ppoż. (wyłącznik ppoż., gaśnice); zagrożenia (dwa źródła, praca agregatu, paliwo); organizacja prac (kto łączy, kto dopuszcza); środki ochrony; wymagane kwalifikacje obsługi.

</details>

🔎 **[29.03](modules/29-eksploatacja/29.03-dokumentacja-techniczna-i-eksploatacyjna.md#przykład)** · Dokumentacja techniczna i eksploatacyjna

**Zadanie.** Po remoncie mieszkania dołożono dwa obwody (płyta indukcyjna, klimatyzacja) i wymieniono RCD na typ A. Jakie dokumenty należy zaktualizować lub sporządzić?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** **Schemat jednokreskowy** rozdzielnicy i **opis obwodów** na drzwiach, **zestawienie obwodów** (przekroje, zabezpieczenia), **protokół z pomiarów** nowych obwodów i badania RCD, dokumenty urządzeń (instrukcje płyty i klimatyzatora, karta RCD). Jeśli budynek ma książkę obiektu — wpis o zmianie i kontroli przez zarządcę.

</details>

🔎 **[29.04](modules/29-eksploatacja/29.04-ogledziny-przeglady-i-konserwacja.md#przykład)** · Oględziny, przeglądy i konserwacja

**Zadanie.** Właściciel domu pyta, co powinien robić sam, a co zlecać. Podziel czynności.

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** **Sam (oględziny):** raz na kilka miesięcy przegląd wzrokowy rozdzielnicy, zapach, ciepło obudów, test RCD przyciskiem według zalecenia producenta, kontrola przedłużaczy i wtyczek. **Zlecić elektrykowi (przegląd):** co najmniej co 5 lat kontrola okresowa z pomiarami (izolacja, pętla, RCD, ciągłość PE), dokręcenie zacisków, termowizja przy dużych obciążeniach, protokół. Kontrolę z art. 62 przeprowadza osoba z kwalifikacjami dozoru.

</details>

🔎 **[29.05](modules/29-eksploatacja/29.05-przyjmowanie-urzadzen-do-eksploatacji.md#przykład)** · Przyjmowanie urządzeń do eksploatacji

**Zadanie.** Firma wykonała instalację elektryczną w nowym domu. Wymień dokumenty, które inwestor powinien dostać przy odbiorze.

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Dokumentacja powykonawcza (schemat rozdzielnicy, trasy, zestawienie obwodów), **protokoły z pomiarów odbiorczych** (ciągłość, izolacja, pętla zwarcia, RCD, uziemienie), instrukcje i karty urządzeń (RCD, SPD, aparatura, osprzęt), opis rozdzielnicy, oświadczenie o zgodności wykonania z projektem i przepisami, dane wykonawcy z numerami świadectw kwalifikacyjnych, gwarancja.

</details>

---

## 30 — Pożar i awaria

🧮 **[30.01](modules/30-pozar-i-awaria/30.01-przyczyny-pozarow-od-instalacji-elektrycznej.md#przykład)** · Przyczyny pożarów od instalacji elektrycznej

**Zadanie.** Zacisk gniazda kuchennego ma opór przejścia 0,05 Ω (luźna śruba). Czajnik 2000 W pracuje 5 minut. Ile ciepła powstaje w zacisku?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Prąd: $I = 2000 / 230 \approx 8{,}7$ A. Moc w zacisku: $P = I^2 R = 8{,}7^2 \cdot 0{,}05 \approx 3{,}8$ W. Energia w 5 min: $3{,}8 \cdot 300 \approx 1140$ J — w małym zacisku zamkniętym w puszce to wystarczy, żeby z czasem stopić izolację. Przy kilku cyklach dziennie zacisk jeszcze się luzuje (rozszerzalność cieplna) i opór rośnie.

</details>

🔎 **[30.02](modules/30-pozar-i-awaria/30.02-gasnice-do-urzadzen-elektrycznych.md#przykład)** · Gaśnice do urządzeń elektrycznych

**Zadanie.** W pomieszczeniu technicznym pali się izolacja przewodów przy rozdzielnicy 400 V. Pod ręką: gaśnica pianowa bez dopuszczenia elektrycznego, gaśnica śniegowa 5 kg i hydrant. Czego użyjesz i w jakiej kolejności?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Jeśli to możliwe — **wyłączasz zasilanie** rozdzielnicy wyłącznikiem przed nią (wyłącznik główny w innym miejscu, PWP). Gasisz **gaśnicą śniegową** z odległości **co najmniej 1 m**. Gaśnicy pianowej i hydrantu **nie używasz**, dopóki nie masz pewności, że zasilanie jest wyłączone. Jednocześnie ktoś dzwoni na 112.

</details>

🔎 **[30.03](modules/30-pozar-i-awaria/30.03-przeciwpozarowy-wylacznik-pradu.md#przykład)** · Przeciwpożarowy wyłącznik prądu

**Zadanie.** Hala magazynowa 6000 m³ ma instalację PV 50 kW na dachu, UPS dla serwerowni i agregat z SZR. Co musi uwzględnić projekt PWP?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** PWP przy wejściu lub złączu, odcinający wszystkie obwody poza ppoż. (oświetlenie ewakuacyjne, oddymianie, SSP). **Agregat** — zablokowanie startu przez SZR po zadziałaniu PWP. **UPS** — wyłączenie wyjścia sygnałem z PWP (EPO) albo wyraźne oznaczenie obwodów, które dalej mają napięcie. **PV** — rozłączniki DC sterowane z PWP lub system szybkiego wyłączania; całość uzgodniona z rzeczoznawcą ppoż. i opisana dla straży.

</details>

🔎 **[30.04](modules/30-pozar-i-awaria/30.04-postepowanie-przy-awarii.md#przykład)** · Postępowanie przy awarii

**Zadanie.** W domu po burzy nie działa połowa gniazd, a pompa ciepła buczy i nie startuje. Wyłączniki w RG są załączone. Co robisz?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Objawy wskazują na **zanik jednej fazy**. Wyłączasz pompę ciepła i inne odbiorniki trójfazowe (praca na dwóch fazach je przegrzewa). Sprawdzasz zabezpieczenia przedlicznikowe w złączu (jeśli masz dostęp i uprawnienia) albo napięcia na zaciskach wyłącznika głównego. Jeśli fazy brak przed licznikiem — **991**. Po powrocie fazy — załączasz odbiorniki stopniowo i zapisujesz zdarzenie.

</details>

🔎 **[30.05](modules/30-pozar-i-awaria/30.05-pozar-w-rozdzielnicy-kolejnosc-dzialan.md#przykład)** · Pożar w rozdzielnicy — kolejność działań

**Zadanie.** W piwnicy bloku z rozdzielnicy wydobywa się dym, słychać trzaski. Jesteś elektrykiem administracji. Opisz swoje działania.

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Ostrzegasz mieszkańców w pobliżu i nie pozwalasz nikomu zbliżać się do rozdzielnicy. Dzwonisz na **112**. Wyłączasz zasilanie **przed** tą rozdzielnicą — w złączu budynku lub w rozdzielnicy głównej (albo PWP). Jeśli ogień jest mały — gasisz **gaśnicą CO₂ lub proszkową z odległości ≥ 1 m**. Jeśli nie — zamykasz drzwi piwnicy i czekasz na straż przy wejściu, przekazujesz informacje o wyłączeniach. Po pożarze — nie załączasz, dopóki rozdzielnica nie zostanie naprawiona i sprawdzona; sporządzasz notatkę.

</details>

---

## 31 — Pierwsza pomoc przy porażeniu

🔎 **[31.01](modules/31-pierwsza-pomoc/31.01-uwolnienie-porazonego-spod-dzialania-pradu.md#przykład)** · Uwolnienie porażonego spod działania prądu

**Zadanie.** W garażu kolega trzyma uszkodzoną szlifierkę, drga i nie może jej puścić. Przedłużacz jest wpięty do gniazda 3 m dalej, rozdzielnica w korytarzu. Co robisz?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Najszybciej: **wyciągasz wtyczkę przedłużacza** z gniazda (3 m — kilka sekund). Nie dotykasz kolegi, dopóki prąd płynie. Gdyby wtyczka była niedostępna — wyłącznik w rozdzielnicy, a jeśli i to za daleko — stajesz na czymś suchym i **odpychasz szlifierkę lub przewód drewnianym przedmiotem**. Po uwolnieniu: ocena przytomności i oddechu, **112**, w razie potrzeby RKO i AED; nawet jeśli kolega czuje się dobrze — do lekarza.

</details>

🔎 **[31.02](modules/31-pierwsza-pomoc/31.02-ocena-stanu-i-wezwanie-pomocy.md#przykład)** · Ocena stanu i wezwanie pomocy

**Zadanie.** Po uwolnieniu porażony leży, nie reaguje na głos, oddycha regularnie. Jesteś z kolegą. Co robicie?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Kolega dzwoni na **112** (głośnik) i przynosi AED, jeśli jest w pobliżu. Ty udrażniasz drogi oddechowe i potwierdzasz prawidłowy oddech (≤ 10 s). Układasz poszkodowanego w **pozycji bezpiecznej**, okrywasz, **regularnie kontrolujesz oddech**. Jeśli przestanie oddychać prawidłowo — od razu na plecy i **RKO 30:2**, AED.

</details>

🧮 **[31.03](modules/31-pierwsza-pomoc/31.03-resuscytacja-krazeniowo-oddechowa.md#przykład)** · Resuscytacja krążeniowo-oddechowa

**Zadanie.** Przez ile czasu trwa jeden cykl 30:2, jeśli uciskasz w tempie 110/min, a dwa oddechy zajmują 6 s? Ile cykli wykonasz w ciągu 2 minut?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** 30 uciśnięć przy 110/min: $30 / 110 \cdot 60 \approx 16{,}4$ s. Cykl: 16,4 + 6 ≈ **22 s**. W 2 minutach (120 s): ok. **5 cykli** — tyle mniej więcej trwa okres między analizami AED.

</details>

🔎 **[31.04](modules/31-pierwsza-pomoc/31.04-aed.md#przykład)** · AED

**Zadanie.** Porażony elektryk nie oddycha. Ty uciskasz, kolega przybiega z AED po 4 minutach. Co dalej?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Nie przerywasz uciśnięć. Kolega **włącza AED**, odsłania klatkę, **przykleja elektrody** (pod prawym obojczykiem, na lewym boku). Na komendę analizy **oboje odsuwacie się**. Jeśli AED zaleca wyładowanie — kolega sprawdza, że nikt nie dotyka, i naciska przycisk. Natychmiast wracasz do **RKO 30:2** przez 2 minuty; zmieniacie się przy kolejnej analizie.

</details>

🔎 **[31.05](modules/31-pierwsza-pomoc/31.05-oparzenia-elektryczne-dlaczego-zawsze-do-lekarza.md#przykład)** · Oparzenia elektryczne — dlaczego zawsze do lekarza

**Zadanie.** Elektryk dotknął fazy w puszce lewą ręką, prąd wyszedł przez prawą, opartą o rurę. Ma małe zaczerwienienie na palcu, czuje się „trochę dziwnie”, serce „kołacze”. Mówi, że pojedzie do domu. Co robisz?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Droga **ręka–ręka** prowadzi przez klatkę piersiową, a kołatanie serca to możliwe zaburzenia rytmu — dzwonisz na **112**. Do przyjazdu ZRM: posadź lub połóż, nie pozwól mu chodzić i prowadzić, schłodź oparzenie palca, zdejmij obrączkę. Przekaż ratownikom: napięcie 230 V, droga prądu, czas zdarzenia, objawy.

</details>

---

## 32 — Przepisy i normy

🔎 **[32.01](modules/32-przepisy-i-normy/32.01-prawo-energetyczne-i-swiadectwa-kwalifikacyjne.md#przykład)** · Prawo energetyczne i świadectwa kwalifikacyjne

**Zadanie.** Firma zatrudnia: elektryka ze świadectwem E wydanym 6 lat temu, ucznia technikum i serwisanta producenta falowników. Kto może samodzielnie wykonywać prace eksploatacyjne?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** **Nikt z nich.** Świadectwo elektryka **wygasło** (5 lat). Uczeń i serwisant mogą pracować **tylko pod nadzorem** osoby z ważnym świadectwem (art. 54 ust. 2). Firma potrzebuje osoby z ważnym świadectwem; elektryk powinien ponownie zdać egzamin.

</details>

🔎 **[32.02](modules/32-przepisy-i-normy/32.02-rozporzadzenie-o-kwalifikacjach-grupy-punkty.md#przykład)** · Rozporządzenie o kwalifikacjach: grupy, punkty, stanowiska E i D

**Zadanie.** Elektryk montuje instalacje w domach, mikroinstalacje PV i wykonuje pomiary okresowe, które sam podpisuje jako kontrolę z art. 62. Jakiego świadectwa potrzebuje?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** **G1**, punkty **1** (urządzenia prądotwórcze przyłączone do sieci — PV) i **2** (≤ 1 kV), zakres: montaż, naprawa, konserwacja, obsługa, **kontrolno-pomiarowe**. Stanowisko **E** do wykonywania prac i pomiarów oraz **D** — do przeprowadzania kontroli okresowej budynku.

</details>

🔎 **[32.03](modules/32-przepisy-i-normy/32.03-prawo-budowlane-kontrole-okresowe.md#przykład)** · Prawo budowlane — kontrole okresowe

**Zadanie.** Właściciel domu jednorodzinnego z 2018 r. pyta, czy musi robić przeglądy instalacji elektrycznej. Co odpowiadasz?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** **Tak** — art. 62 ust. 1 pkt 2 wymaga kontroli co najmniej **raz na 5 lat**, w tym badania instalacji elektrycznej i piorunochronnej (połączenia, osprzęt, zabezpieczenia, ochrona przeciwporażeniowa, izolacja, uziemienia). Zwolnienie dla domów jednorodzinnych dotyczy tylko **kontroli rocznej**. Kontrolę przeprowadza osoba z kwalifikacjami dozoru; protokół trzeba przechowywać (książka obiektu).

</details>

🧮 **[32.04](modules/32-przepisy-i-normy/32.04-warunki-techniczne-budynkow-instalacja.md#przykład)** · Warunki techniczne budynków — instalacja elektryczna

**Zadanie.** W nowym domu wykonawca zastosował w obwodach gniazd przewody YDY 3×2,5, ale bez RCD, „bo przecież jest PE”. Czy to zgodne z WT?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** **Nie.** § 183 ust. 1 pkt 3 WT wymaga stosowania **urządzeń różnicowoprądowych** jako uzupełnienia ochrony przeciwporażeniowej i przeciwpożarowej, a PN-HD 60364-4-41 wymaga RCD 30 mA m.in. dla gniazd ogólnego przeznaczenia. Przewód PE nie zastępuje RCD — chroni przy uszkodzeniu izolacji do obudowy, ale nie przy dotyku bezpośrednim.

</details>

🔎 **[32.05](modules/32-przepisy-i-normy/32.05-bhp-przy-urzadzeniach-energetycznych.md#przykład)** · BHP przy urządzeniach energetycznych — rozporządzenie

**Zadanie.** Kierownik każe ci wymienić wyłącznik w rozdzielnicy pod napięciem, „bo produkcja nie może stanąć”. Firma nie ma technologii prac pod napięciem. Co robisz?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Odmawiasz pracy pod napięciem — to praca w warunkach szczególnego zagrożenia, bez technologii, sprzętu i polecenia pisemnego (§ 23, § 27 rozporządzenia BHP). Masz prawo powstrzymać się od pracy (**art. 210 KP**), zawiadamiając przełożonego. Proponujesz rozwiązanie: krótkie wyłączenie w zaplanowanym oknie, zasilanie zastępcze dla krytycznych odbiorników, praca według polecenia i instrukcji.

</details>

🔎 **[32.06](modules/32-przepisy-i-normy/32.06-normy-pn-hd-60364-i-pozostale.md#przykład)** · Normy: PN-HD 60364 i pozostałe

**Zadanie.** Do których części PN-HD 60364 zajrzysz, projektując łazienkę z ogrzewaniem podłogowym i gniazdem przy umywalce?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** **7-701** (łazienki — strefy, IP, RCD, połączenia wyrównawcze), **4-41** (ochrona przeciwporażeniowa, RCD 30 mA), **5-52** (dobór przewodów i ich ułożenie, także przewodu grzejnego), **5-54** (przewody ochronne, połączenia wyrównawcze), na koniec **6** (sprawdzenie odbiorcze). Plus instrukcja producenta maty grzejnej.

</details>

---

## 33 — Dozór (D)

🔎 **[33.01](modules/33-dozor/33.01-zakres-egzaminu-na-stanowisku-dozoru.md#przykład)** · Zakres egzaminu na stanowisku dozoru

**Zadanie.** Kierownik utrzymania ruchu w zakładzie (moc umowna 800 kW) przygotowuje się do egzaminu D. Które obszary ze zbioru a–i są dla niego szczególnie ważne?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** **(a)** przyłączanie i dostarczanie energii — zakład ma umowę z OSD i grupę przyłączeniową III; **(b)** racjonalne użytkowanie — moc umowna, kompensacja mocy biernej, audyt; **(c)** dokumentacja; **(g)** i **(h)** — przy mocy umownej ≥ 300 kW zakład jest objęty planem ograniczeń (stopnie zasilania); plus BHP (f) i organizacja prac (i).

</details>

🔎 **[33.02](modules/33-dozor/33.02-obowiazki-osoby-dozoru.md#przykład)** · Obowiązki osoby dozoru

**Zadanie.** Monter zgłasza, że rozłącznik w polu SN „grzeje się” (termowizja: +35 °C względem sąsiednich faz). Co robi osoba dozoru?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Ocenia zagrożenie (ΔT > 15 °C — pilne), uzgadnia z operatorem lub odbiorcami **wyłączenie** pola, wydaje **polecenie** na przegląd (zespół, dopuszczenie, uziemienie), organizuje naprawę (dokręcenie, wymianę styków), zleca **pomiary** po naprawie, **przyjmuje** urządzenie do ponownej eksploatacji i dba o **zapis** w dokumentacji.

</details>

🔎 **[33.03](modules/33-dozor/33.03-przylaczanie-do-sieci-i-dostarczanie-energii.md#przykład)** · Przyłączanie do sieci i dostarczanie energii — przepisy

**Zadanie.** Odbiorca w grupie V skarży się, że w sobotę od 8:00 do 20:00 nie było prądu (prace planowane, ogłoszenie pojawiło się w piątek). Czy operator dotrzymał standardów?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Czas przerwy planowanej — **12 h ≤ 16 h** — mieści się w limicie jednorazowym. Ale powiadomienie **dzień wcześniej** narusza wymóg **co najmniej 5 dni** (§ 49). Odbiorca może złożyć reklamację i wniosek o **bonifikatę** według taryfy operatora.

</details>

🔎 **[33.04](modules/33-dozor/33.04-prowadzenie-dokumentacji-technicznej-i.md#przykład)** · Prowadzenie dokumentacji technicznej i eksploatacyjnej

**Zadanie.** W zakładzie dobudowano rozdzielnię z trzema nowymi odpływami i baterią kondensatorów. Jakie dokumenty musi zaktualizować dozór?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Schemat jednokreskowy i dokumentację powykonawczą, **ewidencję urządzeń**, **instrukcję eksploatacji** (nowe urządzenia, łączenia, kondensatory — rozładowanie przed pracą), harmonogram przeglądów i pomiarów, **protokoły przyjęcia** do eksploatacji z pomiarami, oznaczenia na obiekcie, a jeśli zmieniły się zagrożenia — instrukcję organizacji bezpiecznej pracy i szkolenie ludzi.

</details>

🧮 **[33.05](modules/33-dozor/33.05-racjonalne-uzytkowanie-energii.md#przykład)** · Racjonalne użytkowanie energii

**Zadanie.** Zakład pobiera 200 kW mocy czynnej przy cos φ = 0,8. Jaką moc bierną muszą skompensować kondensatory, żeby osiągnąć tg φ = 0,4?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Przy cos φ = 0,8: tg φ₁ = 0,75 → $Q_1 = 200 \cdot 0{,}75 = 150$ kvar. Docelowo: $Q_2 = 200 \cdot 0{,}4 = 80$ kvar. Moc baterii: $Q_C = Q_1 - Q_2 = 70$ kvar. Moc pozorna spada z 250 kVA do $\sqrt{200^2 + 80^2} \approx 215$ kVA — o 14 % mniejszy prąd.

</details>

🧮 **[33.06](modules/33-dozor/33.06-dysponowanie-moca-i-postepowanie-przy.md#przykład)** · Dysponowanie mocą i postępowanie przy zagrożeniu ruchu sieci

**Zadanie.** Zakład ma moc umowną 900 kW, w planie ograniczeń: 20. stopień = 250 kW. PSE ogłasza 20. stopień w godzinach 17–20. Co robi dozór?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Według **planu wyłączeń** ogranicza pobór do **≤ 250 kW** przed 17:00: zatrzymuje linie produkcyjne o niskim priorytecie, sprężarki i suszarnie, zostawia zasilanie bezpieczeństwa (oświetlenie awaryjne, ppoż., IT, procesy, których przerwanie grozi awarią). Kontroluje pobór na liczniku (moc 15-minutowa), **dokumentuje** działania; po 20:00 przywraca odbiory **stopniowo**.

</details>

---

## 34 — Sieci SN i stacje transformatorowe

🔎 **[34.01](modules/34-sieci-sn-i-stacje/34.01-sieci-sredniego-napiecia-budowa.md#przykład)** · Sieci średniego napięcia — budowa

**Zadanie.** Po burzy w części miasta nie ma prądu. Po 20 minutach napięcie wraca, choć ekipa jeszcze nie dojechała do miejsca awarii. Jak to możliwe?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Sieć SN była zasilana promieniowo z jednej strony pętli. Dyspozytor **zdalnie wyłączył** uszkodzony odcinek i **zamknął punkt podziału**, zasilając pozostałą część z drugiej strony. Odbiorcy mają prąd, a uszkodzony odcinek czeka na naprawę — i jest odłączony z obu stron.

</details>

🧮 **[34.02](modules/34-sieci-sn-i-stacje/34.02-stacje-transformatorowe-sn-nn.md#przykład)** · Stacje transformatorowe SN/nN

**Zadanie.** Stacja słupowa 160 kVA zasila wieś. W szczycie zimowym (cos φ ≈ 0,95) pobór wynosi 140 kW. Czy transformator jest przeciążony?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Moc pozorna: $S = P / \cos\varphi = 140 / 0{,}95 \approx 147$ kVA — ok. **92 %** mocy znamionowej. Transformator nie jest przeciążony, ale pracuje blisko granicy; nowe pompy ciepła i wallboxy we wsi mogą wymagać jego wymiany na większy.

</details>

🔎 **[34.03](modules/34-sieci-sn-i-stacje/34.03-laczniki-sn-odlacznik-rozlacznik-wylacznik.md#przykład)** · Łączniki SN: odłącznik, rozłącznik, wyłącznik

**Zadanie.** Trzeba wykonać przegląd pola liniowego SN z wyłącznikiem i odłącznikiem szynowym oraz liniowym. Podaj kolejność wyłączenia i przygotowania.

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** **Wyłącznik** (otwarcie, sprawdzenie położenia) → **odłącznik liniowy** i **odłącznik szynowy** (widoczne przerwy) → zabezpieczenie napędów (blokady, tablice) → **sprawdzenie braku napięcia** wskaźnikiem SN po obu stronach → **uziemnik** / uziemiacze z obu stron (linia może być zasilona z drugiej strony pętli) → osłony i oznakowanie → dopuszczenie.

</details>

🔎 **[34.04](modules/34-sieci-sn-i-stacje/34.04-ochrona-przeciwporazeniowa-powyzej-1-kv.md#przykład)** · Ochrona przeciwporażeniowa powyżej 1 kV

**Zadanie.** Dlaczego podczas zwarcia doziemnego w stacji SN człowiek stojący na żwirze tuż przy obudowie i dotykający jej może być bezpieczny, a stojący 10 m dalej na trawie, w szerokim rozkroku — narażony?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Przy obudowie, dzięki otokowi, potencjał gruntu jest **wyrównany** z potencjałem obudowy — napięcie dotykowe jest małe, a żwir zwiększa rezystancję przejścia. 10 m dalej potencjał gruntu **szybko spada** z odległością (stromy lejek) — między stopami w rozkroku pojawia się znaczne **napięcie krokowe**.

</details>

🔎 **[34.05](modules/34-sieci-sn-i-stacje/34.05-zasady-pracy-przy-urzadzeniach-sn.md#przykład)** · Zasady pracy przy urządzeniach SN

**Zadanie.** Ekipa wymienia izolator na słupie linii 15 kV. Linia jest zasilana z GPZ, a na końcu odgałęzienia jest stacja SN/nN, w której jeden z odbiorców ma agregat 50 kW. Jakie miejsca trzeba wyłączyć i uziemić?

<details><summary>Rozwiązanie</summary>

**Rozwiązanie.** Wyłączyć linię w GPZ (wyłącznik + odłącznik) **i** na końcu odgałęzienia (rozłącznik w stacji SN/nN lub odłącznik przed nią) — bo agregat u odbiorcy, podłączony nieprawidłowo, może zasilić linię przez transformator od strony nN. Sprawdzić brak napięcia wskaźnikiem 15 kV, założyć **uziemiacze z obu stron** miejsca pracy, widoczne ze słupa. Odstęp od części, które pozostają pod napięciem (np. inny tor), co najmniej **1160 mm**.

</details>
