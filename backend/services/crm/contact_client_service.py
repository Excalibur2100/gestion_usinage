from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.crm.contact_client import ContactClient
from db.schemas.crm.contact_client_schemas import *

def create_contact(db: Session, data: ContactClientCreate) -> ContactClient:
    obj = ContactClient(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_contact(db: Session, id_: int) -> Optional[ContactClient]:
    return db.query(ContactClient).filter(ContactClient.id == id_).first()

def get_all_contacts(db: Session) -> List[ContactClient]:
    return db.query(ContactClient).all()

def update_contact(db: Session, id_: int, data: ContactClientUpdate) -> Optional[ContactClient]:
    obj = get_contact(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_contact(db: Session, id_: int) -> bool:
    obj = get_contact(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_contacts(db: Session, search_data: ContactClientSearch) -> List[ContactClient]:
    query = db.query(ContactClient)
    if search_data.client_id:
        query = query.filter(ContactClient.client_id == search_data.client_id)
    if search_data.nom:
        query = query.filter(ContactClient.nom.ilike(f"%{search_data.nom}%"))
    if search_data.principal is not None:
        query = query.filter(ContactClient.principal == search_data.principal)
    return query.all()