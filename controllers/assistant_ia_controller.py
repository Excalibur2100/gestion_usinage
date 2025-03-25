from fastapi import APIRouter
from typing import List
from services.ia.assistant_ia_service import (
    AssistantIAService,
    IAModuleCheckResult,
    IAModule,
)

router = APIRouter(prefix="/assistant-ia", tags=["Assistant IA"])
ia_service = AssistantIAService()

@router.post("/analyse-modules", response_model=IAModuleCheckResult)
def analyse_modules_endpoint(modules: List[IAModule]):
    return ia_service.analyse_modules(modules)

@router.post("/generer-manquants", response_model=List[str])
def generer_fichiers_manquants():
    return ia_service.generer_composants_manquants()

@router.post("/organiser-composants", response_model=List[str])
def organiser_fichiers_et_modules():
    try:
        chemins_crees = ia_service.organiser_et_structurer_modules()
        return chemins_crees
    except Exception as e:
        return [f"Erreur pendant l'organisation : {str(e)}"]

@router.get("/historique-generation", response_model=List[dict])
def afficher_historique_generation():
    return ia_service.lire_historique_generation()

@router.get("/suggestions-modules", response_model=str)
def suggestions_modules():
    return ia_service.suggestion_markdown_modules()

@router.get("/ping-modules", response_model=List[str])
def ping_modules():
    return ia_service.ping_modules()