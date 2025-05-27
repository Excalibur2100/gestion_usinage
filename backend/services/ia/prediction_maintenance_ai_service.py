from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.ia.prediction_maintenance_ai import PredictionMaintenanceAI
from db.schemas.ia.prediction_maintenance_ai_schemas import *

def create_prediction(db: Session, data: PredictionAICreate) -> PredictionMaintenanceAI:
    obj = PredictionMaintenanceAI(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_prediction(db: Session, id_: int) -> Optional[PredictionMaintenanceAI]:
    return db.query(PredictionMaintenanceAI).filter(PredictionMaintenanceAI.id == id_).first()

def get_all_predictions(db: Session) -> List[PredictionMaintenanceAI]:
    return db.query(PredictionMaintenanceAI).all()

def update_prediction(db: Session, id_: int, data: PredictionAIUpdate) -> Optional[PredictionMaintenanceAI]:
    obj = get_prediction(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_prediction(db: Session, id_: int) -> bool:
    obj = get_prediction(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_predictions(db: Session, search_data: PredictionAISearch) -> List[PredictionMaintenanceAI]:
    query = db.query(PredictionMaintenanceAI)
    if search_data.machine_id:
        query = query.filter(PredictionMaintenanceAI.machine_id == search_data.machine_id)
    if search_data.type_prediction:
        query = query.filter(PredictionMaintenanceAI.type_prediction.ilike(f"%{search_data.type_prediction}%"))
    if search_data.niveau_risque:
        query = query.filter(PredictionMaintenanceAI.niveau_risque == search_data.niveau_risque)
    return query.all()