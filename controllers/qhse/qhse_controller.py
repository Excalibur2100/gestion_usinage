from fastapi import APIRouter

router = APIRouter(prefix="/qhse", tags=["qhse"])

@router.get("/details")
async def get_qhse_details():
    return {"message": "Détails du programme QHSE opérationnel"}