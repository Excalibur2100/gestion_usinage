from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.ged.documents_qhse import DocumentQHSE
from db.schemas.ged.documents_qhse_schemas import *

def create_document_qhse(db: Session, data: DocumentQHSECreate) -> DocumentQHSE:
    obj = DocumentQHSE(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_document_qhse(db: Session, id_: int) -> Optional[DocumentQHSE]:
    return db.query(DocumentQHSE).filter(DocumentQHSE.id == id_).first()

def get_all_documents_qhse(db: Session) -> List[DocumentQHSE]:
    return db.query(DocumentQHSE).all()

def update_document_qhse(db: Session, id_: int, data: DocumentQHSEUpdate) -> Optional[DocumentQHSE]:
    obj = get_document_qhse(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_document_qhse(db: Session, id_: int) -> bool:
    obj = get_document_qhse(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_documents_qhse(db: Session, search_data: DocumentQHSESearch) -> List[DocumentQHSE]:
    query = db.query(DocumentQHSE)
    if search_data.entreprise_id:
        query = query.filter(DocumentQHSE.entreprise_id == search_data.entreprise_id)
    if search_data.categorie:
        query = query.filter(DocumentQHSE.categorie == search_data.categorie)
    return query.all()