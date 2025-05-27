from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.ged.documents_qualite import DocumentQualite
from db.schemas.ged.document_qualite_schemas import *

def create_document(db: Session, data: DocumentQualiteCreate) -> DocumentQualite:
    obj = DocumentQualite(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_document(db: Session, id_: int) -> Optional[DocumentQualite]:
    return db.query(DocumentQualite).filter(DocumentQualite.id == id_).first()

def get_all_documents(db: Session) -> List[DocumentQualite]:
    return db.query(DocumentQualite).all()

def update_document(db: Session, id_: int, data: DocumentQualiteUpdate) -> Optional[DocumentQualite]:
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

def search_documents(db: Session, search_data: DocumentQualiteSearch) -> List[DocumentQualite]:
    query = db.query(DocumentQualite)
    if search_data.entreprise_id:
        query = query.filter(DocumentQualite.entreprise_id == search_data.entreprise_id)
    if search_data.type_document:
        query = query.filter(DocumentQualite.type_document == search_data.type_document)
    return query.all()