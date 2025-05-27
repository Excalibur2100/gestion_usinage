from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.crm.client import Client
from db.schemas.crm.client_schemas import *

def create_client(db: Session, data: ClientCreate) -> Client:
    obj = Client(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_client(db: Session, client_id: int) -> Optional[Client]:
    return db.query(Client).filter(Client.id == client_id).first()

def get_all_clients(db: Session) -> List[Client]:
    return db.query(Client).all()

def update_client(db: Session, client_id: int, data: ClientUpdate) -> Optional[Client]:
    obj = get_client(db, client_id)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_client(db: Session, client_id: int) -> bool:
    obj = get_client(db, client_id)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_clients(db: Session, search_data: ClientSearch) -> List[Client]:
    query = db.query(Client)
    if search_data.code_client:
        query = query.filter(Client.code_client.ilike(f"%{search_data.code_client}%"))
    if search_data.nom:
        query = query.filter(Client.nom.ilike(f"%{search_data.nom}%"))
    if search_data.tva:
        query = query.filter(Client.tva.ilike(f"%{search_data.tva}%"))
    if search_data.actif is not None:
        query = query.filter(Client.actif == search_data.actif)
    return query.all()