from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.commercial.condition_paiement import ConditionPaiement
from db.schemas.commercial.condition_paiement_schemas import *

def create_condition(db: Session, data: ConditionPaiementCreate) -> ConditionPaiement:
    obj = ConditionPaiement(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_condition(db: Session, id_: int) -> Optional[ConditionPaiement]:
    return db.query(ConditionPaiement).filter(ConditionPaiement.id == id_).first()

def get_all_conditions(db: Session) -> List[ConditionPaiement]:
    return db.query(ConditionPaiement).all()

def update_condition(db: Session, id_: int, data: ConditionPaiementUpdate) -> Optional[ConditionPaiement]:
    obj = get_condition(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_condition(db: Session, id_: int) -> bool:
    obj = get_condition(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_conditions(db: Session, search_data: ConditionPaiementSearch) -> List[ConditionPaiement]:
    query = db.query(ConditionPaiement)
    if search_data.libelle:
        query = query.filter(ConditionPaiement.libelle.ilike(f"%{search_data.libelle}%"))
    return query.all()
