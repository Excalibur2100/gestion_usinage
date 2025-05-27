import math
from typing import Optional, Any
from sqlalchemy.orm import Session
from backend.db.models.tables.production.outils import Outil  # à adapter selon ton chemin réel

class ConditionsCoupeEngine:

    @staticmethod
    def calculer_n_rpm(vc: float, diametre_outil: float) -> float:
        if diametre_outil <= 0:
            raise ValueError("Le diamètre doit être > 0")
        return round((1000 * vc) / (math.pi * diametre_outil), 0)

    @staticmethod
    def calculer_avance_par_minute(fz: float, n_rpm: float, dents: int) -> float:
        if dents <= 0 or n_rpm <= 0:
            raise ValueError("RPM et nombre de dents doivent être > 0")
        return round(fz * n_rpm * dents, 2)

    @staticmethod
    def recommander_conditions(operation: str, materiau: str) -> Optional[dict]:
        base = {
            "acier": {"fraisage": (180, 0.12, 1.5), "perçage": (100, 0.10, 2.0)},
            "alu":   {"fraisage": (350, 0.18, 3.0), "perçage": (250, 0.15, 2.5)},
            "inox":  {"fraisage": (120, 0.10, 1.0), "perçage": (80, 0.08, 1.5)},
        }
        mat = base.get(materiau.lower())
        if mat and operation.lower() in mat:
            vc, fz, ap = mat[operation.lower()]
            return {"vitesse_coupe": vc, "avance": fz, "profondeur_passage": ap}
        return None

    @staticmethod
    def get_outil_optimal(operation: str, materiau: str, db: Session) -> dict:
        """
        Cherche un outil adapté dans la base. Si aucun trouvé, retourne une suggestion IA.
        """
        outil = (
            db.query(Outil)
            .filter(Outil.operation.ilike(f"%{operation}%"))
            .filter(Outil.materiau.ilike(f"%{materiau}%"))
            .first()
        )

        if outil:
            return {
                "source": "local-db",
                "nom": outil.nom,
                "diametre": outil.diametre,
                "revêtement": outil.revetement,
                "operation": outil.operation,
                "materiau": outil.materiau,
                "référence": outil.reference
            }

        # Si aucun outil en base, fallback IA
        suggestion = ConditionsCoupeEngine.recommander_conditions(operation, materiau)
        if suggestion:
            return {
                "source": "simulation-ia",
                "operation": operation,
                "materiau": materiau,
                **suggestion
            }

        return {
            "source": "aucune donnée",
            "message": "Aucun outil trouvé localement ni suggestion disponible"
        }