from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from backend.db.schemas.gamme_production_schemas.gamme_production_schemas import GammeProductionCreate, GammeProductionRead
from services.production.gamme_production_services import (
    creer_gamme,
    get_toutes_gammes,
    get_gamme_par_id,
    update_gamme,
    supprimer_gamme
)

router = APIRouter(prefix="/gammes", tags=["Gammes de production"])

@router.post("/", response_model=GammeProductionRead)
def creer(data: GammeProductionCreate, db: Session = Depends(get_db)):
    return creer_gamme(db, data)

@router.get("/", response_model=list[GammeProductionRead])
def lire_toutes(db: Session = Depends(get_db)):
    return get_toutes_gammes(db)

@router.get("/{id}", response_model=GammeProductionRead)
def lire_une(id: int, db: Session = Depends(get_db)):
    gamme = get_gamme_par_id(db, id)
    if not gamme:
        raise HTTPException(status_code=404, detail="Gamme non trouvée")
    return gamme

@router.put("/{id}", response_model=GammeProductionRead)
def maj(id: int, data: GammeProductionCreate, db: Session = Depends(get_db)):
    gamme = update_gamme(db, id, data)
    if not gamme:
        raise HTTPException(status_code=404, detail="Gamme non trouvée pour mise à jour")
    return gamme

@router.delete("/{id}", status_code=204)
def supprimer(id: int, db: Session = Depends(get_db)):
    supprimer_gamme(db, id)
    return

