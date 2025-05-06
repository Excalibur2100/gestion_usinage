# Service généré automatiquement
# Module : documentqhse

from sqlalchemy.orm import Session
from db.models.tables.documents_qhse import DocumentsQHSE
from db.schemas.documents_qhse_schemas import DocumentsQHSECreate, DocumentsQHSEUpdate
from fastapi import HTTPException

def get_documents_qhse(db: Session, skip: int = 0, limit: int = 10):
    """
    Récupère une liste paginée des documents QHSE.
    """
    return db.query(DocumentsQHSE).offset(skip).limit(limit).all()

def get_document_qhse_by_id(db: Session, document_id: int):
    """
    Récupère un document QHSE par son ID.
    """
    document = db.query(DocumentsQHSE).filter(DocumentsQHSE.id == document_id).first()
    if not document:
        raise HTTPException(status_code=404, detail="Document QHSE non trouvé")
    return document

def create_document_qhse(db: Session, document_data: DocumentsQHSECreate):
    """
    Crée un nouveau document QHSE.
    """
    document = DocumentsQHSE(**document_data.dict())
    db.add(document)
    db.commit()
    db.refresh(document)
    return document

def update_document_qhse(db: Session, document_id: int, document_data: DocumentsQHSEUpdate):
    """
    Met à jour un document QHSE existant.
    """
    document = get_document_qhse_by_id(db, document_id)
    for key, value in document_data.dict(exclude_unset=True).items():
        setattr(document, key, value)
    db.commit()
    db.refresh(document)
    return document

def delete_document_qhse(db: Session, document_id: int):
    """
    Supprime un document QHSE par son ID.
    """
    document = get_document_qhse_by_id(db, document_id)
    db.delete(document)
    db.commit()