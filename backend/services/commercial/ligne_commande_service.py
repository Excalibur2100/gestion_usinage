from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.commercial.ligne_commande import LigneCommande
from db.schemas.commercial.ligne_commande_schemas import *

def create_ligne(db: Session, data: LigneCommandeCreate) -> LigneCommande:
    obj = LigneCommande(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_ligne(db: Session, ligne_id: int) -> Optional[LigneCommande]:
    return db.query(LigneCommande).filter(LigneCommande.id == ligne_id).first()

def get_all_lignes(db: Session) -> List[LigneCommande]:
    return db.query(LigneCommande).all()

def update_ligne(db: Session, ligne_id: int, data: LigneCommandeUpdate) -> Optional[LigneCommande]:
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

def search_lignes(db: Session, search_data: LigneCommandeSearch) -> List[LigneCommande]:
    query = db.query(LigneCommande)
    if search_data.designation:
        query = query.filter(LigneCommande.designation.ilike(f"%{search_data.designation}%"))
    if search_data.commande_id:
        query = query.filter(LigneCommande.commande_id == search_data.commande_id)
    if search_data.produit_id:
        query = query.filter(LigneCommande.produit_id == search_data.produit_id)
    return query.all()
