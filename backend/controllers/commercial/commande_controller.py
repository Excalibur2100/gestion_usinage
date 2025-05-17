from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.commercial.commande_schemas import *
from backend.services.commercial.commande_services import *

router = APIRouter(prefix="/commandes", tags=["Commandes Client"])

@router.post("/", response_model=CommandeRead)
def create(data: CommandeCreate, db: Session = Depends(get_db)):
    return create_commande(db, data)

@router.get("/", response_model=List[CommandeRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_commandes(db)

@router.get("/{commande_id}", response_model=CommandeRead)
def read(commande_id: int, db: Session = Depends(get_db)):
    obj = get_commande(db, commande_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Commande non trouvée")
    return obj

@router.put("/{commande_id}", response_model=CommandeRead)
def update(commande_id: int, data: CommandeUpdate, db: Session = Depends(get_db)):
    obj = update_commande(db, commande_id, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Commande non trouvée")
    return obj

@router.delete("/{commande_id}")
def delete(commande_id: int, db: Session = Depends(get_db)):
    if not delete_commande(db, commande_id):
        raise HTTPException(status_code=404, detail="Commande non trouvée")
    return {"ok": True}

@router.post("/search", response_model=CommandeSearchResults)
def search(data: CommandeSearch, db: Session = Depends(get_db)):
    return {"results": search_commandes(db, data)}
