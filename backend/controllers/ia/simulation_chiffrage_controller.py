from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.ia.simulation_chiffrage_schemas import *
from services.ia.simulation_chiffrage_service import *

router = APIRouter(prefix="/simulations-chiffrage", tags=["Simulation Chiffrage"])

@router.post("/", response_model=SimulationChiffrageRead)
def create(data: SimulationChiffrageCreate, db: Session = Depends(get_db)):
    return create_simulation(db, data)

@router.get("/", response_model=List[SimulationChiffrageRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_simulations(db)

@router.get("/{id_}", response_model=SimulationChiffrageRead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_simulation(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Simulation non trouvée")
    return obj

@router.put("/{id_}", response_model=SimulationChiffrageRead)
def update(id_: int, data: SimulationChiffrageUpdate, db: Session = Depends(get_db)):
    obj = update_simulation(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Simulation non trouvée")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_simulation(db, id_):
        raise HTTPException(status_code=404, detail="Simulation non trouvée")
    return {"ok": True}

@router.post("/search", response_model=SimulationChiffrageSearchResults)
def search(data: SimulationChiffrageSearch, db: Session = Depends(get_db)):
    return {"results": search_simulations(db, data)}