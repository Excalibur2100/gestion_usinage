from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.finance.journal_comptable import JournalComptable
from db.schemas.finance.journal_comptable_schemas import *

def create_ecriture(db: Session, data: JournalComptableCreate) -> JournalComptable:
    obj = JournalComptable(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_ecriture(db: Session, id_: int) -> Optional[JournalComptable]:
    return db.query(JournalComptable).filter(JournalComptable.id == id_).first()

def get_all_ecritures(db: Session) -> List[JournalComptable]:
    return db.query(JournalComptable).all()

def update_ecriture(db: Session, id_: int, data: JournalComptableUpdate) -> Optional[JournalComptable]:
    obj = get_ecriture(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_ecriture(db: Session, id_: int) -> bool:
    obj = get_ecriture(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_ecritures(db: Session, search_data: JournalComptableSearch) -> List[JournalComptable]:
    query = db.query(JournalComptable)
    if search_data.type_ecriture:
        query = query.filter(JournalComptable.type_ecriture == search_data.type_ecriture)
    if search_data.entreprise_id:
        query = query.filter(JournalComptable.entreprise_id == search_data.entreprise_id)
    return query.all()