from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.config.config_metier_schemas import *
from services.config.config_metier_service import *

router = APIRouter(prefix="/config-metiers", tags=["Configuration Métiers"])

@router.post("/", response_model=ConfigMetierRead)
def create(data: ConfigMetierCreate, db: Session = Depends(get_db)):
    return create_metier(db, data)

@router.get("/", response_model=List[ConfigMetierRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_metiers(db)

@router.get("/{id_}", response_model=ConfigMetierRead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_metier(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Métier non trouvé")
    return obj

@router.put("/{id_}", response_model=ConfigMetierRead)
def update(id_: int, data: ConfigMetierUpdate, db: Session = Depends(get_db)):
    obj = update_metier(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Métier non trouvé")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_metier(db, id_):
        raise HTTPException(status_code=404, detail="Métier non trouvé")
    return {"ok": True}

@router.post("/search", response_model=ConfigMetierSearchResults)
def search(data: ConfigMetierSearch, db: Session = Depends(get_db)):
    return {"results": search_metiers(db, data)}