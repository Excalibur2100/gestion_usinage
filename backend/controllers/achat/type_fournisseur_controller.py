from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.achat.type_fournisseur_schemas import *
from services.achat.type_fournisseur_service import *

router = APIRouter(prefix="/types-fournisseur", tags=["Types de Fournisseur"])

@router.post("/", response_model=TypeFournisseurRead)
def create(data: TypeFournisseurCreate, db: Session = Depends(get_db)):
    return create_type(db, data)

@router.get("/", response_model=List[TypeFournisseurRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_types(db)

@router.get("/{type_id}", response_model=TypeFournisseurRead)
def read(type_id: int, db: Session = Depends(get_db)):
    obj = get_type(db, type_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Type non trouvé")
    return obj

@router.put("/{type_id}", response_model=TypeFournisseurRead)
def update(type_id: int, data: TypeFournisseurUpdate, db: Session = Depends(get_db)):
    obj = update_type(db, type_id, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Type non trouvé")
    return obj

@router.delete("/{type_id}")
def delete(type_id: int, db: Session = Depends(get_db)):
    if not delete_type(db, type_id):
        raise HTTPException(status_code=404, detail="Type non trouvé")
    return {"ok": True}

@router.post("/search", response_model=TypeFournisseurSearchResults)
def search(data: TypeFournisseurSearch, db: Session = Depends(get_db)):
    return {"results": search_types(db, data)}
