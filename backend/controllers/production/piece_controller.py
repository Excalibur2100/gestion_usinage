from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from backend.db.schemas.piece_schemas.piece_schemas import PieceCreate, PieceRead
from db.models.database import get_db
from services.piece.piece_services import (
    creer_piece,
    get_toutes_pieces,
    get_piece_par_id,
    update_piece,
    supprimer_piece,
)

router = APIRouter(
    prefix="/pieces",
    tags=["Pièces"]
)

# ========== CRÉATION ==========
@router.post("/", response_model=PieceRead, status_code=status.HTTP_201_CREATED)
async def create_piece(piece: PieceCreate, db: Session = Depends(get_db)):
    """
    Crée une nouvelle pièce.
    """
    return creer_piece(db, piece)

# ========== TOUS ==========
@router.get("/", response_model=List[PieceRead])
async def read_all_pieces(db: Session = Depends(get_db)):
    """
    Récupère toutes les pièces.
    """
    return get_toutes_pieces(db)

# ========== PAR ID ==========
@router.get("/{piece_id}", response_model=PieceRead)
async def read_piece(piece_id: int, db: Session = Depends(get_db)):
    """
    Récupère une pièce par son ID.
    """
    piece = get_piece_par_id(db, piece_id)
    if not piece:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Pièce avec l'ID {piece_id} non trouvée."
        )
    return piece

# ========== MISE À JOUR ==========
@router.put("/{piece_id}", response_model=PieceRead)
async def update_piece_details(piece_id: int, piece: PieceCreate, db: Session = Depends(get_db)):
    """
    Met à jour une pièce existante.
    """
    updated_piece = update_piece(db, piece_id, piece)
    if not updated_piece:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Pièce avec l'ID {piece_id} non trouvée."
        )
    return updated_piece

# ========== SUPPRESSION ==========
@router.delete("/{piece_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_piece(piece_id: int, db: Session = Depends(get_db)):
    """
    Supprime une pièce par son ID.
    """
    piece = get_piece_par_id(db, piece_id)
    if not piece:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Pièce avec l'ID {piece_id} non trouvée."
        )
    supprimer_piece(db, piece_id)