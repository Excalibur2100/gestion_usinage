from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.ia.optimisation_production_ai_schemas import *
from services.ia.optimisation_production_ai_service import *

router = APIRouter(prefix="/optimisations-ai", tags=["Optimisation IA"])

@router.post("/", response_model=OptimisationAIRead)
def create(data: OptimisationAICreate, db: Session = Depends(get_db)):
    return create_optimisation(db, data)

@router.get("/", response_model=List[OptimisationAIRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_optimisations(db)

@router.get("/{id_}", response_model=OptimisationAIRead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_optimisation(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Optimisation non trouvée")
    return obj

@router.put("/{id_}", response_model=OptimisationAIRead)
def update(id_: int, data: OptimisationAIUpdate, db: Session = Depends(get_db)):
    obj = update_optimisation(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Optimisation non trouvée")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_optimisation(db, id_):
        raise HTTPException(status_code=404, detail="Optimisation non trouvée")
    return {"ok": True}

@router.post("/search", response_model=OptimisationAISearchResults)
def search(data: OptimisationAISearch, db: Session = Depends(get_db)):
    return {"results": search_optimisations(db, data)}