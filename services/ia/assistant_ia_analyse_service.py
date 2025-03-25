# services/ia/assistant_ia_analyse_service.py

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from pathlib import Path


class IAModule(BaseModel):
    nom: str
    elements: List[str]

class IAModuleCheckResult(BaseModel):
    message: str
    suggestion_code: Optional[str] = None
    impact: Optional[str] = None
    created_at: datetime = datetime.utcnow()


def analyse_modules(modules: List[IAModule]) -> IAModuleCheckResult:
    composants_attendus = {"controller", "service", "schema", "view"}
    suggestions = []

    for module in modules:
        manquants = composants_attendus - set(module.elements)
        if manquants:
            suggestions.append(f"- Le module **{module.nom}** est incomplet : il manque {', '.join(manquants)}")

    if suggestions:
        return IAModuleCheckResult(
            message="Certains modules sont incomplets.",
            suggestion_code="\n".join(suggestions),
            impact="Des fonctionnalités peuvent être manquantes ou instables."
        )

    return IAModuleCheckResult(
        message="Tous les modules sont complets.",
    )

def detecter_composants_modules() -> dict:
    """
    Analyse tous les modules présents et détecte les composants manquants
    :return: dictionnaire des modules avec les composants manquants
    """
    dossiers = {
        "controllers": "controller",
        "services": "service",
        "views": "view",
        "models": "model"
    }

    base_path = Path(".")
    modules_detectes = {}

    # Construction de la map : {module_name: {controller, service, ...}}
    for dossier, suffixe in dossiers.items():
        chemin = base_path / dossier
        if not chemin.exists():
            continue

        for fichier in chemin.glob("*.py"):
            nom = fichier.stem.replace(f"_{suffixe}", "")
            if nom == "__init__":
                continue
            if nom not in modules_detectes:
                modules_detectes[nom] = set()
            modules_detectes[nom].add(suffixe)

    # Détection des composants manquants
    resultats = {}
    composants_attendus = set(dossiers.values())

    for module, composants_presents in modules_detectes.items():
        manquants = composants_attendus - composants_presents
        if manquants:
            resultats[module] = list(manquants)

    return resultats

def generer_composants_manquants(base_path=".") -> List[str]:
    """
    Génére automatiquement les fichiers manquants détectés pour chaque module
    """
    composants_manquants = detecter_composants_modules()
    resultats = []

    templates = {
        "controller": "from fastapi import APIRouter\n\nrouter = APIRouter(prefix='/{module_name}', tags=['{module_name.capitalize()}'])\n\n",
        "service": "def get_{module_name}():\n    pass\n",
        "view": "def render_{module_name}():\n    pass\n",
        "model": "from sqlalchemy import Column, Integer\nfrom db.base import Base\n\nclass {ModelName}(Base):\n    __tablename__ = '{module_name}s'\n    id = Column(Integer, primary_key=True)\n"
    }

    paths = {
        "controller": "controllers",
        "service": "services",
        "view": "views",
        "model": "models"
    }

    for module, manquants in composants_manquants.items():
        for composant in manquants:
            dossier = paths[composant]
            chemin_fichier = Path(base_path) / dossier / f"{module}_{composant}.py"
            if not chemin_fichier.exists():
                contenu = templates[composant].replace("{module_name}", module).replace("{ModelName}", module.capitalize())
                chemin_fichier.parent.mkdir(parents=True, exist_ok=True)
                with open(chemin_fichier, "w", encoding="utf-8") as f:
                    f.write(contenu)
                resultats.append(str(chemin_fichier))

    return resultats