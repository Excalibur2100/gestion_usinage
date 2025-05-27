from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.finance.facture import Facture
from db.schemas.finance.facture_schemas import *

def create_facture(db: Session, data: FactureCreate) -> Facture:
    obj = Facture(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_facture(db: Session, id_: int) -> Optional[Facture]:
    return db.query(Facture).filter(Facture.id == id_).first()

def get_all_factures(db: Session) -> List[Facture]:
    return db.query(Facture).all()

def update_facture(db: Session, id_: int, data: FactureUpdate) -> Optional[Facture]:
    obj = get_facture(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_facture(db: Session, id_: int) -> bool:
    obj = get_facture(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_factures(db: Session, search_data: FactureSearch) -> List[Facture]:
    query = db.query(Facture)
    if search_data.code_facture:
        query = query.filter(Facture.code_facture.ilike(f"%{search_data.code_facture}%"))
    if search_data.entreprise_id:
        query = query.filter(Facture.entreprise_id == search_data.entreprise_id)
    if search_data.commande_id:
        query = query.filter(Facture.commande_id == search_data.commande_id)
    if search_data.statut:
        query = query.filter(Facture.statut == search_data.statut)
    return query.all()