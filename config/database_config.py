"""
Configuration de la base de données
Compatible avec SQLite, PostgreSQL, MySQL selon l’environnement
"""

import os

# === Mode : sqlite par défaut (développement local)
DEFAULT_SQLITE_URL = "sqlite:///./gestion_usinage.db"

# === Exemple URL PostgreSQL (pour production/docker)
# Exemple : postgresql+psycopg2://username:password@host:port/dbname
DEFAULT_POSTGRESQL_URL = (
    "postgresql+psycopg2://erp_admin:admin123@localhost:5432/erp_usinage"
)

# === Sélection automatique selon variable d’environnement
URL = os.getenv("DATABASE_URL", DEFAULT_SQLITE_URL)

# === Optionnel : affichage
if URL.startswith("sqlite"):
    MODE = "DEV (SQLite)"
else:
    MODE = "PROD (PostgreSQL ou autre)"
