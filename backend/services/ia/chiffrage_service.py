from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.ia.chiffrage import Chiffrage
from db.schemas.ia.chiffrage_schemas import *

def create_chiffrage(db: Session, data: ChiffrageCreate) -> Chiffrage:
    obj = Chiffrage(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_chiffrage(db: Session, id_: int) -> Optional[Chiffrage]:
    return db.query(Chiffrage).filter(Chiffrage.id == id_).first()

def get_all_chiffrages(db: Session) -> List[Chiffrage]:
    return db.query(Chiffrage).all()

def update_chiffrage(db: Session, id_: int, data: ChiffrageUpdate) -> Optional[Chiffrage]:
    obj = get_chiffrage(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_chiffrage(db: Session, id_: int) -> bool:
    obj = get_chiffrage(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_chiffrages(db: Session, search_data: ChiffrageSearch) -> List[Chiffrage]:
    query = db.query(Chiffrage)
    if search_data.piece_id:
        query = query.filter(Chiffrage.piece_id == search_data.piece_id)
    if search_data.utilisateur_id:
        query = query.filter(Chiffrage.utilisateur_id == search_data.utilisateur_id)
    if search_data.entreprise_id:
        query = query.filter(Chiffrage.entreprise_id == search_data.entreprise_id)
    if search_data.origine:
        query = query.filter(Chiffrage.origine == search_data.origine)
    return query.all()