
from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.crm.relance import Relance
from db.schemas.crm.relance_schemas import *

def create_relance(db: Session, data: RelanceCreate) -> Relance:
    obj = Relance(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_relance(db: Session, id_: int) -> Optional[Relance]:
    return db.query(Relance).filter(Relance.id == id_).first()

def get_all_relances(db: Session) -> List[Relance]:
    return db.query(Relance).all()

def update_relance(db: Session, id_: int, data: RelanceUpdate) -> Optional[Relance]:
    obj = get_relance(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_relance(db: Session, id_: int) -> bool:
    obj = get_relance(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_relances(db: Session, search_data: RelanceSearch) -> List[Relance]:
    query = db.query(Relance)
    if search_data.client_id:
        query = query.filter(Relance.client_id == search_data.client_id)
    if search_data.statut:
        query = query.filter(Relance.statut == search_data.statut)
    if search_data.canal:
        query = query.filter(Relance.canal == search_data.canal)
    return query.all()