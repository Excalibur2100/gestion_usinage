from sqlalchemy.orm import Session
from typing import List, Optional
from db.models.tables.ia.suggestion_outil import SuggestionOutil
from db.schemas.ia.suggestion_outil_schemas import *

def create_suggestion(db: Session, data: SuggestionOutilCreate) -> SuggestionOutil:
    obj = SuggestionOutil(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_suggestion(db: Session, suggestion_id: int) -> Optional[SuggestionOutil]:
    return db.query(SuggestionOutil).filter(SuggestionOutil.id == suggestion_id).first()

def get_all_suggestions(db: Session) -> List[SuggestionOutil]:
    return db.query(SuggestionOutil).order_by(SuggestionOutil.date_suggestion.desc()).all()

def update_suggestion(db: Session, suggestion_id: int, data: SuggestionOutilUpdate) -> Optional[SuggestionOutil]:
    obj = get_suggestion(db, suggestion_id)
    if obj:
        for key, value in data.dict(exclude_unset=True).items():
            setattr(obj, key, value)
        db.commit()
        db.refresh(obj)
        return obj
    return None

def delete_suggestion(db: Session, suggestion_id: int) -> bool:
    obj = get_suggestion(db, suggestion_id)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False