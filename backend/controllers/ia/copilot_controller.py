from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from openai import OpenAI
from config import OPENAI_API_KEY
import os

# Modèle de requête
class CopilotRequest(BaseModel):
    prompt: str
    model: str = "gpt-3.5-turbo"

# Modèle de réponse
class CopilotResponse(BaseModel):
    result: str

# Configuration client OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

router = APIRouter(prefix="/api/ia/copilot", tags=["Assistant IA"])

@router.post("/", response_model=CopilotResponse)
async def generate_code(data: CopilotRequest):
    """
    Appelle l'IA OpenAI avec un prompt et retourne le code généré.
    """
    try:
        response = client.chat.completions.create(
            model=data.model,
            messages=[
                {"role": "system", "content": "Tu es un assistant développeur Python expert."},
                {"role": "user", "content": data.prompt}
            ],
            temperature=0.2,
        )
        return {"result": response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur IA : {str(e)}")

client = OpenAI(api_key=OPENAI_API_KEY)
