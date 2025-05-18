from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.commercial.campagne_commerciale_schemas import *
from services.commercial.campagne_commerciale_service import *

router = APIRouter(prefix="/campagnes-commerciales", tags=["Campagnes Commerciales"])

@router.post("/", response_model=CampagneCommercialeRead)
def create(data: CampagneCommercialeCreate, db: Session = Depends(get_db)):
    return create_campagne(db, data)

@router.get("/", response_model=List[CampagneCommercialeRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_campagnes(db)

@router.get("/{campagne_id}", response_model=CampagneCommercialeRead)
def read(campagne_id: int, db: Session = Depends(get_db)):
    obj = get_campagne(db, campagne_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Campagne non trouvée")
    return obj

@router.put("/{campagne_id}", response_model=CampagneCommercialeRead)
def update(campagne_id: int, data: CampagneCommercialeUpdate, db: Session = Depends(get_db)):
    obj = update_campagne(db, campagne_id, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Campagne non trouvée")
    return obj

@router.delete("/{campagne_id}")
def delete(campagne_id: int, db: Session = Depends(get_db)):
    if not delete_campagne(db, campagne_id):
        raise HTTPException(status_code=404, detail="Campagne non trouvée")
    return {"ok": True}

@router.post("/search", response_model=CampagneCommercialeSearchResults)
def search(data: CampagneCommercialeSearch, db: Session = Depends(get_db)):
    return {"results": search_campagnes(db, data)}
