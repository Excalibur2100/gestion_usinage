import unittest
import os
from pathlib import Path
from ia.core.file_management import FileManager

class TestFileManager(unittest.TestCase):
    def setUp(self):
        """
        Prépare un environnement de test propre avant chaque test.
        """
        self.base_path = "test_file_management"
        self.file_manager = FileManager(base_path=self.base_path)
        # Assure-toi que le dossier de test existe
        Path(self.base_path).mkdir(parents=True, exist_ok=True)

    def tearDown(self):
        """
        Nettoie l'environnement de test après chaque test.
        """
        if Path(self.base_path).exists():
            for item in Path(self.base_path).glob("**/*"):
                if item.is_file():
                    item.unlink()  # Supprime les fichiers
            for item in Path(self.base_path).glob("**/*"):
                if item.is_dir():
                    item.rmdir()  # Supprime les dossiers vides
            Path(self.base_path).rmdir()  # Supprime le dossier racine

    def test_create_folder(self):
        """
        Teste la création d'un dossier.
        """
        folder_name = "new_folder"
        folder_path = self.file_manager.create_folder(folder_name)
        self.assertTrue(Path(folder_path).exists())
        self.assertTrue(Path(folder_path).is_dir())

    def test_organize_files(self):
        """
        Teste l'organisation des fichiers dans des dossiers.
        """
        structure = {
            "controllers": ["user_controller.py", "order_controller.py"],
            "services": ["user_service.py", "order_service.py"]
        }
        created_files = self.file_manager.organize_files(structure)
        for folder, files in structure.items():
            for file_name in files:
                file_path = Path(self.base_path) / folder / file_name
                self.assertTrue(file_path.exists())
                self.assertIn(str(file_path), created_files)

    def test_list_files(self):
        """
        Teste la liste des fichiers dans un dossier.
        """
        folder_name = "test_folder"
        self.file_manager.create_folder(folder_name)
        file_path = Path(self.base_path) / folder_name / "test_file.txt"
        file_path.write_text("Test content", encoding="utf-8")
        files = self.file_manager.list_files(folder_name)
        self.assertIn(str(file_path), files)

    def test_delete_file(self):
        """
        Teste la suppression d'un fichier.
        """
        folder_name = "test_folder"
        self.file_manager.create_folder(folder_name)
        file_path = Path(self.base_path) / folder_name / "test_file.txt"
        file_path.write_text("Test content", encoding="utf-8")
        self.assertTrue(file_path.exists())
        result = self.file_manager.delete_file(f"{folder_name}/test_file.txt")
        self.assertTrue(result)
        self.assertFalse(file_path.exists())

    def test_list_files_nonexistent_folder(self):
        """
        Teste la gestion d'une erreur lorsque le dossier n'existe pas.
        """
        with self.assertRaises(FileNotFoundError):
            self.file_manager.list_files("nonexistent_folder")

if __name__ == "__main__":
    unittest.main()