from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from db.schemas.schemas import PieceUsinage
from services.usinage.usinage_service import calculer_parametres_usinage
from db.models.database import get_db

router = APIRouter()

@router.post("/calcul-parametres")
def calcul_parametres_usinage(piece: PieceUsinage, db: Session = Depends(get_db)):
    try:
        resultats = calculer_parametres_usinage(piece)
        return resultats
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))