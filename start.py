#!/usr/bin/env python3
"""
Quick Start - Nejjednodušší způsob spuštění video downloaderu
"""

import os
import sys

def main():
    print("🚀 Spouštím Easy Video Downloader...")
    
    # Zkontroluj, zda existuje virtuální prostředí
    if not os.path.exists("venv"):
        print("❌ Virtuální prostředí neexistuje!")
        print("💡 Spusťte nejdříve: python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt")
        return
    
    # Spusť Download.py
    try:
        from Download import main as download_main
        download_main()
    except ImportError as e:
        print(f"❌ Chyba importu: {e}")
        print("💡 Ujistěte se, že máte nainstalované všechny závislosti")
    except Exception as e:
        print(f"❌ Neočekávaná chyba: {e}")

if __name__ == "__main__":
    main()
