from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.ged.documents_qhse_schemas import *
from services.ged.document_qhse_service import *

router = APIRouter(prefix="/documents-qhse", tags=["Documents QHSE"])

@router.post("/", response_model=DocumentQHSERead)
def create(data: DocumentQHSECreate, db: Session = Depends(get_db)):
    return create_document_qhse(db, data)

@router.get("/", response_model=List[DocumentQHSERead])
def read_all(db: Session = Depends(get_db)):
    return get_all_documents_qhse(db)

@router.get("/{id_}", response_model=DocumentQHSERead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_document_qhse(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Document QHSE non trouvé")
    return obj

@router.put("/{id_}", response_model=DocumentQHSERead)
def update(id_: int, data: DocumentQHSEUpdate, db: Session = Depends(get_db)):
    obj = update_document_qhse(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Document QHSE non trouvé")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_document_qhse(db, id_):
        raise HTTPException(status_code=404, detail="Document QHSE non trouvé")
    return {"ok": True}

@router.post("/search", response_model=DocumentQHSESearchResults)
def search(data: DocumentQHSESearch, db: Session = Depends(get_db)):
    return {"results": search_documents_qhse(db, data)}