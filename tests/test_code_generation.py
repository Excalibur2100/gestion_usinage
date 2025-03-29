import unittest
from pathlib import Path
from ia.core.code_generation import CodeGenerator

class TestCodeGenerator(unittest.TestCase):
    def setUp(self):
        """
        Prépare un environnement de test propre avant chaque test.
        """
        self.code_generator = CodeGenerator()
        self.test_file_path = "test_code_generation/test_file.py"
        # Assure-toi que le dossier de test existe
        Path(self.test_file_path).parent.mkdir(parents=True, exist_ok=True)

    def tearDown(self):
        """
        Nettoie l'environnement de test après chaque test.
        """
        if Path(self.test_file_path).exists():
            Path(self.test_file_path).unlink()
        if Path(self.test_file_path).parent.exists():
            Path(self.test_file_path).parent.rmdir()

    def test_generate_file(self):
        """
        Teste la génération d'un fichier avec du contenu donné.
        """
        content = "# Ceci est un fichier de test\nprint('Hello, world!')"
        result = self.code_generator.generate_file(self.test_file_path, content)
        self.assertTrue(Path(self.test_file_path).exists())
        self.assertEqual(Path(self.test_file_path).read_text(encoding="utf-8"), content)
        self.assertEqual(result, f"Fichier généré : {self.test_file_path}")

    def test_suggest_code(self):
        """
        Teste la suggestion de code basée sur une description.
        """
        description = "Créer une fonction pour additionner deux nombres"
        suggestion = self.code_generator.suggest_code(description)
        self.assertIn("# Code suggéré pour :", suggestion)
        self.assertIn("def example_function():", suggestion)

if __name__ == "__main__":
    unittest.main()