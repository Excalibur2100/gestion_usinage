from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.ia.conditions_coupe import ConditionsCoupe
from db.schemas.ia.conditions_coupe_schemas import *

def create_conditions(db: Session, data: ConditionsCoupeCreate) -> ConditionsCoupe:
    obj = ConditionsCoupe(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_conditions(db: Session, id_: int) -> Optional[ConditionsCoupe]:
    return db.query(ConditionsCoupe).filter(ConditionsCoupe.id == id_).first()

def get_all_conditions(db: Session) -> List[ConditionsCoupe]:
    return db.query(ConditionsCoupe).all()

def update_conditions(db: Session, id_: int, data: ConditionsCoupeUpdate) -> Optional[ConditionsCoupe]:
    obj = get_conditions(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_conditions(db: Session, id_: int) -> bool:
    obj = get_conditions(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_conditions(db: Session, search_data: ConditionsCoupeSearch) -> List[ConditionsCoupe]:
    query = db.query(ConditionsCoupe)
    if search_data.piece_id:
        query = query.filter(ConditionsCoupe.piece_id == search_data.piece_id)
    if search_data.outil_id:
        query = query.filter(ConditionsCoupe.outil_id == search_data.outil_id)
    if search_data.materiau_id:
        query = query.filter(ConditionsCoupe.materiau_id == search_data.materiau_id)
    if search_data.operation:
        query = query.filter(ConditionsCoupe.operation.ilike(f"%{search_data.operation}%"))
    return query.all()