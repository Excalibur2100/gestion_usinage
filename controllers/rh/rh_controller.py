
from fastapi import APIRouter

router = APIRouter(prefix="/rh", tags=["RH"])

@router.get("/")
async def get_rh():
    return {"message": "Endpoint RH opérationnel"}
