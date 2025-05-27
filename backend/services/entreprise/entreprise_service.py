from sqlalchemy.orm import Session
from typing import List, Optional
from db.models.tables.entreprise.entreprise import Entreprise
from db.schemas.entreprise.entreprise_schemas import *

def create_entreprise(db: Session, data: EntrepriseCreate) -> Entreprise:
    obj = Entreprise(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_entreprise(db: Session, id_: int) -> Optional[Entreprise]:
    return db.query(Entreprise).filter(Entreprise.id == id_).first()

def get_all_entreprises(db: Session) -> List[Entreprise]:
    return db.query(Entreprise).all()

def update_entreprise(db: Session, id_: int, data: EntrepriseUpdate) -> Optional[Entreprise]:
    obj = get_entreprise(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_entreprise(db: Session, id_: int) -> bool:
    obj = get_entreprise(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_entreprises(db: Session, search_data: EntrepriseSearch) -> List[Entreprise]:
    query = db.query(Entreprise)
    if search_data.nom:
        query = query.filter(Entreprise.nom.ilike(f"%{search_data.nom}%"))
    if search_data.siret:
        query = query.filter(Entreprise.siret.ilike(f"%{search_data.siret}%"))
    if search_data.pays:
        query = query.filter(Entreprise.pays.ilike(f"%{search_data.pays}%"))
    return query.all()