from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from backend.db.schemas.commercial.commande_piece_schemas import CommandePieceCreate, CommandePieceRead, CommandePieceUpdate
from backend.services.commercial.commande_piece_services import (
    creer_commande_piece,
    get_toutes_commandes_pieces,
    get_commande_piece_par_id,
    update_commande_piece,
    supprimer_commande_piece
)

router = APIRouter(prefix="/commande-piece", tags=["Commande Piece"])

@router.post("/", response_model=CommandePieceRead)
def creer(data: CommandePieceCreate, db: Session = Depends(get_db)):
    return creer_commande_piece(db, data)

@router.get("/", response_model=list[CommandePieceRead])
def lire_toutes(db: Session = Depends(get_db)):
    return get_toutes_commandes_pieces(db)

@router.get("/{id}", response_model=CommandePieceRead)
def lire_une(id: int, db: Session = Depends(get_db)):
    ligne = get_commande_piece_par_id(db, id)
    if not ligne:
        raise HTTPException(status_code=404, detail="Ligne non trouvée")
    return ligne

@router.put("/{id}", response_model=CommandePieceRead)
def maj(id: int, data: CommandePieceUpdate, db: Session = Depends(get_db)):
    ligne = update_commande_piece(db, id, data)
    if not ligne:
        raise HTTPException(status_code=404, detail="Ligne non trouvée pour mise à jour")
    return ligne

@router.delete("/{id}", status_code=204)
def supprimer(id: int, db: Session = Depends(get_db)):
    supprimer_commande_piece(db, id)
    return

@router.get("/", response_model=list[CommandePieceRead])
async def get_commande_pieces():
    return {"message": "Liste des commandes de pièces"}


