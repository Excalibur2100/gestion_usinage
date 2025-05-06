from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/planning_employes", response_class=HTMLResponse)
async def afficher_planning_employes(request: Request):
    return templates.TemplateResponse("planningemploye_templates/planning_employe_template.html", {
        "request": request,
        "employes": [
            {"nom": "Alice", "poste": "Tourneur", "creneau": "08h - 16h"},
            {"nom": "Bob", "poste": "Fraiseur", "creneau": "14h - 22h"},
        ]
    })
