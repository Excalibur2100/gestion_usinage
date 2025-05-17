"""
Configuration des niveaux de logs pour tout le projet ERP
Compatible avec SQLAlchemy, FastAPI, services internes, IA, etc.
"""

import os

# === Niveau de log global
# Valeurs possibles : DEBUG, INFO, WARNING, ERROR, CRITICAL
LEVEL = os.getenv("LOG_LEVEL", "INFO")

# === Format de log par défaut
FORMAT = "%(asctime)s [%(levelname)s] %(message)s"
