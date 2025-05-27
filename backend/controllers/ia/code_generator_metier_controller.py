from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from core.ia.code_generator_engine import CodeGeneratorEngine

router = APIRouter(prefix="/code-generator-metier", tags=["Code Generator Métier"])

class CodeRequest(BaseModel):
    prompt: str
    langage: str = "python"
    modele: str = "gpt-4"

class CodeValidationRequest(BaseModel):
    code: str

@router.post("/generer")
def generer_code(data: CodeRequest):
    code = CodeGeneratorEngine.generer_code_depuis_prompt(data.prompt, data.langage, data.modele)
    return {"code_genere": code}

@router.post("/valider")
def valider_code(data: CodeValidationRequest):
    valide = CodeGeneratorEngine.valider_code(data.code)
    return {"valide": valide}