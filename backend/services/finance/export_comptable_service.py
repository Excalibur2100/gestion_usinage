from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.finance.export_comptable import ExportComptable
from db.schemas.finance.export_comptable_schemas import *

def create_export(db: Session, data: ExportComptableCreate) -> ExportComptable:
    obj = ExportComptable(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_export(db: Session, id_: int) -> Optional[ExportComptable]:
    return db.query(ExportComptable).filter(ExportComptable.id == id_).first()

def get_all_exports(db: Session) -> List[ExportComptable]:
    return db.query(ExportComptable).all()

def update_export(db: Session, id_: int, data: ExportComptableUpdate) -> Optional[ExportComptable]:
    obj = get_export(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_export(db: Session, id_: int) -> bool:
    obj = get_export(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_exports(db: Session, search_data: ExportComptableSearch) -> List[ExportComptable]:
    query = db.query(ExportComptable)
    if search_data.entreprise_id:
        query = query.filter(ExportComptable.entreprise_id == search_data.entreprise_id)
    if search_data.type_export:
        query = query.filter(ExportComptable.type_export.ilike(f"%{search_data.type_export}%"))
    if search_data.format_export:
        query = query.filter(ExportComptable.format_export == search_data.format_export)
    return query.all()