from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.ia.chiffrage_piece_schemas import *
from services.ia.chiffrage_piece_service import *

router = APIRouter(prefix="/chiffrage-pieces", tags=["Chiffrage Pièces"])

@router.post("/", response_model=ChiffragePieceRead)
def create(data: ChiffragePieceCreate, db: Session = Depends(get_db)):
    return create_piece(db, data)

@router.get("/", response_model=List[ChiffragePieceRead])
def get_all(db: Session = Depends(get_db)):
    return get_all_pieces(db)

@router.get("/{id_}", response_model=ChiffragePieceRead)
def get_one(id_: int, db: Session = Depends(get_db)):
    obj = get_piece(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Pièce non trouvée")
    return obj

@router.put("/{id_}", response_model=ChiffragePieceRead)
def update(id_: int, data: ChiffragePieceUpdate, db: Session = Depends(get_db)):
    obj = update_piece(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Pièce non trouvée")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_piece(db, id_):
        raise HTTPException(status_code=404, detail="Pièce non trouvée")
    return {"ok": True}

@router.post("/{id_}/operations", response_model=ChiffrageOperationRead)
def add_operation(id_: int, data: ChiffrageOperationCreate, db: Session = Depends(get_db)):
    piece = get_piece(db, id_)
    if not piece:
        raise HTTPException(status_code=404, detail="Pièce non trouvée")
    return create_operation(db, data, piece_id=id_)

@router.post("/machines", response_model=ChiffrageMachineRead)
def create_machine_route(data: ChiffrageMachineCreate, db: Session = Depends(get_db)):
    return create_machine(db, data)