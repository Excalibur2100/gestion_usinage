import unittest
from ia.core.security import Security

class TestSecurity(unittest.TestCase):
    def setUp(self):
        """
        Prépare un environnement de test propre avant chaque test.
        """
        self.security = Security()

    def test_validate_action_allowed(self):
        """
        Teste qu'une action autorisée passe sans problème.
        """
        action = "create_file"
        result = self.security.validate_action(action)
        self.assertTrue(result)

    def test_validate_action_delete(self):
        """
        Teste qu'une action contenant 'delete' est bloquée.
        """
        action = "delete_file"
        with self.assertRaises(ValueError) as context:
            self.security.validate_action(action)
        self.assertEqual(str(context.exception), "Action non autorisée : suppression interdite.")

    def test_validate_action_shutdown(self):
        """
        Teste qu'une action contenant 'shutdown' est bloquée.
        """
        action = "shutdown_system"
        with self.assertRaises(ValueError) as context:
            self.security.validate_action(action)
        self.assertEqual(str(context.exception), "Action non autorisée : arrêt du système interdit.")

    def test_validate_action_case_insensitive(self):
        """
        Teste que la validation est insensible à la casse.
        """
        action = "DeLeTe_file"
        with self.assertRaises(ValueError) as context:
            self.security.validate_action(action)
        self.assertEqual(str(context.exception), "Action non autorisée : suppression interdite.")

if __name__ == "__main__":
    unittest.main()