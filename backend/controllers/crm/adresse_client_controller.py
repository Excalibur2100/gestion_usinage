from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.crm.adresse_client_schemas import *
from services.crm.adresse_client_service import *

router = APIRouter(prefix="/adresses-client", tags=["Adresses Client"])

@router.post("/", response_model=AdresseClientRead)
def create(data: AdresseClientCreate, db: Session = Depends(get_db)):
    return create_adresse(db, data)

@router.get("/", response_model=List[AdresseClientRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_adresses(db)

@router.get("/{id_}", response_model=AdresseClientRead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_adresse(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Adresse non trouvée")
    return obj

@router.put("/{id_}", response_model=AdresseClientRead)
def update(id_: int, data: AdresseClientUpdate, db: Session = Depends(get_db)):
    obj = update_adresse(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Adresse non trouvée")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_adresse(db, id_):
        raise HTTPException(status_code=404, detail="Adresse non trouvée")
    return {"ok": True}

@router.post("/search", response_model=AdresseClientSearchResults)
def search(data: AdresseClientSearch, db: Session = Depends(get_db)):
    return {"results": search_adresses(db, data)}