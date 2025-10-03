# 🚀 RYCHLÝ START - Video Web Grabber

## 📦 Instalace (pouze jednou)

```bash
# 1. Vytvořte virtuální prostředí
python3 -m venv venv

# 2. Aktivujte virtuální prostředí
source venv/bin/activate

# 3. Nainstalujte závislosti
pip install -r requirements.txt
```

## 🎬 Spuštění

### Nejjednodušší způsob:
```bash
./start.sh
```

### Nebo přímo:
```bash
source venv/bin/activate
python3 Download.py
```

## 📋 Jak používat

### 1️⃣ Stáhnout jedno video
- Vyberte možnost `1`
- Zadejte URL videa
- Vyberte kvalitu (doporučeno: nejlepší)
- Video se stáhne automaticky

### 2️⃣ Batch stahování (více videí)
**Způsob A - Ze souboru:**
- Přidejte URL do `addresses.txt` (každou na nový řádek)
- Vyberte možnost `2` → `1`
- Nastavte počet současných stahování
- Všechna videa se stáhnou automaticky

**Způsob B - Ruční zadání:**
- Vyberte možnost `2` → `2`
- Zadávejte URL jedna po druhé
- Prázdný řádek ukončí zadávání
- Nastavte počet současných stahování

### 3️⃣ Zobrazit informace o videu
- Vyberte možnost `3`
- Zadejte URL videa
- Zobrazí se detaily bez stahování

## 📁 Výstup

Všechna videa se ukládají do složky `downloads/` ve formátu MP4 v nejvyšší dostupné kvalitě.

## 🆘 Řešení problémů

- **Chyba importu**: Zkontrolujte, zda máte aktivované virtuální prostředí
- **Chyba stahování**: Zkontrolujte internetové připojení a platnost URL
- **Podrobné chyby**: Podívejte se do souboru `downloader.log`

## 💡 Tipy

- Pro nejlepší výsledky používejte 2-3 současná stahování
- Některá videa mohou mít neobvyklé formáty - script je automaticky vyřeší
- Všechny podporované weby najdete v nápovědě (možnost `5`)

---
**Hotovo! Nyní můžete stahovat videa jednoduše a rychle! 🎉**
