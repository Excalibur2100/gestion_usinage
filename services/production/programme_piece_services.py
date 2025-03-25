from sqlalchemy.orm import Session
from db.models.models import ProgrammePiece
from db.schemas.schemas import ProgrammePieceCreate
from typing import List, Optional

# ========== CRÉATION ==========
def creer_programme(db: Session, data: ProgrammePieceCreate) -> ProgrammePiece:
    programme = ProgrammePiece(**data.dict())
    db.add(programme)
    db.commit()
    db.refresh(programme)
    return programme

# ========== TOUS ==========
def get_tous_programmes(db: Session) -> List[ProgrammePiece]:
    return db.query(ProgrammePiece).all()

# ========== PAR ID ==========
def get_programme_par_id(db: Session, id: int) -> Optional[ProgrammePiece]:
    return db.query(ProgrammePiece).filter(ProgrammePiece.id == id).first()

# ========== MISE À JOUR ==========
def update_programme(db: Session, id: int, data: ProgrammePieceCreate) -> Optional[ProgrammePiece]:
    programme = get_programme_par_id(db, id)
    if programme:
        for key, value in data.dict().items():
            setattr(programme, key, value)
        db.commit()
        db.refresh(programme)
    return programme

# ========== SUPPRESSION ==========
def supprimer_programme(db: Session, id: int) -> None:
    programme = get_programme_par_id(db, id)
    if programme:
        db.delete(programme)
        db.commit()
