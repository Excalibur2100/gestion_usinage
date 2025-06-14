from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db.database import get_db
from backend.db.schemas.achat.lignes_reception_schemas import (
    LigneReceptionCreate, LigneReceptionUpdate, LigneReceptionRead, LigneReceptionSearch
)
from backend.services.achat.lignes_reception_service import (
    creer_ligne_reception, get_ligne_reception, list_lignes_reception, update_ligne_reception,
    delete_ligne_reception, bulk_create_lignes_reception, bulk_delete_lignes_reception,
    search_lignes_reception, export_lignes_reception_csv
)

router = APIRouter(prefix="/lignes-reception", tags=["Lignes Réception"])

@router.post("/", response_model=LigneReceptionRead)
def create_ligne(data: LigneReceptionCreate, db: Session = Depends(get_db)):
    return creer_ligne_reception(db, data)

@router.get("/{ligne_id}", response_model=LigneReceptionRead)
def read_ligne(ligne_id: int, db: Session = Depends(get_db)):
    return get_ligne_reception(db, ligne_id)

@router.get("/", response_model=list[LigneReceptionRead])
def list_all_lignes(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    return list_lignes_reception(db, skip, limit)

@router.put("/{ligne_id}", response_model=LigneReceptionRead)
def update_ligne_endpoint(ligne_id: int, data: LigneReceptionUpdate, db: Session = Depends(get_db)):
    return update_ligne_reception(db, ligne_id, data.dict(exclude_unset=True))

@router.delete("/{ligne_id}")
def delete_ligne_endpoint(ligne_id: int, db: Session = Depends(get_db)):
    return delete_ligne_reception(db, ligne_id)

@router.post("/bulk", response_model=list[LigneReceptionRead])
def bulk_create(data: list[LigneReceptionCreate], db: Session = Depends(get_db)):
    return bulk_create_lignes_reception(db, data)

@router.delete("/bulk")
def bulk_delete(ids: list[int], db: Session = Depends(get_db)):
    return {"deleted": bulk_delete_lignes_reception(db, ids)}

@router.post("/search", response_model=dict)
def search(data: LigneReceptionSearch, db: Session = Depends(get_db)):
    return search_lignes_reception(db, data)

@router.get("/export/csv")
def export_csv(db: Session = Depends(get_db)):
    csv_buffer = export_lignes_reception_csv(db)
    return {"csv": csv_buffer.getvalue()}