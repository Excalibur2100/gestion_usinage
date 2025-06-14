from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.dependencies import get_db
from backend.services.achat.service_metier import reception_metier_service
from backend.db.models.tables.achat.receptions import Reception


router = APIRouter(
    prefix="/api/v1/metier/receptions",
    tags=["Réceptions - Métier"]
)


@router.post("/statut-automatique/{reception_id}", response_model=Reception, summary="Appliquer un statut automatique", description="Recalcule et applique automatiquement le statut d’une réception en fonction des lignes reçues")
def appliquer_statut_automatique(reception_id: int, db: Session = Depends(get_db)):
    reception = reception_metier_service.appliquer_statut_automatique(db, reception_id)
    if not reception:
        raise HTTPException(status_code=404, detail="Réception non trouvée")
    return reception


@router.post("/valider/{reception_id}", response_model=Reception, summary="Valider une réception", description="Valide manuellement une réception, après vérification des lignes")
def valider_reception(reception_id: int, db: Session = Depends(get_db)):
    try:
        return reception_metier_service.valider_reception(db, reception_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=404, detail="Réception non trouvée")


@router.post("/archiver/{reception_id}", response_model=Reception, summary="Archiver une réception", description="Met une réception en statut archivé")
def archiver_reception(reception_id: int, db: Session = Depends(get_db)):
    reception = reception_metier_service.archiver_reception(db, reception_id)
    if not reception:
        raise HTTPException(status_code=404, detail="Réception non trouvée")
    return reception