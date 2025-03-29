
from fastapi import APIRouter

router = APIRouter(prefix="/outil", tags=["RH"])

@router.get("/")
async def get_rh():
    return {"message": "Endpoint outil opérationnel"}