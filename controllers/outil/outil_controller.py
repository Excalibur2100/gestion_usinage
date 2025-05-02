
from fastapi import APIRouter

router = APIRouter(prefix="/outil", tags=["outil"])

@router.get("/details")
async def get_outil():
    return {"message": "Endpoint outil opérationnel"}