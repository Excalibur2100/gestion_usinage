from fastapi import APIRouter, Request
from core.templates import templates
from fastapi.responses import HTMLResponse

router = APIRouter()

# Données simulées
fake_modules = [
    {"nom": "production", "chemins_trouves": ["controller", "template", "model"]},
    {"nom": "rh", "chemins_trouves": ["controller"]}
]

fake_logs = [
    {
        "timestamp": "2025-05-04 16:32",
        "fichiers_crees": ["controller/rh_controller.py", "templates/rh_templates/contrat_template.html"]
    }
]

@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard_templates/dashboard.html", {
        "request": request,
        "nb_modules": len(fake_modules),
        "nb_incomplets": sum(1 for m in fake_modules if len(m["chemins_trouves"]) < 3),
        "composants": fake_modules,
        "logs": fake_logs
    })
