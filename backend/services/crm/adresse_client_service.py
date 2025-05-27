from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.crm.adresse_client import AdresseClient
from db.schemas.crm.adresse_client_schemas import *

def create_adresse(db: Session, data: AdresseClientCreate) -> AdresseClient:
    obj = AdresseClient(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_adresse(db: Session, id_: int) -> Optional[AdresseClient]:
    return db.query(AdresseClient).filter(AdresseClient.id == id_).first()

def get_all_adresses(db: Session) -> List[AdresseClient]:
    return db.query(AdresseClient).all()

def update_adresse(db: Session, id_: int, data: AdresseClientUpdate) -> Optional[AdresseClient]:
    obj = get_adresse(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_adresse(db: Session, id_: int) -> bool:
    obj = get_adresse(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_adresses(db: Session, search_data: AdresseClientSearch) -> List[AdresseClient]:
    query = db.query(AdresseClient)
    if search_data.client_id:
        query = query.filter(AdresseClient.client_id == search_data.client_id)
    if search_data.type_adresse:
        query = query.filter(AdresseClient.type_adresse.ilike(f"%{search_data.type_adresse}%"))
    if search_data.ville:
        query = query.filter(AdresseClient.ville.ilike(f"%{search_data.ville}%"))
    if search_data.principale is not None:
        query = query.filter(AdresseClient.principale == search_data.principale)
    return query.all()