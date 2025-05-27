from fastapi import APIRouter
from pydantic import BaseModel
from core.ia.assistant_engine import AssistantEngine

router = APIRouter(prefix="/assistants-ia-metier", tags=["Assistant IA Métier"])

class PromptRequest(BaseModel):
    prompt: str
    moteur: str = "gpt-4"
    temperature: float = 0.7

@router.post("/generer")
def generer(data: PromptRequest):
    reponse = AssistantEngine.generer_reponse(data.prompt, data.moteur, data.temperature)
    return {"prompt": data.prompt, "reponse": reponse}