from fastapi import APIRouter, Request
from core.templates import templates
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def global_dashboard(request: Request):
    return templates.TemplateResponse("global_dashboard.html", {"request": request})
