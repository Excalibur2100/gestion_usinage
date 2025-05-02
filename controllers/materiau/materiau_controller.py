
from fastapi import APIRouter

router = APIRouter(prefix="/materiau", tags=["materiaux"])

@router.get("/")
async def get_rh():
    return {"message": "Endpoint matériau opérationnel"}