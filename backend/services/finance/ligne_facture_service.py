from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.finance.ligne_facture import LigneFacture
from db.schemas.finance.ligne_facture_schemas import *

def create_ligne_facture(db: Session, data: LigneFactureCreate) -> LigneFacture:
    obj = LigneFacture(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_ligne_facture(db: Session, id_: int) -> Optional[LigneFacture]:
    return db.query(LigneFacture).filter(LigneFacture.id == id_).first()

def get_all_lignes_facture(db: Session) -> List[LigneFacture]:
    return db.query(LigneFacture).all()

def update_ligne_facture(db: Session, id_: int, data: LigneFactureUpdate) -> Optional[LigneFacture]:
    obj = get_ligne_facture(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_ligne_facture(db: Session, id_: int) -> bool:
    obj = get_ligne_facture(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_lignes_facture(db: Session, search_data: LigneFactureSearch) -> List[LigneFacture]:
    query = db.query(LigneFacture)
    if search_data.facture_id:
        query = query.filter(LigneFacture.facture_id == search_data.facture_id)
    if search_data.piece_id:
        query = query.filter(LigneFacture.piece_id == search_data.piece_id)
    if search_data.designation:
        query = query.filter(LigneFacture.designation.ilike(f"%{search_data.designation}%"))
    return query.all()