from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.commercial.action_commerciale_schemas import *
from services.commercial.action_commerciale_service import *

router = APIRouter(prefix="/actions-commerciales", tags=["Actions Commerciales"])

@router.post("/", response_model=ActionCommercialeRead)
def create(data: ActionCommercialeCreate, db: Session = Depends(get_db)):
    return create_action(db, data)

@router.get("/", response_model=List[ActionCommercialeRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_actions(db)

@router.get("/{action_id}", response_model=ActionCommercialeRead)
def read(action_id: int, db: Session = Depends(get_db)):
    obj = get_action(db, action_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Action non trouvée")
    return obj

@router.put("/{action_id}", response_model=ActionCommercialeRead)
def update(action_id: int, data: ActionCommercialeUpdate, db: Session = Depends(get_db)):
    obj = update_action(db, action_id, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Action non trouvée")
    return obj

@router.delete("/{action_id}")
def delete(action_id: int, db: Session = Depends(get_db)):
    if not delete_action(db, action_id):
        raise HTTPException(status_code=404, detail="Action non trouvée")
    return {"ok": True}

@router.post("/search", response_model=ActionCommercialeSearchResults)
def search(data: ActionCommercialeSearch, db: Session = Depends(get_db)):
    return {"results": search_actions(db, data)}
