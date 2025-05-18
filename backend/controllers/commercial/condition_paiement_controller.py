from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.commercial.condition_paiement_schemas import *
from services.commercial.condition_paiement_service import *

router = APIRouter(prefix="/conditions-paiement", tags=["Conditions Paiement"])

@router.post("/", response_model=ConditionPaiementRead)
def create(data: ConditionPaiementCreate, db: Session = Depends(get_db)):
    return create_condition(db, data)

@router.get("/", response_model=List[ConditionPaiementRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_conditions(db)

@router.get("/{id_}", response_model=ConditionPaiementRead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_condition(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Condition non trouvée")
    return obj

@router.put("/{id_}", response_model=ConditionPaiementRead)
def update(id_: int, data: ConditionPaiementUpdate, db: Session = Depends(get_db)):
    obj = update_condition(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Condition non trouvée")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_condition(db, id_):
        raise HTTPException(status_code=404, detail="Condition non trouvée")
    return {"ok": True}

@router.post("/search", response_model=ConditionPaiementSearchResults)
def search(data: ConditionPaiementSearch, db: Session = Depends(get_db)):
    return {"results": search_conditions(db, data)}
