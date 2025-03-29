import json
from pathlib import Path
from datetime import datetime, timezone
from typing import List, Dict

class Learning:
    def __init__(self, log_path: str = "logs/intelligence/learning_logs.json"):
        """
        Initialise le gestionnaire de logs d'apprentissage.
        :param log_path: Chemin du fichier de logs.
        """
        self.log_path = Path(log_path)
        self.log_path.parent.mkdir(parents=True, exist_ok=True)
        if not self.log_path.exists():
            self.log_path.write_text("[]", encoding="utf-8")

    def log_action(self, action: str, result: str, metadata: Dict = None):
        """
        Enregistre une action et son résultat dans le fichier de logs.
        :param action: Description de l'action effectuée.
        :param result: Résultat de l'action.
        :param metadata: Informations supplémentaires sur l'action.
        """
        metadata = metadata or {}
        log_entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "action": action,
            "result": result,
            "metadata": metadata
        }
        logs = self._read_logs()
        logs.append(log_entry)
        self._write_logs(logs)

    def get_logs(self) -> List[Dict]:
        """
        Retourne tous les logs enregistrés.
        :return: Liste des entrées de logs.
        """
        return self._read_logs()

    def filter_logs(self, keyword: str) -> List[Dict]:
        """
        Filtre les logs contenant un mot-clé spécifique.
        :param keyword: Mot-clé à rechercher dans les actions ou résultats.
        :return: Liste des entrées de logs correspondantes.
        """
        logs = self._read_logs()
        return [log for log in logs if keyword.lower() in log["action"].lower() or keyword.lower() in log["result"].lower()]

    def clear_logs(self):
        """
        Supprime tous les logs enregistrés.
        """
        self._write_logs([])

    def _read_logs(self) -> List[Dict]:
        """
        Lit les logs depuis le fichier.
        :return: Liste des entrées de logs.
        """
        if not self.log_path.exists():
            self.log_path.write_text("[]", encoding="utf-8")
        return json.loads(self.log_path.read_text(encoding="utf-8"))

    def _write_logs(self, logs: List[Dict]):
        """
        Écrit les logs dans le fichier.
        :param logs: Liste des entrées de logs à enregistrer.
        """
        self.log_path.write_text(json.dumps(logs, indent=4, ensure_ascii=False), encoding="utf-8")