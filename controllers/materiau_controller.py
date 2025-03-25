from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.schemas import MateriauCreate, MateriauRead
from services.materiau.materiau_services import (
    creer_materiau,
    get_tous_materiaux,
    get_materiau_par_id,
    update_materiau,
    supprimer_materiau
)

router = APIRouter(prefix="/materiaux", tags=["Matériaux"])

@router.post("/", response_model=MateriauRead)
def creer(materiau_data: MateriauCreate, db: Session = Depends(get_db)):
    return creer_materiau(db, materiau_data)

@router.get("/", response_model=list[MateriauRead])
def lire_tous(db: Session = Depends(get_db)):
    return get_tous_materiaux(db)

@router.get("/{id}", response_model=MateriauRead)
def lire_un(id: int, db: Session = Depends(get_db)):
    materiau = get_materiau_par_id(db, id)
    if not materiau:
        raise HTTPException(status_code=404, detail="Matériau non trouvé")
    return materiau

@router.put("/{id}", response_model=MateriauRead)
def maj(id: int, materiau_data: MateriauCreate, db: Session = Depends(get_db)):
    materiau = update_materiau(db, id, materiau_data)
    if not materiau:
        raise HTTPException(status_code=404, detail="Matériau non trouvé pour mise à jour")
    return materiau

@router.delete("/{id}", status_code=204)
def supprimer(id: int, db: Session = Depends(get_db)):
    supprimer_materiau(db, id)
