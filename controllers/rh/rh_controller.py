from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.schemas import RHCreate, RHRead
from services.rh.rh_services import (
    creer_rh,
    get_tous_rh,
    get_rh_par_id,
    update_rh,
    supprimer_rh
)

router = APIRouter(prefix="/rh", tags=["RH"])

# ========== CRÉATION ==========
@router.post("/", response_model=RHRead)
def creer(rh_data: RHCreate, db: Session = Depends(get_db)):
    return creer_rh(db, rh_data)

# ========== TOUS ==========
@router.get("/", response_model=list[RHRead])
def lire_tous(db: Session = Depends(get_db)):
    return get_tous_rh(db)

# ========== PAR ID ==========
@router.get("/{id}", response_model=RHRead)
def lire_un(id: int, db: Session = Depends(get_db)):
    rh = get_rh_par_id(db, id)
    if not rh:
        raise HTTPException(status_code=404, detail="RH non trouvé")
    return rh

# ========== MISE À JOUR ==========
@router.put("/{id}", response_model=RHRead)
def maj_rh(id: int, rh_data: RHCreate, db: Session = Depends(get_db)):
    rh = update_rh(db, id, rh_data)
    if not rh:
        raise HTTPException(status_code=404, detail="RH non trouvé pour mise à jour")
    return rh

# ========== SUPPRESSION ==========
@router.delete("/{id}", status_code=204)
def supprimer(id: int, db: Session = Depends(get_db)):
    supprimer_rh(db, id)
    return