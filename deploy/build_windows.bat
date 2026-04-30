@echo off
cd /d %~dp0\..
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m PyInstaller --noconfirm --onefile --windowed --name StylModa_v3 main.py
copy landing\index.html dist\landing_index.html >nul
copy landing\style.css dist\landing_style.css >nul
echo Build complete. See dist\StylModa_v3.exe
