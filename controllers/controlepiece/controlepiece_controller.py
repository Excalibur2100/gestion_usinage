from fastapi import APIRouter

router = APIRouter(prefix="/controle_piece", tags=["controle_piece"])

@router.get("/details")
async def get_controle_piece_details():
    return {"message": "Détails de la pièce de contrôle opérationnel"}