from fastapi import APIRouter, Request, Form
from core.templates import templates
from fastapi.responses import HTMLResponse

router = APIRouter()
#templates = Jinja2Templates(directory="templates")

@router.get("/chiffrage", response_class=HTMLResponse)
async def form_chiffrage(request: Request):
    return templates.TemplateResponse("chiffrage_templates/chiffrage_template.html", {"request": request})

@router.post("/chiffrage/calculer", response_class=HTMLResponse)
async def calcul_chiffrage(
    request: Request,
    matiere: float = Form(...),
    machine: float = Form(...),
    taux_machine: float = Form(...),
    main_oeuvre: float = Form(...),
    taux_mo: float = Form(...)
):
    total = matiere + (machine * taux_machine) + (main_oeuvre * taux_mo)
    return templates.TemplateResponse("chiffrage_templates/chiffrage_template.html", {
        "request": request,
        "total": round(total, 2)
    })
