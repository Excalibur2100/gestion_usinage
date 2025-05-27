from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.finance.commission_schemas import *
from services.finance.commission_service import *

router = APIRouter(prefix="/commissions", tags=["Commissions"])

@router.post("/", response_model=CommissionRead)
def create(data: CommissionCreate, db: Session = Depends(get_db)):
    return create_commission(db, data)

@router.get("/", response_model=List[CommissionRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_commissions(db)

@router.get("/{id_}", response_model=CommissionRead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_commission(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Commission non trouvée")
    return obj

@router.put("/{id_}", response_model=CommissionRead)
def update(id_: int, data: CommissionUpdate, db: Session = Depends(get_db)):
    obj = update_commission(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Commission non trouvée")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_commission(db, id_):
        raise HTTPException(status_code=404, detail="Commission non trouvée")
    return {"ok": True}

@router.post("/search", response_model=CommissionSearchResults)
def search(data: CommissionSearch, db: Session = Depends(get_db)):
    return {"results": search_commissions(db, data)}