from sqlalchemy.orm import Session
from db.models.models import Fournisseur
from db.schemas.schemas import FournisseurCreate
from typing import List, Optional

# ========== CRÉATION ==========
def creer_fournisseur(db: Session, fournisseur_data: FournisseurCreate) -> Fournisseur:
    fournisseur = Fournisseur(**fournisseur_data.dict())
    db.add(fournisseur)
    db.commit()
    db.refresh(fournisseur)
    return fournisseur

# ========== TOUS ==========
def get_tous_fournisseurs(db: Session) -> List[Fournisseur]:
    return db.query(Fournisseur).all()

# ========== PAR ID ==========
def get_fournisseur_par_id(db: Session, fournisseur_id: int) -> Optional[Fournisseur]:
    return db.query(Fournisseur).filter(Fournisseur.id == fournisseur_id).first()

# ========== MISE À JOUR ==========
def update_fournisseur(db: Session, fournisseur_id: int, fournisseur_data: FournisseurCreate) -> Optional[Fournisseur]:
    fournisseur = db.query(Fournisseur).filter(Fournisseur.id == fournisseur_id).first()
    if fournisseur:
        for key, value in fournisseur_data.dict().items():
            setattr(fournisseur, key, value)
        db.commit()
        db.refresh(fournisseur)
    return fournisseur

# ========== SUPPRESSION ==========
def supprimer_fournisseur(db: Session, fournisseur_id: int) -> None:
    fournisseur = db.query(Fournisseur).filter(Fournisseur.id == fournisseur_id).first()
    if fournisseur:
        db.delete(fournisseur)
        db.commit()
