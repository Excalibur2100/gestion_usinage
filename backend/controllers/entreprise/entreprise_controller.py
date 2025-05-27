from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.entreprise.entreprise_schemas import *
from services.entreprise.entreprise_service import *

router = APIRouter(prefix="/entreprises", tags=["Entreprises"])

@router.post("/", response_model=EntrepriseRead)
def create(data: EntrepriseCreate, db: Session = Depends(get_db)):
    return create_entreprise(db, data)

@router.get("/", response_model=List[EntrepriseRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_entreprises(db)

@router.get("/{id_}", response_model=EntrepriseRead)
def read(id_: int, db: Session = Depends(get_db)):
    entreprise = get_entreprise(db, id_)
    if not entreprise:
        raise HTTPException(status_code=404, detail="Entreprise non trouvée")
    return entreprise

@router.put("/{id_}", response_model=EntrepriseRead)
def update(id_: int, data: EntrepriseUpdate, db: Session = Depends(get_db)):
    entreprise = update_entreprise(db, id_, data)
    if not entreprise:
        raise HTTPException(status_code=404, detail="Entreprise non trouvée")
    return entreprise

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_entreprise(db, id_):
        raise HTTPException(status_code=404, detail="Entreprise non trouvée")
    return {"ok": True}

@router.post("/search", response_model=EntrepriseSearchResults)
def search(data: EntrepriseSearch, db: Session = Depends(get_db)):
    result = search_entreprises(db, data)
    return {"results": result}