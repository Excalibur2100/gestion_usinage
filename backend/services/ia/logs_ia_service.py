from typing import List, Optional
from sqlalchemy.orm import Session

from backend.db.models.tables.ia.logs_ia import LogIA
from backend.db.schemas.ia.log_ia_schemas import *

def create_log(db: Session, data: LogIACreate) -> LogIA:
    obj = LogIA(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_log(db: Session, id_: int) -> Optional[LogIA]:
    return db.query(LogIA).filter(LogIA.id == id_).first()

def get_all_logs(db: Session) -> List[LogIA]:
    return db.query(LogIA).all()

def update_log(db: Session, id_: int, data: LogIAUpdate) -> Optional[LogIA]:
    obj = get_log(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_log(db: Session, id_: int) -> bool:
    obj = get_log(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_logs(db: Session, search_data: LogIASearch) -> List[LogIA]:
    query = db.query(LogIA)
    if search_data.utilisateur_id:
        query = query.filter(LogIA.utilisateur_id == search_data.utilisateur_id)
    if search_data.module:
        query = query.filter(LogIA.module == search_data.module)
    if search_data.niveau:
        query = query.filter(LogIA.niveau == search_data.niveau)
    if search_data.statut:
        query = query.filter(LogIA.statut == search_data.statut)
    return query.all()