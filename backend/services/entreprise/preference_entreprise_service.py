from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.entreprise.preference_entreprise import PreferenceEntreprise
from db.schemas.entreprise.preference_entreprise_schemas import *

def create_preference(db: Session, data: PreferenceEntrepriseCreate) -> PreferenceEntreprise:
    obj = PreferenceEntreprise(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_preference(db: Session, id_: int) -> Optional[PreferenceEntreprise]:
    return db.query(PreferenceEntreprise).filter(PreferenceEntreprise.id == id_).first()

def get_all_preferences(db: Session) -> List[PreferenceEntreprise]:
    return db.query(PreferenceEntreprise).all()

def update_preference(db: Session, id_: int, data: PreferenceEntrepriseUpdate) -> Optional[PreferenceEntreprise]:
    obj = get_preference(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_preference(db: Session, id_: int) -> bool:
    obj = get_preference(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_preferences(db: Session, search_data: PreferenceEntrepriseSearch) -> List[PreferenceEntreprise]:
    query = db.query(PreferenceEntreprise)
    if search_data.entreprise_id:
        query = query.filter(PreferenceEntreprise.entreprise_id == search_data.entreprise_id)
    if search_data.langue:
        query = query.filter(PreferenceEntreprise.langue == search_data.langue)
    return query.all()