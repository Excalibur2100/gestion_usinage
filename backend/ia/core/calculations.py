import math
from typing import List

class Calculator:
    def complex_calculation(self, x: float, y: float) -> float:
        """
        Effectue un calcul complexe basé sur deux valeurs.
        :param x: Première valeur.
        :param y: Deuxième valeur.
        :return: Résultat du calcul.
        """
        return math.sqrt(x**2 + y**2)

    def average(self, numbers: List[float]) -> float:
        """
        Calcule la moyenne d'une liste de nombres.
        :param numbers: Liste de nombres.
        :return: Moyenne des nombres.
        """
        if not numbers:
            raise ValueError("La liste des nombres est vide.")
        return sum(numbers) / len(numbers)

    def optimize_process(self, data: List[float]) -> List[float]:
        """
        Optimise un processus en triant les données.
        :param data: Liste de données à optimiser.
        :return: Liste triée.
        """
        return sorted(data)