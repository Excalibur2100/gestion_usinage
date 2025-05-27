from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.ia.suggestion_outil_schemas import *
from services.ia.suggestion_outil_service import *

router = APIRouter(prefix="/suggestions-outils", tags=["Suggestions IA Outils"])

@router.post("/", response_model=SuggestionOutilRead)
def create(data: SuggestionOutilCreate, db: Session = Depends(get_db)):
    return create_suggestion(db, data)

@router.get("/", response_model=List[SuggestionOutilRead])
def list_all(db: Session = Depends(get_db)):
    return get_all_suggestions(db)

@router.get("/{id_}", response_model=SuggestionOutilRead)
def get_one(id_: int, db: Session = Depends(get_db)):
    obj = get_suggestion(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Suggestion non trouvée")
    return obj

@router.put("/{id_}", response_model=SuggestionOutilRead)
def update(id_: int, data: SuggestionOutilUpdate, db: Session = Depends(get_db)):
    obj = update_suggestion(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Suggestion non trouvée")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_suggestion(db, id_):
        raise HTTPException(status_code=404, detail="Suggestion non trouvée")
    return {"ok": True}