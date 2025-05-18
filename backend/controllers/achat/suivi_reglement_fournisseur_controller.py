from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.achat.suivi_reglement_fournisseur_schemas import *
from services.achat.suivi_reglement_fournisseur_service import *

router = APIRouter(prefix="/reglements-fournisseur", tags=["Suivi Paiement Fournisseur"])

@router.post("/", response_model=SuiviReglementFournisseurRead)
def create(data: SuiviReglementFournisseurCreate, db: Session = Depends(get_db)):
    return create_reglement(db, data)

@router.get("/", response_model=List[SuiviReglementFournisseurRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_reglements(db)

@router.get("/{reglement_id}", response_model=SuiviReglementFournisseurRead)
def read(reglement_id: int, db: Session = Depends(get_db)):
    obj = get_reglement(db, reglement_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Règlement non trouvé")
    return obj

@router.put("/{reglement_id}", response_model=SuiviReglementFournisseurRead)
def update(reglement_id: int, data: SuiviReglementFournisseurUpdate, db: Session = Depends(get_db)):
    obj = update_reglement(db, reglement_id, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Règlement non trouvé")
    return obj

@router.delete("/{reglement_id}")
def delete(reglement_id: int, db: Session = Depends(get_db)):
    if not delete_reglement(db, reglement_id):
        raise HTTPException(status_code=404, detail="Règlement non trouvé")
    return {"ok": True}

@router.post("/search", response_model=SuiviReglementFournisseurSearchResults)
def search(data: SuiviReglementFournisseurSearch, db: Session = Depends(get_db)):
    return {"results": search_reglements(db, data)}
