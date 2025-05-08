from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from typing import Generator
import logging

# Récupère la configuration depuis config.py
from config import DATABASE_URL, LOG_LEVEL

# Configurer les logs
logging.basicConfig(level=LOG_LEVEL)
logger = logging.getLogger(__name__)

# Créer le moteur SQLAlchemy
try:
    engine = create_engine(DATABASE_URL, echo=False, future=True)
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

