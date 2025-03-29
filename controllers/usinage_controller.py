from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.usinage.usinage_service import calculer_parametres_usinage

router = APIRouter(prefix="/usinage", tags=["Usinage"])

class PieceData(BaseModel):
    longueur: float
    largeur: float
    hauteur: float
    materiau: str
    operations: list[str]  # Exemple : ["fraisage", "perçage"]

@router.post("/calcul-parametres")
def calculer_parametres(piece: PieceData):
    try:
        resultats = calculer_parametres_usinage(piece.dict())
        return {"status": "success", "data": resultats}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))