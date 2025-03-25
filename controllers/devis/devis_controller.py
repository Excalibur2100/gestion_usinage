from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.schemas import DevisCreate, DevisRead
from services.devis.devis_services import (
    creer_devis,
    get_tous_devis,
    get_devis_par_id,
    update_devis,
    supprimer_devis
)

router = APIRouter(prefix="/devis", tags=["Devis"])

# ========== CRÉATION ==========
@router.post("/", response_model=DevisRead)
def creer(devis_data: DevisCreate, db: Session = Depends(get_db)):
    return creer_devis(db, devis_data)

# ========== TOUS ==========
@router.get("/", response_model=list[DevisRead])
def lire_tous(db: Session = Depends(get_db)):
    return get_tous_devis(db)

# ========== PAR ID ==========
@router.get("/{id}", response_model=DevisRead)
def lire_un(id: int, db: Session = Depends(get_db)):
    devis = get_devis_par_id(db, id)
    if not devis:
        raise HTTPException(status_code=404, detail="Devis non trouvé")
    return devis

# ========== MISE À JOUR ==========
@router.put("/{id}", response_model=DevisRead)
def maj_devis(id: int, devis_data: DevisCreate, db: Session = Depends(get_db)):
    devis = update_devis(db, id, devis_data)
    if not devis:
        raise HTTPException(status_code=404, detail="Devis non trouvé pour mise à jour")
    return devis

# ========== SUPPRESSION ==========
@router.delete("/{id}", status_code=204)
def supprimer(id: int, db: Session = Depends(get_db)):
    supprimer_devis(db, id)
    return
