
from fastapi import APIRouter

router = APIRouter(prefix="/materiau", tags=["RH"])

@router.get("/")
async def get_rh():
    return {"message": "Endpoint matériau opérationnel"}