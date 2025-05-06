from fastapi import APIRouter

router = APIRouter(prefix="/tracabilite", tags=["tracabilite"])

@router.get("/details")
async def get_tracabilite_details():
    return {"message": "Détails la tracabilité"}