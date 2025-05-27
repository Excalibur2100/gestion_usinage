from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.entreprise.profil_acces import ProfilAcces
from db.schemas.entreprise.profil_acces_schemas import *

def create_profil(db: Session, data: ProfilAccesCreate) -> ProfilAcces:
    obj = ProfilAcces(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_profil(db: Session, id_: int) -> Optional[ProfilAcces]:
    return db.query(ProfilAcces).filter(ProfilAcces.id == id_).first()

def get_all_profils(db: Session) -> List[ProfilAcces]:
    return db.query(ProfilAcces).all()

def update_profil(db: Session, id_: int, data: ProfilAccesUpdate) -> Optional[ProfilAcces]:
    obj = get_profil(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_profil(db: Session, id_: int) -> bool:
    obj = get_profil(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_profils(db: Session, search_data: ProfilAccesSearch) -> List[ProfilAcces]:
    query = db.query(ProfilAcces)
    if search_data.entreprise_id:
        query = query.filter(ProfilAcces.entreprise_id == search_data.entreprise_id)
    if search_data.nom:
        query = query.filter(ProfilAcces.nom.ilike(f"%{search_data.nom}%"))
    return query.all()