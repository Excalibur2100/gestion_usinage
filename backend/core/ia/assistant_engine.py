class AssistantEngine:

    @staticmethod
    def generer_reponse(prompt: str, moteur: str = "gpt-4", temperature: float = 0.7) -> str:
        """
        Simule une réponse IA à un prompt (fonction factice pour usage local).
        """
        if "ordre fabrication" in prompt.lower():
            return "Ordre de fabrication généré automatiquement pour la pièce spécifiée."
        elif "planning" in prompt.lower():
            return "Planning mis à jour. L'équipe de nuit est assignée."
        else:
            return f"Réponse IA simulée : '{prompt[:40]}...'"

    @staticmethod
    def extraire_tags(prompt: str) -> list:
        """
        Extrait des mots-clés potentiels d’un prompt (simulation).
        """
        mots = prompt.lower().split()
        return [mot for mot in mots if len(mot) > 4]
    