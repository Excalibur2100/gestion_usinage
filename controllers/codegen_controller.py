# controllers/codegen_controller.py

from fastapi import APIRouter
from services.ia.code_generator_service import generate_code, CodeGenRequest, CodeGenResponse

router = APIRouter(prefix="/codegen", tags=["Générateur de code"])

@router.post("/generate", response_model=CodeGenResponse)
def create_code(request: CodeGenRequest):
    return generate_code(request)