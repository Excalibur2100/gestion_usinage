# controllers/assistant_ia_controller.py

from fastapi import APIRouter
from services.ia.assistant_ia_service import analyse_module_status, IAResponse

router = APIRouter(prefix="/assistant-ia", tags=["Assistant IA"])

@router.post("/analyse-modules", response_model=IAResponse)
def analyse_modules(modules: list[dict]):
    return analyse_module_status(modules)