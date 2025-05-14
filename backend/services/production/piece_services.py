from sqlalchemy.orm import Session
from typing import List, Optional
from db.models.tables import Piece
from backend.db.schemas.piece_schemas.piece_schemas import PieceCreate

def creer_piece(db: Session, piece_data: PieceCreate) -> Piece:
    """
    Crée une nouvelle pièce.
    """
    piece = Piece(**piece_data.dict())
    db.add(piece)
    db.commit()
    db.refresh(piece)
    return piece

def get_toutes_pieces(db: Session) -> List[Piece]:
    """
    Récupère toutes les pièces.
    """
    return db.query(Piece).all()

def get_piece_par_id(db: Session, piece_id: int) -> Optional[Piece]:
    """
    Récupère une pièce par son ID.
    """
    return db.query(Piece).filter(Piece.id == piece_id).first()

def update_piece(db: Session, piece_id: int, piece_data: PieceCreate) -> Optional[Piece]:
    """
    Met à jour une pièce existante.
    """
    piece = db.query(Piece).filter(Piece.id == piece_id).first()
    if piece:
        for key, value in piece_data.dict(exclude_unset=True).items():
            setattr(piece, key, value)
        db.commit()
        db.refresh(piece)
    return piece

def supprimer_piece(db: Session, piece_id: int) -> None:
    """
    Supprime une pièce par son ID.
    """
    piece = db.query(Piece).filter(Piece.id == piece_id).first()
    if piece:
        db.delete(piece)
        db.commit()