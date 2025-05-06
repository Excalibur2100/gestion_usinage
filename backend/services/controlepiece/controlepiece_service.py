from sqlalchemy.orm import Session
from db.models.tables.controle_piece import ControlePiece
from db.schemas.controle_pieces_schemas import ControlePieceCreate, ControlePieceUpdate
from fastapi import HTTPException

def get_controles_pieces(db: Session, skip: int = 0, limit: int = 10):
    """
    Récupère une liste paginée des contrôles de pièces.
    """
    return db.query(ControlePiece).offset(skip).limit(limit).all()

def get_controle_piece_by_id(db: Session, controle_id: int):
    """
    Récupère un contrôle de pièce par son ID.
    """
    controle = db.query(ControlePiece).filter(ControlePiece.id == controle_id).first()
    if not controle:
        raise HTTPException(status_code=404, detail="Contrôle de pièce non trouvé")
    return controle

def create_controle_piece(db: Session, controle_data: ControlePieceCreate):
    """
    Crée un nouveau contrôle de pièce.
    """
    controle = ControlePiece(
        piece_id=controle_data.piece_id,
        instrument_id=controle_data.instrument_id,
        resultat=controle_data.resultat,
        date_controle=controle_data.date_controle,
        remarque=controle_data.remarque,
    )
    db.add(controle)
    db.commit()
    db.refresh(controle)
    return controle

def update_controle_piece(db: Session, controle_id: int, controle_data: ControlePieceUpdate):
    """
    Met à jour un contrôle de pièce existant.
    """
    controle = get_controle_piece_by_id(db, controle_id)
    if controle_data.piece_id is not None:
        controle.piece_id = controle_data.piece_id
    if controle_data.instrument_id is not None:
        controle.instrument_id = controle_data.instrument_id
    if controle_data.resultat is not None:
        controle.resultat = controle_data.resultat
    if controle_data.date_controle is not None:
        controle.date_controle = controle_data.date_controle
    if controle_data.remarque is not None:
        controle.remarque = controle_data.remarque
    db.commit()
    db.refresh(controle)
    return controle

def delete_controle_piece(db: Session, controle_id: int):
    """
    Supprime un contrôle de pièce par son ID.
    """
    controle = get_controle_piece_by_id(db, controle_id)
    db.delete(controle)
    db.commit()