from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.schemas import PieceCreate, PieceRead
from services.piece.piece_services import (
    creer_piece,
    get_toutes_pieces,
    get_piece_par_id,
    update_piece,
    supprimer_piece
)

router = APIRouter(prefix="/pieces", tags=["Pièces"])

@router.post("/", response_model=PieceRead)
def creer(piece_data: PieceCreate, db: Session = Depends(get_db)):
    return creer_piece(db, piece_data)

@router.get("/", response_model=list[PieceRead])
def lire_toutes(db: Session = Depends(get_db)):
    return get_toutes_pieces(db)

@router.get("/{id}", response_model=PieceRead)
def lire_une(id: int, db: Session = Depends(get_db)):
    piece = get_piece_par_id(db, id)
    if not piece:
        raise HTTPException(status_code=404, detail="Pièce non trouvée")
    return piece

@router.put("/{id}", response_model=PieceRead)
def maj_piece(id: int, piece_data: PieceCreate, db: Session = Depends(get_db)):
    piece = update_piece(db, id, piece_data)
    if not piece:
        raise HTTPException(status_code=404, detail="Pièce non trouvée pour mise à jour")
    return piece

@router.delete("/{id}", status_code=204)
def supprimer(id: int, db: Session = Depends(get_db)):
    supprimer_piece(db, id)
