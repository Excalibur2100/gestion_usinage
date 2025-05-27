class CodeGeneratorEngine:

    @staticmethod
    def generer_code_depuis_prompt(prompt: str, langage: str = "python", modele: str = "gpt-4") -> str:
        """
        Fonction simulée pour générer du code basé sur un prompt.
        À remplacer par appel réel IA (OpenAI, local, etc.)
        """
        if langage == "python":
            return f"# Code généré pour : {prompt}\ndef fonction():\n    pass"
        elif langage == "javascript":
            return f"// JS généré : {prompt}\nfunction run() {{\n    // ...\n}}"
        else:
            return f"// Code générique pour : {prompt}"

    @staticmethod
    def valider_code(code: str) -> bool:
        """
        Validation très simplifiée (exemple).
        """
        return len(code.strip()) > 0 and ("def " in code or "function" in code or "{" in code)