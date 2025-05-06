from fastapi import APIRouter

router = APIRouter(prefix="/stat_rh", tags=["stat_rh"])

@router.get("/details")
async def get_stat_rh_details():
    return {"message": "Détails des ressources humaines opérationnelles"}