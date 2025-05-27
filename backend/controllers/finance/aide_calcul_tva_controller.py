from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.finance.aide_calcul_tva_schemas import *
from services.finance.aide_calcul_tva_service import *

router = APIRouter(prefix="/aide-tva", tags=["Aide Calcul TVA"])

@router.post("/", response_model=AideCalculTVARead)
def create(data: AideCalculTVACreate, db: Session = Depends(get_db)):
    return create_aide_tva(db, data)

@router.get("/", response_model=List[AideCalculTVARead])
def read_all(db: Session = Depends(get_db)):
    return get_all_aides_tva(db)

@router.get("/{id_}", response_model=AideCalculTVARead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_aide_tva(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Calcul non trouvé")
    return obj

@router.put("/{id_}", response_model=AideCalculTVARead)
def update(id_: int, data: AideCalculTVAUpdate, db: Session = Depends(get_db)):
    obj = update_aide_tva(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Calcul non trouvé")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_aide_tva(db, id_):
        raise HTTPException(status_code=404, detail="Calcul non trouvé")
    return {"ok": True}

@router.post("/search", response_model=AideCalculTVASearchResults)
def search(data: AideCalculTVASearch, db: Session = Depends(get_db)):
    return {"results": search_aides_tva(db, data)}