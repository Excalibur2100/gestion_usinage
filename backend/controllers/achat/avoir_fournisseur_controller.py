from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.achat.avoir_fournisseur_schemas import *
from services.achat.avoir_fournisseur_service import *

router = APIRouter(prefix="/avoirs-fournisseur", tags=["Avoirs Fournisseur"])

@router.post("/", response_model=AvoirFournisseurRead)
def create(data: AvoirFournisseurCreate, db: Session = Depends(get_db)):
    return create_avoir(db, data)

@router.get("/", response_model=List[AvoirFournisseurRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_avoirs(db)

@router.get("/{avoir_id}", response_model=AvoirFournisseurRead)
def read(avoir_id: int, db: Session = Depends(get_db)):
    obj = get_avoir(db, avoir_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Avoir non trouvé")
    return obj

@router.put("/{avoir_id}", response_model=AvoirFournisseurRead)
def update(avoir_id: int, data: AvoirFournisseurUpdate, db: Session = Depends(get_db)):
    obj = update_avoir(db, avoir_id, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Avoir non trouvé")
    return obj

@router.delete("/{avoir_id}")
def delete(avoir_id: int, db: Session = Depends(get_db)):
    if not delete_avoir(db, avoir_id):
        raise HTTPException(status_code=404, detail="Avoir non trouvé")
    return {"ok": True}

@router.post("/search", response_model=AvoirFournisseurSearchResults)
def search(data: AvoirFournisseurSearch, db: Session = Depends(get_db)):
    return {"results": search_avoirs(db, data)}
