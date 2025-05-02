from fastapi import APIRouter

router = APIRouter(prefix="/gamme_production", tags=["gamme_production"])

@router.get("/details")
async def get_gamme_production_details():
    return {"message": "Detailed information about Document Qgamme_production opérationnel"}