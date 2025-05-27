from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.finance.config_paiement_schemas import *
from services.finance.config_paiement_service import *

router = APIRouter(prefix="/config-paiements", tags=["Configuration Paiements"])

@router.post("/", response_model=ConfigPaiementRead)
def create(data: ConfigPaiementCreate, db: Session = Depends(get_db)):
    return create_config_paiement(db, data)

@router.get("/", response_model=List[ConfigPaiementRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_config_paiements(db)

@router.get("/{id_}", response_model=ConfigPaiementRead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_config_paiement(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Modalité non trouvée")
    return obj

@router.put("/{id_}", response_model=ConfigPaiementRead)
def update(id_: int, data: ConfigPaiementUpdate, db: Session = Depends(get_db)):
    obj = update_config_paiement(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Modalité non trouvée")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_config_paiement(db, id_):
        raise HTTPException(status_code=404, detail="Modalité non trouvée")
    return {"ok": True}

@router.post("/search", response_model=ConfigPaiementSearchResults)
def search(data: ConfigPaiementSearch, db: Session = Depends(get_db)):
    return {"results": search_config_paiements(db, data)}