from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.achat.facture_fournisseur_schemas import *
from services.achat.facture_fournisseur_service import *

router = APIRouter(prefix="/factures-fournisseur", tags=["Factures Fournisseur"])

@router.post("/", response_model=FactureFournisseurRead)
def create(data: FactureFournisseurCreate, db: Session = Depends(get_db)):
    return create_facture_fournisseur(db, data)

@router.get("/", response_model=List[FactureFournisseurRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_factures_fournisseur(db)

@router.get("/{id_}", response_model=FactureFournisseurRead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_facture_fournisseur(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Facture fournisseur non trouvée")
    return obj

@router.put("/{id_}", response_model=FactureFournisseurRead)
def update(id_: int, data: FactureFournisseurUpdate, db: Session = Depends(get_db)):
    obj = update_facture_fournisseur(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Facture fournisseur non trouvée")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_facture_fournisseur(db, id_):
        raise HTTPException(status_code=404, detail="Facture fournisseur non trouvée")
    return {"ok": True}

@router.post("/search", response_model=FactureFournisseurSearchResults)
def search(data: FactureFournisseurSearch, db: Session = Depends(get_db)):
    return {"results": search_factures_fournisseur(db, data)}