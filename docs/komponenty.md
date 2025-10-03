# 🧩 Video Web Grabber - Komponenty Dokumentace

**Datum:** 8. srpna 2025  
**Analyzováno pomocí:** ZEN MCP Server (Llama/DeepSeek model)  
**Verze:** 1.0  

---

## 📊 **Přehled Architektury**

### **Architekturní Vzor:** Functional/OOP Hybrid
- **1 hlavní třída** (VideoDownloader)
- **6 modulů** s celkem **16 funkcemi**
- **Minimalistické závislosti** (yt-dlp + requests)
- **Clean separation of concerns**

---

## 🏗️ **Hlavní Komponenty**

### **1. Core Engine**

#### **`VideoDownloader` třída** (`video_downloader.py`)
**Popis:** Hlavní engine pro stahování videí pomocí yt-dlp

**Public API:**
```python
class VideoDownloader:
    def __init__(self, download_dir: str = "downloads", log_level: str = "INFO")
    def get_site_config(self, url: str) -> Dict[str, Any]
    def download_video(self, url: str, custom_opts: Optional[Dict[str, Any]] = None) -> bool
    def get_video_info(self, url: str) -> Optional[Dict[str, Any]]
    def read_urls_from_file(self, file_path: str) -> List[str]
    def download_single_video_safe(self, url: str, custom_opts: Optional[Dict[str, Any]] = None) -> Dict[str, Any]
    def download_batch(self, urls: List[str], max_workers: int = 3, custom_opts: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]
```

**Klíčové vlastnosti:**
- ✅ Thread-safe batch processing
- ✅ Site-specific configuration
- ✅ Comprehensive error handling
- ✅ Progress tracking
- ✅ Flexible output options

---

### **2. User Interface Layer**

#### **`Download.py`** - Hlavní CLI rozhraní
**Funkce:** 9 funkcí pro interaktivní uživatelské rozhraní

```python
def print_header()           # ASCII art header
def print_menu()             # Hlavní menu
def get_user_choice()        # Input handling
def download_single_video()  # Single video workflow
def batch_download()         # Batch download workflow (101 řádků)
def show_video_info()        # Video info display
def show_settings()          # Settings management
def show_help()              # Help system
def main()                   # Main entry point
```

**Charakteristiky:**
- 🎨 Emoji-rich UX
- 🔄 Interactive menu system
- ⚙️ Quality selection
- 📁 Directory management

---

### **3. Konfigurace**

#### **`config.py`** - Centralizované nastavení
**Struktury:**

```python
# Quality presets (5 options)
QUALITY_PRESETS = {
    'best': 'best[ext=mp4]/best',
    'high': 'best[height<=1080][ext=mp4]/best[height<=1080]',
    'medium': 'best[height<=720][ext=mp4]/best[height<=720]',
    'low': 'best[height<=480][ext=mp4]/best[height<=480]',
    'audio_only': 'bestaudio[ext=m4a]/bestaudio'
}

# Site-specific configs (3 sites)
SITE_CONFIGS = {
    'xhamster.com': {...},
    'youtube.com': {...},
    'vimeo.com': {...}
}

# User agents (3 browsers)
USER_AGENTS = {
    'chrome': '...',
    'firefox': '...',
    'safari': '...'
}
```

---

### **4. Utility Moduly**

#### **`batch_downloader.py`** - Batch Processing Wrapper
```python
def main()  # Simple batch downloader wrapper
```

#### **`start.py`** - Environment Launcher
```python
def main()  # Environment check + launcher
```

#### **`test_downloader.py`** - Test Suite
```python
def test_url_reading()    # URL file reading test
def test_video_info()     # Video info extraction test
def test_site_config()    # Site configuration test
def main()                # Test runner
```

---

## 🔗 **Dependency Graf**

```
External Dependencies:
├── yt-dlp (core video downloading)
├── requests (HTTP requests)
├── pathlib (modern file handling)
└── concurrent.futures (parallel processing)

Internal Dependencies:
config.py
    ↓
video_downloader.py
    ↓
├── Download.py (CLI interface)
├── batch_downloader.py (batch wrapper)
├── start.py (launcher)
└── test_downloader.py (testing)
```

---

## 📡 **API Reference**

### **VideoDownloader Methods**

#### **`__init__(download_dir, log_level)`**
- **Účel:** Inicializace downloaderu
- **Parametry:** 
  - `download_dir: str` - Výstupní složka
  - `log_level: str` - Úroveň logování
- **Vytváří:** Logging setup, base yt-dlp config

#### **`get_site_config(url) -> Dict`**
- **Účel:** Získání site-specific konfigurace
- **Logika:** URL parsing → domain detection → config lookup
- **Fallback:** Default options pokud site není podporován

#### **`download_video(url, custom_opts) -> bool`**
- **Účel:** Stažení jednoho videa
- **Workflow:** Config merge → yt-dlp execution → error handling
- **Return:** Success/failure status

#### **`download_batch(urls, max_workers, custom_opts) -> List[Dict]`**
- **Účel:** Paralelní stahování více videí
- **Concurrency:** ThreadPoolExecutor (1-5 workers)
- **Return:** List výsledků pro každé video

---

## 🎯 **Design Patterns**

### **Implementované vzory:**
- ✅ **Facade Pattern** - VideoDownloader jako unified interface
- ✅ **Strategy Pattern** - Site-specific configurations
- ✅ **Template Method** - Standardizovaný download workflow
- ✅ **Factory Pattern** - Dynamic config selection

### **Architekturní principy:**
- ✅ **Single Responsibility** - Každý modul má jasný účel
- ✅ **Open/Closed** - Extensible přes config
- ✅ **Dependency Inversion** - Config injection
- ✅ **Interface Segregation** - Focused public APIs

---

## 📈 **Scalability Charakteristiky**

### **Současné možnosti:**
- **Concurrent downloads:** 1-5 workers
- **Memory efficient:** Streaming bez buffering
- **I/O optimized:** Asynchronní operations

### **Bottlenecks:**
- Single-threaded UI
- Monolitická struktura
- Žádné caching

---

## 🔧 **Rozšiřitelnost**

### **Snadné rozšíření:**
- ✅ Nové sites přes `SITE_CONFIGS`
- ✅ Quality presets přes `QUALITY_PRESETS`
- ✅ User agents přes `USER_AGENTS`

### **Budoucí možnosti:**
- 🔮 GUI interface
- 🔮 Web API endpoints
- 🔮 Plugin architecture
- 🔮 Database backend

---

*Dokumentace vygenerována pomocí ZEN MCP Server s Llama/DeepSeek modelem*
