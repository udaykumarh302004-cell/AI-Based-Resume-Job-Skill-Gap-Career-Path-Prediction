#!/usr/bin/env bash
# ============================================================
#  CareerAI - one-click launcher for Linux / macOS
# ============================================================
cd "$(dirname "$0")" || exit 1

echo "[1/4] Creating virtual environment (first run only)..."
if [ ! -d venv ]; then
    python3 -m venv venv
fi

echo "[2/4] Activating virtual environment..."
# shellcheck disable=SC1091
source venv/bin/activate

echo "[3/4] Installing dependencies..."
python -m pip install --quiet --upgrade pip
pip install --quiet -r requirements.txt

echo "[4/4] Initializing database and starting the app..."
python init_db.py
python app.py
