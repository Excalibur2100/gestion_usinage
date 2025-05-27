from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.finance.paiement import Paiement
from db.schemas.finance.paiement_schemas import *

def create_paiement(db: Session, data: PaiementCreate) -> Paiement:
    obj = Paiement(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_paiement(db: Session, id_: int) -> Optional[Paiement]:
    return db.query(Paiement).filter(Paiement.id == id_).first()

def get_all_paiements(db: Session) -> List[Paiement]:
    return db.query(Paiement).all()

def update_paiement(db: Session, id_: int, data: PaiementUpdate) -> Optional[Paiement]:
    obj = get_paiement(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_paiement(db: Session, id_: int) -> bool:
    obj = get_paiement(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_paiements(db: Session, search_data: PaiementSearch) -> List[Paiement]:
    query = db.query(Paiement)
    if search_data.facture_id:
        query = query.filter(Paiement.facture_id == search_data.facture_id)
    if search_data.entreprise_id:
        query = query.filter(Paiement.entreprise_id == search_data.entreprise_id)
    if search_data.mode_paiement:
        query = query.filter(Paiement.mode_paiement == search_data.mode_paiement)
    return query.all()