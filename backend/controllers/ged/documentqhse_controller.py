from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.models.database import get_db
from backend.services.ged.document_rh_service import (
    get_documents_qhse,
    get_document_qhse_by_id,
    create_document_qhse,
    update_document_qhse,
    delete_document_qhse,
)
from backend.db.schemas.ged.documents_qhse_schemas import DocumentsQHSECreate, DocumentsQHSEUpdate

router = APIRouter(prefix="/documentqhse", tags=["Document QHSE"])

@router.get("/", response_model=list)
def list_documents(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Endpoint pour récupérer tous les documents QHSE.
    """
    return get_documents_qhse(db, skip=skip, limit=limit)

@router.get("/{document_id}", response_model=dict)
def get_document(document_id: int, db: Session = Depends(get_db)):
    """
    Endpoint pour récupérer un document QHSE spécifique par son ID.
    """
    return get_document_qhse_by_id(db, document_id)

@router.post("/", response_model=dict)
def create_document(document_data: DocumentsQHSECreate, db: Session = Depends(get_db)):
    """
    Endpoint pour créer un nouveau document QHSE.
    """
    return create_document_qhse(db, document_data)

@router.put("/{document_id}", response_model=dict)
def update_document(document_id: int, document_data: DocumentsQHSEUpdate, db: Session = Depends(get_db)):
    """
    Endpoint pour mettre à jour un document QHSE existant.
    """
    return update_document_qhse(db, document_id, document_data)

@router.delete("/{document_id}")
def delete_document(document_id: int, db: Session = Depends(get_db)):
    """
    Endpoint pour supprimer un document QHSE par son ID.
    """
    delete_document_qhse(db, document_id)
    return {"message": "Document QHSE supprimé avec succès"}