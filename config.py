"""
config.py
Application configuration for CareerAI - AI-Based Resume-Job Skill Gap
& Career Path Prediction System.
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


class Config:
    """Central configuration object loaded by the Flask app."""

    SECRET_KEY = os.environ.get("SECRET_KEY", "careerai-dev-secret-key-change-in-production")

    # Database (SQLite by default - no external DB server required)
    # Override with the CAREERAI_DB env var if you want PostgreSQL/MySQL.
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "CAREERAI_DB", f"sqlite:///{os.path.join(BASE_DIR, 'careerai.db')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # File uploads
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
    MAX_CONTENT_LENGTH = 8 * 1024 * 1024  # 8 MB max upload size
    ALLOWED_EXTENSIONS = {"pdf", "docx", "txt"}
