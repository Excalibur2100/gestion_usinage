from fastapi import APIRouter

router = APIRouter(prefix="/stat_production", tags=["stat_production"])

@router.get("/details")
async def get_stat_production_details():
    return {"message": "Détails de la production opérationnelle"}