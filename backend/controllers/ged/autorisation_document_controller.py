from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.ged.autorisation_document_schemas import *
from services.ged.autorisation_document_service import *

router = APIRouter(prefix="/autorisations-documents", tags=["Autorisations Documents"])

@router.post("/", response_model=AutorisationDocumentRead)
def create(data: AutorisationDocumentCreate, db: Session = Depends(get_db)):
    return create_autorisation(db, data)

@router.get("/", response_model=List[AutorisationDocumentRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_autorisations(db)

@router.get("/{id_}", response_model=AutorisationDocumentRead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_autorisation(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Autorisation non trouvée")
    return obj

@router.put("/{id_}", response_model=AutorisationDocumentRead)
def update(id_: int, data: AutorisationDocumentUpdate, db: Session = Depends(get_db)):
    obj = update_autorisation(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Autorisation non trouvée")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_autorisation(db, id_):
        raise HTTPException(status_code=404, detail="Autorisation non trouvée")
    return {"ok": True}

@router.post("/search", response_model=AutorisationDocumentSearchResults)
def search(data: AutorisationDocumentSearch, db: Session = Depends(get_db)):
    return {"results": search_autorisations(db, data)}