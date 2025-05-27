from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.finance.devis import Devis
from db.schemas.finance.devis_schemas import *

def create_devis(db: Session, data: DevisCreate) -> Devis:
    obj = Devis(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_devis(db: Session, id_: int) -> Optional[Devis]:
    return db.query(Devis).filter(Devis.id == id_).first()

def get_all_devis(db: Session) -> List[Devis]:
    return db.query(Devis).all()

def update_devis(db: Session, id_: int, data: DevisUpdate) -> Optional[Devis]:
    obj = get_devis(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_devis(db: Session, id_: int) -> bool:
    obj = get_devis(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_devis(db: Session, search_data: DevisSearch) -> List[Devis]:
    query = db.query(Devis)
    if search_data.code_devis:
        query = query.filter(Devis.code_devis.ilike(f"%{search_data.code_devis}%"))
    if search_data.client_id:
        query = query.filter(Devis.client_id == search_data.client_id)
    if search_data.entreprise_id:
        query = query.filter(Devis.entreprise_id == search_data.entreprise_id)
    if search_data.statut:
        query = query.filter(Devis.statut == search_data.statut)
    return query.all()