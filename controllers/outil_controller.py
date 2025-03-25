from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.schemas import OutilCreate, OutilRead
from services.outil.outil_services import (
    creer_outil,
    get_tous_outils,
    get_outil_par_id,
    update_outil,
    supprimer_outil
)

router = APIRouter(prefix="/outils", tags=["Outils"])

@router.post("/", response_model=OutilRead)
def creer(outil_data: OutilCreate, db: Session = Depends(get_db)):
    return creer_outil(db, outil_data)

@router.get("/", response_model=list[OutilRead])
def lire_tous(db: Session = Depends(get_db)):
    return get_tous_outils(db)

@router.get("/{id}", response_model=OutilRead)
def lire_un(id: int, db: Session = Depends(get_db)):
    outil = get_outil_par_id(db, id)
    if not outil:
        raise HTTPException(status_code=404, detail="Outil non trouvé")
    return outil

@router.put("/{id}", response_model=OutilRead)
def maj_outil(id: int, outil_data: OutilCreate, db: Session = Depends(get_db)):
    outil = update_outil(db, id, outil_data)
    if not outil:
        raise HTTPException(status_code=404, detail="Outil non trouvé pour mise à jour")
    return outil

@router.delete("/{id}", status_code=204)
def supprimer(id: int, db: Session = Depends(get_db)):
    supprimer_outil(db, id)
