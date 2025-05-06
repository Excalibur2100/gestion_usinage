import json
import shutil
from pathlib import Path
from fastapi import APIRouter, Request, Form, UploadFile
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

CONFIG_PATH = Path("config_metiers.json")

@router.get("/setup", response_class=HTMLResponse)
async def afficher_setup(request: Request):
    return templates.TemplateResponse("setup_templates/setup_template.html", {"request": request})


@router.post("/setup", response_class=HTMLResponse)
async def enregistrer_metiers(
    request: Request,
    metiers: list[str] = Form(...),
    logo: UploadFile = Form(None)
):
    config_data = {
        "metiers_actifs": metiers,
        "setup_complet": True
    }

    # ✅ Créer le dossier au besoin
    Path("static/images").mkdir(parents=True, exist_ok=True)

    # ✅ Sauvegarder le logo s'il a bien été uploadé
    if logo and logo.filename and logo.file:
        try:
            logo_path = Path("static/images/logo_client.png")
            with open(logo_path, "wb") as buffer:
                shutil.copyfileobj(logo.file, buffer)
            config_data["logo_path"] = str(logo_path)
        except Exception as e:
            print(f"Erreur lors de l'enregistrement du logo : {e}")

    # ✅ Enregistrer la configuration
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(config_data, f, indent=4)

    return RedirectResponse(url="/", status_code=303)
