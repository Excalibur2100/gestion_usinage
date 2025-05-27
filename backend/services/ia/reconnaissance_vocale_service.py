from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.ia.reconnaissance_vocale import ReconnaissanceVocale
from db.schemas.ia.reconnaissance_vocale_schemas import *

def create_reconnaissance(db: Session, data: ReconnaissanceVocaleCreate) -> ReconnaissanceVocale:
    obj = ReconnaissanceVocale(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_reconnaissance(db: Session, id_: int) -> Optional[ReconnaissanceVocale]:
    return db.query(ReconnaissanceVocale).filter(ReconnaissanceVocale.id == id_).first()

def get_all_reconnaissances(db: Session) -> List[ReconnaissanceVocale]:
    return db.query(ReconnaissanceVocale).all()

def update_reconnaissance(db: Session, id_: int, data: ReconnaissanceVocaleUpdate) -> Optional[ReconnaissanceVocale]:
    obj = get_reconnaissance(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_reconnaissance(db: Session, id_: int) -> bool:
    obj = get_reconnaissance(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_reconnaissances(db: Session, search_data: ReconnaissanceVocaleSearch) -> List[ReconnaissanceVocale]:
    query = db.query(ReconnaissanceVocale)
    if search_data.utilisateur_id:
        query = query.filter(ReconnaissanceVocale.utilisateur_id == search_data.utilisateur_id)
    if search_data.langue:
        query = query.filter(ReconnaissanceVocale.langue == search_data.langue)
    if search_data.intention:
        query = query.filter(ReconnaissanceVocale.intention.ilike(f"%{search_data.intention}%"))
    return query.all()