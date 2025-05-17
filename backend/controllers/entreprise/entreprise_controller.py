from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services.entreprise.entreprise_service import *
from backend.db.schemas.entreprise.entreprise_schemas import *
from backend.db.models.database import get_db


router = APIRouter(prefix="/entreprises", tags=["Entreprises"])

@router.post("/", response_model=EntrepriseRead)
def create(data: EntrepriseCreate, db: Session = Depends(get_db)):
    return create_entreprise(db, data)

@router.get("/", response_model=list[EntrepriseRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_entreprises(db)

@router.get("/{entreprise_id}", response_model=EntrepriseRead)
def read(entreprise_id: int, db: Session = Depends(get_db)):
    entreprise = get_entreprise(db, entreprise_id)
    if not entreprise:
        raise HTTPException(status_code=404, detail="Entreprise non trouvée")
    return entreprise

@router.put("/{entreprise_id}", response_model=EntrepriseRead)
def update(entreprise_id: int, data: EntrepriseUpdate, db: Session = Depends(get_db)):
    entreprise = update_entreprise(db, entreprise_id, data)
    if not entreprise:
        raise HTTPException(status_code=404, detail="Entreprise non trouvée")
    return entreprise

@router.delete("/{entreprise_id}")
def delete(entreprise_id: int, db: Session = Depends(get_db)):
    if not delete_entreprise(db, entreprise_id):
        raise HTTPException(status_code=404, detail="Entreprise non trouvée")
    return {"ok": True}

@router.post("/search", response_model=EntrepriseSearchResults)
def search(data: EntrepriseSearch, db: Session = Depends(get_db)):
    result = search_entreprises(db, data)
    return {"results": result}
