from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.finance.config_marge_schemas import *
from services.finance.config_marge_service import *

router = APIRouter(prefix="/config-marges", tags=["Configuration Marges"])

@router.post("/", response_model=ConfigMargeRead)
def create(data: ConfigMargeCreate, db: Session = Depends(get_db)):
    return create_marge(db, data)

@router.get("/", response_model=List[ConfigMargeRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_marges(db)

@router.get("/{id_}", response_model=ConfigMargeRead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_marge(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Marge non trouvée")
    return obj

@router.put("/{id_}", response_model=ConfigMargeRead)
def update(id_: int, data: ConfigMargeUpdate, db: Session = Depends(get_db)):
    obj = update_marge(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Marge non trouvée")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_marge(db, id_):
        raise HTTPException(status_code=404, detail="Marge non trouvée")
    return {"ok": True}

@router.post("/search", response_model=ConfigMargeSearchResults)
def search(data: ConfigMargeSearch, db: Session = Depends(get_db)):
    return {"results": search_marges(db, data)}