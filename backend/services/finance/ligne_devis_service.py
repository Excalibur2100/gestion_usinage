from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.finance.ligne_devis import LigneDevis
from db.schemas.finance.ligne_devis_schemas import *

def create_ligne(db: Session, data: LigneDevisCreate) -> LigneDevis:
    obj = LigneDevis(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_ligne(db: Session, id_: int) -> Optional[LigneDevis]:
    return db.query(LigneDevis).filter(LigneDevis.id == id_).first()

def get_all_lignes(db: Session) -> List[LigneDevis]:
    return db.query(LigneDevis).all()

def update_ligne(db: Session, id_: int, data: LigneDevisUpdate) -> Optional[LigneDevis]:
    obj = get_ligne(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_ligne(db: Session, id_: int) -> bool:
    obj = get_ligne(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_lignes(db: Session, search_data: LigneDevisSearch) -> List[LigneDevis]:
    query = db.query(LigneDevis)
    if search_data.devis_id:
        query = query.filter(LigneDevis.devis_id == search_data.devis_id)
    if search_data.piece_id:
        query = query.filter(LigneDevis.piece_id == search_data.piece_id)
    if search_data.designation:
        query = query.filter(LigneDevis.designation.ilike(f"%{search_data.designation}%"))
    return query.all()