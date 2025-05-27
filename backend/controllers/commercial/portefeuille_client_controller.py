from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.commercial.portefeuille_client_schemas import *
from services.commercial.portefeuille_client_service import *

router = APIRouter(prefix="/portefeuilles-clients", tags=["Portefeuilles Clients"])

@router.post("/", response_model=PortefeuilleClientRead)
def create(data: PortefeuilleClientCreate, db: Session = Depends(get_db)):
    return create_portefeuille(db, data)

@router.get("/", response_model=List[PortefeuilleClientRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_portefeuilles(db)

@router.get("/{id_}", response_model=PortefeuilleClientRead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_portefeuille(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Portefeuille non trouvé")
    return obj

@router.put("/{id_}", response_model=PortefeuilleClientRead)
def update(id_: int, data: PortefeuilleClientUpdate, db: Session = Depends(get_db)):
    obj = update_portefeuille(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Portefeuille non trouvé")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_portefeuille(db, id_):
        raise HTTPException(status_code=404, detail="Portefeuille non trouvé")
    return {"ok": True}

@router.post("/search", response_model=PortefeuilleClientSearchResults)
def search(data: PortefeuilleClientSearch, db: Session = Depends(get_db)):
    return {"results": search_portefeuilles(db, data)}
