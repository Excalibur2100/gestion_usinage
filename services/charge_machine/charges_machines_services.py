from sqlalchemy.orm import Session
from db.models.tables.charges_machine import ChargeMachine
from db.schemas.schemas import ChargeMachineCreate
from typing import List, Optional

# ========== CRÉER ==========
def creer_charge_machine(db: Session, charge_data: ChargeMachineCreate) -> ChargeMachine:
    charge = ChargeMachine(**charge_data.dict())
    db.add(charge)
    db.commit()
    db.refresh(charge)
    return charge

# ========== TOUS ==========
def get_charges_machine(db: Session) -> List[ChargeMachine]:
    return db.query(ChargeMachine).all()

# ========== PAR ID ==========
def get_charge_machine_par_id(db: Session, charge_id: int) -> Optional[ChargeMachine]:
    return db.query(ChargeMachine).filter(ChargeMachine.id == charge_id).first()

# ========== MISE À JOUR ==========
def update_charge_machine(db: Session, charge_id: int, charge_data: ChargeMachineCreate) -> Optional[ChargeMachine]:
    charge = get_charge_machine_par_id(db, charge_id)
    if charge:
        for key, value in charge_data.dict().items():
            setattr(charge, key, value)
        db.commit()
        db.refresh(charge)
    return charge

# ========== SUPPRESSION ==========
def supprimer_charge_machine(db: Session, charge_id: int) -> None:
    charge = get_charge_machine_par_id(db, charge_id)
    if charge:
        db.delete(charge)
        db.commit()
