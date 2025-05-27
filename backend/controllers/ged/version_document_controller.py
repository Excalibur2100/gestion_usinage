from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.ged.version_document_schemas import *
from services.ged.version_document_service import *

router = APIRouter(prefix="/versions-documents", tags=["Versions Documents"])

@router.post("/", response_model=VersionDocumentRead)
def create(data: VersionDocumentCreate, db: Session = Depends(get_db)):
    return create_version(db, data)

@router.get("/", response_model=List[VersionDocumentRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_versions(db)

@router.get("/{id_}", response_model=VersionDocumentRead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_version(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Version non trouvée")
    return obj

@router.put("/{id_}", response_model=VersionDocumentRead)
def update(id_: int, data: VersionDocumentUpdate, db: Session = Depends(get_db)):
    obj = update_version(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Version non trouvée")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_version(db, id_):
        raise HTTPException(status_code=404, detail="Version non trouvée")
    return {"ok": True}

@router.post("/search", response_model=VersionDocumentSearchResults)
def search(data: VersionDocumentSearch, db: Session = Depends(get_db)):
    return {"results": search_versions(db, data)}