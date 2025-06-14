# backend/core/ia/achat/lignes_reception_engine.py

from typing import Literal
from datetime import datetime
from sqlalchemy import func
from backend.db.models.tables.achat.lignes_reception import LigneReception  # Ajustez le chemin d'import selon votre projet

def evaluer_conformite_ligne(qte_commandee: float, qte_recue: float) -> Literal["conforme", "partielle", "non_conforme", "surplus"]:
    """
    Évalue le statut de conformité d’une ligne de réception :
    - "conforme" : reçue >= commandée
    - "partielle" : reçue > 0 mais < commandée
    - "non_conforme" : reçue == 0
    - "surplus" : reçue > commandée
    """
    if qte_recue == 0:
        return "non_conforme"
    elif qte_recue < qte_commandee:
        return "partielle"
    elif qte_recue == qte_commandee:
        return "conforme"
    elif qte_recue > qte_commandee:
        return "surplus"
    # Valeur par défaut pour garantir un retour sur tous les chemins
    return "non_conforme"


def generer_numero_ligne_reception(db, reception_id: int) -> str:
    """
    Génère un numéro unique pour chaque ligne de réception basé sur l'ID de la réception.
    Exemple : "REC-2025-001-001"
    """
    annee = datetime.now().year
    prefix = f"REC-{annee}-{reception_id}-"

    # Compte combien de lignes existent déjà pour cette réception
    count = db.query(func.count(LigneReception.id)).filter(LigneReception.reception_id == reception_id).scalar()
    
    numero = f"{prefix}{str(count + 1).zfill(3)}"
    return numero