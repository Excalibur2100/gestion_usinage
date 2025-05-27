from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.config.config_langue_schemas import *
from services.config.config_langue_service import *

router = APIRouter(prefix="/config-langues", tags=["Configuration Langues"])

@router.post("/", response_model=ConfigLangueRead)
def create(data: ConfigLangueCreate, db: Session = Depends(get_db)):
    return create_langue(db, data)

@router.get("/", response_model=List[ConfigLangueRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_langues(db)

@router.get("/{id_}", response_model=ConfigLangueRead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_langue(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Langue non trouvée")
    return obj

@router.put("/{id_}", response_model=ConfigLangueRead)
def update(id_: int, data: ConfigLangueUpdate, db: Session = Depends(get_db)):
    obj = update_langue(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Langue non trouvée")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_langue(db, id_):
        raise HTTPException(status_code=404, detail="Langue non trouvée")
    return {"ok": True}

@router.post("/search", response_model=ConfigLangueSearchResults)
def search(data: ConfigLangueSearch, db: Session = Depends(get_db)):
    return {"results": search_langues(db, data)}