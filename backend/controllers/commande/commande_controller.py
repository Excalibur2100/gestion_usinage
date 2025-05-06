from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from db.schemas.commande_schemas import CommandeCreate, CommandeRead, CommandeUpdate
from backend.db.models.database import get_db
from services.commande.commande_services import (
    creer_commande,
    get_toutes_commandes,
    get_commande_par_id,
    update_commande,
    supprimer_commande,
)

router = APIRouter(
    prefix="/commandes",  # Utilisation du pluriel pour refléter les bonnes pratiques REST
    tags=["Commandes"]   # Catégorisation dans Swagger UI
)

# ========== CRÉATION ==========
@router.post("/", response_model=CommandeRead, status_code=status.HTTP_201_CREATED)
async def create_commande(commande: CommandeCreate, db: Session = Depends(get_db)):
    """
    Crée une nouvelle commande.
    """
    return creer_commande(db, commande)

# ========== TOUS ==========
@router.get("/", response_model=List[CommandeRead])
async def read_all_commandes(db: Session = Depends(get_db)):
    """
    Récupère toutes les commandes.
    """
    return get_toutes_commandes(db)

# ========== PAR ID ==========
@router.get("/{commande_id}", response_model=CommandeRead)
async def read_commande(commande_id: int, db: Session = Depends(get_db)):
    """
    Récupère une commande par son ID.
    """
    commande = get_commande_par_id(db, commande_id)
    if not commande:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Commande avec l'ID {commande_id} non trouvée."
        )
    return commande

# ========== MISE À JOUR ==========
@router.put("/{commande_id}", response_model=CommandeRead)
async def update_commande_details(commande_id: int, commande: CommandeUpdate, db: Session = Depends(get_db)):
    """
    Met à jour une commande existante.
    """
    updated_commande = update_commande(db, commande_id, commande)
    if not updated_commande:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Commande avec l'ID {commande_id} non trouvée."
        )
    return updated_commande

# ========== SUPPRESSION ==========
@router.delete("/{commande_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_commande(commande_id: int, db: Session = Depends(get_db)):
    """
    Supprime une commande par son ID.
    """
    commande = get_commande_par_id(db, commande_id)
    if not commande:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Commande avec l'ID {commande_id} non trouvée."
        )
    supprimer_commande(db, commande_id)