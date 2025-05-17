from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.achat.ligne_commande_fournisseur import LigneCommandeFournisseur
from db.schemas.achat.ligne_commande_fournisseur_schemas import *

def create_ligne(db: Session, data: LigneCommandeFournisseurCreate) -> LigneCommandeFournisseur:
    obj = LigneCommandeFournisseur(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_ligne(db: Session, ligne_id: int) -> Optional[LigneCommandeFournisseur]:
    return db.query(LigneCommandeFournisseur).filter(LigneCommandeFournisseur.id == ligne_id).first()

def get_all_lignes(db: Session) -> List[LigneCommandeFournisseur]:
    return db.query(LigneCommandeFournisseur).all()

def update_ligne(db: Session, ligne_id: int, data: LigneCommandeFournisseurUpdate) -> Optional[LigneCommandeFournisseur]:
    obj = get_ligne(db, ligne_id)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_ligne(db: Session, ligne_id: int) -> bool:
    obj = get_ligne(db, ligne_id)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_lignes(db: Session, search_data: LigneCommandeFournisseurSearch) -> List[LigneCommandeFournisseur]:
    query = db.query(LigneCommandeFournisseur)
    if search_data.designation:
        query = query.filter(LigneCommandeFournisseur.designation.ilike(f"%{search_data.designation}%"))
    if search_data.commande_id:
        query = query.filter(LigneCommandeFournisseur.commande_id == search_data.commande_id)
    if search_data.produit_id:
        query = query.filter(LigneCommandeFournisseur.produit_id == search_data.produit_id)
    return query.all()
