from fastapi import APIRouter

router = APIRouter(prefix="/absence", tags=["absence"])

@router.get("/details")
async def get_absence_details():
    return {"message": "Détails de l'absence opérationnel"}