from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.models.database import get_db
from backend.services.ia.analyse_fichiers_services import (
    get_analyses_fichiers,
    get_analyse_fichier_by_id,
    create_analyse_fichier,
    update_analyse_fichier,
    delete_analyse_fichier,
)
from backend.db.schemas.ia.analyse_fichier_schemas import AnalyseFichierCreate, AnalyseFichierUpdate

router = APIRouter(prefix="/analyse_fichier", tags=["Analyse Fichier"])

@router.get("/", response_model=list)
def list_analyses(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_analyses_fichiers(db, skip=skip, limit=limit)

@router.get("/{analyse_id}", response_model=dict)
def get_analyse(analyse_id: int, db: Session = Depends(get_db)):
    return get_analyse_fichier_by_id(db, analyse_id)

@router.post("/", response_model=dict)
def create_analyse(analyse_data: AnalyseFichierCreate, db: Session = Depends(get_db)):
    return create_analyse_fichier(db, analyse_data)

@router.put("/{analyse_id}", response_model=dict)
def update_analyse(analyse_id: int, analyse_data: AnalyseFichierUpdate, db: Session = Depends(get_db)):
    return update_analyse_fichier(db, analyse_id, analyse_data)

@router.delete("/{analyse_id}")
def delete_analyse(analyse_id: int, db: Session = Depends(get_db)):
    delete_analyse_fichier(db, analyse_id)
    return {"message": "Analyse de fichier supprimée avec succès", "analyse_id": analyse_id}