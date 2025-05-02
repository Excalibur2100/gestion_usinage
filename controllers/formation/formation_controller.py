from fastapi import APIRouter

router = APIRouter(prefix="/formation", tags=["formation"])

@router.get("/details")
async def get_formation_details():
    return {"message": "Detailed information about Document formation opérationnel"}