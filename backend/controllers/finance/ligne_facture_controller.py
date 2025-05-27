from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.finance.ligne_facture_schemas import *
from services.finance.ligne_facture_service import *

router = APIRouter(prefix="/lignes-facture", tags=["Lignes Facture"])

@router.post("/", response_model=LigneFactureRead)
def create(data: LigneFactureCreate, db: Session = Depends(get_db)):
    return create_ligne_facture(db, data)

@router.get("/", response_model=List[LigneFactureRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_lignes_facture(db)

@router.get("/{id_}", response_model=LigneFactureRead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_ligne_facture(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Ligne non trouvée")
    return obj

@router.put("/{id_}", response_model=LigneFactureRead)
def update(id_: int, data: LigneFactureUpdate, db: Session = Depends(get_db)):
    obj = update_ligne_facture(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Ligne non trouvée")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_ligne_facture(db, id_):
        raise HTTPException(status_code=404, detail="Ligne non trouvée")
    return {"ok": True}

@router.post("/search", response_model=LigneFactureSearchResults)
def search(data: LigneFactureSearch, db: Session = Depends(get_db)):
    return {"results": search_lignes_facture(db, data)}