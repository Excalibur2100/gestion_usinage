from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from services.ia.assistant_ia_service import (
    analyser_composants_modules,
    generer_composants_manquants,
    organiser_et_structurer_modules,
    lire_historique_generation,
    suggestion_markdown_modules
)

router = APIRouter(prefix="/ia", tags=["Assistant IA"])
templates = Jinja2Templates(directory="templates")

@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    modules = analyser_composants_modules()
    nb_modules = len(modules)
    nb_incomplets = sum(1 for m in modules if len(m.chemins_trouves) < 3)
    return templates.TemplateResponse("ia_templates/dashboard.html", {
        "request": request,
        "modules": modules,
        "nb_modules": nb_modules,
        "nb_incomplets": nb_incomplets
    })

@router.post("/creer-fichiers")
async def creer_fichiers_manquants():
    fichiers = generer_composants_manquants()
    return RedirectResponse(url="/ia/dashboard", status_code=303)

@router.post("/organiser-composants", response_class=JSONResponse)
async def organiser_fichiers_et_modules():
    try:
        chemins_crees = organiser_et_structurer_modules()
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
        from pathlib import Path
        import json
        if not Path(chemin_fichier).exists():
            return JSONResponse(status_code=404, content={"message": "Fichier non trouvé"})
        with open(chemin_fichier, "r", encoding="utf-8") as f:
            contenu = json.load(f)
        return contenu
    except Exception as e:
        return JSONResponse(status_code=500, content={"erreur": str(e)})

@router.get("/historique-generation", response_model=list[dict])
def afficher_historique_generation():
    return lire_historique_generation()

@router.get("/suggestions-modules", response_model=str)
def suggestions_modules():
    return suggestion_markdown_modules()