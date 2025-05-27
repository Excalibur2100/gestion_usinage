from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.ged.signature_document_schemas import *
from services.ged.signature_document_service import *

router = APIRouter(prefix="/signatures-documents", tags=["Signatures Documents"])

@router.post("/", response_model=SignatureDocumentRead)
def create(data: SignatureDocumentCreate, db: Session = Depends(get_db)):
    return create_signature(db, data)

@router.get("/", response_model=List[SignatureDocumentRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_signatures(db)

@router.get("/{id_}", response_model=SignatureDocumentRead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_signature(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Signature non trouvée")
    return obj

@router.put("/{id_}", response_model=SignatureDocumentRead)
def update(id_: int, data: SignatureDocumentUpdate, db: Session = Depends(get_db)):
    obj = update_signature(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Signature non trouvée")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_signature(db, id_):
        raise HTTPException(status_code=404, detail="Signature non trouvée")
    return {"ok": True}

@router.post("/search", response_model=SignatureDocumentSearchResults)
def search(data: SignatureDocumentSearch, db: Session = Depends(get_db)):
    return {"results": search_signatures(db, data)}