from sqlalchemy.orm import Session
from backend.db.models.tables.entreprise.entreprise import Entreprise
from backend.db.schemas.entreprise.entreprise_schemas import *

def create_entreprise(db: Session, data: EntrepriseCreate) -> Entreprise:
    db_obj = Entreprise(**data.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_entreprise(db: Session, entreprise_id: int) -> Entreprise:
    return db.query(Entreprise).filter(Entreprise.id == entreprise_id).first()

def get_all_entreprises(db: Session) -> list[Entreprise]:
    return db.query(Entreprise).all()

from typing import Optional

def update_entreprise(db: Session, entreprise_id: int, data: EntrepriseUpdate) -> Optional[Entreprise]:
    entreprise = db.query(Entreprise).filter(Entreprise.id == entreprise_id).first()
    if not entreprise:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(entreprise, key, value)
    db.commit()
    db.refresh(entreprise)
    return entreprise

def delete_entreprise(db: Session, entreprise_id: int) -> bool:
    entreprise = db.query(Entreprise).filter(Entreprise.id == entreprise_id).first()
    if entreprise:
        db.delete(entreprise)
        db.commit()
        return True
    return False

def search_entreprises(db: Session, search_data: EntrepriseSearch) -> list[Entreprise]:
    query = db.query(Entreprise)
    if search_data.nom:
        query = query.filter(Entreprise.nom.ilike(f"%{search_data.nom}%"))
    if search_data.siret:
        query = query.filter(Entreprise.siret.ilike(f"%{search_data.siret}%"))
    if search_data.pays:
        query = query.filter(Entreprise.pays.ilike(f"%{search_data.pays}%"))
    return query.all()
