class ExternalDataEngine:

    @staticmethod
    def get_prix_matiere(matiere: str) -> float:
        """
        Simule un appel API ou web pour récupérer un prix matière €/kg
        """
        base_prix = {
            "aluminium": 3.50,
            "acier": 1.80,
            "inox": 4.20,
            "cuivre": 8.00,
            "titane": 20.00
        }
        return base_prix.get(matiere.lower(), 5.0)