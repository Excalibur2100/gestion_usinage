# backend/services/achat/service_metier/reception_metier_service.py

from typing import Optional
from datetime import datetime

from sqlalchemy.orm import Session

from backend.db.models.tables.achat.receptions import Reception
from backend.db.models.tables.achat.lignes_reception import LigneReception

from backend.db.schemas.achat.reception_schemas import (
    StatutReceptionEnum,
    ReceptionCreate
)


def generer_reference_reception(date: Optional[datetime] = None) -> str:
    """
    Génère automatiquement un numéro de réception du type : REC-2025-0605080012
    """
    date = date or datetime.now()
    return f"REC-{date.year}-{date.strftime('%m%d%H%M%S')}"


def valider_reception_avant_creation(
    db: Session,
    reception_data: ReceptionCreate
) -> Optional[str]:
    """
    Règle métier avant insertion en base :
    - Si statut = 'refusée', commentaire obligatoire.
    """
    if reception_data.statut == StatutReceptionEnum.refusee and not reception_data.commentaire:
        return "Un commentaire est obligatoire pour une réception refusée."
    return None


def calcul_statut_reception(db: Session, reception_id: int) -> Optional[StatutReceptionEnum]:
    """
    Calcule dynamiquement le statut d'une réception en fonction des lignes associées.
    """
    reception = db.get(Reception, reception_id)
    if not reception:
        return None

    lignes = reception.lignes_reception

    if not lignes or len(lignes) == 0:
        return StatutReceptionEnum.en_attente

    total_lignes = len(lignes)
    lignes_recues = [l for l in lignes if l.quantite_recue and l.quantite_recue >= l.quantite_commandee]
    lignes_partielles = [l for l in lignes if l.quantite_recue and 0 < l.quantite_recue < l.quantite_commandee]

    if len(lignes_recues) == total_lignes:
        return StatutReceptionEnum.recue
    elif lignes_recues or lignes_partielles:
        return StatutReceptionEnum.partiellement_recue
    else:
        return StatutReceptionEnum.en_attente


def appliquer_statut_automatique(db: Session, reception_id: int) -> Optional[Reception]:
    """
    Applique automatiquement le statut calculé à la réception.
    """
    reception = db.get(Reception, reception_id)
    if not reception:
        return None

    nouveau_statut = calcul_statut_reception(db, reception_id)
    if nouveau_statut and nouveau_statut != reception.statut:
        reception.statut = nouveau_statut
        db.commit()
        db.refresh(reception)
    return reception


def archiver_reception(db: Session, reception_id: int) -> Optional[Reception]:
    """
    Archive manuellement une réception.
    """
    reception = db.get(Reception, reception_id)
    if not reception:
        return None

    reception.statut = StatutReceptionEnum.archivee
    db.commit()
    db.refresh(reception)
    return reception


def valider_reception(db: Session, reception_id: int) -> Optional[Reception]:
    """
    Validation manuelle d'une réception par un opérateur.
    """
    reception = db.get(Reception, reception_id)
    if not reception:
        return None

    if not reception.lignes_reception or len(reception.lignes_reception) == 0:
        raise ValueError("Impossible de valider une réception sans ligne.")

    reception.statut = StatutReceptionEnum.recue
    db.commit()
    db.refresh(reception)
    return reception