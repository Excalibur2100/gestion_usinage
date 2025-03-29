from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from typing import List
from pathlib import Path
from pydantic import BaseModel
from services.ia.assistant_ia_service import AssistantIAService
from pydantic import BaseModel, Field
import json

router = APIRouter(prefix="/ia", tags=["Assistant IA"])
templates = Jinja2Templates(directory="templates")

ia_service = AssistantIAService()

class CodeRequest(BaseModel):
    description: str


@router.get("/dashboard", response_class=JSONResponse)
async def afficher_dashboard_ia(request: Request):
    composants = ia_service.analyser_composants_modules()
    return templates.TemplateResponse(request, "dashboard.html", {"composants": composants})

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

@router.get("/calcul-complexe", response_class=JSONResponse)
async def calcul_complexe(x: float, y: float):
    try:
        result = ia_service.calculator.complex_calculation(x, y)
        return JSONResponse(content={"result": result})
    except Exception as e:
        return JSONResponse(content={"message": "Erreur pendant le calcul", "erreur": str(e)}, status_code=500)
    
from pydantic import BaseModel

class CodeRequest(BaseModel):
    description: str = Field(..., min_length=1, description="La description ne peut pas être vide.")

@router.post("/generer-code", response_class=JSONResponse)
async def generer_code(request: CodeRequest):
    try:
        suggestion = ia_service.code_generator.suggest_code(request.description)
        return JSONResponse(content={"suggestion": suggestion})
    except Exception as e:
        return JSONResponse(content={"message": "Erreur pendant la génération de code", "erreur": str(e)}, status_code=500)
    
@router.get("/logs", response_class=JSONResponse)
async def lire_logs():
    try:
        logs = ia_service.learning.get_logs()
        return JSONResponse(content={"logs": logs})
    except Exception as e:
        return JSONResponse(content={"message": "Erreur pendant la lecture des logs", "erreur": str(e)}, status_code=500)
    
@router.delete("/logs", response_class=JSONResponse)
async def effacer_logs():
    try:
        ia_service.learning.clear_logs()
        return JSONResponse(content={"message": "Tous les logs ont été effacés."})
    except Exception as e:
        return JSONResponse(content={"message": "Erreur pendant la suppression des logs", "erreur": str(e)}, status_code=500)