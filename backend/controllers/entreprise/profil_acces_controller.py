from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.entreprise.profil_acces_schemas import *
from services.entreprise.profil_acces_service import *

router = APIRouter(prefix="/profils-acces", tags=["Profils Accès"])

@router.post("/", response_model=ProfilAccesRead)
def create(data: ProfilAccesCreate, db: Session = Depends(get_db)):
    return create_profil(db, data)

@router.get("/", response_model=List[ProfilAccesRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_profils(db)

@router.get("/{id_}", response_model=ProfilAccesRead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_profil(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Profil non trouvé")
    return obj

@router.put("/{id_}", response_model=ProfilAccesRead)
def update(id_: int, data: ProfilAccesUpdate, db: Session = Depends(get_db)):
    obj = update_profil(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Profil non trouvé")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_profil(db, id_):
        raise HTTPException(status_code=404, detail="Profil non trouvé")
    return {"ok": True}

@router.post("/search", response_model=ProfilAccesSearchResults)
def search(data: ProfilAccesSearch, db: Session = Depends(get_db)):
    return {"results": search_profils(db, data)}