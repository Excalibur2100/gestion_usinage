from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.crm.relance_schemas import *
from services.crm.relance_service import *

router = APIRouter(prefix="/relances", tags=["Relances Client"])

@router.post("/", response_model=RelanceRead)
def create(data: RelanceCreate, db: Session = Depends(get_db)):
    return create_relance(db, data)

@router.get("/", response_model=List[RelanceRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_relances(db)

@router.get("/{id_}", response_model=RelanceRead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_relance(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Relance non trouvée")
    return obj

@router.put("/{id_}", response_model=RelanceRead)
def update(id_: int, data: RelanceUpdate, db: Session = Depends(get_db)):
    obj = update_relance(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Relance non trouvée")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_relance(db, id_):
        raise HTTPException(status_code=404, detail="Relance non trouvée")
    return {"ok": True}

@router.post("/search", response_model=RelanceSearchResults)
def search(data: RelanceSearch, db: Session = Depends(get_db)):
    return {"results": search_relances(db, data)}