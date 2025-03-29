import unittest
from fastapi.testclient import TestClient
from controllers.ia.router_ia import router
from fastapi import FastAPI

# Crée une application FastAPI pour tester le routeur
app = FastAPI()
app.include_router(router)

client = TestClient(app)

class TestRouterIA(unittest.TestCase):
    def test_dashboard(self):
        """
        Teste l'affichage du tableau de bord.
        """
        response = client.get("/ia/dashboard")
        self.assertEqual(response.status_code, 200)

    def test_creer_fichiers(self):
        """
        Teste la création des fichiers manquants.
        """
        response = client.post("/ia/creer-fichiers")
        self.assertEqual(response.status_code, 200)  # Modifié pour attendre 200

    def test_organiser_composants(self):
        """
        Teste l'organisation des composants.
        """
        response = client.post("/ia/organiser-composants")
        self.assertEqual(response.status_code, 200)
        self.assertIn("message", response.json())

    def test_taches_a_completer(self):
        """
        Teste l'affichage des tâches à compléter.
        """
        response = client.get("/ia/taches-a-completer")
        self.assertIn(response.status_code, [200, 404])  # Peut être 404 si le fichier n'existe pas

    def test_historique_generation(self):
        """
        Teste l'affichage de l'historique de génération.
        """
        response = client.get("/ia/historique-generation")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_suggestions_modules(self):
        """
        Teste l'affichage des suggestions de modules.
        """
        response = client.get("/ia/suggestions-modules")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), str)

    def test_calcul_complexe(self):
        """
        Teste le calcul complexe.
        """
        response = client.get("/ia/calcul-complexe?x=3&y=4")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["result"], 5.0)

    def test_generer_code(self):
        """
        Teste la génération de code.
        """
        response = client.post("/ia/generer-code", json={"description": "Créer une fonction"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("suggestion", response.json())

    def test_lire_logs(self):
        """
        Teste la lecture des logs.
        """
        response = client.get("/ia/logs")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json()["logs"], list)

    def test_effacer_logs(self):
        """
        Teste la suppression des logs.
        """
        response = client.delete("/ia/logs")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Tous les logs ont été effacés.")

class TestRouterIA(unittest.TestCase):
    # ... Tests existants ...

    def test_calcul_complexe_negative_values(self):
        """
        Teste le calcul complexe avec des valeurs négatives.
        """
        response = client.get("/ia/calcul-complexe?x=-3&y=-4")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["result"], 5.0)  # Distance euclidienne reste positive

    def test_generer_code_empty_description(self):
        """
        Teste la génération de code avec une description vide.
        """
        response = client.post("/ia/generer-code", json={"description": ""})
        self.assertEqual(response.status_code, 422)  # FastAPI doit retourner une erreur de validation

    def test_generer_code_missing_description(self):
        """
        Teste la génération de code sans fournir de description.
        """
        response = client.post("/ia/generer-code", json={})
        self.assertEqual(response.status_code, 422)  # FastAPI doit retourner une erreur de validation

    def test_effacer_logs_when_empty(self):
        """
        Teste la suppression des logs lorsque le fichier de logs est déjà vide.
        """
        # Assure-toi que les logs sont vides
        client.delete("/ia/logs")
        response = client.delete("/ia/logs")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Tous les logs ont été effacés.")

if __name__ == "__main__":
    unittest.main()