from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.crm.historique_client import HistoriqueClient
from db.schemas.crm.historique_client_schemas import *

def create_historique(db: Session, data: HistoriqueClientCreate) -> HistoriqueClient:
    obj = HistoriqueClient(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_historique(db: Session, id_: int) -> Optional[HistoriqueClient]:
    return db.query(HistoriqueClient).filter(HistoriqueClient.id == id_).first()

def get_all_historiques(db: Session) -> List[HistoriqueClient]:
    return db.query(HistoriqueClient).all()

def update_historique(db: Session, id_: int, data: HistoriqueClientUpdate) -> Optional[HistoriqueClient]:
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

def search_historiques(db: Session, search_data: HistoriqueClientSearch) -> List[HistoriqueClient]:
    query = db.query(HistoriqueClient)
    if search_data.client_id:
        query = query.filter(HistoriqueClient.client_id == search_data.client_id)
    if search_data.type_action:
        query = query.filter(HistoriqueClient.type_action.ilike(f"%{search_data.type_action}%"))
    if search_data.auteur:
        query = query.filter(HistoriqueClient.auteur.ilike(f"%{search_data.auteur}%"))
    return query.all()