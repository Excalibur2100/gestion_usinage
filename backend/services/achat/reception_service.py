from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.achat.reception import Reception
from db.schemas.achat.reception_schemas import *

def create_reception(db: Session, data: ReceptionCreate) -> Reception:
    obj = Reception(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_reception(db: Session, reception_id: int) -> Optional[Reception]:
    return db.query(Reception).filter(Reception.id == reception_id).first()

def get_all_receptions(db: Session) -> List[Reception]:
    return db.query(Reception).all()

def update_reception(db: Session, reception_id: int, data: ReceptionUpdate) -> Optional[Reception]:
    obj = get_reception(db, reception_id)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_reception(db: Session, reception_id: int) -> bool:
    obj = get_reception(db, reception_id)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_receptions(db: Session, search_data: ReceptionSearch) -> List[Reception]:
    query = db.query(Reception)
    if search_data.statut:
        query = query.filter(Reception.statut == search_data.statut)
    if search_data.ligne_commande_id:
        query = query.filter(Reception.ligne_commande_id == search_data.ligne_commande_id)
    if search_data.utilisateur_id:
        query = query.filter(Reception.utilisateur_id == search_data.utilisateur_id)
    return query.all()
