from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.models.database import get_db
from services.affectationmachine.affectationmachine_service import (
    get_affectations_machines,
    get_affectation_machine_by_id,
    create_affectation_machine,
    update_affectation_machine,
    delete_affectation_machine,
)
from backend.db.schemas.affectation_machine_schemas.affectation_machine_schemas import AffectationMachineCreate, AffectationMachineUpdate

router = APIRouter(prefix="/affectation_machine", tags=["Affectation Machine"])

@router.get("/", response_model=list)
def list_affectations(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_affectations_machines(db, skip=skip, limit=limit)

@router.get("/{affectation_id}", response_model=dict)
def get_affectation(affectation_id: int, db: Session = Depends(get_db)):
    return get_affectation_machine_by_id(db, affectation_id)

@router.post("/", response_model=dict)
def create_affectation(affectation_data: AffectationMachineCreate, db: Session = Depends(get_db)):
    return create_affectation_machine(db, affectation_data)

@router.put("/{affectation_id}", response_model=dict)
def update_affectation(affectation_id: int, affectation_data: AffectationMachineUpdate, db: Session = Depends(get_db)):
    return update_affectation_machine(db, affectation_id, affectation_data)

@router.delete("/{affectation_id}")
def delete_affectation(affectation_id: int, db: Session = Depends(get_db)):
    delete_affectation_machine(db, affectation_id)
    return {"message": "Affectation de machine supprimée avec succès"}