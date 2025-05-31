#!/usr/bin/env python3
"""
Download.py - Video Web Grabber
Hlavní spouštěcí script pro stahování videí z webových stránek.
Jednoduché interaktivní rozhraní pro grabování videí.
"""

import os
import sys
import time
from pathlib import Path
from video_downloader import VideoDownloader


def print_header():
    """Zobrazí hlavičku aplikace."""
    # Červená barva ANSI
    RED = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

    print(f"{RED}{BOLD}")
    print("╔══════════════════════════════════════════════════════════════════════════════╗")
    print("║                                                                              ║")
    print("║  ██╗   ██╗██╗██████╗ ███████╗ ██████╗     ██╗    ██╗███████╗██████╗          ║")
    print("║  ██║   ██║██║██╔══██╗██╔════╝██╔═══██╗    ██║    ██║██╔════╝██╔══██╗         ║")
    print("║  ██║   ██║██║██║  ██║█████╗  ██║   ██║    ██║ █╗ ██║█████╗  ██████╔╝         ║")
    print("║  ╚██╗ ██╔╝██║██║  ██║██╔══╝  ██║   ██║    ██║███╗██║██╔══╝  ██╔══██╗         ║")
    print("║   ╚████╔╝ ██║██████╔╝███████╗╚██████╔╝    ╚███╔███╔╝███████╗██████╔╝         ║")
    print("║    ╚═══╝  ╚═╝╚═════╝ ╚══════╝ ╚═════╝      ╚══╝╚══╝ ╚══════╝╚═════╝          ║")
    print("║                                                                              ║")
    print("║   ██████╗ ██████╗  █████╗ ██████╗ ██████╗ ███████╗██████╗                   ║")
    print("║  ██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗                  ║")
    print("║  ██║  ███╗██████╔╝███████║██████╔╝██████╔╝█████╗  ██████╔╝                  ║")
    print("║  ██║   ██║██╔══██╗██╔══██║██╔══██╗██╔══██╗██╔══╝  ██╔══██╗                  ║")
    print("║  ╚██████╔╝██║  ██║██║  ██║██████╔╝██████╔╝███████╗██║  ██║                  ║")
    print("║   ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝                  ║")
    print("║                                                                              ║")
    print("╚══════════════════════════════════════════════════════════════════════════════╝")
    print(f"{RESET}")
    print("🎬 Jednoduchý nástroj pro stahování videí v nejvyšší kvalitě")
    print("🌐 Podporuje XHamster, YouTube, Vimeo a mnoho dalších")
    print("=" * 78)


def print_menu():
    """Zobrazí hlavní menu."""
    print("\n📋 HLAVNÍ MENU:")
    print("1️⃣  Stáhnout jedno video (zadání URL)")
    print("2️⃣  Batch stahování (více videí najednou)")
    print("3️⃣  Zobrazit informace o videu")
    print("4️⃣  Nastavení")
    print("5️⃣  Nápověda")
    print("0️⃣  Ukončit")
    print("-" * 40)


def get_user_choice():
    """Získá volbu uživatele."""
    while True:
        try:
            choice = input("👉 Vyberte možnost (0-5): ").strip()
            if choice in ['0', '1', '2', '3', '4', '5']:
                return choice
            else:
                print("❌ Neplatná volba. Zadejte číslo 0-5.")
        except KeyboardInterrupt:
            print("\n\n👋 Ukončuji aplikaci...")
            sys.exit(0)


