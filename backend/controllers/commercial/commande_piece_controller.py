from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.commercial.commande_piece_schemas import *
from services.commercial.commande_piece_service import *

router = APIRouter(prefix="/commande-pieces", tags=["Commandes Pièces Client"])

@router.post("/", response_model=CommandePieceRead)
def create(data: CommandePieceCreate, db: Session = Depends(get_db)):
    return create_commande_piece(db, data)

@router.get("/", response_model=List[CommandePieceRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_commande_pieces(db)

@router.get("/{id_}", response_model=CommandePieceRead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_commande_piece(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Commande pièce non trouvée")
    return obj

@router.put("/{id_}", response_model=CommandePieceRead)
def update(id_: int, data: CommandePieceUpdate, db: Session = Depends(get_db)):
    obj = update_commande_piece(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Commande pièce non trouvée")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_commande_piece(db, id_):
        raise HTTPException(status_code=404, detail="Commande pièce non trouvée")
    return {"ok": True}

@router.post("/search", response_model=CommandePieceSearchResults)
def search(data: CommandePieceSearch, db: Session = Depends(get_db)):
    return {"results": search_commande_pieces(db, data)}
