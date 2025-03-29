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

class CodeGenerator:
    def generate_file(self, file_path: str, content: str) -> str:
        """
        Génère un fichier avec le contenu spécifié.
        :param file_path: Chemin du fichier à créer.
        :param content: Contenu à écrire dans le fichier.
        :return: Message confirmant la création du fichier.
        """
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return f"Fichier généré : {file_path}"

    def suggest_code(self, description: str) -> str:
        """
        Simule une suggestion de code basée sur une description.
        :param description: Description de la fonctionnalité à coder.
        :return: Code suggéré (simulé).
        """
        # Exemple de suggestion simulée
        return f"# Code suggéré pour : {description}\ndef example_function():\n    pass"