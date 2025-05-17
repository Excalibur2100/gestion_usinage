from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.achat.evaluation_fournisseur_schemas import *
from services.achat.evaluation_fournisseur_service import *

router = APIRouter(prefix="/evaluations-fournisseur", tags=["Evaluations Fournisseur"])

@router.post("/", response_model=EvaluationFournisseurRead)
def create(data: EvaluationFournisseurCreate, db: Session = Depends(get_db)):
    return create_evaluation(db, data)

@router.get("/", response_model=List[EvaluationFournisseurRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_evaluations(db)

@router.get("/{evaluation_id}", response_model=EvaluationFournisseurRead)
def read(evaluation_id: int, db: Session = Depends(get_db)):
    obj = get_evaluation(db, evaluation_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Évaluation non trouvée")
    return obj

@router.put("/{evaluation_id}", response_model=EvaluationFournisseurRead)
def update(evaluation_id: int, data: EvaluationFournisseurUpdate, db: Session = Depends(get_db)):
    obj = update_evaluation(db, evaluation_id, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Évaluation non trouvée")
    return obj

@router.delete("/{evaluation_id}")
def delete(evaluation_id: int, db: Session = Depends(get_db)):
    if not delete_evaluation(db, evaluation_id):
        raise HTTPException(status_code=404, detail="Évaluation non trouvée")
    return {"ok": True}

@router.post("/search", response_model=EvaluationFournisseurSearchResults)
def search(data: EvaluationFournisseurSearch, db: Session = Depends(get_db)):
    return {"results": search_evaluations(db, data)}
