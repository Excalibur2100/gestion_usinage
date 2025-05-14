from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from backend.db.schemas.programme_piece_schemas.programme_piece_schemas import ProgrammePieceCreate, ProgrammePieceRead
from services.production.programme_piece_services import (
    creer_programme,
    get_tous_programmes,
    get_programme_par_id,
    update_programme,
    supprimer_programme
)

router = APIRouter(prefix="/programmes", tags=["Programmes"])

@router.post("/", response_model=ProgrammePieceRead)
def creer(data: ProgrammePieceCreate, db: Session = Depends(get_db)):
    return creer_programme(db, data)

@router.get("/", response_model=list[ProgrammePieceRead])
def lire_tous(db: Session = Depends(get_db)):
    return get_tous_programmes(db)

@router.get("/{id}", response_model=ProgrammePieceRead)
def lire_un(id: int, db: Session = Depends(get_db)):
    prog = get_programme_par_id(db, id)
    if not prog:
        raise HTTPException(status_code=404, detail="Programme non trouvé")
    return prog

@router.put("/{id}", response_model=ProgrammePieceRead)
def maj(id: int, data: ProgrammePieceCreate, db: Session = Depends(get_db)):
    prog = update_programme(db, id, data)
    if not prog:
        raise HTTPException(status_code=404, detail="Programme non trouvé pour mise à jour")
    return prog

@router.delete("/{id}", status_code=204)
def supprimer(id: int, db: Session = Depends(get_db)):
    supprimer_programme(db, id)
    return

