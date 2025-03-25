from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.schemas import PointageCreate, PointageRead
from services.pointage.pointage_services import (
    creer_pointage,
    get_tous_pointages,
    get_pointage_par_id,
    update_pointage,
    supprimer_pointage
)

router = APIRouter(prefix="/pointages", tags=["Pointage"])

@router.post("/", response_model=PointageRead)
def creer(pointage_data: PointageCreate, db: Session = Depends(get_db)):
    return creer_pointage(db, pointage_data)

@router.get("/", response_model=list[PointageRead])
def lire_tous(db: Session = Depends(get_db)):
    return get_tous_pointages(db)

@router.get("/{id}", response_model=PointageRead)
def lire_un(id: int, db: Session = Depends(get_db)):
    pointage = get_pointage_par_id(db, id)
    if not pointage:
        raise HTTPException(status_code=404, detail="Pointage non trouvé")
    return pointage

@router.put("/{id}", response_model=PointageRead)
def maj(id: int, pointage_data: PointageCreate, db: Session = Depends(get_db)):
    pointage = update_pointage(db, id, pointage_data)
    if not pointage:
        raise HTTPException(status_code=404, detail="Pointage non trouvé pour mise à jour")
    return pointage

@router.delete("/{id}", status_code=204)
def supprimer(id: int, db: Session = Depends(get_db)):
    supprimer_pointage(db, id)
    return