from fastapi import APIRouter

router = APIRouter(prefix="/maintenance", tags=["maintenance"])

@router.get("/")
async def get_maintenance():
    return {"message": "Liste des maintenances"}