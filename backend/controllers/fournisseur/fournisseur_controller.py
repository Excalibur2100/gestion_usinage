from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from backend.db.schemas.fournisseur_schemas.fournisseur_schemas import FournisseurCreate, FournisseurRead
from db.models.database import get_db
from services.fournisseur.fournisseur_services import (
    creer_fournisseur,
    get_tous_fournisseurs,
    get_fournisseur_par_id,
    update_fournisseur,
    supprimer_fournisseur,
)

router = APIRouter(
    prefix="/fournisseurs",  # Utilisation du pluriel pour refléter les bonnes pratiques REST
    tags=["Fournisseurs"]   # Catégorisation dans Swagger UI
)

# ========== CRÉATION ==========
@router.post("/", response_model=FournisseurRead, status_code=status.HTTP_201_CREATED)
async def create_fournisseur(fournisseur: FournisseurCreate, db: Session = Depends(get_db)):
    """
    Crée un nouveau fournisseur.
    """
    return creer_fournisseur(db, fournisseur)

# ========== TOUS ==========
@router.get("/", response_model=List[FournisseurRead])
async def read_all_fournisseurs(db: Session = Depends(get_db)):
    """
    Récupère tous les fournisseurs.
    """
    return get_tous_fournisseurs(db)

# ========== PAR ID ==========
@router.get("/{fournisseur_id}", response_model=FournisseurRead)
async def read_fournisseur(fournisseur_id: int, db: Session = Depends(get_db)):
    """
    Récupère un fournisseur par son ID.
    """
    fournisseur = get_fournisseur_par_id(db, fournisseur_id)
    if not fournisseur:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Fournisseur avec l'ID {fournisseur_id} non trouvé."
        )
    return fournisseur

# ========== MISE À JOUR ==========
@router.put("/{fournisseur_id}", response_model=FournisseurRead)
async def update_fournisseur_details(fournisseur_id: int, fournisseur: FournisseurCreate, db: Session = Depends(get_db)):
    """
    Met à jour un fournisseur existant.
    """
    updated_fournisseur = update_fournisseur(db, fournisseur_id, fournisseur)
    if not updated_fournisseur:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Fournisseur avec l'ID {fournisseur_id} non trouvé."
        )
    return updated_fournisseur

# ========== SUPPRESSION ==========
@router.delete("/{fournisseur_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_fournisseur(fournisseur_id: int, db: Session = Depends(get_db)):
    """
    Supprime un fournisseur par son ID.
    """
    fournisseur = get_fournisseur_par_id(db, fournisseur_id)
    if not fournisseur:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Fournisseur avec l'ID {fournisseur_id} non trouvé."
        )
    supprimer_fournisseur(db, fournisseur_id)