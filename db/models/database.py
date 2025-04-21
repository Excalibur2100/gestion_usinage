from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from dotenv import load_dotenv
from typing import Generator
import os
import logging

# Configurer les logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Charger les variables d'environnement
load_dotenv()

# Charger l'URL de la base de données
DATABASE_URL = os.getenv("DATABASE_URL", None)

if not DATABASE_URL:
    logger.error("DATABASE_URL n'est pas configurée. Vérifiez votre fichier .env.")
    raise ValueError("DATABASE_URL n'est pas configurée dans le fichier .env")

# Créer le moteur SQLAlchemy
try:
    engine = create_engine(DATABASE_URL, echo=False, future=True)
    # Vérifier la connexion à la base de données
    with engine.connect() as connection:
        logger.info("Connexion à la base de données réussie.")
except Exception as e:
    logger.error(f"Erreur lors de la connexion à la base de données : {e}. URL utilisée : {DATABASE_URL}")
    raise

# Configurer la session
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


# Dépendance FastAPI pour obtenir une session DB
def get_db() -> Generator[Session, None, None]:
    """
    Fournit une session de base de données pour les requêtes FastAPI.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()