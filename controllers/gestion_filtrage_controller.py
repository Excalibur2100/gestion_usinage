from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.schemas import GestionFiltrageCreate, GestionFiltrageRead
from services.securite.gestion_filtrage_services import (
    creer_filtrage, get_filtrages, get_filtrage_par_id,
    update_filtrage, supprimer_filtrage
)
from typing import List

router = APIRouter(prefix="/filtrages", tags=["Gestion Filtrage"])

@router.post("/", response_model=GestionFiltrageRead)
def create(data: GestionFiltrageCreate, db: Session = Depends(get_db)):
    return creer_filtrage(db, data)

@router.get("/", response_model=List[GestionFiltrageRead])
def read_all(db: Session = Depends(get_db)):
    return get_filtrages(db)

@router.get("/{id}", response_model=GestionFiltrageRead)
def read(id: int, db: Session = Depends(get_db)):
    filtrage = get_filtrage_par_id(db, id)
    if not filtrage:
        raise HTTPException(status_code=404, detail="Filtrage non trouvé")
    return filtrage

@router.put("/{id}", response_model=GestionFiltrageRead)
def update(id: int, data: GestionFiltrageCreate, db: Session = Depends(get_db)):
    filtrage = update_filtrage(db, id, data)
    if not filtrage:
        raise HTTPException(status_code=404, detail="Filtrage non trouvé pour mise à jour")
    return filtrage

@router.delete("/{id}", status_code=204)
def delete(id: int, db: Session = Depends(get_db)):
    supprimer_filtrage(db, id)
    
@router.get("/")
async def get_gestion_filtrage():
    return {"message": "Liste des filtrages"}