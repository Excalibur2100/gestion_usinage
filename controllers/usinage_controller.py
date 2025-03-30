from fastapi import APIRouter, HTTPException
from db.schemas.schemas import PieceUsinage
from services.usinage.usinage_service import calculer_parametres_usinage

router = APIRouter(prefix="/usinage", tags=["Usinage"])

@router.post("/calcul-parametres")
def calcul_parametres_usinage(piece: PieceUsinage):
    try:
        resultats = calculer_parametres_usinage(
            piece.model_dump(),
            piece.outils_disponibles,  # Accès corrigé
            piece.machines_disponibles  # Accès corrigé
        )
        return {"status": "success", "data": resultats}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))