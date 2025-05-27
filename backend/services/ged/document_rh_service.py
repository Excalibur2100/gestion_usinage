from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.ged.document_rh import DocumentRH
from db.schemas.ged.documents_rh_schemas import *

def create_document(db: Session, data: DocumentRHCreate) -> DocumentRH:
    obj = DocumentRH(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_document(db: Session, id_: int) -> Optional[DocumentRH]:
    return db.query(DocumentRH).filter(DocumentRH.id == id_).first()

def get_all_documents(db: Session) -> List[DocumentRH]:
    return db.query(DocumentRH).all()

def update_document(db: Session, id_: int, data: DocumentRHUpdate) -> Optional[DocumentRH]:
    obj = get_document(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_document(db: Session, id_: int) -> bool:
    obj = get_document(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_documents(db: Session, search_data: DocumentRHSearch) -> List[DocumentRH]:
    query = db.query(DocumentRH)
    if search_data.employe_id:
        query = query.filter(DocumentRH.employe_id == search_data.employe_id)
    if search_data.type_document:
        query = query.filter(DocumentRH.type_document == search_data.type_document)
    return query.all()