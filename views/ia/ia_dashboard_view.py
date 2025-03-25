from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from services.ia.assistant_ia_service import analyser_composants_modules
from fastapi.responses import RedirectResponse
from services.ia.assistant_ia_service import generer_composants_manquants

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/ia/dashboard", response_class=HTMLResponse)
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


@router.post("/ia/creer-fichiers")
async def creer_fichiers_manquants():
    fichiers = generer_composants_manquants()
    return RedirectResponse(url="/ia/dashboard", status_code=303)