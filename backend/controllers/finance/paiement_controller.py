from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.finance.paiement_schemas import *
from services.finance.paiement_service import *

router = APIRouter(prefix="/paiements", tags=["Paiements"])

@router.post("/", response_model=PaiementRead)
def create(data: PaiementCreate, db: Session = Depends(get_db)):
    return create_paiement(db, data)

@router.get("/", response_model=List[PaiementRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_paiements(db)

@router.get("/{id_}", response_model=PaiementRead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_paiement(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Paiement non trouvé")
    return obj

@router.put("/{id_}", response_model=PaiementRead)
def update(id_: int, data: PaiementUpdate, db: Session = Depends(get_db)):
    obj = update_paiement(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Paiement non trouvé")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_paiement(db, id_):
        raise HTTPException(status_code=404, detail="Paiement non trouvé")
    return {"ok": True}

@router.post("/search", response_model=PaiementSearchResults)
def search(data: PaiementSearch, db: Session = Depends(get_db)):
    return {"results": search_paiements(db, data)}