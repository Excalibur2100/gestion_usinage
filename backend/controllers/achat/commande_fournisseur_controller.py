from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.achat.ligne_commande_fournisseur_schemas import *
from services.achat.ligne_commande_fournisseur_service import *

router = APIRouter(prefix="/lignes-commande-fournisseur", tags=["Lignes Commande Fournisseur"])

@router.post("/", response_model=LigneCommandeFournisseurRead)
def create(data: LigneCommandeFournisseurCreate, db: Session = Depends(get_db)):
    return create_ligne(db, data)

@router.get("/", response_model=List[LigneCommandeFournisseurRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_lignes(db)

@router.get("/{ligne_id}", response_model=LigneCommandeFournisseurRead)
def read(ligne_id: int, db: Session = Depends(get_db)):
    ligne = get_ligne(db, ligne_id)
    if not ligne:
        raise HTTPException(status_code=404, detail="Ligne non trouvée")
    return ligne

@router.put("/{ligne_id}", response_model=LigneCommandeFournisseurRead)
def update(ligne_id: int, data: LigneCommandeFournisseurUpdate, db: Session = Depends(get_db)):
    ligne = update_ligne(db, ligne_id, data)
    if not ligne:
        raise HTTPException(status_code=404, detail="Ligne non trouvée")
    return ligne

@router.delete("/{ligne_id}")
def delete(ligne_id: int, db: Session = Depends(get_db)):
    if not delete_ligne(db, ligne_id):
        raise HTTPException(status_code=404, detail="Ligne non trouvée")
    return {"ok": True}

@router.post("/search", response_model=LigneCommandeFournisseurSearchResults)
def search(data: LigneCommandeFournisseurSearch, db: Session = Depends(get_db)):
    return {"results": search_lignes(db, data)}
