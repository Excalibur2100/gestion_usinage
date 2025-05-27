from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.finance.config_marge import ConfigMarge
from db.schemas.finance.config_marge_schemas import *

def create_marge(db: Session, data: ConfigMargeCreate) -> ConfigMarge:
    obj = ConfigMarge(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_marge(db: Session, id_: int) -> Optional[ConfigMarge]:
    return db.query(ConfigMarge).filter(ConfigMarge.id == id_).first()

def get_all_marges(db: Session) -> List[ConfigMarge]:
    return db.query(ConfigMarge).all()

def update_marge(db: Session, id_: int, data: ConfigMargeUpdate) -> Optional[ConfigMarge]:
    obj = get_marge(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_marge(db: Session, id_: int) -> bool:
    obj = get_marge(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_marges(db: Session, search_data: ConfigMargeSearch) -> List[ConfigMarge]:
    query = db.query(ConfigMarge)
    if search_data.client_id:
        query = query.filter(ConfigMarge.client_id == search_data.client_id)
    if search_data.entreprise_id:
        query = query.filter(ConfigMarge.entreprise_id == search_data.entreprise_id)
    if search_data.type_marge:
        query = query.filter(ConfigMarge.type_marge == search_data.type_marge)
    return query.all()