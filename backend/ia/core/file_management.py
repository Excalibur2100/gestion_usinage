from pathlib import Path
from typing import List

class FileManager:
    def __init__(self, base_path: str = "."):
        """
        Initialise le gestionnaire de fichiers.
        :param base_path: Chemin de base pour les opérations sur les fichiers.
        """
        self.base_path = Path(base_path)

    def organize_files(self, structure: dict) -> List[str]:
        """
        Organise les fichiers selon une structure donnée.
        :param structure: Dictionnaire définissant la structure des dossiers et fichiers.
                          Exemple : {"controllers": ["user_controller.py", "order_controller.py"]}
        :return: Liste des chemins des fichiers créés ou organisés.
        """
        created_paths = []
        for folder, files in structure.items():
            folder_path = self.base_path / folder
            folder_path.mkdir(parents=True, exist_ok=True)
            for file_name in files:
                file_path = folder_path / file_name
                if not file_path.exists():
                    file_path.touch()  # Crée un fichier vide
                    created_paths.append(str(file_path))
        return created_paths

    def create_folder(self, folder_name: str) -> str:
        """
        Crée un dossier s'il n'existe pas déjà.
        :param folder_name: Nom du dossier à créer.
        :return: Chemin du dossier créé.
        """
        folder_path = self.base_path / folder_name
        folder_path.mkdir(parents=True, exist_ok=True)
        return str(folder_path)

    def list_files(self, folder_name: str) -> List[str]:
        """
        Liste tous les fichiers dans un dossier donné.
        :param folder_name: Nom du dossier à explorer.
        :return: Liste des chemins des fichiers dans le dossier.
        """
        folder_path = self.base_path / folder_name
        if not folder_path.exists():
            raise FileNotFoundError(f"Le dossier {folder_name} n'existe pas.")
        return [str(file) for file in folder_path.glob("**/*") if file.is_file()]

    def delete_file(self, file_path: str) -> bool:
        """
        Supprime un fichier donné.
        :param file_path: Chemin du fichier à supprimer.
        :return: True si le fichier a été supprimé, False s'il n'existait pas.
        """
        path = self.base_path / file_path
        if path.exists() and path.is_file():
            path.unlink()
            return True
        return False