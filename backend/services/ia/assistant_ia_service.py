import os
import ast
import json
from datetime import datetime
from datetime import timezone
from pathlib import Path
from typing import List, Optional
from pydantic import BaseModel

# Import des modules de core
from ia.core.learning import Learning
from ia.core.code_generation import CodeGenerator
from ia.core.calculations import Calculator
from ia.core.security import Security
from ia.core.file_management import FileManager


class IAModule(BaseModel):
    nom: str
    elements: List[str]


class IAModuleCheckResult(BaseModel):
    message: str
    suggestion_code: Optional[str] = None
    impact: Optional[str] = None
    created_at: datetime


class ModeleDetecte(BaseModel):
    nom: str
    chemins_trouves: List[str] = []


class AssistantIAService:
    def __init__(self, base_path: str = "."):
        self.base_path = Path(base_path)
        # Initialisation des modules de core
        self.learning = Learning()
        self.code_generator = CodeGenerator()
        self.calculator = Calculator()
        self.security = Security()
        self.file_manager = FileManager()

    def fichier_existe(self, chemin_relatif: str) -> bool:
        return (self.base_path / chemin_relatif).exists()

    def generer_fichier_si_absent(self, chemin_relatif: str, contenu: str) -> str:
        chemin_complet = self.base_path / chemin_relatif
        if not chemin_complet.exists():
            chemin_complet.parent.mkdir(parents=True, exist_ok=True)
            with open(chemin_complet, "w", encoding="utf-8") as f:
                f.write(contenu)
            return f"[Créé] {chemin_relatif}"
        else:
            return f"[Ignoré] {chemin_relatif} existe déjà."

    def analyser_composants_modules(self) -> List[ModeleDetecte]:
        dossiers_a_verifier = {
            "controllers": "_controller.py",
            "services": "_service.py",
            "views": "_view.py",
        }
        modules = []
        modeles = self.extraire_modeles_db()
        for modele in modeles:
            composants_trouves = []
            for dossier, suffixe in dossiers_a_verifier.items():
                chemin_fichier = Path(f"{dossier}/{modele}{suffixe}")
                if chemin_fichier.exists():
                    composants_trouves.append(f"{dossier}/{modele}{suffixe}")
            modules.append(ModeleDetecte(nom=modele, chemins_trouves=composants_trouves))
        return modules

    def extraire_modeles_db(self, models_path: str = "db/models") -> List[str]:
        modeles = []
        for fichier in Path(models_path).glob("*.py"):
            contenu = fichier.read_text(encoding="utf-8")
            arbre = ast.parse(contenu)
            for noeud in arbre.body:
                if isinstance(noeud, ast.ClassDef):
                    bases = [b.id for b in noeud.bases if isinstance(b, ast.Name)]
                    if "Base" in bases:
                        modeles.append(noeud.name.lower())
        return sorted(set(modeles))

    def generer_composants_manquants(self) -> List[str]:
        suffixes = {
            "controllers": "_controller.py",
            "services": "_service.py",
            "views": "_view.py",
        }
        contenus = {
            "controllers": "# Contrôleur généré automatiquement\n",
            "services": "# Service généré automatiquement\n",
            "views": "# Vue générée automatiquement\n",
        }
        modules_detectes = self.analyser_composants_modules()
        fichiers_crees = []
        for module in modules_detectes:
            for dossier, suffixe in suffixes.items():
                fichier = f"{dossier}/{module.nom}{suffixe}"
                if not Path(fichier).exists():
                    contenu = contenus[dossier] + f"# Module : {module.nom}\n"
                    Path(fichier).parent.mkdir(parents=True, exist_ok=True)
                    Path(fichier).write_text(contenu, encoding="utf-8")
                    fichiers_crees.append(fichier)

        if fichiers_crees:
            log_path = Path("logs/intelligence/taches_a_completer.json")
            log_path.parent.mkdir(parents=True, exist_ok=True)
            log_entry = {
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "fichiers_crees": fichiers_crees
            }
            if log_path.exists():
                existing_logs = json.loads(log_path.read_text(encoding="utf-8"))
            else:
                existing_logs = []
            existing_logs.append(log_entry)
            log_path.write_text(json.dumps(existing_logs, indent=2), encoding="utf-8")
        return fichiers_crees

    def organiser_et_structurer_modules(self) -> List[str]:
        composants = self.analyser_composants_modules()
        chemins = []

        dossiers = {
            "controllers": "controllers",
            "services": "services",
            "views": "views"
        }

        for module in composants:
            for chemin in module.chemins_trouves:
                nom_fichier = Path(chemin).name
                dossier_cible = chemin.split("/")[0]
                nom_module = module.nom
                nouveau_dossier = f"{dossiers[dossier_cible]}/{nom_module}"
                nouveau_chemin = f"{nouveau_dossier}/{nom_fichier}"

                Path(nouveau_dossier).mkdir(parents=True, exist_ok=True)
                ancien_chemin = Path(chemin)
                if ancien_chemin.exists():
                    ancien_chemin.rename(nouveau_chemin)
                    chemins.append(nouveau_chemin)

        return chemins

    def lire_historique_generation(self) -> List[dict]:
        log_path = Path("logs/intelligence/taches_a_completer.json")
        if log_path.exists():
            return json.loads(log_path.read_text(encoding="utf-8"))
        return []

    def suggestion_markdown_modules(self) -> str:
        modules = self.analyser_composants_modules()
        lignes = ["## Suggestions des modules", ""]
        for module in modules:
            lignes.append(f"- **{module.nom}** : {len(module.chemins_trouves)} composants")
            for chemin in module.chemins_trouves:
                lignes.append(f"  - {chemin}")
        return "\n".join(lignes)

    def analyse_modules(self, modules: List[IAModule]) -> IAModuleCheckResult:
        attendus = {"controller", "service", "view"}
        suggestions = []

        for module in modules:
            manquants = attendus - set(module.elements)
            if manquants:
                suggestions.append(
                    f"Le module **{module.nom}** est incomplet : il manque {', '.join(manquants)}"
                )

        if suggestions:
            return IAModuleCheckResult(
                message="Certains modules sont incomplets.",
                suggestion_code="\n".join(suggestions),
                impact="Des fonctionnalités peuvent être manquantes ou instables.",
                created_at=datetime.utcnow()
            )
        return IAModuleCheckResult(
            message="Tous les modules sont complets.",
            created_at=datetime.utcnow()
        )

    def ping_modules(self) -> List[str]:
        """Liste tous les modules Python dans controllers/, services/ et views/"""
        chemins = []
        for dossier in ["controllers", "services", "views"]:
            base_path = self.base_path / dossier
            if base_path.exists():
                fichiers = base_path.glob("**/*.py")
                chemins += [str(f.relative_to(self.base_path)) for f in fichiers if f.is_file()]
        return chemins

    def effectuer_calcul_complexe(self, x: float, y: float) -> float:
        """Exemple d'utilisation du module Calculator."""
        return self.calculator.complex_calculation(x, y)