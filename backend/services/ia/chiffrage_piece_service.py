from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.ia.chiffrage_piece import ChiffragePiece
from db.models.tables.ia.chiffrage_operation import ChiffrageOperation
from db.models.tables.ia.chiffrage_machine import ChiffrageMachine
from db.schemas.ia.chiffrage_piece_schemas import *

# ----- PIÈCE -----
def create_piece(db: Session, data: ChiffragePieceCreate) -> ChiffragePiece:
    obj = ChiffragePiece(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_piece(db: Session, id_: int) -> Optional[ChiffragePiece]:
    return db.query(ChiffragePiece).filter(ChiffragePiece.id == id_).first()

def get_all_pieces(db: Session) -> List[ChiffragePiece]:
    return db.query(ChiffragePiece).all()

def update_piece(db: Session, id_: int, data: ChiffragePieceUpdate) -> Optional[ChiffragePiece]:
    obj = get_piece(db, id_)
    if obj:
        for key, value in data.dict(exclude_unset=True).items():
            setattr(obj, key, value)
        db.commit()
        db.refresh(obj)
        return obj
    return None

def delete_piece(db: Session, id_: int) -> bool:
    obj = get_piece(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

# ----- MACHINE -----
def create_machine(db: Session, data: ChiffrageMachineCreate) -> ChiffrageMachine:
    obj = ChiffrageMachine(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

# ----- OPÉRATION -----
def create_operation(db: Session, data: ChiffrageOperationCreate, piece_id: int) -> ChiffrageOperation:
    obj = ChiffrageOperation(**data.dict(), piece_id=piece_id)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj