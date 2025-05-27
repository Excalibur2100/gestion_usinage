from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.crm.historique_client_schemas import *
from services.crm.historique_client_service import *

router = APIRouter(prefix="/historiques-client", tags=["Historique Client"])

@router.post("/", response_model=HistoriqueClientRead)
def create(data: HistoriqueClientCreate, db: Session = Depends(get_db)):
    return create_historique(db, data)

@router.get("/", response_model=List[HistoriqueClientRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_historiques(db)

@router.get("/{id_}", response_model=HistoriqueClientRead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_historique(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Historique non trouvé")
    return obj

@router.put("/{id_}", response_model=HistoriqueClientRead)
def update(id_: int, data: HistoriqueClientUpdate, db: Session = Depends(get_db)):
    obj = update_historique(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Historique non trouvé")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_historique(db, id_):
        raise HTTPException(status_code=404, detail="Historique non trouvé")
    return {"ok": True}

@router.post("/search", response_model=HistoriqueClientSearchResults)
def search(data: HistoriqueClientSearch, db: Session = Depends(get_db)):
    return {"results": search_historiques(db, data)}