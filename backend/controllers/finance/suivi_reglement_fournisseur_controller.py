from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.finance.suivi_reglement_fournisseur_schemas import *
from services.finance.suivi_reglement_fournisseur_service import *

router = APIRouter(prefix="/suivis-reglements-fournisseur", tags=["Règlements Fournisseur"])

@router.post("/", response_model=SuiviReglementFournisseurRead)
def create(data: SuiviReglementFournisseurCreate, db: Session = Depends(get_db)):
    return create_suivi(db, data)

@router.get("/", response_model=List[SuiviReglementFournisseurRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_suivis(db)

@router.get("/{id_}", response_model=SuiviReglementFournisseurRead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_suivi(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Suivi non trouvé")
    return obj

@router.put("/{id_}", response_model=SuiviReglementFournisseurRead)
def update(id_: int, data: SuiviReglementFournisseurUpdate, db: Session = Depends(get_db)):
    obj = update_suivi(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Suivi non trouvé")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_suivi(db, id_):
        raise HTTPException(status_code=404, detail="Suivi non trouvé")
    return {"ok": True}

@router.post("/search", response_model=SuiviReglementFournisseurSearchResults)
def search(data: SuiviReglementFournisseurSearch, db: Session = Depends(get_db)):
    return {"results": search_suivis(db, data)}