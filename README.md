# Video Web Grabber

Profesionální script pro stahování videí z různých webových stránek v původní kvalitě a rozlišení.

## 🚀 Rychlý start (3 kroky)

### 1. Instalace
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Spuštění
```bash
python3 Download.py
```

### 3. Použití
- Vyberte **možnost 1** pro stažení jednoho videa
- Vyberte **možnost 2** pro batch stahování více videí
- Zadejte URL a sledujte progress stahování

**Hotovo! Videa se ukládají do složky `downloads/` 📁**

## Funkce

- ✅ Stahování v nejvyšší dostupné kvalitě
- ✅ Zachování původního rozlišení
- ✅ Podpora různých formátů (MP4, WebM, atd.)
- ✅ Stahování metadat, titulků a náhledů
- ✅ Konfigurovatelné nastavení pro různé weby
- ✅ **Batch stahování z textového souboru**
- ✅ **Paralelní stahování více videí současně**
- ✅ Detailní logování
- ✅ Command-line interface

## Instalace

1. Naklonujte nebo stáhněte tento projekt
2. Nainstalujte závislosti:

```bash
pip install -r requirements.txt
```

## Použití

### 🎯 Jednoduché interaktivní rozhraní (DOPORUČENO)

**Nejjednodušší způsob:**
```bash
# Linux/Mac
./start.sh

# Nebo přímo Python
python3 Download.py
```

**Funkce interaktivního rozhraní:**
- 🎬 Stahování jednotlivých videí s průvodcem
- 📦 Batch stahování s interaktivním nastavením
- 🔍 Zobrazení informací o videu před stahováním
- ⚙️ Jednoduché nastavení kvality a složek
- ❓ Integrovaná nápověda

### 📦 Batch stahování (pokročilé)

1. **Přidejte URL adresy do souboru `addresses.txt`** (každou na nový řádek):
```
https://cz.xhamster.com/videos/example1
https://www.youtube.com/watch?v=example2
https://vimeo.com/example3
```

2. **Spusťte batch downloader**:
```bash
python batch_downloader.py
# nebo
python video_downloader.py -b
```

### 🎯 Command-line použití

```bash
# Stáhnout jedno video
python video_downloader.py "https://example.com/video"

# Batch stahování s 5 současnými downloady
python video_downloader.py -b addresses.txt -w 5

# Zobrazit pouze informace o videu
python video_downloader.py "URL" --info-only

# Použít vlastní formát
python video_downloader.py "URL" -f "best[height<=720]"
```

### Příklady

```bash
# Batch stahování z addresses.txt
python video_downloader.py -b

# Batch stahování s vlastním souborem
python video_downloader.py -b my_urls.txt -w 5

# Stáhnout video z XHamster
python video_downloader.py "https://cz.xhamster.com/videos/example-video"

# Stáhnout pouze audio
python video_downloader.py "URL" -f "bestaudio"

# Stáhnout v HD kvalitě (max 1080p)
python video_downloader.py "URL" -f "best[height<=1080]"

# Zobrazit informace o všech videích v addresses.txt
python video_downloader.py -b --info-only
```

## Podporované weby

Script podporuje **1000+ webů** díky yt-dlp knihovně. Zde je seznam nejpopulárnějších:

### 🎬 Video platformy
- **YouTube** - youtube.com
- **Vimeo** - vimeo.com
- **Dailymotion** - dailymotion.com
- **Twitch** - twitch.tv
- **Facebook** - facebook.com
- **Instagram** - instagram.com
- **TikTok** - tiktok.com
- **Twitter/X** - twitter.com, x.com

### 🔞 Adult weby
- **XHamster** - xhamster.com
- **Pornhub** - pornhub.com
- **XVideos** - xvideos.com
- **RedTube** - redtube.com
- **YouPorn** - youporn.com
- **Tube8** - tube8.com
- **SpankBang** - spankbang.com
- **XNXX** - xnxx.com

### 📺 Streaming služby
- **BBC iPlayer** - bbc.co.uk/iplayer
- **Arte** - arte.tv
- **CNN** - cnn.com
- **ESPN** - espn.com
- **MTV** - mtv.com
- **National Geographic** - nationalgeographic.com

### 🎵 Hudební platformy
- **SoundCloud** - soundcloud.com
- **Bandcamp** - bandcamp.com
- **Mixcloud** - mixcloud.com
- **Audiomack** - audiomack.com

### 🎓 Vzdělávací platformy
- **Coursera** - coursera.org
- **Khan Academy** - khanacademy.org
- **TED** - ted.com
- **Udemy** - udemy.com

### 🌍 Mezinárodní weby
- **Bilibili** - bilibili.com (Čína)
- **Niconico** - nicovideo.jp (Japonsko)
- **VK** - vk.com (Rusko)
- **Odnoklassniki** - ok.ru (Rusko)
- **Weibo** - weibo.com (Čína)

### 📱 Mobilní platformy
- **9GAG** - 9gag.com
- **Reddit** - reddit.com
- **Imgur** - imgur.com
- **Vine** - vine.co

### 🎮 Gaming platformy
- **Twitch Clips** - clips.twitch.tv
- **Steam** - store.steampowered.com
- **GameTrailers** - gametrailers.com

### 📰 Zpravodajské weby
- **Reuters** - reuters.com
- **Associated Press** - apnews.com
- **France24** - france24.com
- **Deutsche Welle** - dw.com

**A stovky dalších!** Kompletní seznam najdete na: https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md

## Konfigurace

Můžete upravit nastavení v souboru `config.py` pro různé scénáře použití.

## Batch stahování

### Formát souboru addresses.txt

```
# Video URLs - každá URL na samostatném řádku
# Řádky začínající # jsou komentáře a budou ignorovány

https://cz.xhamster.com/videos/example1
https://www.youtube.com/watch?v=example2
https://vimeo.com/example3

# Můžete přidávat komentáře
https://example.com/video4  # Tento komentář bude ignorován
```

### Paralelní stahování

- **Výchozí**: 3 současné downloady
- **Doporučeno**: 2-5 workerů (více může způsobit blokování)
- **Nastavení**: použijte `-w NUMBER` parametr

```bash
# Stahovat 5 videí současně
python video_downloader.py -b -w 5
```

## Výstupní soubory

Pro každé video se stáhnou:
- Video soubor (MP4/WebM)
- Metadata (JSON)
- Náhled (JPG/WebP)
- Titulky (pokud jsou dostupné)
- Popis videa

## Logování

Všechny aktivity se zaznamenávají do souboru `downloader.log`.

## Řešení problémů

Pokud se vyskytnou problémy:

1. Zkontrolujte, zda je URL platná
2. Zkuste aktualizovat yt-dlp: `pip install --upgrade yt-dlp`
3. Zkontrolujte log soubor pro detailní chybové zprávy
4. Některé weby mohou vyžadovat specifické nastavení

## Právní upozornění

Používejte tento script pouze pro legální účely a respektujte autorská práva a podmínky použití webových stránek.
