import json
from pathlib import Path
from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

CONFIG_PATH = Path("config_metiers.json")

METIERS_LIST = [
    ("usinage", "🛠️ Usinage"),
    ("soudure", "🔩 Soudure / Tuyauterie"),
    ("mecanique", "🔧 Mécanicien industriel"),
    ("assemblage", "⚙️ Montage / Assemblage"),
    ("controle", "📏 Contrôle qualité"),
    ("robotique", "🤖 Robotique / Maintenance"),
    ("logistique", "🚛 Logistique / Magasin"),
    ("chaudronnerie", "🏗️ Chaudronnerie"),
    ("electricite", "⚡ Électricité industrielle"),
    ("automatisme", "🎛️ Automatisme / régulation"),
    ("peinture", "🎨 Peinture industrielle"),
    ("maintenance", "🧰 Maintenance générale"),
    ("outillage", "🔧 Outillage / fabrication d’outils"),
    ("injection", "🧪 Plasturgie / Injection"),
    ("fonderie", "🏭 Fonderie / Forge"),
    ("decoupe", "✂️ Découpe laser / plasma"),
    ("pliage", "🔺 Pliage / Formage"),
]


@router.get("/parametres", response_class=HTMLResponse)
async def afficher_parametres(request: Request):
    metiers_actifs = []
    if CONFIG_PATH.exists():
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            config = json.load(f)
            metiers_actifs = config.get("metiers_actifs", [])

    return templates.TemplateResponse("parametres_templates/parametres_template.html", {

        "request": request,
        "metiers_actifs": metiers_actifs,
        "metiers_disponibles": METIERS_LIST
    })

@router.post("/parametres", response_class=HTMLResponse)
async def modifier_metiers(request: Request, metiers: list[str] = Form([])):
    config = {"setup_complet": True, "metiers_actifs": metiers}

    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4)

    return RedirectResponse(url="/", status_code=303)
