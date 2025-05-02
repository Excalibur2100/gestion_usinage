from fastapi import APIRouter

router = APIRouter(prefix="/pointage", tags=["pointage"])

@router.get("/details")
async def get_pointage_details():
    return {"message": "Détails du pointage opérationnel"}