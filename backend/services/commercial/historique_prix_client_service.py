from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.commercial.historique_prix_client import HistoriquePrixClient
from db.schemas.commercial.historique_prix_client_schemas import *

def create_historique(db: Session, data: HistoriquePrixClientCreate) -> HistoriquePrixClient:
    obj = HistoriquePrixClient(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_historique(db: Session, id_: int) -> Optional[HistoriquePrixClient]:
    return db.query(HistoriquePrixClient).filter(HistoriquePrixClient.id == id_).first()

def get_all_historiques(db: Session) -> List[HistoriquePrixClient]:
    return db.query(HistoriquePrixClient).all()

def update_historique(db: Session, id_: int, data: HistoriquePrixClientUpdate) -> Optional[HistoriquePrixClient]:
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

def search_historiques(db: Session, search_data: HistoriquePrixClientSearch) -> List[HistoriquePrixClient]:
    query = db.query(HistoriquePrixClient)
    if search_data.client_id:
        query = query.filter(HistoriquePrixClient.client_id == search_data.client_id)
    if search_data.piece_id:
        query = query.filter(HistoriquePrixClient.piece_id == search_data.piece_id)
    return query.all()
