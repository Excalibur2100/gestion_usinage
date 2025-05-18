from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.commercial.commande import Commande
from db.schemas.commercial.commande_schemas import *

def create_commande(db: Session, data: CommandeCreate) -> Commande:
    obj = Commande(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_commande(db: Session, commande_id: int) -> Optional[Commande]:
    return db.query(Commande).filter(Commande.id == commande_id).first()

def get_all_commandes(db: Session) -> List[Commande]:
    return db.query(Commande).all()

def update_commande(db: Session, commande_id: int, data: CommandeUpdate) -> Optional[Commande]:
    obj = get_commande(db, commande_id)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_commande(db: Session, commande_id: int) -> bool:
    obj = get_commande(db, commande_id)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_commandes(db: Session, search_data: CommandeSearch) -> List[Commande]:
    query = db.query(Commande)
    if search_data.code_commande:
        query = query.filter(Commande.code_commande.ilike(f"%{search_data.code_commande}%"))
    if search_data.client_id:
        query = query.filter(Commande.client_id == search_data.client_id)
    if search_data.statut:
        query = query.filter(Commande.statut == search_data.statut)
    return query.all()
