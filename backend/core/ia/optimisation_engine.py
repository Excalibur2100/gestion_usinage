from typing import Optional
from datetime import datetime

class OptimisationEngine:

    @staticmethod
    def generer_recommandation(operation: str, duree_actuelle: float, machine: Optional[str] = None) -> dict:
        """
        Génère une suggestion d'optimisation IA fondée sur l'analyse de l'opération et la durée observée.
        """
        conseils_operation = {
            "fraisage": "Réduire les temps morts par changement d’outils rapide et augmenter l'avance si matière le permet.",
            "perçage": "Utiliser forets carbure, augmenter la vitesse de coupe et optimiser la lubrification.",
            "tournage": "Améliorer la stabilité de la pièce, réduire les interruptions d'usinage.",
            "alésage": "Vérifier les tolérances et employer des outils à haute précision.",
            "filetage": "Utiliser filetage par interpolation si possible pour réduire les passes."
        }

        taux_gain = 0.05  # par défaut
        conseil = conseils_operation.get(operation.lower(), "Analyser la chaîne de production pour éliminer les goulots.")

        # Ajustement dynamique selon la durée
        if duree_actuelle >= 6.0:
            taux_gain = 0.20
            conseil += " Envisager une stratégie de réduction de cycle ou une automatisation partielle."
        elif duree_actuelle >= 3.0:
            taux_gain = 0.12
        elif duree_actuelle >= 1.5:
            taux_gain = 0.08

        gain = round(duree_actuelle * taux_gain, 2)
        taux_percent = round(taux_gain * 100, 1)

        message = (
            f"Opération '{operation}' optimisée. Gain estimé : {gain}h "
            f"sur {duree_actuelle}h ({taux_percent}%)."
        )
        if machine:
            message += f" Machine concernée : {machine}."

        return {
            "operation": operation,
            "machine": machine,
            "gain_estime": f"-{gain}h",
            "conseil": conseil,
            "taux_optimisation": f"{taux_percent}%",
            "message": message,
            "timestamp": datetime.utcnow().isoformat()
        }

    @staticmethod
    def format_resume(nom: str, conseil: str, gain: str) -> str:
        return f"[{nom}] Gain estimé : {gain} | Conseil : {conseil}"