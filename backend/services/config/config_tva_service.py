from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.config.config_tva import ConfigTVA
from db.schemas.config.config_tva_schemas import *

def create_tva(db: Session, data: ConfigTVACreate) -> ConfigTVA:
    obj = ConfigTVA(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_tva(db: Session, id_: int) -> Optional[ConfigTVA]:
    return db.query(ConfigTVA).filter(ConfigTVA.id == id_).first()

def get_all_tva(db: Session) -> List[ConfigTVA]:
    return db.query(ConfigTVA).all()

def update_tva(db: Session, id_: int, data: ConfigTVAUpdate) -> Optional[ConfigTVA]:
    obj = get_tva(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_tva(db: Session, id_: int) -> bool:
    obj = get_tva(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_tva(db: Session, search_data: ConfigTVASearch) -> List[ConfigTVA]:
    query = db.query(ConfigTVA)
    if search_data.nom:
        query = query.filter(ConfigTVA.nom.ilike(f"%{search_data.nom}%"))
    if search_data.pays:
        query = query.filter(ConfigTVA.pays.ilike(f"%{search_data.pays}%"))
    if search_data.actif is not None:
        query = query.filter(ConfigTVA.actif == search_data.actif)
    return query.all()