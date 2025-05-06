
from fastapi import APIRouter

router = APIRouter(prefix="/non_conformite", tags=["non_conformite"])

@router.get("/")
async def get_non_conformite():
    return {"message": "Endpoint non conformité opérationnel"}