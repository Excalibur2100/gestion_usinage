from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.ia.prediction_maintenance_ai_schemas import *
from services.ia.prediction_maintenance_ai_service import *

router = APIRouter(prefix="/predictions-ai", tags=["Prédiction IA Maintenance"])

@router.post("/", response_model=PredictionAIRead)
def create(data: PredictionAICreate, db: Session = Depends(get_db)):
    return create_prediction(db, data)

@router.get("/", response_model=List[PredictionAIRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_predictions(db)

@router.get("/{id_}", response_model=PredictionAIRead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_prediction(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Prédiction non trouvée")
    return obj

@router.put("/{id_}", response_model=PredictionAIRead)
def update(id_: int, data: PredictionAIUpdate, db: Session = Depends(get_db)):
    obj = update_prediction(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Prédiction non trouvée")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_prediction(db, id_):
        raise HTTPException(status_code=404, detail="Prédiction non trouvée")
    return {"ok": True}

@router.post("/search", response_model=PredictionAISearchResults)
def search(data: PredictionAISearch, db: Session = Depends(get_db)):
    return {"results": search_predictions(db, data)}