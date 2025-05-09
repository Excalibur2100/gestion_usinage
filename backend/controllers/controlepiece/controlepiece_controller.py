from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.models.database import get_db
from services.controlepiece.controlepiece_service import (
    get_controles_pieces,
    get_controle_piece_by_id,
    create_controle_piece,
    update_controle_piece,
    delete_controle_piece,
)
from backend.db.schemas.controle_pieces_schemas.controle_pieces_schemas import ControlePieceCreate, ControlePieceUpdate

router = APIRouter(prefix="/controle_piece", tags=["Contrôle Pièce"])

@router.get("/", response_model=list)
def list_controles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Endpoint pour récupérer tous les contrôles de pièces.
    """
    return get_controles_pieces(db, skip=skip, limit=limit)

@router.get("/{controle_id}", response_model=dict)
def get_controle(controle_id: int, db: Session = Depends(get_db)):
    """
    Endpoint pour récupérer un contrôle de pièce spécifique par son ID.
    """
    return get_controle_piece_by_id(db, controle_id)

@router.post("/", response_model=dict)
def create_controle(controle_data: ControlePieceCreate, db: Session = Depends(get_db)):
    """
    Endpoint pour créer un nouveau contrôle de pièce.
    """
    return create_controle_piece(db, controle_data)

@router.put("/{controle_id}", response_model=dict)
def update_controle(controle_id: int, controle_data: ControlePieceUpdate, db: Session = Depends(get_db)):
    """
    Endpoint pour mettre à jour un contrôle de pièce existant.
    """
    return update_controle_piece(db, controle_id, controle_data)

@router.delete("/{controle_id}")
def delete_controle(controle_id: int, db: Session = Depends(get_db)):
    """
    Endpoint pour supprimer un contrôle de pièce par son ID.
    """
    delete_controle_piece(db, controle_id)
    return {"message": "Contrôle de pièce supprimé avec succès"}