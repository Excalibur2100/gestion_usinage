from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.commercial.portefeuille_client import PortefeuilleClient
from db.schemas.commercial.portefeuille_client_schemas import *

def create_portefeuille(db: Session, data: PortefeuilleClientCreate) -> PortefeuilleClient:
    obj = PortefeuilleClient(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_portefeuille(db: Session, id_: int) -> Optional[PortefeuilleClient]:
    return db.query(PortefeuilleClient).filter(PortefeuilleClient.id == id_).first()

def get_all_portefeuilles(db: Session) -> List[PortefeuilleClient]:
    return db.query(PortefeuilleClient).all()

def update_portefeuille(db: Session, id_: int, data: PortefeuilleClientUpdate) -> Optional[PortefeuilleClient]:
    obj = get_portefeuille(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_portefeuille(db: Session, id_: int) -> bool:
    obj = get_portefeuille(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_portefeuilles(db: Session, search_data: PortefeuilleClientSearch) -> List[PortefeuilleClient]:
    query = db.query(PortefeuilleClient)
    if search_data.client_id:
        query = query.filter(PortefeuilleClient.client_id == search_data.client_id)
    if search_data.utilisateur_id:
        query = query.filter(PortefeuilleClient.utilisateur_id == search_data.utilisateur_id)
    return query.all()
