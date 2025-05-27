from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.crm.opportunite import Opportunite
from db.schemas.crm.opportunite_schemas import *

def create_opportunite(db: Session, data: OpportuniteCreate) -> Opportunite:
    obj = Opportunite(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_opportunite(db: Session, id_: int) -> Optional[Opportunite]:
    return db.query(Opportunite).filter(Opportunite.id == id_).first()

def get_all_opportunites(db: Session) -> List[Opportunite]:
    return db.query(Opportunite).all()

def update_opportunite(db: Session, id_: int, data: OpportuniteUpdate) -> Optional[Opportunite]:
    obj = get_opportunite(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_opportunite(db: Session, id_: int) -> bool:
    obj = get_opportunite(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_opportunites(db: Session, search_data: OpportuniteSearch) -> List[Opportunite]:
    query = db.query(Opportunite)
    if search_data.client_id:
        query = query.filter(Opportunite.client_id == search_data.client_id)
    if search_data.statut:
        query = query.filter(Opportunite.statut == search_data.statut)
    if search_data.titre:
        query = query.filter(Opportunite.titre.ilike(f"%{search_data.titre}%"))
    return query.all()