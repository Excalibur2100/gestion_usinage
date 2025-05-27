from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.ged.version_document import VersionDocument
from db.schemas.ged.version_document_schemas import *

def create_version(db: Session, data: VersionDocumentCreate) -> VersionDocument:
    obj = VersionDocument(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_version(db: Session, id_: int) -> Optional[VersionDocument]:
    return db.query(VersionDocument).filter(VersionDocument.id == id_).first()

def get_all_versions(db: Session) -> List[VersionDocument]:
    return db.query(VersionDocument).all()

def update_version(db: Session, id_: int, data: VersionDocumentUpdate) -> Optional[VersionDocument]:
    obj = get_version(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_version(db: Session, id_: int) -> bool:
    obj = get_version(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_versions(db: Session, search_data: VersionDocumentSearch) -> List[VersionDocument]:
    query = db.query(VersionDocument)
    if search_data.document_id:
        query = query.filter(VersionDocument.document_id == search_data.document_id)
    if search_data.numero_version:
        query = query.filter(VersionDocument.numero_version == search_data.numero_version)
    return query.all()