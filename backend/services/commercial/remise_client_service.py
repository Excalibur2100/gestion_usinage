from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.commercial.remise_client import RemiseClient
from db.schemas.commercial.remise_client_schemas import *

def create_remise(db: Session, data: RemiseClientCreate) -> RemiseClient:
    obj = RemiseClient(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_remise(db: Session, id_: int) -> Optional[RemiseClient]:
    return db.query(RemiseClient).filter(RemiseClient.id == id_).first()

def get_all_remises(db: Session) -> List[RemiseClient]:
    return db.query(RemiseClient).all()

def update_remise(db: Session, id_: int, data: RemiseClientUpdate) -> Optional[RemiseClient]:
    obj = get_remise(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_remise(db: Session, id_: int) -> bool:
    obj = get_remise(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_remises(db: Session, search_data: RemiseClientSearch) -> List[RemiseClient]:
    query = db.query(RemiseClient)
    if search_data.client_id:
        query = query.filter(RemiseClient.client_id == search_data.client_id)
    if search_data.piece_id:
        query = query.filter(RemiseClient.piece_id == search_data.piece_id)
    if search_data.type_remise:
        query = query.filter(RemiseClient.type_remise == search_data.type_remise)
    return query.all()
