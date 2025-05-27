from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.ia.suggestion_outil_metier_schemas import SuggestionOutilIARequest
from services.ia.suggestion_outil_metier_service import generer_suggestion_outil_ia

router = APIRouter(prefix="/suggestions-outils-metier", tags=["IA Métier - Suggestions Outils"])

@router.post("/generer")
def generer(data: SuggestionOutilIARequest, db: Session = Depends(get_db)):
    return generer_suggestion_outil_ia(data, db)