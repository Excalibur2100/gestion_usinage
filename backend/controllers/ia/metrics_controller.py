from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.db.models.database import SessionLocal
from backend.services.metrics.metrics_service import add_metric

router = APIRouter()

# Dépendance pour la session de base de données
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/metrics/")
def create_metric(machine_id: int, temperature: float, vibration: float, db: Session = Depends(get_db)):
    return add_metric(db, machine_id, temperature, vibration)