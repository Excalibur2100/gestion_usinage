from sqlalchemy.orm import Session
from db.models.models import Commande
from db.schemas.schemas import CommandeCreate
from typing import List, Optional

# ========== CRÉATION ==========
def creer_commande(db: Session, commande_data: CommandeCreate) -> Commande:
    commande = Commande(**commande_data.dict())
    db.add(commande)
    db.commit()
    db.refresh(commande)
    return commande

# ========== TOUS ==========
def get_toutes_commandes(db: Session) -> List[Commande]:
    return db.query(Commande).all()

# ========== PAR ID ==========
def get_commande_par_id(db: Session, commande_id: int) -> Optional[Commande]:
    return db.query(Commande).filter(Commande.id == commande_id).first()

# ========== MISE À JOUR ==========
def update_commande(db: Session, commande_id: int, commande_data: CommandeCreate) -> Optional[Commande]:
    commande = db.query(Commande).filter(Commande.id == commande_id).first()
    if commande:
        for key, value in commande_data.dict().items():
            setattr(commande, key, value)
        db.commit()
        db.refresh(commande)
    return commande

# ========== SUPPRESSION ==========
def supprimer_commande(db: Session, commande_id: int) -> None:
    commande = db.query(Commande).filter(Commande.id == commande_id).first()
    if commande:
        db.delete(commande)
        db.commit()
