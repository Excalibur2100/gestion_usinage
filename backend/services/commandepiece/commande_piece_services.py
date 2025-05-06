from sqlalchemy.orm import Session
from db.models.tables import CommandePiece
from db.schemas.schemas import CommandePieceCreate
from typing import List, Optional

# ========== CRÉATION ==========
def creer_commande_piece(db: Session, data: CommandePieceCreate) -> CommandePiece:
    ligne = CommandePiece(**data.dict())
    db.add(ligne)
    db.commit()
    db.refresh(ligne)
    return ligne

# ========== TOUTES ==========
def get_toutes_commandes_pieces(db: Session) -> List[CommandePiece]:
    return db.query(CommandePiece).all()

# ========== PAR ID ==========
def get_commande_piece_par_id(db: Session, id: int) -> Optional[CommandePiece]:
    return db.query(CommandePiece).filter(CommandePiece.id == id).first()

# ========== MISE À JOUR ==========
def update_commande_piece(db: Session, id: int, data: CommandePieceCreate) -> Optional[CommandePiece]:
    ligne = get_commande_piece_par_id(db, id)
    if ligne:
        for key, value in data.dict().items():
            setattr(ligne, key, value)
        db.commit()
        db.refresh(ligne)
    return ligne

# ========== SUPPRESSION ==========
def supprimer_commande_piece(db: Session, id: int) -> None:
    ligne = get_commande_piece_par_id(db, id)
    if ligne:
        db.delete(ligne)
        db.commit()
