from fastapi import APIRouter
from pydantic import BaseModel
from core.ia.optimisation_engine import OptimisationEngine

router = APIRouter(prefix="/optimisations-ai-metier", tags=["Optimisation IA Métier"])

class OptimisationRequest(BaseModel):
    operation: str
    duree_actuelle: float
    machine: str

@router.post("/generer")
def generer_optimisation(data: OptimisationRequest):
    result = OptimisationEngine.generer_recommandation(
        operation=data.operation,
        duree_actuelle=data.duree_actuelle,
        machine=data.machine
    )
    return result