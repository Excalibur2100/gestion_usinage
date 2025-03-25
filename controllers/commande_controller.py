from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.schemas import CommandeCreate, CommandeRead
from services.commande.commande_services import (
    creer_commande,
    get_toutes_commandes,
    get_commande_par_id,
    update_commande,
    supprimer_commande
)

router = APIRouter(prefix="/commandes", tags=["Commandes"])

# ========== CRÉATION ==========
@router.post("/", response_model=CommandeRead)
def creer(commande_data: CommandeCreate, db: Session = Depends(get_db)):
    return creer_commande(db, commande_data)

# ========== TOUS ==========
@router.get("/", response_model=list[CommandeRead])
def lire_toutes(db: Session = Depends(get_db)):
    return get_toutes_commandes(db)

# ========== PAR ID ==========
@router.get("/{id}", response_model=CommandeRead)
def lire_une(id: int, db: Session = Depends(get_db)):
    commande = get_commande_par_id(db, id)
    if not commande:
        raise HTTPException(status_code=404, detail="Commande non trouvée")
    return commande

# ========== MISE À JOUR ==========
@router.put("/{id}", response_model=CommandeRead)
def maj_commande(id: int, commande_data: CommandeCreate, db: Session = Depends(get_db)):
    commande = update_commande(db, id, commande_data)
    if not commande:
        raise HTTPException(status_code=404, detail="Commande non trouvée pour mise à jour")
    return commande

# ========== SUPPRESSION ==========
@router.delete("/{id}", status_code=204)
def supprimer(id: int, db: Session = Depends(get_db)):
    supprimer_commande(db, id)
    return
