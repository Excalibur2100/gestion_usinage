from sqlalchemy.orm import Session
from backend.db.models.tables.planning.affectation_machine import AffectationMachine
from backend.db.schemas.planning.affectation_machine_schemas import AffectationMachineCreate, AffectationMachineUpdate
from fastapi import HTTPException

def get_affectations_machines(db: Session, skip: int = 0, limit: int = 10):
    """
    Récupère une liste paginée des affectations de machines.
    """
    return db.query(AffectationMachine).offset(skip).limit(limit).all()

def get_affectation_machine_by_id(db: Session, affectation_id: int):
    """
    Récupère une affectation de machine par son ID.
    """
    affectation = db.query(AffectationMachine).filter(AffectationMachine.id == affectation_id).first()
    if not affectation:
        raise HTTPException(status_code=404, detail="Affectation de machine non trouvée")
    return affectation

def create_affectation_machine(db: Session, affectation_data: AffectationMachineCreate):
    """
    Crée une nouvelle affectation de machine.
    """
    affectation = AffectationMachine(
        machine_id=affectation_data.machine_id,
        utilisateur_id=affectation_data.utilisateur_id,
        date_affectation=affectation_data.date_affectation,
        tache=affectation_data.tache,
        statut=affectation_data.statut,
    )
    db.add(affectation)
    db.commit()
    db.refresh(affectation)
    return affectation

def update_affectation_machine(db: Session, affectation_id: int, affectation_data: AffectationMachineUpdate):
    """
    Met à jour une affectation de machine existante.
    """
    affectation = get_affectation_machine_by_id(db, affectation_id)
    if affectation_data.machine_id:
        affectation.machine_id = affectation_data.machine_id
    if affectation_data.utilisateur_id:
        affectation.utilisateur_id = affectation_data.utilisateur_id
    if affectation_data.date_affectation:
        affectation.date_affectation = affectation_data.date_affectation
    if affectation_data.tache:
        affectation.tache = affectation_data.tache
    if affectation_data.statut:
        affectation.statut = affectation_data.statut
    db.commit()
    db.refresh(affectation)
    return affectation

def delete_affectation_machine(db: Session, affectation_id: int):
    """
    Supprime une affectation de machine par son ID.
    """
    affectation = get_affectation_machine_by_id(db, affectation_id)
    db.delete(affectation)
    db.commit()