# backend/services/achat/service_metier/lignes_reception_metier_service.py

from typing import Optional
from sqlalchemy.orm import Session

from backend.db.models.tables.achat.lignes_reception import LigneReception


def calcul_conformite_ligne(ligne: LigneReception) -> str:
    """
    Calcule l’état de conformité d’une ligne de réception.
    - Conforme : quantité reçue == quantité commandée
    - Partielle : 0 < reçue < commandée
    - Non conforme : reçue == 0
    - Surplus : reçue > commandée
    """
    quantite_recue = getattr(ligne, "quantite_recue", 0)
    quantite_commandee = getattr(ligne, "quantite_commandee", 0)
    if int(quantite_recue) == 0:
        return "non_conforme"
    elif int(quantite_recue) < int(quantite_commandee):
        return "partielle"
    elif int(quantite_recue) == int(quantite_commandee):
        return "conforme"
    else:
        return "surplus"


def recalculer_etat_ligne(db: Session, ligne_id: int) -> Optional[dict]:
    """
    Recalcule dynamiquement l'état d'une ligne de réception à partir des quantités.
    Retourne un dict contenant l'état et les valeurs.
    """
    ligne = db.get(LigneReception, ligne_id)
    if not ligne:
        return None

    etat = calcul_conformite_ligne(ligne)
    return {
        "id": ligne.id,
        "designation": ligne.designation,
        "quantite_commandee": ligne.quantite_commandee,
        "quantite_recue": ligne.quantite_recue,
        "etat": etat
    }