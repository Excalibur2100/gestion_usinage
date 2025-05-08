import os
from dotenv import load_dotenv

# Charge les variables d'environnement depuis le fichier .env à la racine
load_dotenv()

# --- Configuration de l'environnement ---
APP_ENV = os.getenv("APP_ENV", "development")
APP_DEBUG = os.getenv("APP_DEBUG", "False").lower() == "true"

# --- Configuration des logs ---
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# --- Base de données ---
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL manquante dans le fichier .env")

# --- Clé secrète pour les sessions ou sécurité JWT ---
SECRET_KEY = os.getenv("SECRET_KEY", "changeme")

# --- OpenAI / Assistant IA ---
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
