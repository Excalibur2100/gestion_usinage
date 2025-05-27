from typing import Optional
from datetime import datetime

class PredictionEngine:

    @staticmethod
    def generer_prediction(type_prediction: str, machine: Optional[str] = None, contexte: Optional[str] = None) -> dict:
        """
        Génère une prédiction IA fictive basée sur le type de panne.
        """
        niveaux_risque = {
            "usure outil": "élevé",
            "panne capteur": "modéré",
            "calibration": "faible"
        }

        delais_estimes = {
            "usure outil": "5 jours",
            "panne capteur": "12h",
            "calibration": "10 jours"
        }

        risque = niveaux_risque.get(type_prediction.lower(), "modéré")
        delai = delais_estimes.get(type_prediction.lower(), "3 jours")

        message = f"Risque détecté : {type_prediction.upper()}"
        if machine:
            message += f" sur la machine {machine}"

        if contexte:
            message += f". Contexte : {contexte}"

        message += f". Risque : {risque.upper()}, intervention recommandée sous {delai}."

        return {
            "type_prediction": type_prediction,
            "niveau_risque": risque,
            "delai_prediction": delai,
            "message": message,
            "source_ia": "simulation interne"
        }