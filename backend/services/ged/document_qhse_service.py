from sqlalchemy.orm import Session
from backend.db.models.tables.ged.document_rh import DocumentRH
from backend.db.schemas.ged.documents_rh_schemas import DocumentRHCreate, DocumentRHUpdate
from fastapi import HTTPException

def get_documents_rh(db: Session, skip: int = 0, limit: int = 10):
    """
    Récupère une liste paginée des documents RH.
    """
    return db.query(DocumentRH).offset(skip).limit(limit).all()

def get_document_rh_by_id(db: Session, document_id: int):
    """
    Récupère un document RH par son ID.
    """
    document = db.query(DocumentRH).filter(DocumentRH.id == document_id).first()
    if not document:
        raise HTTPException(status_code=404, detail="Document RH non trouvé")
    return document

def create_document_rh(db: Session, document_data: DocumentRHCreate):
    """
    Crée un nouveau document RH.
    """
    document = DocumentRH(**document_data.dict())
    db.add(document)
    db.commit()
    db.refresh(document)
    return document

def update_document_rh(db: Session, document_id: int, document_data: DocumentRHUpdate):
    """
    Met à jour un document RH existant.
    """
    document = get_document_rh_by_id(db, document_id)
    for key, value in document_data.dict(exclude_unset=True).items():
        setattr(document, key, value)
    db.commit()
    db.refresh(document)
    return document

def delete_document_rh(db: Session, document_id: int):
    """
    Supprime un document RH par son ID.
    """
    document = get_document_rh_by_id(db, document_id)
    db.delete(document)
    db.commit()
    return {"message": "Document RH supprimé avec succès"}