from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from typing import List
from pathlib import Path
import json


from services.ia.assistant_ia_service import AssistantIAService

router = APIRouter(prefix="/ia", tags=["Assistant IA"])
templates = Jinja2Templates(directory="templates")

ia_service = AssistantIAService()

@router.get("/dashboard", response_class=JSONResponse)
async def afficher_dashboard_ia(request: Request):
    composants = ia_service.analyser_composants_modules()
    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "composants": composants
    })

@router.post("/creer-fichiers", response_class=RedirectResponse)
async def creer_fichiers_manquants():
    ia_service.generer_composants_manquants()
    return RedirectResponse(url="/ia/dashboard", status_code=303)

@router.post("/organiser-composants", response_class=JSONResponse)
async def organiser_fichiers_et_modules():
    try:
        chemins_crees = ia_service.organiser_et_structurer_modules()
        return JSONResponse(content={
            "message": "Fichiers générés et organisés avec succès",
            "chemins": chemins_crees
        })
    except Exception as e:
        return JSONResponse(content={"message": "Erreur pendant l'organisation", "erreur": str(e)}, status_code=500)

@router.get("/taches-a-completer", response_class=JSONResponse)
async def afficher_taches_a_completer():
    try:
        chemin_fichier = "logs/intelligence/taches_a_completer.json"
        if not Path(chemin_fichier).exists():
            return JSONResponse(status_code=404, content={"message": "Fichier non trouvé"})
        with open(chemin_fichier, "r", encoding="utf-8") as f:
            contenu = json.load(f)
        return JSONResponse(content=contenu)
    except Exception as e:
        return JSONResponse(status_code=500, content={"erreur": str(e)})

@router.get("/historique-generation", response_model=List[dict])
async def afficher_historique_generation():
    return ia_service.lire_historique_generation()

@router.get("/suggestions-modules", response_model=str)
async def suggestions_modules():
    return ia_service.suggestion_markdown_modules()