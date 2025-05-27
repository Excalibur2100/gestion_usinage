from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.ged.documents_reglementaires import DocumentReglementaire
from db.schemas.ged.documents_reglementaires_schemas import *

def create_document(db: Session, data: DocumentReglementaireCreate) -> DocumentReglementaire:
    obj = DocumentReglementaire(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_document(db: Session, id_: int) -> Optional[DocumentReglementaire]:
    return db.query(DocumentReglementaire).filter(DocumentReglementaire.id == id_).first()

def get_all_documents(db: Session) -> List[DocumentReglementaire]:
    return db.query(DocumentReglementaire).all()

def update_document(db: Session, id_: int, data: DocumentReglementaireUpdate) -> Optional[DocumentReglementaire]:
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

def search_documents(db: Session, search_data: DocumentReglementaireSearch) -> List[DocumentReglementaire]:
    query = db.query(DocumentReglementaire)
    if search_data.entreprise_id:
        query = query.filter(DocumentReglementaire.entreprise_id == search_data.entreprise_id)
    if search_data.type_document:
        query = query.filter(DocumentReglementaire.type_document == search_data.type_document)
    return query.all()