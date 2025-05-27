from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.finance.devis_schemas import *
from services.finance.devis_services import *

router = APIRouter(prefix="/devis", tags=["Devis"])

@router.post("/", response_model=DevisRead)
def create(data: DevisCreate, db: Session = Depends(get_db)):
    return create_devis(db, data)

@router.get("/", response_model=List[DevisRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_devis(db)

@router.get("/{id_}", response_model=DevisRead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_devis(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Devis non trouvé")
    return obj

@router.put("/{id_}", response_model=DevisRead)
def update(id_: int, data: DevisUpdate, db: Session = Depends(get_db)):
    obj = update_devis(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Devis non trouvé")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_devis(db, id_):
        raise HTTPException(status_code=404, detail="Devis non trouvé")
    return {"ok": True}

@router.post("/search", response_model=DevisSearchResults)
def search(data: DevisSearch, db: Session = Depends(get_db)):
    return {"results": search_devis(db, data)}