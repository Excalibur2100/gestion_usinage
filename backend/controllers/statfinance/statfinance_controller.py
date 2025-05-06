from fastapi import APIRouter

router = APIRouter(prefix="/stat_finance", tags=["stat_finance"])

@router.get("/details")
async def get_stat_finance_details():
    return {"message": "Détails des finances opérationnelles"}