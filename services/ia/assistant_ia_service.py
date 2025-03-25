import os
import ast
import json
from datetime import datetime
from pathlib import Path
from typing import List, Optional
from pydantic import BaseModel

# === MODELES ===

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

# === SERVICE ===

class AssistantIAService:

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

    def analyser_composants_modules(self) -> List[ModeleDetecte]:
        suffixes = {
            "controllers": "_controller.py",
            "services": "_service.py",
            "views": "_view.py"
        }
        modeles = self.extraire_modeles_db()
        modules = []

        for modele in modeles:
            composants = []
            for dossier, suffixe in suffixes.items():
                chemin = Path(f"{dossier}/{modele}{suffixe}")
                if chemin.exists():
                    composants.append(str(chemin))
            modules.append(ModeleDetecte(nom=modele, chemins_trouves=composants))
        return modules

    def generer_composants_manquants(self) -> List[str]:
        suffixes = {
            "controllers": "_controller.py",
            "services": "_service.py",
            "views": "_view.py"
        }
        contenus = {
            "controllers": "# Contrôleur généré automatiquement\n",
            "services": "# Service généré automatiquement\n",
            "views": "# Vue générée automatiquement\n"
        }

        fichiers_crees = []
        composants = self.analyser_composants_modules()

        for module in composants:
            for dossier, suffixe in suffixes.items():
                chemin = Path(f"{dossier}/{module.nom}{suffixe}")
                if not chemin.exists():
                    contenu = contenus[dossier] + f"# Module : {module.nom}\n"
                    chemin.parent.mkdir(parents=True, exist_ok=True)
                    chemin.write_text(contenu, encoding="utf-8")
                    fichiers_crees.append(str(chemin))

        if fichiers_crees:
            log_path = Path("logs/intelligence/taches_a_completer.json")
            log_path.parent.mkdir(parents=True, exist_ok=True)

            log_entry = {
                "timestamp": datetime.utcnow().isoformat(),
                "fichiers_crees": fichiers_crees
            }

            if log_path.exists():
                logs = json.loads(log_path.read_text(encoding="utf-8"))
            else:
                logs = []

            logs.append(log_entry)
            log_path.write_text(json.dumps(logs, indent=2), encoding="utf-8")

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
        composants = self.analyser_composants_modules()
        lignes = ["## Suggestions de l'IA\n"]
        for m in composants:
            lignes.append(f"- **{m.nom}** :")
            if m.chemins_trouves:
                for chemin in m.chemins_trouves:
                    lignes.append(f"  - {chemin}")
            else:
                lignes.append("  - Aucun fichier détecté")
        return "\n".join(lignes)