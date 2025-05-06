from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from backend.db.models.database import get_db
from backend.db.schemas.securite_schemas import LogsSecuriteCreate, LogsSecuriteRead
from services.securite.securite_service import (
    creer_log_securite,
    get_tous_logs_securite,
    get_log_securite_par_id,
    supprimer_log_securite,
)

router = APIRouter(
    prefix="/securite",
    tags=["Sécurité"]
)

@router.post("/logs/", response_model=LogsSecuriteRead, status_code=status.HTTP_201_CREATED)
def creer_log(data: LogsSecuriteCreate, db: Session = Depends(get_db)):
    """
    Crée un nouveau log de sécurité.
    """
    return creer_log_securite(db, data.evenement, data.description, data.niveau)

@router.get("/logs/", response_model=List[LogsSecuriteRead])
def lire_tous_logs(db: Session = Depends(get_db)):
    """
    Récupère tous les logs de sécurité.
    """
    return get_tous_logs_securite(db)

@router.get("/logs/{log_id}", response_model=LogsSecuriteRead)
def lire_log_par_id(log_id: int, db: Session = Depends(get_db)):
    """
    Récupère un log de sécurité par son ID.
    """
    log = get_log_securite_par_id(db, log_id)
    if not log:
        raise HTTPException(status_code=404, detail="Log de sécurité non trouvé")
    return log

@router.delete("/logs/{log_id}", status_code=status.HTTP_204_NO_CONTENT)
def supprimer_log(log_id: int, db: Session = Depends(get_db)):
    """
    Supprime un log de sécurité par son ID.
    """
    log = get_log_securite_par_id(db, log_id)
    if not log:
        raise HTTPException(status_code=404, detail="Log de sécurité non trouvé")
    supprimer_log_securite(db, log_id)