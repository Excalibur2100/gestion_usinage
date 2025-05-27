from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.ged.document_qualite_schemas import *
from services.ged.document_qualite_service import *

router = APIRouter(prefix="/documents-qualite", tags=["Documents Qualité"])

@router.post("/", response_model=DocumentQualiteRead)
def create(data: DocumentQualiteCreate, db: Session = Depends(get_db)):
    return create_document(db, data)

@router.get("/", response_model=List[DocumentQualiteRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_documents(db)

@router.get("/{id_}", response_model=DocumentQualiteRead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_document(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Document non trouvé")
    return obj

@router.put("/{id_}", response_model=DocumentQualiteRead)
def update(id_: int, data: DocumentQualiteUpdate, db: Session = Depends(get_db)):
    obj = update_document(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Document non trouvé")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_document(db, id_):
        raise HTTPException(status_code=404, detail="Document non trouvé")
    return {"ok": True}

@router.post("/search", response_model=DocumentQualiteSearchResults)
def search(data: DocumentQualiteSearch, db: Session = Depends(get_db)):
    return {"results": search_documents(db, data)}