class Security:
    def validate_action(self, action: str):
        """
        Valide une action avant exécution.
        :param action: Description de l'action à valider.
        :raises ValueError: Si l'action est jugée non autorisée.
        """
        if "delete" in action.lower():
            raise ValueError("Action non autorisée : suppression interdite.")
        if "shutdown" in action.lower():
            raise ValueError("Action non autorisée : arrêt du système interdit.")
        print(f"Action validée : {action}")
        return True