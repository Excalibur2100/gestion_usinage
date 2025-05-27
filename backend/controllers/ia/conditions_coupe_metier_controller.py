from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from core.ia.conditions_coupe_engine import ConditionsCoupeEngine
from backend.db.models.database import get_db

router = APIRouter(prefix="/conditions-coupe-metier", tags=["Conditions de Coupe Métier"])

# -----------------------
# SCHÉMAS D’ENTRÉE
# -----------------------

class CalculRPMRequest(BaseModel):
    vitesse_coupe: float
    diametre_outil: float

class CalculVfRequest(BaseModel):
    avance_dent: float
    n_rpm: float
    nb_dents: int

class SuggestionRequest(BaseModel):
    operation: str
    materiau: str

class OutilOptimalRequest(BaseModel):
    operation: str
    materiau: str

# -----------------------
# ROUTES MÉTIER
# -----------------------

@router.post("/calcul-rpm")
def calculer_n_rpm(data: CalculRPMRequest):
    """
    Calcule la vitesse de rotation (rpm) à partir de la vitesse de coupe et du diamètre outil.
    """
    try:
        n = ConditionsCoupeEngine.calculer_n_rpm(data.vitesse_coupe, data.diametre_outil)
        return {"rpm": n}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/calcul-vf")
def calculer_vf(data: CalculVfRequest):
    """
    Calcule l'avance en mm/min (Vf) en fonction de fz, rpm et nombre de dents.
    """
    try:
        vf = ConditionsCoupeEngine.calculer_avance_par_minute(data.avance_dent, data.n_rpm, data.nb_dents)
        return {"avance_mm_min": vf}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/recommander")
def recommander_conditions(data: SuggestionRequest):
    """
    Recommande des conditions de coupe Vc / Fz / ap en fonction de l'opération et du matériau.
    """
    resultat = ConditionsCoupeEngine.recommander_conditions(data.operation, data.materiau)
    if not resultat:
        raise HTTPException(status_code=404, detail="Aucune recommandation trouvée.")
    return resultat

@router.post("/outils-optimaux")
def get_outil_optimal(data: OutilOptimalRequest, db: Session = Depends(get_db)):
    """
    Recherche un outil adapté en base ou suggéré par l'IA en fonction de l’opération et du matériau.
    """
    result = ConditionsCoupeEngine.get_outil_optimal(
        operation=data.operation,
        materiau=data.materiau,
        db=db
    )
    if result.get("source") == "aucune donnée":
        raise HTTPException(status_code=404, detail=result["message"])
    return result