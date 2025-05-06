from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db.models.database import get_db
from backend.db.schemas.controle_robot_schemas import ControleRobotCreate, ControleRobotRead
from backend.services.controlerobot.controle_robot_service import (
    creer_controle_robot,
    get_tous_controles_robot,
    get_controle_robot_par_id,
    update_controle_robot,
    supprimer_controle_robot
)

router = APIRouter(prefix="/controle-robots", tags=["Contrôle Robots"])

@router.post("/", response_model=ControleRobotRead)
def creer(data: ControleRobotCreate, db: Session = Depends(get_db)):
    return creer_controle_robot(db, data)

@router.get("/", response_model=list[ControleRobotRead])
def lire_tous(db: Session = Depends(get_db)):
    return get_tous_controles_robot(db)

@router.get("/{id}", response_model=ControleRobotRead)
def lire_un(id: int, db: Session = Depends(get_db)):
    controle = get_controle_robot_par_id(db, id)
    if not controle:
        raise HTTPException(status_code=404, detail="Contrôle non trouvé")
    return controle

@router.put("/{id}", response_model=ControleRobotRead)
def maj(id: int, data: ControleRobotCreate, db: Session = Depends(get_db)):
    controle = update_controle_robot(db, id, data)
    if not controle:
        raise HTTPException(status_code=404, detail="Contrôle non trouvé pour mise à jour")
    return controle

@router.delete("/{id}", status_code=204)
def supprimer(id: int, db: Session = Depends(get_db)):
    supprimer_controle_robot(db, id)
    return

