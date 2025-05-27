from typing import Optional

class SuggestionOutilEngine:

    @staticmethod
    def suggérer_outil(operation: str, materiau: str) -> dict:
        """
        Génère une suggestion d'outil en fonction de l'opération et du matériau.
        """
        base = {
            "fraisage": {
                "aluminium": ("Fraise carbure monobloc 3 dents", "95%"),
                "acier": ("Fraise HSS revêtue TiAlN", "90%"),
                "inox": ("Fraise céramique", "85%"),
                "titane": ("Fraise carbure revêtue TiAlN", "88%"),
                "cuivre": ("Fraise carbure 2 dents", "92%"),
                "laiton": ("Fraise carbure 2 dents", "93%"),
                "plastique": ("Fraise carbure 1 dent", "90%")
            },
            "perçage": {
                "aluminium": ("Foret HSS 2 lèvres", "90%"),
                "acier": ("Foret HSS revêtu TiN", "88%"),
                "inox": ("Foret cobalt", "85%"),
                "titane": ("Foret carbure revêtu TiAlN", "87%"),
                "cuivre": ("Foret HSS affûté", "89%"),
                "laiton": ("Foret HSS affûté", "90%"),
                "plastique": ("Foret HSS affûté", "88%")
            },
            "tournage": {
                "aluminium": ("Plaquette carbure P20", "92%"),
                "acier": ("Plaquette carbure P30", "90%"),
                "inox": ("Plaquette carbure M20", "88%"),
                "titane": ("Plaquette carbure K20", "85%"),
                "cuivre": ("Plaquette carbure N10", "89%"),
                "laiton": ("Plaquette carbure N10", "90%"),
                "plastique": ("Plaquette carbure N10", "87%")
            },
            "alésage": {
                "aluminium": ("Alésoir carbure", "93%"),
                "acier": ("Alésoir HSS", "90%"),
                "inox": ("Alésoir carbure revêtu", "88%"),
                "titane": ("Alésoir carbure revêtu", "85%"),
                "cuivre": ("Alésoir HSS affûté", "89%"),
                "laiton": ("Alésoir HSS affûté", "90%"),
                "plastique": ("Alésoir HSS affûté", "88%")
            },
            "filetage": {
                "aluminium": ("Taraud HSS", "90%"),
                "acier": ("Taraud HSS revêtu TiN", "88%"),
                "inox": ("Taraud HSS revêtu TiAlN", "85%"),
                "titane": ("Taraud carbure revêtu", "87%"),
                "cuivre": ("Taraud HSS affûté", "89%"),
                "laiton": ("Taraud HSS affûté", "90%"),
                "plastique": ("Taraud HSS affûté", "88%")
            }
        }

        operation = operation.lower()
        materiau = materiau.lower()

        outil, score = base.get(operation, {}).get(materiau, ("Outil générique", "70%"))

        commentaire = f"Outil recommandé pour {operation} sur {materiau}"
        moteur = "tool-sim-ia"

        return {
            "outil_suggere": outil,
            "operation": operation,
            "materiau": materiau,
            "score": score,
            "commentaire": commentaire,
            "moteur": moteur
        }