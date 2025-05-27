from typing import Optional
from datetime import datetime
import random

class SimulationChiffrageEngine:

    @staticmethod
    def simuler_chiffrage(scenario: str, complexite: str = "moyenne") -> dict:
        """
        Génère une simulation de chiffrage IA basée sur des méthodes d'estimation avancées.
        """
        # Multiplicateurs de complexité basés sur les pratiques industrielles
        multiplicateur_complexite = {
            "faible": 0.8,
            "moyenne": 1.0,
            "élevée": 1.3
        }

        # Estimation du temps de cycle en heures
        base_duree = round(random.uniform(1.0, 3.0), 2)

        # Coût horaire moyen en euros, basé sur des données industrielles
        cout_horaire = random.uniform(40, 60)
        base_cout = round(base_duree * cout_horaire, 2)

        # Taux de marge simulé entre 10% et 25%
        taux_marge = round(random.uniform(10, 25), 2)

        # Application du facteur de complexité
        facteur = multiplicateur_complexite.get(complexite.lower(), 1.0)
        duree_finale = round(base_duree * facteur, 2)
        cout_final = round(base_cout * facteur, 2)
        marge_simulee = round(cout_final * (taux_marge / 100), 2)

        return {
            "scenario": scenario,
            "duree_estimee": duree_finale,
            "cout_estime": cout_final,
            "marge_simulee": marge_simulee,
            "commentaire": f"Simulation IA basée sur complexité '{complexite}'",
            "source": "simulation-engine",
            "timestamp": datetime.utcnow().isoformat()
        }