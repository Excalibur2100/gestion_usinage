import unittest
import os
import json
from pathlib import Path
from ia.core.learning import Learning

class TestLearning(unittest.TestCase):
    def setUp(self):
        """
        Prépare un environnement de test propre avant chaque test.
        """
        self.log_path = "test_logs/learning_logs.json"
        self.learning = Learning(log_path=self.log_path)
        # Assure-toi que le dossier de test existe
        Path(self.log_path).parent.mkdir(parents=True, exist_ok=True)
        # Crée le fichier de logs s'il n'existe pas
        if not Path(self.log_path).exists():
            Path(self.log_path).write_text("[]", encoding="utf-8")

    def tearDown(self):
        """
        Nettoie l'environnement de test après chaque test.
        """
        if Path(self.log_path).exists():
            Path(self.log_path).unlink()

    def test_log_action(self):
        """
        Teste l'enregistrement d'une action dans les logs.
        """
        self.learning.log_action("Test Action", "Success", {"key": "value"})
        logs = self.learning.get_logs()
        self.assertEqual(len(logs), 1)
        self.assertEqual(logs[0]["action"], "Test Action")
        self.assertEqual(logs[0]["result"], "Success")
        self.assertEqual(logs[0]["metadata"]["key"], "value")

    def test_get_logs(self):
        """
        Teste la récupération des logs.
        """
        self.learning.log_action("Action 1", "Success")
        self.learning.log_action("Action 2", "Failure")
        logs = self.learning.get_logs()
        self.assertEqual(len(logs), 2)
        self.assertEqual(logs[0]["action"], "Action 1")
        self.assertEqual(logs[1]["action"], "Action 2")

    def test_filter_logs(self):
        """
        Teste le filtrage des logs par mot-clé.
        """
        self.learning.log_action("Action 1", "Success")
        self.learning.log_action("Action 2", "Failure")
        filtered_logs = self.learning.filter_logs("Success")
        self.assertEqual(len(filtered_logs), 1)
        self.assertEqual(filtered_logs[0]["result"], "Success")

    def test_clear_logs(self):
        """
        Teste la suppression de tous les logs.
        """
        self.learning.log_action("Action 1", "Success")
        self.learning.log_action("Action 2", "Failure")
        self.learning.clear_logs()
        logs = self.learning.get_logs()
        self.assertEqual(len(logs), 0)

    def test_log_file_creation(self):
        """
        Teste si le fichier de logs est créé automatiquement.
        """
        self.assertTrue(Path(self.log_path).exists())

if __name__ == "__main__":
    unittest.main()