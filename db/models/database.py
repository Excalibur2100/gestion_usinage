from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import os

# URL de la base de données
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://excalibur:Christopher@localhost:5432/gestion_usinage"
)

# Création de l'engine SQLAlchemy
engine = create_engine(DATABASE_URL, echo=False, future=True)

# Création du SessionLocal
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Dépendance FastAPI pour obtenir une session DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()