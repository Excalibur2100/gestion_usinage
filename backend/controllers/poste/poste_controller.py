from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.poste_schemas.poste_schemas import PosteCreate, PosteUpdate, PosteRead
from services.poste.poste_service import (
    create_poste,
    get_all_postes,
    get_poste_by_id,
    update_poste,
    delete_poste
)

router = APIRouter(prefix="/api/postes", tags=["Postes"])

@router.post("/", response_model=PosteRead)
def create(data: PosteCreate, db: Session = Depends(get_db)):
    return create_poste(db, data)

@router.get("/", response_model=list[PosteRead])
def read_all(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return get_all_postes(db, skip, limit)

@router.get("/{poste_id}", response_model=PosteRead)
def read_one(poste_id: int, db: Session = Depends(get_db)):
    poste = get_poste_by_id(db, poste_id)
    if not poste:
        raise HTTPException(status_code=404, detail="Poste non trouvé")
    return poste

@router.put("/{poste_id}", response_model=PosteRead)
def update(poste_id: int, data: PosteUpdate, db: Session = Depends(get_db)):
    poste = update_poste(db, poste_id, data)
    if not poste:
        raise HTTPException(status_code=404, detail="Poste non trouvé")
    return poste

@router.delete("/{poste_id}")
def delete(poste_id: int, db: Session = Depends(get_db)):
    if not delete_poste(db, poste_id):
        raise HTTPException(status_code=404, detail="Poste non trouvé")
    return {"detail": "Poste supprimé"}
