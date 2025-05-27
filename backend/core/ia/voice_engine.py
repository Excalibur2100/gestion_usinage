from typing import Optional
from datetime import datetime

class VoiceEngine:

    @staticmethod
    def simuler_transcription(audio_fichier: str, langue: str = "fr") -> dict:
        """
        Simule une reconnaissance vocale sur un fichier audio.
        """
        transcription = {
            "fr": "Lancer la production de la pièce 128",
            "en": "Start production of part 128"
        }.get(langue.lower(), "Commande non reconnue")

        intention = "demarrer_production" if "production" in transcription.lower() else "inconnue"

        return {
            "audio_fichier": audio_fichier,
            "langue": langue,
            "transcription": transcription,
            "intention": intention,
            "resultat_action": VoiceEngine.interpreter_intention(intention),
            "moteur_utilise": "simulation-voice-ai",
            "timestamp": datetime.utcnow().isoformat()
        }

    @staticmethod
    def interpreter_intention(intention: str) -> str:
        """
        Retourne une réponse ou action associée à l’intention vocale.
        """
        actions = {
            "demarrer_production": "Ordre de fabrication créé et machine lancée",
            "inconnue": "Aucune action déclenchée"
        }
        return actions.get(intention, "Action non définie")