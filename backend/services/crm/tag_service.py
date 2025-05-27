# tag_service.py - contenu à injecter completfrom typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.crm.tag import Tag
from db.schemas.crm.tag_schemas import *

def create_tag(db: Session, data: TagCreate) -> Tag:
    obj = Tag(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_tag(db: Session, id_: int) -> Optional[Tag]:
    return db.query(Tag).filter(Tag.id == id_).first()

def get_all_tags(db: Session) -> List[Tag]:
    return db.query(Tag).all()

def update_tag(db: Session, id_: int, data: TagUpdate) -> Optional[Tag]:
    obj = get_tag(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_tag(db: Session, id_: int) -> bool:
    obj = get_tag(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_tags(db: Session, search_data: TagSearch) -> List[Tag]:
    query = db.query(Tag)
    if search_data.nom:
        query = query.filter(Tag.nom.ilike(f"%{search_data.nom}%"))
    return query.all()