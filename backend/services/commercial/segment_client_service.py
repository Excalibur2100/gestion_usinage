from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.commercial.segment_client import SegmentClient
from db.schemas.commercial.segment_client_schemas import *

def create_segment(db: Session, data: SegmentClientCreate) -> SegmentClient:
    obj = SegmentClient(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_segment(db: Session, id_: int) -> Optional[SegmentClient]:
    return db.query(SegmentClient).filter(SegmentClient.id == id_).first()

def get_all_segments(db: Session) -> List[SegmentClient]:
    return db.query(SegmentClient).all()

def update_segment(db: Session, id_: int, data: SegmentClientUpdate) -> Optional[SegmentClient]:
    obj = get_segment(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_segment(db: Session, id_: int) -> bool:
    obj = get_segment(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_segments(db: Session, search_data: SegmentClientSearch) -> List[SegmentClient]:
    query = db.query(SegmentClient)
    if search_data.libelle:
        query = query.filter(SegmentClient.libelle.ilike(f"%{search_data.libelle}%"))
    return query.all()
