from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.finance.reglement_schemas import *
from services.finance.reglement_service import *

router = APIRouter(prefix="/reglements", tags=["Règlements"])

@router.post("/", response_model=ReglementRead)
def create(data: ReglementCreate, db: Session = Depends(get_db)):
    return create_reglement(db, data)

@router.get("/", response_model=List[ReglementRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_reglements(db)

@router.get("/{id_}", response_model=ReglementRead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_reglement(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Règlement non trouvé")
    return obj

@router.put("/{id_}", response_model=ReglementRead)
def update(id_: int, data: ReglementUpdate, db: Session = Depends(get_db)):
    obj = update_reglement(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Règlement non trouvé")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_reglement(db, id_):
        raise HTTPException(status_code=404, detail="Règlement non trouvé")
    return {"ok": True}

@router.post("/search", response_model=ReglementSearchResults)
def search(data: ReglementSearch, db: Session = Depends(get_db)):
    return {"results": search_reglements(db, data)}