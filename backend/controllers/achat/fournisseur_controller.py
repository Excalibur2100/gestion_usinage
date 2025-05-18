from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.achat.fournisseur_schemas import *
from services.achat.fournisseur_services import *

router = APIRouter(prefix="/fournisseurs", tags=["Fournisseurs"])

@router.post("/", response_model=FournisseurRead)
def create(data: FournisseurCreate, db: Session = Depends(get_db)):
    return create_fournisseur(db, data)

@router.get("/", response_model=List[FournisseurRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_fournisseurs(db)

@router.get("/{fournisseur_id}", response_model=FournisseurRead)
def read(fournisseur_id: int, db: Session = Depends(get_db)):
    obj = get_fournisseur(db, fournisseur_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Fournisseur non trouvé")
    return obj

@router.put("/{fournisseur_id}", response_model=FournisseurRead)
def update(fournisseur_id: int, data: FournisseurUpdate, db: Session = Depends(get_db)):
    obj = update_fournisseur(db, fournisseur_id, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Fournisseur non trouvé")
    return obj

@router.delete("/{fournisseur_id}")
def delete(fournisseur_id: int, db: Session = Depends(get_db)):
    if not delete_fournisseur(db, fournisseur_id):
        raise HTTPException(status_code=404, detail="Fournisseur non trouvé")
    return {"ok": True}

@router.post("/search", response_model=FournisseurSearchResults)
def search(data: FournisseurSearch, db: Session = Depends(get_db)):
    return {"results": search_fournisseurs(db, data)}
