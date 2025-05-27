from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.commercial.objectif_commercial import ObjectifCommercial
from db.schemas.commercial.objectif_commercial_schemas import *

def create_objectif(db: Session, data: ObjectifCommercialCreate) -> ObjectifCommercial:
    obj = ObjectifCommercial(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_objectif(db: Session, id_: int) -> Optional[ObjectifCommercial]:
    return db.query(ObjectifCommercial).filter(ObjectifCommercial.id == id_).first()

def get_all_objectifs(db: Session) -> List[ObjectifCommercial]:
    return db.query(ObjectifCommercial).all()

def update_objectif(db: Session, id_: int, data: ObjectifCommercialUpdate) -> Optional[ObjectifCommercial]:
    obj = get_objectif(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_objectif(db: Session, id_: int) -> bool:
    obj = get_objectif(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_objectifs(db: Session, search_data: ObjectifCommercialSearch) -> List[ObjectifCommercial]:
    query = db.query(ObjectifCommercial)
    if search_data.utilisateur_id:
        query = query.filter(ObjectifCommercial.utilisateur_id == search_data.utilisateur_id)
    if search_data.periode:
        query = query.filter(ObjectifCommercial.periode == search_data.periode)
    return query.all()
