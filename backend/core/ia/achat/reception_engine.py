from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import func
from backend.db.models.tables.achat.receptions import Reception, StatutReception


def generer_numero_reception(db: Session) -> str:
    """
    Génère un numéro unique de réception au format : REC-YYYY-XXX
    Exemple : REC-2025-001
    """
    annee = datetime.now().year
    prefix = f"REC-{annee}-"

    # Compte combien il y a déjà de réceptions cette année
    count = db.query(func.count(Reception.id)).filter(
        func.extract('year', Reception.date_reception) == annee
    ).scalar()

    numero = f"{prefix}{str(count + 1).zfill(3)}"
    return numero


def suggestion_statut_par_conformite(quantites: list[int], attendues: list[int]) -> StatutReception:
    """
    Suggestion de statut basé sur une comparaison simple des quantités reçues vs attendues.
    """
    if not quantites or not attendues or len(quantites) != len(attendues):
        return StatutReception.en_attente

    complet = all(q >= a for q, a in zip(quantites, attendues))
    partiel = any(0 < q < a for q, a in zip(quantites, attendues))

    if complet:
        return StatutReception.recue
    elif partiel:
        return StatutReception.partiellement_recue
    else:
        return StatutReception.en_attente


def generer_document_reception_placeholder(reception_id: int) -> str:
    """
    Génère un chemin de document associé fictif.
    (À remplacer par une vraie génération PDF ou autre)
    """
    date_str = datetime.now().strftime("%Y%m%d")
    return f"documents/receptions/reception_{reception_id}_{date_str}.pdf"