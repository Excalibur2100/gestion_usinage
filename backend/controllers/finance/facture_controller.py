from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.finance.facture_schemas import *
from services.finance.facture_service import *

router = APIRouter(prefix="/factures", tags=["Factures"])

@router.post("/", response_model=FactureRead)
def create(data: FactureCreate, db: Session = Depends(get_db)):
    return create_facture(db, data)

@router.get("/", response_model=List[FactureRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_factures(db)

@router.get("/{id_}", response_model=FactureRead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_facture(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Facture non trouvée")
    return obj

@router.put("/{id_}", response_model=FactureRead)
def update(id_: int, data: FactureUpdate, db: Session = Depends(get_db)):
    obj = update_facture(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Facture non trouvée")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_facture(db, id_):
        raise HTTPException(status_code=404, detail="Facture non trouvée")
    return {"ok": True}

@router.post("/search", response_model=FactureSearchResults)
def search(data: FactureSearch, db: Session = Depends(get_db)):
    return {"results": search_factures(db, data)}