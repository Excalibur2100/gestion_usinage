from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.config.config_langue import ConfigLangue
from db.schemas.config.config_langue_schemas import *

def create_langue(db: Session, data: ConfigLangueCreate) -> ConfigLangue:
    obj = ConfigLangue(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_langue(db: Session, id_: int) -> Optional[ConfigLangue]:
    return db.query(ConfigLangue).filter(ConfigLangue.id == id_).first()

def get_all_langues(db: Session) -> List[ConfigLangue]:
    return db.query(ConfigLangue).all()

def update_langue(db: Session, id_: int, data: ConfigLangueUpdate) -> Optional[ConfigLangue]:
    obj = get_langue(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_langue(db: Session, id_: int) -> bool:
    obj = get_langue(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_langues(db: Session, search_data: ConfigLangueSearch) -> List[ConfigLangue]:
    query = db.query(ConfigLangue)
    if search_data.code:
        query = query.filter(ConfigLangue.code.ilike(f"%{search_data.code}%"))
    if search_data.libelle:
        query = query.filter(ConfigLangue.libelle.ilike(f"%{search_data.libelle}%"))
    if search_data.active is not None:
        query = query.filter(ConfigLangue.active == search_data.active)
    return query.all()