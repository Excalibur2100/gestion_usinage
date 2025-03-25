from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.schemas import FournisseurCreate, FournisseurRead
from services.fournisseur.fournisseur_services import (
    creer_fournisseur,
    get_tous_fournisseurs,
    get_fournisseur_par_id,
    update_fournisseur,
    supprimer_fournisseur
)

router = APIRouter(prefix="/fournisseurs", tags=["Fournisseurs"])

# ========== CRÉATION ==========
@router.post("/", response_model=FournisseurRead)
def creer(fournisseur_data: FournisseurCreate, db: Session = Depends(get_db)):
    return creer_fournisseur(db, fournisseur_data)

# ========== TOUS ==========
@router.get("/", response_model=list[FournisseurRead])
def lire_tous(db: Session = Depends(get_db)):
    return get_tous_fournisseurs(db)

# ========== PAR ID ==========
@router.get("/{id}", response_model=FournisseurRead)
def lire_un(id: int, db: Session = Depends(get_db)):
    fournisseur = get_fournisseur_par_id(db, id)
    if not fournisseur:
        raise HTTPException(status_code=404, detail="Fournisseur non trouvé")
    return fournisseur

# ========== MISE À JOUR ==========
@router.put("/{id}", response_model=FournisseurRead)
def maj_fournisseur(id: int, fournisseur_data: FournisseurCreate, db: Session = Depends(get_db)):
    fournisseur = update_fournisseur(db, id, fournisseur_data)
    if not fournisseur:
        raise HTTPException(status_code=404, detail="Fournisseur non trouvé pour mise à jour")
    return fournisseur

# ========== SUPPRESSION ==========
@router.delete("/{id}", status_code=204)
def supprimer(id: int, db: Session = Depends(get_db)):
    supprimer_fournisseur(db, id)
    return
