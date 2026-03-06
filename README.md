# Bulls and Cows

Tento projekt je jednoduchá hra „Bulls and Cows“. 
Program vygeneruje náhodné 4místné číslo s unikátními číslicemi 
(první číslice není nula) a hráč se ho snaží uhodnout. 
Program informuje hráče o počtu „bulls“ (správné číslo na správné pozici) a „cows“ (správné číslo, ale na špatné pozici).

---

## Instalace ##

### 1. Klonování repozitáře
Naklonujte nebo stáhněte tento projekt do svého počítače.

### 2. Vytvoření a aktivace virtuálního prostředí v terminálu
Doporučený postup je spustit projekt v samostatném virtuálním prostředí:

| python -m venv venv      |               |
|--------------------------|---------------|
|                          |               |
| source venv/bin/activate | # Linux / Mac |
| venv\Scripts\activate    | # Windows     |

### 3. Instalace závislostí
Projekt používá pouze standardní knihovnu Pythonu, není potřeba instalovat žádné externí balíčky.

### 4. Použití
**Soubor main.py spusťte v jakémkoliv editoru kódu a bavte se**

## Ukázkový výstup programu

Ahoj, zahrajeme si hru Bulls and Cows!
Pravidla hry:
- hledej 4místné číslo
- bull znamená správná číslice na správné pozici
- cow znamená správná číslice, ale na špatné pozici

Zadej svůj tip (4 různá čísla, nezačínej nulou): 1234

Zadal jsi: 1234
1 bull, 2 cows

Zadej svůj tip (4 různá čísla, nezačínej nulou): 5678

Zadal jsi: 5678
0 bulls, 1 cow

Juhuu, uhodl jsi!

## Očekávaný výstup
Výsledkem běhu skriptu je interaktivní hra v terminálu, která:
- umožňuje hráči zadávat tipy,
- kontroluje správný formát vstupu,
- vypisuje počet „bulls“ a „cows“ po každém tipu,
- končí, když hráč uhodne celé 4místné číslo.
