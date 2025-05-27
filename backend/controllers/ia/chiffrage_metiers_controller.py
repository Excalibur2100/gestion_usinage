from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from io import BytesIO

from backend.db.models.database import get_db
from db.schemas.ia.chiffrage_metiers_schemas import (
    ChiffrageSimpleRequest, ChiffrageCompletRequest, ChiffrageIntelligentRequest
)
from services.ia.chiffrage_metier_service import (
    calculer_cout_total, chiffrage_complet, chiffrage_intelligent
)

router = APIRouter(prefix="/chiffrage-metier", tags=["Chiffrage Métier"])

@router.post("/calcul-cout-total")
def route_cout_total(data: ChiffrageSimpleRequest):
    try:
        total = calculer_cout_total(data)
        return {"cout_total": total}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/calcul-complet")
def route_complet(data: ChiffrageCompletRequest):
    try:
        return chiffrage_complet(data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/intelligent")
def route_chiffrage_ai(data: ChiffrageIntelligentRequest, db: Session = Depends(get_db)):
    try:
        return chiffrage_intelligent(data, db)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/export")
def route_export(data: ChiffrageIntelligentRequest, db: Session = Depends(get_db)):
    try:
        result = chiffrage_intelligent(data, db)
        buffer = BytesIO()
        buffer.write(result["resume"].encode("utf-8"))
        buffer.seek(0)
        return StreamingResponse(
            buffer,
            media_type="application/octet-stream",
            headers={"Content-Disposition": f"attachment; filename=chiffrage_piece_{data.piece_id}.txt"}
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))