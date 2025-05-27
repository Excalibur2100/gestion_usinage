from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.config.config_metier import ConfigMetier
from db.schemas.config.config_metier_schemas import *

def create_metier(db: Session, data: ConfigMetierCreate) -> ConfigMetier:
    obj = ConfigMetier(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_metier(db: Session, id_: int) -> Optional[ConfigMetier]:
    return db.query(ConfigMetier).filter(ConfigMetier.id == id_).first()

def get_all_metiers(db: Session) -> List[ConfigMetier]:
    return db.query(ConfigMetier).all()

def update_metier(db: Session, id_: int, data: ConfigMetierUpdate) -> Optional[ConfigMetier]:
    obj = get_metier(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_metier(db: Session, id_: int) -> bool:
    obj = get_metier(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_metiers(db: Session, search_data: ConfigMetierSearch) -> List[ConfigMetier]:
    query = db.query(ConfigMetier)
    if search_data.nom:
        query = query.filter(ConfigMetier.nom.ilike(f"%{search_data.nom}%"))
    if search_data.actif is not None:
        query = query.filter(ConfigMetier.actif == search_data.actif)
    return query.all()