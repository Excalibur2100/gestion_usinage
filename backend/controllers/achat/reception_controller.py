from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.achat.reception_schemas import *
from services.achat.reception_service import *

router = APIRouter(prefix="/receptions", tags=["Réceptions"])

@router.post("/", response_model=ReceptionRead)
def create(data: ReceptionCreate, db: Session = Depends(get_db)):
    return create_reception(db, data)

@router.get("/", response_model=List[ReceptionRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_receptions(db)

@router.get("/{reception_id}", response_model=ReceptionRead)
def read(reception_id: int, db: Session = Depends(get_db)):
    obj = get_reception(db, reception_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Réception non trouvée")
    return obj

@router.put("/{reception_id}", response_model=ReceptionRead)
def update(reception_id: int, data: ReceptionUpdate, db: Session = Depends(get_db)):
    obj = update_reception(db, reception_id, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Réception non trouvée")
    return obj

@router.delete("/{reception_id}")
def delete(reception_id: int, db: Session = Depends(get_db)):
    if not delete_reception(db, reception_id):
        raise HTTPException(status_code=404, detail="Réception non trouvée")
    return {"ok": True}

@router.post("/search", response_model=ReceptionSearchResults)
def search(data: ReceptionSearch, db: Session = Depends(get_db)):
    return {"results": search_receptions(db, data)}
