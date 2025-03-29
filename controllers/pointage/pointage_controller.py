from fastapi import APIRouter

router = APIRouter(prefix="/pointage", tags=["RH"])

@router.get("/")
async def get_rh():
    return {"message": "Endpoint pointage opérationnel"}