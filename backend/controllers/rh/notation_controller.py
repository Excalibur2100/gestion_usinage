
from fastapi import APIRouter

router = APIRouter(prefix="/notation_rh", tags=["notation_rh"])

@router.get("/")
async def get_notation_rh():
    return {"message": "Endpoint notation RH opérationnel"}