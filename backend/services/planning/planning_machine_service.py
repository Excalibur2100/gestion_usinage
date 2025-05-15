 from sqlalchemy.orm import Session
from typing import List, Optional
from db.models.table import PlanningMachine
from db.schemas.schemas import PlanningMachineCreate

# ========== CRÉATION ==========
def creer_planning_machine(db: Session, planning_data: PlanningMachineCreate) -> PlanningMachine:
    planning = PlanningMachine(**planning_data.model_dump())
    db.add(planning)
    db.commit()
    db.refresh(planning)
    return planning

# ========== TOUS ==========
def get_tous_plannings_machine(db: Session) -> List[PlanningMachine]:
    return db.query(PlanningMachine).all()

# ========== PAR ID ==========
def get_planning_machine_par_id(db: Session, planning_id: int) -> Optional[PlanningMachine]:
    return db.query(PlanningMachine).filter(PlanningMachine.id == planning_id).first()

# ========== MISE À JOUR ==========
def update_planning_machine(db: Session, planning_id: int, planning_data: PlanningMachineCreate) -> Optional[PlanningMachine]:
    planning = get_planning_machine_par_id(db, planning_id)
    if planning:
        for key, value in planning_data.model_dump().items():
            setattr(planning, key, value)
        db.commit()
        db.refresh(planning)
    return planning

# ========== SUPPRESSION ==========
def supprimer_planning_machine(db: Session, planning_id: int) -> None:
    planning = get_planning_machine_par_id(db, planning_id)
    if planning:
        db.delete(planning)
        db.commit()

def verifier_conflits_planning(planning):
    """
    Vérifie les conflits dans un planning donné.
    :param planning: Liste des tâches ou des événements.
    :return: Liste des conflits détectés.
    """
    conflits = []
    # Exemple de logique pour détecter les conflits
    for i, tache1 in enumerate(planning):
        for j, tache2 in enumerate(planning):
            if i != j and tache1["debut"] < tache2["fin"] and tache1["fin"] > tache2["debut"]:
                conflits.append((tache1, tache2))
    return conflits