def download_single_video():
    """Stáhne jedno video."""
    print("\n🎯 STAHOVÁNÍ JEDNOHO VIDEA")
    print("-" * 30)
    
    url = input("📎 Zadejte URL videa: ").strip()
    if not url:
        print("❌ URL nesmí být prázdné!")
        return
    
    if not url.startswith(('http://', 'https://')):
        print("❌ URL musí začínat http:// nebo https://")
        return
    
    # Volba složky
    download_dir = input("📁 Složka pro stažení (Enter = 'downloads'): ").strip() or "downloads"
    
    # Volba kvality
    print("\n🎨 Kvalita videa:")
    print("1. Nejlepší dostupná (doporučeno)")
    print("2. 1080p max")
    print("3. 720p max")
    print("4. Pouze audio")
    
    quality_choice = input("Vyberte kvalitu (1-4, Enter = 1): ").strip() or "1"
    
    quality_map = {
        '1': 'best[ext=mp4]/best',
        '2': 'best[height<=1080][ext=mp4]/best[height<=1080]',
        '3': 'best[height<=720][ext=mp4]/best[height<=720]',
        '4': 'bestaudio[ext=m4a]/bestaudio'
    }
    
    format_selector = quality_map.get(quality_choice, 'best[ext=mp4]/best')
    
    print(f"\n🚀 Zahajuji stahování...")
    print(f"📎 URL: {url}")
    print(f"📁 Složka: {download_dir}")
    print(f"🎨 Kvalita: {format_selector}")
    print("-" * 50)
    
    # Stahování
    downloader = VideoDownloader(download_dir, "INFO")
    custom_opts = {'format': format_selector}
    
    success = downloader.download_video(url, custom_opts)
    
    if success:
        print("\n✅ Video bylo úspěšně staženo!")
    else:
        print("\n❌ Stahování selhalo. Zkontrolujte log pro detaily.")
    
    input("\n📱 Stiskněte Enter pro pokračování...")


def batch_download():
    """Batch stahování více videí."""
    print("\n📦 BATCH STAHOVÁNÍ")
    print("-" * 20)
    
    print("Můžete zadat URL adresy dvěma způsoby:")
    print("1️⃣  Načíst ze souboru addresses.txt")
    print("2️⃣  Zadat ručně (jedna po druhé)")
    
    method = input("\nVyberte způsob (1-2): ").strip()
    
    urls = []
    
    if method == "1":
        # Načtení ze souboru
        if not os.path.exists("addresses.txt"):
            print("❌ Soubor addresses.txt neexistuje!")
            print("💡 Vytvořím prázdný soubor addresses.txt...")
            with open("addresses.txt", "w", encoding="utf-8") as f:
                f.write("# Přidejte URL adresy zde - každou na nový řádek\n")
                f.write("# Řádky začínající # jsou komentáře\n\n")
            print("✅ Soubor vytvořen. Přidejte URL adresy a spusťte znovu.")
            return
        
        downloader = VideoDownloader("downloads", "INFO")
        urls = downloader.read_urls_from_file("addresses.txt")
        
        if not urls:
            print("❌ V souboru addresses.txt nejsou žádné platné URL!")
            return
            
        print(f"📋 Načteno {len(urls)} URL ze souboru addresses.txt")
        
    elif method == "2":
        # Ruční zadání
        print("\n📝 Zadávejte URL adresy (prázdný řádek ukončí zadávání):")
        while True:
            url = input(f"URL #{len(urls)+1}: ").strip()
            if not url:
                break
            if url.startswith(('http://', 'https://')):
                urls.append(url)
                print(f"✅ Přidáno: {url}")
            else:
                print("❌ Neplatná URL, přeskakuji...")
        
        if not urls:
            print("❌ Nebyly zadány žádné platné URL!")
            return
    else:
        print("❌ Neplatná volba!")
        return
    
    # Zobrazení seznamu
    print(f"\n📋 SEZNAM VIDEÍ K STAŽENÍ ({len(urls)} videí):")
    for i, url in enumerate(urls, 1):
        print(f"  {i:2d}. {url}")
    
    # Potvrzení
    confirm = input(f"\n❓ Stáhnout všech {len(urls)} videí? (y/N): ").strip().lower()
    if confirm not in ['y', 'yes', 'ano']:
        print("❌ Stahování zrušeno.")
        return
    
    # Nastavení workerů
    try:
        workers = int(input("⚡ Počet současných stahování (1-5, Enter = 3): ").strip() or "3")
        workers = max(1, min(5, workers))
    except ValueError:
        workers = 3
    
    # Složka
    download_dir = input("📁 Složka pro stažení (Enter = 'downloads'): ").strip() or "downloads"
    
    print(f"\n🚀 Zahajuji batch stahování...")
    print(f"📦 Videí: {len(urls)}")
    print(f"⚡ Workerů: {workers}")
    print(f"📁 Složka: {download_dir}")
    print("=" * 50)
    
    # Stahování
    downloader = VideoDownloader(download_dir, "INFO")
    results = downloader.download_batch(urls, workers)
    
    # Výsledky
    successful = sum(1 for r in results if r['success'])
    failed = len(results) - successful
    
    print("\n" + "=" * 50)
    print("📊 VÝSLEDKY BATCH STAHOVÁNÍ")
    print("=" * 50)
    print(f"✅ Úspěšně staženo: {successful}")
    print(f"❌ Selhalo: {failed}")
    print(f"📁 Soubory uloženy do: {download_dir}/")
    
    if failed > 0:
        print(f"\n❌ Selhala stahování:")
        for result in results:
            if not result['success']:
                print(f"   • {result['url']}")
    
    input("\n📱 Stiskněte Enter pro pokračování...")


