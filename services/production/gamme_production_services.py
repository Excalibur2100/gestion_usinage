from sqlalchemy.orm import Session
from db.models.tables import GammeProduction
from db.schemas.schemas import GammeProductionCreate
from typing import List, Optional

# ========== CRÉATION ==========
def creer_gamme(db: Session, data: GammeProductionCreate) -> GammeProduction:
    gamme = GammeProduction(**data.dict())
    db.add(gamme)
    db.commit()
    db.refresh(gamme)
    return gamme

# ========== TOUS ==========
def get_toutes_gammes(db: Session) -> List[GammeProduction]:
    return db.query(GammeProduction).all()

# ========== PAR ID ==========
def get_gamme_par_id(db: Session, id: int) -> Optional[GammeProduction]:
    return db.query(GammeProduction).filter(GammeProduction.id == id).first()

# ========== MISE À JOUR ==========
def update_gamme(db: Session, id: int, data: GammeProductionCreate) -> Optional[GammeProduction]:
    gamme = get_gamme_par_id(db, id)
    if gamme:
        for key, value in data.dict().items():
            setattr(gamme, key, value)
        db.commit()
        db.refresh(gamme)
    return gamme

# ========== SUPPRESSION ==========
def supprimer_gamme(db: Session, id: int) -> None:
    gamme = get_gamme_par_id(db, id)
    if gamme:
        db.delete(gamme)
        db.commit()
