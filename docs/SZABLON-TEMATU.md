# Szablon tematu

Każdy plik tematu w `modules/NN-nazwa/` ma ten sam układ. Ten dokument opisuje, co powinno się znaleźć w każdej sekcji, żeby moduły były spójne niezależnie od tego, kiedy i przez kogo zostały napisane.

[← README](../README.md)

## Nagłówek

```markdown
# 07.04 — Charakterystyki B, C i D

> **Moduł:** [07 — Zabezpieczenia nadprądowe](README.md) · **Oznaczenia:** 🏠📋 · **Zakres SEP:** (a) (c) · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - PN-HD 60364-4-43 — dobór zabezpieczeń (omówienie własnymi słowami, bez cytowania normy)
> - H. Markiewicz, *Instalacje elektryczne*, rozdz. … (s. …)
> - Katalog producenta: [charakterystyki wyłączników …](link)

← [poprzedni temat](...) · [spis modułu](README.md) · [następny temat](...) →
```

**Zakres SEP** to litery z § 6 ust. 1 pkt 1 rozporządzenia z 2022 r. (opis w [sep/zakres.md](../sep/zakres.md)). Temat bez związku z egzaminem ma w tym polu „—”.

## Sekcje

| Sekcja | Zawartość | Wskazówki |
|--------|-----------|-----------|
| **Po co to jest** | 2–4 zdania: gdzie to spotkasz w domu, w czym pomaga, o co pyta komisja | Konkretnie: „bez tego nie dobierzesz zabezpieczenia w module 16” |
| **Po ludzku** | Wyjaśnienie bez wzorów; jedna dobra analogia (woda w rurach, ruch drogowy) | Krótkie zdania. Każde nowe słowo wyjaśnione przy pierwszym użyciu albo podlinkowane do [słowniczka](../SLOWNICZEK.md) |
| **Jak to wygląda** | 2–6 zdjęć z podpisem „na co patrzeć” | Zasady i licencje: [GRAFIKI.md](GRAFIKI.md). Brakujące zdjęcie → znacznik `📷 DO ZROBIENIA` |
| **Schemat** | Własny schemat SVG z `assets/schematy/` albo diagram Mermaid | Symbole wg PN-EN 60617; kolory żył zgodne z rzeczywistością |
| **Pojęcia** | Tabela: pojęcie · po ludzku · termin normowy lub symbol | Nowe hasła dopisz też do słowniczka |
| **Liczby do zapamiętania** | Tabela: wartość lub wzór · co oznacza · **kiedy obowiązuje** · źródło | Każda liczba z warunkiem i źródłem. Ta sekcja trafia w całości do `SCIAGA.md` |
| **W praktyce** | Procedura krok po kroku | Prace na instalacji zaczynają się od 5 zasad bezpieczeństwa i kończą sprawdzeniem |
| **Błędy i zagrożenia** | 3–6 punktów | ⚠️ przy błędach groźnych dla życia; zawsze z wyjaśnieniem, *dlaczego* to groźne |
| **Przykład** | Obliczenie rozwiązane w całości albo przypadek z życia | Dane → rysunek → rachunek → sprawdzenie → wniosek |
| **Pytania SEP** | 3–8 pytań sformułowanych tak, jak zadaje je komisja | Odpowiedź pod `<details>`: 3–6 zdań, które da się powiedzieć na głos. Pytania kopiuj też do [sep/pytania.md](../sep/pytania.md) |
| **Sprawdź się** | „Rozpoznaj na zdjęciu”, „znajdź błąd na schemacie”, krótkie zadania | Odpowiedzi pod `<details>`; zadania własne |
| **Źródła** | Konkretne jednostki redakcyjne przepisów, numery i części norm, rozdziały i strony książek | Pozycje z [RESOURCES.md](../RESOURCES.md); anglojęzyczne oznaczone 🇬🇧 |

## Format pytań i odpowiedzi

```markdown
1. **Jakie zadanie ma wyłącznik różnicowoprądowy o prądzie 30 mA?**

<details>
<summary>Odpowiedź</summary>

Wyłącznik porównuje prąd płynący do odbiornika i z powrotem. Jeśli część prądu „ucieka” inną drogą — na przykład przez człowieka do ziemi — i różnica przekroczy próg zadziałania, wyłącznik odłącza obwód. Przy 30 mA stanowi ochronę uzupełniającą: chroni także przy dotyku bezpośrednim i gdy zawiodą inne środki ochrony. Nie chroni przed porażeniem między fazą a neutralnym, bo wtedy różnicy prądów nie ma.
</details>
```

## Format zdjęć

```markdown
![Wyłącznik nadprądowy B16 z opisanym frontem](../../assets/foto/07-wylacznik-b16.jpg)
*Na co patrzeć: litera i liczba (B16) to charakterystyka i prąd znamionowy; liczba w ramce (6000) to zdolność zwarciowa w amperach.*
```

Brakujące zdjęcie:

```markdown
> 📷 **DO ZROBIENIA:** rozdzielnica mieszkaniowa po zdjęciu osłony — widać szynę TH35, listwy N i PE, mostki grzebieniowe; kadr na wprost, bez cieni.
```

## Konwencje zapisu

- Przecinek dziesiętny: `0{,}4`. Jednostki pismem prostym: `\mathrm{A}`, `\mathrm{mm^2}`, odstęp `\ ` między liczbą a jednostką.
- Symbole wielkości zgodne z normami: $U_0$ — napięcie fazowe względem ziemi, $I_a$ — prąd zapewniający samoczynne zadziałanie, $Z_s$ — impedancja pętli zwarcia, $I_{\Delta n}$ — znamionowy prąd różnicowy.
- W tabelach Markdown zamiast `|` w module liczby pisz `\lvert x \rvert`.
- Oznaczenia przewodów i aparatów pisz jak na nadruku: `YDYp 3×2,5`, `B16`, `RCD 40/0,03 A typ A`.
- Odwołania do przepisów: „rozporządzenie z 2022 r., § 5 pkt 1”, do norm: „PN-HD 60364-4-41, p. 411.3.2”.

## Status tematu i modułu

- 🔲 szkielet — tylko nagłówki.
- 🟡 w trakcie — część sekcji wypełniona.
- ✅ pełny — wszystkie sekcje, zdjęcia lub znaczniki `📷`, pytania z odpowiedziami, źródła.

Po wypełnieniu tematu zmień status w nagłówku pliku, w tabeli tematów w `README.md` modułu, wpisz „Liczby do zapamiętania” do `SCIAGA.md`, a gdy cały moduł jest gotowy — zmień status w mapie modułów w głównym `README.md`.
