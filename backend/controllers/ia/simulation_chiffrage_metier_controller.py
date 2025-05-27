from fastapi import APIRouter
from pydantic import BaseModel
from core.ia.simulation_chiffrage_engine import SimulationChiffrageEngine

router = APIRouter(prefix="/simulations-chiffrage-metier", tags=["Simulation Chiffrage Métier"])

class SimulationChiffrageRequest(BaseModel):
    scenario: str
    complexite: str = "moyenne"  # "faible", "moyenne", "élevée"

@router.post("/generer")
def generer_chiffrage_simule(data: SimulationChiffrageRequest):
    return SimulationChiffrageEngine.simuler_chiffrage(
        scenario=data.scenario,
        complexite=data.complexite
    )