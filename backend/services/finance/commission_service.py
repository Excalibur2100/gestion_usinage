from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.finance.commission import Commission
from db.schemas.finance.commission_schemas import *

def create_commission(db: Session, data: CommissionCreate) -> Commission:
    obj = Commission(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_commission(db: Session, id_: int) -> Optional[Commission]:
    return db.query(Commission).filter(Commission.id == id_).first()

def get_all_commissions(db: Session) -> List[Commission]:
    return db.query(Commission).all()

def update_commission(db: Session, id_: int, data: CommissionUpdate) -> Optional[Commission]:
    obj = get_commission(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_commission(db: Session, id_: int) -> bool:
    obj = get_commission(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_commissions(db: Session, search_data: CommissionSearch) -> List[Commission]:
    query = db.query(Commission)
    if search_data.utilisateur_id:
        query = query.filter(Commission.utilisateur_id == search_data.utilisateur_id)
    if search_data.entreprise_id:
        query = query.filter(Commission.entreprise_id == search_data.entreprise_id)
    if search_data.statut:
        query = query.filter(Commission.statut == search_data.statut)
    return query.all()