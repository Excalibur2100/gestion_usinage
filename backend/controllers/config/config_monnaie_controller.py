from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.config.config_monnaie_schemas import *
from services.config.config_monnaie_service import *

router = APIRouter(prefix="/config-monnaies", tags=["Configuration Monnaies"])

@router.post("/", response_model=ConfigMonnaieRead)
def create(data: ConfigMonnaieCreate, db: Session = Depends(get_db)):
    return create_monnaie(db, data)

@router.get("/", response_model=List[ConfigMonnaieRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_monnaies(db)

@router.get("/{id_}", response_model=ConfigMonnaieRead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_monnaie(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Monnaie non trouvée")
    return obj

@router.put("/{id_}", response_model=ConfigMonnaieRead)
def update(id_: int, data: ConfigMonnaieUpdate, db: Session = Depends(get_db)):
    obj = update_monnaie(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Monnaie non trouvée")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_monnaie(db, id_):
        raise HTTPException(status_code=404, detail="Monnaie non trouvée")
    return {"ok": True}

@router.post("/search", response_model=ConfigMonnaieSearchResults)
def search(data: ConfigMonnaieSearch, db: Session = Depends(get_db)):
    return {"results": search_monnaies(db, data)}