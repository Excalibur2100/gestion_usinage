from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.achat.avoir_fournisseur import AvoirFournisseur
from db.schemas.achat.avoir_fournisseur_schemas import *

def create_avoir(db: Session, data: AvoirFournisseurCreate) -> AvoirFournisseur:
    obj = AvoirFournisseur(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_avoir(db: Session, avoir_id: int) -> Optional[AvoirFournisseur]:
    return db.query(AvoirFournisseur).filter(AvoirFournisseur.id == avoir_id).first()

def get_all_avoirs(db: Session) -> List[AvoirFournisseur]:
    return db.query(AvoirFournisseur).all()

def update_avoir(db: Session, avoir_id: int, data: AvoirFournisseurUpdate) -> Optional[AvoirFournisseur]:
    obj = get_avoir(db, avoir_id)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_avoir(db: Session, avoir_id: int) -> bool:
    obj = get_avoir(db, avoir_id)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_avoirs(db: Session, search_data: AvoirFournisseurSearch) -> List[AvoirFournisseur]:
    query = db.query(AvoirFournisseur)
    if search_data.numero_avoir:
        query = query.filter(AvoirFournisseur.numero_avoir.ilike(f"%{search_data.numero_avoir}%"))
    if search_data.fournisseur_id:
        query = query.filter(AvoirFournisseur.fournisseur_id == search_data.fournisseur_id)
    if search_data.statut:
        query = query.filter(AvoirFournisseur.statut == search_data.statut)
    return query.all()
