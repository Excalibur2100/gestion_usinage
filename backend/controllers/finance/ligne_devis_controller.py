from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.finance.ligne_devis_schemas import *
from services.finance.ligne_devis_service import *

router = APIRouter(prefix="/lignes-devis", tags=["Lignes Devis"])

@router.post("/", response_model=LigneDevisRead)
def create(data: LigneDevisCreate, db: Session = Depends(get_db)):
    return create_ligne(db, data)

@router.get("/", response_model=List[LigneDevisRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_lignes(db)

@router.get("/{id_}", response_model=LigneDevisRead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_ligne(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Ligne non trouvée")
    return obj

@router.put("/{id_}", response_model=LigneDevisRead)
def update(id_: int, data: LigneDevisUpdate, db: Session = Depends(get_db)):
    obj = update_ligne(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Ligne non trouvée")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_ligne(db, id_):
        raise HTTPException(status_code=404, detail="Ligne non trouvée")
    return {"ok": True}

@router.post("/search", response_model=LigneDevisSearchResults)
def search(data: LigneDevisSearch, db: Session = Depends(get_db)):
    return {"results": search_lignes(db, data)}