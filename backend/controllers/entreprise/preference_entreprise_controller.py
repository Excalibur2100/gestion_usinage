from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.entreprise.preference_entreprise_schemas import *
from services.entreprise.preference_entreprise_service import *

router = APIRouter(prefix="/preferences-entreprise", tags=["Préférences Entreprise"])

@router.post("/", response_model=PreferenceEntrepriseRead)
def create(data: PreferenceEntrepriseCreate, db: Session = Depends(get_db)):
    return create_preference(db, data)

@router.get("/", response_model=List[PreferenceEntrepriseRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_preferences(db)

@router.get("/{id_}", response_model=PreferenceEntrepriseRead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_preference(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Préférence non trouvée")
    return obj

@router.put("/{id_}", response_model=PreferenceEntrepriseRead)
def update(id_: int, data: PreferenceEntrepriseUpdate, db: Session = Depends(get_db)):
    obj = update_preference(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Préférence non trouvée")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_preference(db, id_):
        raise HTTPException(status_code=404, detail="Préférence non trouvée")
    return {"ok": True}

@router.post("/search", response_model=PreferenceEntrepriseSearchResults)
def search(data: PreferenceEntrepriseSearch, db: Session = Depends(get_db)):
    return {"results": search_preferences(db, data)}