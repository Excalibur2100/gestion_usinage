from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from backend.db.schemas.rh.formation_schemas import FormationCreate, FormationUpdate, FormationRead
from backend.services.rh.formation_service import (
    create_formation,
    get_all_formations,
    get_formation_by_id,
    update_formation,
    delete_formation
)

router = APIRouter(prefix="/api/formations", tags=["Formations"])

@router.post("/", response_model=FormationRead)
def create(data: FormationCreate, db: Session = Depends(get_db)):
    return create_formation(db, data)

@router.get("/", response_model=list[FormationRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_formations(db)

@router.get("/{formation_id}", response_model=FormationRead)
def read_one(formation_id: int, db: Session = Depends(get_db)):
    formation = get_formation_by_id(db, formation_id)
    if not formation:
        raise HTTPException(status_code=404, detail="Formation non trouvée")
    return formation

@router.put("/{formation_id}", response_model=FormationRead)
def update(formation_id: int, data: FormationUpdate, db: Session = Depends(get_db)):
    formation = update_formation(db, formation_id, data)
    if not formation:
        raise HTTPException(status_code=404, detail="Formation non trouvée")
    return formation

@router.delete("/{formation_id}")
def delete(formation_id: int, db: Session = Depends(get_db)):
    formation = delete_formation(db, formation_id)
    if not formation:
        raise HTTPException(status_code=404, detail="Formation non trouvée")
    return {"detail": "Formation supprimée"}
