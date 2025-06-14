# backend/controllers/achat/metier_controller/lignes_reception_metier_controller.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.dependencies import get_db
from backend.services.achat.service_metier import lignes_reception_metier_service


router = APIRouter(
    prefix="/api/v1/metier/lignes-reception",
    tags=["Lignes de réception - Métier"]
)


@router.post("/etat/{ligne_id}", summary="Recalculer l’état d’une ligne", description="Retourne l’état de conformité d’une ligne de réception (conforme, partielle, non conforme, surplus)")
def recalculer_etat_ligne(ligne_id: int, db: Session = Depends(get_db)):
    result = lignes_reception_metier_service.recalculer_etat_ligne(db, ligne_id)
    if not result:
        raise HTTPException(status_code=404, detail="Ligne non trouvée")
    return result