def show_video_info():
    """Zobrazí informace o videu."""
    print("\n🔍 INFORMACE O VIDEU")
    print("-" * 25)
    
    url = input("📎 Zadejte URL videa: ").strip()
    if not url:
        print("❌ URL nesmí být prázdné!")
        return
    
    if not url.startswith(('http://', 'https://')):
        print("❌ URL musí začínat http:// nebo https://")
        return
    
    print("🔄 Načítám informace...")
    
    downloader = VideoDownloader("temp", "ERROR")  # Tichý režim
    info = downloader.get_video_info(url)
    
    if info:
        print("\n📋 INFORMACE O VIDEU:")
        print("=" * 40)
        for key, value in info.items():
            if value is not None:
                key_display = key.replace('_', ' ').title()
                if key == 'duration' and isinstance(value, (int, float)):
                    minutes = int(value // 60)
                    seconds = int(value % 60)
                    value = f"{minutes}:{seconds:02d} ({value}s)"
                elif key == 'filesize' and isinstance(value, (int, float)):
                    value = f"{value / (1024*1024):.1f} MB"
                print(f"{key_display:15}: {value}")
    else:
        print("❌ Nepodařilo se načíst informace o videu.")
    
    input("\n📱 Stiskněte Enter pro pokračování...")


def show_settings():
    """Zobrazí nastavení."""
    print("\n⚙️  NASTAVENÍ")
    print("-" * 15)
    print("📁 Výchozí složka: downloads/")
    print("⚡ Výchozí počet workerů: 3")
    print("🎨 Výchozí kvalita: Nejlepší dostupná")
    print("📝 Soubor s URL: addresses.txt")
    print("📊 Log soubor: downloader.log")
    print("\n💡 Pro změnu nastavení upravte config.py")
    
    input("\n📱 Stiskněte Enter pro pokračování...")


def show_help():
    """Zobrazí nápovědu."""
    print("\n❓ NÁPOVĚDA")
    print("-" * 12)
    print("🎯 JEDNOTLIVÉ VIDEO:")
    print("   • Zadejte URL videa")
    print("   • Vyberte kvalitu a složku")
    print("   • Video se stáhne automaticky")
    print()
    print("📦 BATCH STAHOVÁNÍ:")
    print("   • Přidejte URL do addresses.txt (každou na nový řádek)")
    print("   • Nebo zadejte URL ručně jedna po druhé")
    print("   • Nastavte počet současných stahování (1-5)")
    print()
    print("🔍 INFORMACE O VIDEU:")
    print("   • Zobrazí detaily bez stahování")
    print("   • Užitečné pro kontrolu před stahováním")
    print()
    print("📋 PODPOROVANÉ WEBY:")
    print("   • XHamster, YouTube, Vimeo, Pornhub")
    print("   • Instagram, TikTok, Twitter/X")
    print("   • A stovky dalších...")
    print()
    print("🆘 ŘEŠENÍ PROBLÉMŮ:")
    print("   • Zkontrolujte internetové připojení")
    print("   • Ověřte platnost URL")
    print("   • Podívejte se do downloader.log")
    
    input("\n📱 Stiskněte Enter pro pokračování...")


def main():
    """Hlavní funkce aplikace."""
    try:
        while True:
            os.system('clear' if os.name == 'posix' else 'cls')  # Vyčistí obrazovku
            print_header()
            print_menu()
            
            choice = get_user_choice()
            
            if choice == '0':
                print("\n👋 Děkuji za použití Easy Video Downloader!")
                break
            elif choice == '1':
                download_single_video()
            elif choice == '2':
                batch_download()
            elif choice == '3':
                show_video_info()
            elif choice == '4':
                show_settings()
            elif choice == '5':
                show_help()
    
    except KeyboardInterrupt:
        print("\n\n👋 Aplikace ukončena uživatelem.")
    except Exception as e:
        print(f"\n❌ Neočekávaná chyba: {e}")
        print("📝 Zkontrolujte downloader.log pro více informací.")


if __name__ == "__main__":
    main()
