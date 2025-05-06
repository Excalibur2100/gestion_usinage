from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from pathlib import Path

class UCLTemplates(Jinja2Templates):
    def TemplateResponse(self, name: str, context: dict, *args, **kwargs):
        logo_path = Path("static/images/logo_client.png")
        context["logo_url"] = "/static/images/logo_client.png" if logo_path.exists() else None
        return super().TemplateResponse(name, context, *args, **kwargs)

# Utilisation unique dans toute l'app
templates = UCLTemplates(directory="templates")
