from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.config.config_tva_schemas import *
from services.config.config_tva_service import *

router = APIRouter(prefix="/config-tva", tags=["Configuration TVA"])

@router.post("/", response_model=ConfigTVARead)
def create(data: ConfigTVACreate, db: Session = Depends(get_db)):
    return create_tva(db, data)

@router.get("/", response_model=List[ConfigTVARead])
def read_all(db: Session = Depends(get_db)):
    return get_all_tva(db)

@router.get("/{id_}", response_model=ConfigTVARead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_tva(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="TVA non trouvée")
    return obj

@router.put("/{id_}", response_model=ConfigTVARead)
def update(id_: int, data: ConfigTVAUpdate, db: Session = Depends(get_db)):
    obj = update_tva(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="TVA non trouvée")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_tva(db, id_):
        raise HTTPException(status_code=404, detail="TVA non trouvée")
    return {"ok": True}

@router.post("/search", response_model=ConfigTVASearchResults)
def search(data: ConfigTVASearch, db: Session = Depends(get_db)):
    return {"results": search_tva(db, data)}