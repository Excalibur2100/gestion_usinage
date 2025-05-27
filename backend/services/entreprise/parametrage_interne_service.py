from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.entreprise.parametrage_interne import ParametrageInterne
from db.schemas.entreprise.parametrage_interne_schemas import *

def create_parametre(db: Session, data: ParametrageInterneCreate) -> ParametrageInterne:
    obj = ParametrageInterne(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_parametre(db: Session, id_: int) -> Optional[ParametrageInterne]:
    return db.query(ParametrageInterne).filter(ParametrageInterne.id == id_).first()

def get_all_parametres(db: Session) -> List[ParametrageInterne]:
    return db.query(ParametrageInterne).all()

def update_parametre(db: Session, id_: int, data: ParametrageInterneUpdate) -> Optional[ParametrageInterne]:
    obj = get_parametre(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_parametre(db: Session, id_: int) -> bool:
    obj = get_parametre(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_parametres(db: Session, search_data: ParametrageInterneSearch) -> List[ParametrageInterne]:
    query = db.query(ParametrageInterne)
    if search_data.entreprise_id:
        query = query.filter(ParametrageInterne.entreprise_id == search_data.entreprise_id)
    if search_data.cle:
        query = query.filter(ParametrageInterne.cle.ilike(f"%{search_data.cle}%"))
    if search_data.actif is not None:
        query = query.filter(ParametrageInterne.actif == search_data.actif)
    return query.all()