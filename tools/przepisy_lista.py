"""Lista aktów prawnych cytowanych w bazie — wspólna dla PRZEPISY.md i alertu o zmianach.

eli: identyfikator w API Sejmu (https://api.sejm.gov.pl/eli/acts/DU/<rok>/<poz>) — akt pierwotny.
tj: ostatni znany tekst jednolity (aktualizuj ręcznie po alercie).
wzor: wyrażenie regularne, po którym rozpoznaje się akt w tekście tematu.
"""

AKTY = [
    {"klucz": "pe", "nazwa": "Ustawa z 10 kwietnia 1997 r. — Prawo energetyczne", "eli": "DU/1997/348",
     "tj": "Dz.U. 2026 poz. 43", "co": "świadectwa kwalifikacyjne (art. 54), przyłączanie, ograniczenia w dostawach",
     "wzor": r"Prawo energetyczne|Prawa energetycznego|Prawem energetycznym|10 kwietnia 1997"},
    {"klucz": "pb", "nazwa": "Ustawa z 7 lipca 1994 r. — Prawo budowlane", "eli": "DU/1994/414",
     "tj": "Dz.U. 2026 poz. 524", "co": "kontrole okresowe (art. 62), książka obiektu (art. 64), okres przejściowy WT (art. 102a)",
     "wzor": r"Prawo budowlane|Prawa budowlanego|7 lipca 1994|art\. 62 PB"},
    {"klucz": "kwal", "nazwa": "Rozporządzenie MKiŚ z 1 lipca 2022 r. w sprawie stwierdzania posiadania kwalifikacji",
     "eli": "DU/2022/1392", "tj": "Dz.U. 2022 poz. 1392", "co": "grupy G1–G3, stanowiska E i D, zakres egzaminu",
     "wzor": r"1 lipca 2022|2022 poz\. 1392|rozp(?:orządzeni[ea])?\.? (?:z|o) (?:2022|kwalifikacj)"},
    {"klucz": "bhp", "nazwa": "Rozporządzenie ME z 28 sierpnia 2019 r. w sprawie BHP przy urządzeniach energetycznych",
     "eli": "DU/2019/1830", "tj": "Dz.U. 2021 poz. 1210", "co": "polecenia, funkcje, przygotowanie strefy, odstępy DL/DV",
     "wzor": r"28 sierpnia 2019|2021 poz\. 1210|rozp(?:orządzeni[ea])?\.? BHP|BHP przy urządzeniach energetycznych"},
    {"klucz": "sys", "nazwa": "Rozporządzenie MKiŚ z 22 marca 2023 r. w sprawie warunków funkcjonowania systemu elektroenergetycznego",
     "eli": "DU/2023/819", "tj": "Dz.U. 2025 poz. 919", "co": "grupy przyłączeniowe, parametry jakości, przerwy, reklamacje",
     "wzor": r"22 marca 2023|2023 poz\. 819|systemow\w+|funkcjonowania systemu"},
    {"klucz": "wt", "nazwa": "Rozporządzenie MI z 12 kwietnia 2002 r. w sprawie warunków technicznych, jakim powinny odpowiadać budynki",
     "eli": "DU/2002/690", "tj": "wielokrotnie zmieniane — nowe WT zapowiedziane, stan: [32.04](modules/32-przepisy-i-normy/32.04-warunki-techniczne-budynkow-instalacja.md)",
     "co": "§ 180–186: instalacja elektryczna w budynku, PWP",
     "wzor": r"12 kwietnia 2002|warunk\w+ techniczn\w+|\bWT\b"},
    {"klucz": "kp", "nazwa": "Ustawa z 26 czerwca 1974 r. — Kodeks pracy", "eli": "DU/1974/141", "tj": "—",
     "co": "obowiązki pracodawcy w zakresie BHP", "wzor": r"Kodeks\w* pracy"},
    {"klucz": "szkol", "nazwa": "Rozporządzenie MGiP z 27 lipca 2004 r. w sprawie szkolenia w dziedzinie BHP",
     "eli": "DU/2004/1860", "tj": "Dz.U. 2024 poz. 1327", "co": "szkolenia wstępne i okresowe",
     "wzor": r"szkoleni\w+ w dziedzinie BHP|2024 poz\. 1327"},
    {"klucz": "ppoz", "nazwa": "Rozporządzenie MSWiA z 7 czerwca 2010 r. w sprawie ochrony przeciwpożarowej budynków",
     "eli": "DU/2010/719", "tj": "—", "co": "gaśnice, ochrona ppoż. obiektów",
     "wzor": r"7 czerwca 2010|MSWiA z 2010"},
    {"klucz": "oze", "nazwa": "Ustawa z 20 lutego 2015 r. o odnawialnych źródłach energii", "eli": "DU/2015/478", "tj": "—",
     "co": "mikroinstalacje, prosument", "wzor": r"20 lutego 2015|ustaw\w+ o OZE|odnawialnych źródłach energii"},
    {"klucz": "efekt", "nazwa": "Ustawa z 20 maja 2016 r. o efektywności energetycznej", "eli": "DU/2016/831", "tj": "—",
     "co": "audyt energetyczny przedsiębiorstwa", "wzor": r"20 maja 2016|efektywności energetycznej"},
    {"klucz": "norm", "nazwa": "Ustawa z 12 września 2002 r. o normalizacji", "eli": "DU/2002/1386", "tj": "—",
     "co": "art. 5 ust. 3 — stosowanie norm jest dobrowolne", "wzor": r"o normalizacji"},
]

UE = [
    {"nazwa": "Rozporządzenie (UE) 2019/1781 — ekoprojekt silników", "url": "https://eur-lex.europa.eu/eli/reg/2019/1781/oj", "wzor": r"2019/1781"},
    {"nazwa": "Rozporządzenie (UE) 2019/2020 — ekoprojekt źródeł światła", "url": "https://eur-lex.europa.eu/eli/reg/2019/2020/oj", "wzor": r"2019/2020"},
    {"nazwa": "Rozporządzenie delegowane (UE) 2019/2015 — etykiety źródeł światła", "url": "https://eur-lex.europa.eu/eli/reg_del/2019/2015/oj", "wzor": r"2019/2015"},
    {"nazwa": "Rozporządzenie (UE) nr 1194/2012 — ekoprojekt lamp (uchylone)", "url": "https://eur-lex.europa.eu/eli/reg/2012/1194/oj", "wzor": r"1194/2012"},
    {"nazwa": "Rozporządzenie (UE) nr 305/2011 — wyroby budowlane (CPR)", "url": "https://eur-lex.europa.eu/eli/reg/2011/305/oj", "wzor": r"305/2011"},
    {"nazwa": "Dyrektywa 2014/32/UE — przyrządy pomiarowe (MID)", "url": "https://eur-lex.europa.eu/eli/dir/2014/32/oj", "wzor": r"2014/32/UE"},
    {"nazwa": "Dyrektywa (UE) 2023/1791 — efektywność energetyczna (EED)", "url": "https://eur-lex.europa.eu/eli/dir/2023/1791/oj", "wzor": r"2023/1791"},
]

# Wyszukiwanie nowego rozporządzenia o warunkach technicznych (alert)
NOWE_WT = {"title": "warunków technicznych, jakim powinny odpowiadać budynki", "od": "2025-01-01"}


def _isap_nieuzywane(eli):
    _, rok, poz = eli.split("/")
    return f"https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU{rok}{int(poz):07d}" if int(rok) >= 2012 else None


def eli_url(eli):
    return f"https://eli.gov.pl/eli/{eli}/ogl"
