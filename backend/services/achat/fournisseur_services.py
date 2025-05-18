from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.achat.fournisseur import Fournisseur
from db.schemas.achat.fournisseur_schemas import *

def create_fournisseur(db: Session, data: FournisseurCreate) -> Fournisseur:
    obj = Fournisseur(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_fournisseur(db: Session, fournisseur_id: int) -> Optional[Fournisseur]:
    return db.query(Fournisseur).filter(Fournisseur.id == fournisseur_id).first()

def get_all_fournisseurs(db: Session) -> List[Fournisseur]:
    return db.query(Fournisseur).all()

def update_fournisseur(db: Session, fournisseur_id: int, data: FournisseurUpdate) -> Optional[Fournisseur]:
    obj = get_fournisseur(db, fournisseur_id)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_fournisseur(db: Session, fournisseur_id: int) -> bool:
    obj = get_fournisseur(db, fournisseur_id)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_fournisseurs(db: Session, search_data: FournisseurSearch) -> List[Fournisseur]:
    query = db.query(Fournisseur)
    if search_data.code_fournisseur:
        query = query.filter(Fournisseur.code_fournisseur.ilike(f"%{search_data.code_fournisseur}%"))
    if search_data.nom:
        query = query.filter(Fournisseur.nom.ilike(f"%{search_data.nom}%"))
    if search_data.tva:
        query = query.filter(Fournisseur.tva.ilike(f"%{search_data.tva}%"))
    return query.all()
