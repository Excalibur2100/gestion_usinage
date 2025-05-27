from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.ia.assistant_ia import AssistantIA
from db.schemas.ia.assistant_ia_schemas import *

def create_session(db: Session, data: AssistantIACreate) -> AssistantIA:
    obj = AssistantIA(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_session(db: Session, id_: int) -> Optional[AssistantIA]:
    return db.query(AssistantIA).filter(AssistantIA.id == id_).first()

def get_all_sessions(db: Session) -> List[AssistantIA]:
    return db.query(AssistantIA).all()

def update_session(db: Session, id_: int, data: AssistantIAUpdate) -> Optional[AssistantIA]:
    obj = get_session(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_session(db: Session, id_: int) -> bool:
    obj = get_session(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_sessions(db: Session, search_data: AssistantIASearch) -> List[AssistantIA]:
    query = db.query(AssistantIA)
    if search_data.utilisateur_id:
        query = query.filter(AssistantIA.utilisateur_id == search_data.utilisateur_id)
    if search_data.nom_session:
        query = query.filter(AssistantIA.nom_session.ilike(f"%{search_data.nom_session}%"))
    return query.all()