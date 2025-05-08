import os
import time
import subprocess
from ia.api.copilot_api import AssistantIA

class TaskManager:
    def __init__(self, api_key):
        self.assistant = AssistantIA(api_key=api_key)
        self.tasks = []  # Liste des tâches à exécuter

    def add_task(self, task_description):
        """
        Ajoute une tâche à la liste des tâches.
        """
        self.tasks.append(task_description)
        print(f"Tâche ajoutée : {task_description}")

    def create_file(self, file_path, content):
        """
        Crée un nouveau fichier avec le contenu spécifié.
        """
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            file.write(content)
        print(f"Fichier créé : {file_path}")

    def process_tasks(self):
        """
        Traite les tâches en attente.
        """
        while True:
            if self.tasks:
                task = self.tasks.pop(0)
                print(f"Traitement de la tâche : {task}")
                result = self.assistant.handle_task(task)
                file_path = f"ia/features/{task.replace(' ', '_').lower()}.py"
                self.create_file(file_path, result)
                print(f"Tâche terminée et fichier créé : {file_path}")
            else:
                print("Aucune tâche en attente. En attente de nouvelles tâches...")
            time.sleep(5)

    def generate_tests(self, task_description):
        """
        Génère des tests unitaires pour une fonctionnalité.
        """
        test_description = f"Créer des tests unitaires pour : {task_description}"
        test_code = self.assistant.handle_task(test_description)
        test_file_path = f"ia/tests/test_{task_description.replace(' ', '_').lower()}.py"
        self.create_file(test_file_path, test_code)
        print(f"Tests générés : {test_file_path}")
        return test_file_path

    def run_tests(self):
        """
        Exécute les tests unitaires et retourne les résultats.
        """
        result = subprocess.run(["pytest", "ia/tests"], capture_output=True, text=True)
        print(result.stdout)
        return result.stdout

    def automate_development(self, task_description):
        """
        Automatisation complète : génère une fonctionnalité, des tests, et les exécute.
        """
        print(f"Développement de la tâche : {task_description}")
        code = self.assistant.handle_task(task_description)
        file_path = f"ia/features/{task_description.replace(' ', '_').lower()}.py"
        self.create_file(file_path, code)

        test_file_path = self.generate_tests(task_description)

        print("Exécution des tests...")
        test_results = self.run_tests()
        return {"code_file": file_path, "test_file": test_file_path, "test_results": test_results}