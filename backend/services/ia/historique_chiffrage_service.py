from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.ia.historique_chiffrage import HistoriqueChiffrage
from db.schemas.ia.historique_chiffrage_schemas import *

def create_historique(db: Session, data: HistoriqueChiffrageCreate) -> HistoriqueChiffrage:
    obj = HistoriqueChiffrage(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_historique(db: Session, id_: int) -> Optional[HistoriqueChiffrage]:
    return db.query(HistoriqueChiffrage).filter(HistoriqueChiffrage.id == id_).first()

def get_all_historiques(db: Session) -> List[HistoriqueChiffrage]:
    return db.query(HistoriqueChiffrage).all()

def update_historique(db: Session, id_: int, data: HistoriqueChiffrageUpdate) -> Optional[HistoriqueChiffrage]:
    obj = get_historique(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_historique(db: Session, id_: int) -> bool:
    obj = get_historique(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_historiques(db: Session, search_data: HistoriqueChiffrageSearch) -> List[HistoriqueChiffrage]:
    query = db.query(HistoriqueChiffrage)
    if search_data.chiffrage_id:
        query = query.filter(HistoriqueChiffrage.chiffrage_id == search_data.chiffrage_id)
    if search_data.utilisateur_id:
        query = query.filter(HistoriqueChiffrage.utilisateur_id == search_data.utilisateur_id)
    if search_data.version:
        query = query.filter(HistoriqueChiffrage.version == search_data.version)
    return query.all()