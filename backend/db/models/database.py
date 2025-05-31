from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from typing import Generator
import logging

# 📦 Configuration centrale
try:
    from backend.config import DATABASE_URL, LOG_LEVEL
except ImportError as e:
    raise ImportError("Assurez-vous que 'backend/config.py' définit 'DATABASE_URL' et 'LOG_LEVEL'.") from e


# === Configuration du logger SQL
logging.basicConfig(level=LOG_LEVEL, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("database")

# === Création du moteur PostgreSQL
if DATABASE_URL is None:
    logger.error("❌ DATABASE_URL est manquant ou None. Veuillez le définir dans 'backend/config.py'.")
    raise ValueError("DATABASE_URL ne doit pas être None.")

try:
    engine = create_engine(
        DATABASE_URL,
        echo=False,
        future=True,
        pool_pre_ping=True,
    )
    with engine.connect() as connection:
        logger.info("✅ Connexion à PostgreSQL réussie.")
except Exception as e:
    logger.error(f"❌ Connexion échouée : {e}\n➡️ URL utilisée : {DATABASE_URL}")
    raise

# === Session locale SQLAlchemy
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# === Dépendance FastAPI (get_db)
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

__all__ = ["engine", "SessionLocal", "get_db"]
