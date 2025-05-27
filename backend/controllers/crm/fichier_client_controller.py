from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.crm.fichier_client_schemas import *
from services.crm.fichier_client_service import *

router = APIRouter(prefix="/fichiers-client", tags=["Fichiers Client"])

@router.post("/", response_model=FichierClientRead)
def create(data: FichierClientCreate, db: Session = Depends(get_db)):
    return create_fichier(db, data)

@router.get("/", response_model=List[FichierClientRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_fichiers(db)

@router.get("/{id_}", response_model=FichierClientRead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_fichier(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Fichier non trouvé")
    return obj

@router.put("/{id_}", response_model=FichierClientRead)
def update(id_: int, data: FichierClientUpdate, db: Session = Depends(get_db)):
    obj = update_fichier(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Fichier non trouvé")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_fichier(db, id_):
        raise HTTPException(status_code=404, detail="Fichier non trouvé")
    return {"ok": True}

@router.post("/search", response_model=FichierClientSearchResults)
def search(data: FichierClientSearch, db: Session = Depends(get_db)):
    return {"results": search_fichiers(db, data)}