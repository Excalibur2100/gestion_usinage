from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from  db.models.database import get_db
from  services.documentrh.documentrh_service import (
    get_documents_rh,
    get_document_rh_by_id,
    create_document_rh,
    update_document_rh,
    delete_document_rh,
)
from backend.db.schemas.documents_rh_schemas.documents_rh_schemas import DocumentRHCreate, DocumentRHUpdate

router = APIRouter(prefix="/documentrh", tags=["Document RH"])

@router.get("/", response_model=list)
def list_documents(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Endpoint pour récupérer tous les documents RH.
    """
    return get_documents_rh(db, skip=skip, limit=limit)

@router.get("/{document_id}", response_model=dict)
def get_document(document_id: int, db: Session = Depends(get_db)):
    """
    Endpoint pour récupérer un document RH spécifique par son ID.
    """
    return get_document_rh_by_id(db, document_id)

@router.post("/", response_model=dict)
def create_document(document_data: DocumentRHCreate, db: Session = Depends(get_db)):
    """
    Endpoint pour créer un nouveau document RH.
    """
    return create_document_rh(db, document_data)

@router.put("/{document_id}", response_model=dict)
def update_document(document_id: int, document_data: DocumentRHUpdate, db: Session = Depends(get_db)):
    """
    Endpoint pour mettre à jour un document RH existant.
    """
    return update_document_rh(db, document_id, document_data)

@router.delete("/{document_id}")
def delete_document(document_id: int, db: Session = Depends(get_db)):
    """
    Endpoint pour supprimer un document RH par son ID.
    """
    return delete_document_rh(db, document_id)