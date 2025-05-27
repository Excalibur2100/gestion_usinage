from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.finance.config_paiement import ConfigPaiement
from db.schemas.finance.config_paiement_schemas import *

def create_config_paiement(db: Session, data: ConfigPaiementCreate) -> ConfigPaiement:
    obj = ConfigPaiement(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_config_paiement(db: Session, id_: int) -> Optional[ConfigPaiement]:
    return db.query(ConfigPaiement).filter(ConfigPaiement.id == id_).first()

def get_all_config_paiements(db: Session) -> List[ConfigPaiement]:
    return db.query(ConfigPaiement).all()

def update_config_paiement(db: Session, id_: int, data: ConfigPaiementUpdate) -> Optional[ConfigPaiement]:
    obj = get_config_paiement(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_config_paiement(db: Session, id_: int) -> bool:
    obj = get_config_paiement(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_config_paiements(db: Session, search_data: ConfigPaiementSearch) -> List[ConfigPaiement]:
    query = db.query(ConfigPaiement)
    if search_data.libelle:
        query = query.filter(ConfigPaiement.libelle.ilike(f"%{search_data.libelle}%"))
    if search_data.actif is not None:
        query = query.filter(ConfigPaiement.actif == search_data.actif)
    return query.all()