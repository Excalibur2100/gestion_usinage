from typing import Optional, List
from sqlalchemy.orm import Session
from db.models.tables.achat.commande_fournisseur import CommandeFournisseur
from db.schemas.achat.commande_fournisseur_schemas import (
    CommandeFournisseurCreate,
    CommandeFournisseurUpdate,
    CommandeFournisseurSearch
)

# === CREATE ===
def create_commande(db: Session, data: CommandeFournisseurCreate) -> CommandeFournisseur:
    obj = CommandeFournisseur(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

# === READ ONE ===
def get_commande(db: Session, commande_id: int) -> Optional[CommandeFournisseur]:
    return db.query(CommandeFournisseur).filter(CommandeFournisseur.id == commande_id).first()

# === READ ALL ===
def get_all_commandes(db: Session) -> List[CommandeFournisseur]:
    return db.query(CommandeFournisseur).all()

# === UPDATE ===
def update_commande(db: Session, commande_id: int, data: CommandeFournisseurUpdate) -> Optional[CommandeFournisseur]:
    obj = get_commande(db, commande_id)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

# === DELETE ===
def delete_commande(db: Session, commande_id: int) -> bool:
    obj = get_commande(db, commande_id)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

# === SEARCH ===
def search_commandes(db: Session, search_data: CommandeFournisseurSearch) -> List[CommandeFournisseur]:
    query = db.query(CommandeFournisseur)
    if search_data.code_commande:
        query = query.filter(CommandeFournisseur.code_commande.ilike(f"%{search_data.code_commande}%"))
    if search_data.statut:
        query = query.filter(CommandeFournisseur.statut == search_data.statut)
    if search_data.fournisseur_id:
        query = query.filter(CommandeFournisseur.fournisseur_id == search_data.fournisseur_id)
    return query.all()
