from sqlalchemy.orm import Session
from typing import List, Optional
from db.models.models import Piece
from db.schemas.schemas import PieceCreate

def creer_piece(db: Session, piece_data: PieceCreate) -> Piece:
    piece = Piece(**piece_data.dict())
    db.add(piece)
    db.commit()
    db.refresh(piece)
    return piece

def get_toutes_pieces(db: Session) -> List[Piece]:
    return db.query(Piece).all()

def get_piece_par_id(db: Session, piece_id: int) -> Optional[Piece]:
    return db.query(Piece).filter(Piece.id == piece_id).first()

def update_piece(db: Session, piece_id: int, piece_data: PieceCreate) -> Optional[Piece]:
    piece = db.query(Piece).filter(Piece.id == piece_id).first()
    if piece:
        for key, value in piece_data.dict().items():
            setattr(piece, key, value)
        db.commit()
        db.refresh(piece)
    return piece

def supprimer_piece(db: Session, piece_id: int) -> None:
    piece = db.query(Piece).filter(Piece.id == piece_id).first()
    if piece:
        db.delete(piece)
        db.commit()
