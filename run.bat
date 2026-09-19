@echo off
REM ============================================================
REM  CareerAI - one-click launcher for Windows
REM ============================================================
cd /d "%~dp0"

echo [1/4] Creating virtual environment (first run only)...
if not exist venv (
    python -m venv venv
)

echo [2/4] Activating virtual environment...
call venv\Scripts\activate.bat

echo [3/4] Installing dependencies...
python -m pip install --quiet --upgrade pip
pip install --quiet -r requirements.txt

echo [4/4] Initializing database and starting the app...
python init_db.py
python app.py

pause
