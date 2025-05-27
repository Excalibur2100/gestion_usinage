from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.finance.reglement import Reglement
from db.schemas.finance.reglement_schemas import *

def create_reglement(db: Session, data: ReglementCreate) -> Reglement:
    obj = Reglement(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_reglement(db: Session, id_: int) -> Optional[Reglement]:
    return db.query(Reglement).filter(Reglement.id == id_).first()

def get_all_reglements(db: Session) -> List[Reglement]:
    return db.query(Reglement).all()

def update_reglement(db: Session, id_: int, data: ReglementUpdate) -> Optional[Reglement]:
    obj = get_reglement(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_reglement(db: Session, id_: int) -> bool:
    obj = get_reglement(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_reglements(db: Session, search_data: ReglementSearch) -> List[Reglement]:
    query = db.query(Reglement)
    if search_data.facture_id:
        query = query.filter(Reglement.facture_id == search_data.facture_id)
    if search_data.entreprise_id:
        query = query.filter(Reglement.entreprise_id == search_data.entreprise_id)
    if search_data.mode:
        query = query.filter(Reglement.mode == search_data.mode)
    if search_data.statut:
        query = query.filter(Reglement.statut == search_data.statut)
    return query.all()