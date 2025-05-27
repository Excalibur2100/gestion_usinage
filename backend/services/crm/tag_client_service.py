from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.crm.tag_client import TagClient
from db.schemas.crm.tag_client_schemas import *

def create_tag_client(db: Session, data: TagClientCreate) -> TagClient:
    obj = TagClient(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_tag_client(db: Session, id_: int) -> Optional[TagClient]:
    return db.query(TagClient).filter(TagClient.id == id_).first()

def get_all_tags_clients(db: Session) -> List[TagClient]:
    return db.query(TagClient).all()

def update_tag_client(db: Session, id_: int, data: TagClientUpdate) -> Optional[TagClient]:
    obj = get_tag_client(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_tag_client(db: Session, id_: int) -> bool:
    obj = get_tag_client(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_tag_clients(db: Session, search_data: TagClientSearch) -> List[TagClient]:
    query = db.query(TagClient)
    if search_data.client_id:
        query = query.filter(TagClient.client_id == search_data.client_id)
    if search_data.tag_id:
        query = query.filter(TagClient.tag_id == search_data.tag_id)
    return query.all()