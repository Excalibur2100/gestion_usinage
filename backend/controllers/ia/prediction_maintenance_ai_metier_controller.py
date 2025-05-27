from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
from core.ia.prediction_engine import PredictionEngine

router = APIRouter(prefix="/predictions-ai-metier", tags=["Prédiction IA Métier"])

class PredictionRequest(BaseModel):
    type_prediction: str
    machine: str
    contexte: Optional[str] = None

@router.post("/generer")
def generer_prediction(data: PredictionRequest):
    return PredictionEngine.generer_prediction(
        type_prediction=data.type_prediction,
        machine=data.machine,
        contexte=data.contexte
    )