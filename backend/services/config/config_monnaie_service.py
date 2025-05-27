from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.config.config_monnaie import ConfigMonnaie
from db.schemas.config.config_monnaie_schemas import *

def create_monnaie(db: Session, data: ConfigMonnaieCreate) -> ConfigMonnaie:
    obj = ConfigMonnaie(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_monnaie(db: Session, id_: int) -> Optional[ConfigMonnaie]:
    return db.query(ConfigMonnaie).filter(ConfigMonnaie.id == id_).first()

def get_all_monnaies(db: Session) -> List[ConfigMonnaie]:
    return db.query(ConfigMonnaie).all()

def update_monnaie(db: Session, id_: int, data: ConfigMonnaieUpdate) -> Optional[ConfigMonnaie]:
    obj = get_monnaie(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_monnaie(db: Session, id_: int) -> bool:
    obj = get_monnaie(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_monnaies(db: Session, search_data: ConfigMonnaieSearch) -> List[ConfigMonnaie]:
    query = db.query(ConfigMonnaie)
    if search_data.code:
        query = query.filter(ConfigMonnaie.code.ilike(f"%{search_data.code}%"))
    if search_data.libelle:
        query = query.filter(ConfigMonnaie.libelle.ilike(f"%{search_data.libelle}%"))
    if search_data.active is not None:
        query = query.filter(ConfigMonnaie.active == search_data.active)
    return query.all()