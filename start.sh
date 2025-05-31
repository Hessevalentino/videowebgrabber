#!/bin/bash

# Easy Video Downloader - Spouštěcí script
echo "🚀 Spouštím Easy Video Downloader..."

# Zkontroluj, zda existuje virtuální prostředí
if [ ! -d "venv" ]; then
    echo "❌ Virtuální prostředí neexistuje!"
    echo "💡 Vytvářím virtuální prostředí..."
    python3 -m venv venv
    echo "📦 Instaluji závislosti..."
    source venv/bin/activate
    pip install -r requirements.txt
fi

# Aktivuj virtuální prostředí
source venv/bin/activate

# Spusť aplikaci
python3 Download.py
