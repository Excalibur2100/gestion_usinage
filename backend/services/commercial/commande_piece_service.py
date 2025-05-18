from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.commercial.commande_piece import CommandePiece
from db.schemas.commercial.commande_piece_schemas import *

def create_commande_piece(db: Session, data: CommandePieceCreate) -> CommandePiece:
    obj = CommandePiece(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_commande_piece(db: Session, id_: int) -> Optional[CommandePiece]:
    return db.query(CommandePiece).filter(CommandePiece.id == id_).first()

def get_all_commande_pieces(db: Session) -> List[CommandePiece]:
    return db.query(CommandePiece).all()

def update_commande_piece(db: Session, id_: int, data: CommandePieceUpdate) -> Optional[CommandePiece]:
    obj = get_commande_piece(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_commande_piece(db: Session, id_: int) -> bool:
    obj = get_commande_piece(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_commande_pieces(db: Session, search_data: CommandePieceSearch) -> List[CommandePiece]:
    query = db.query(CommandePiece)
    if search_data.commande_id:
        query = query.filter(CommandePiece.commande_id == search_data.commande_id)
    if search_data.piece_id:
        query = query.filter(CommandePiece.piece_id == search_data.piece_id)
    if search_data.designation:
        query = query.filter(CommandePiece.designation.ilike(f"%{search_data.designation}%"))
    return query.all()
