from fastapi import APIRouter

router = APIRouter(prefix="/client", tags=["RH"])

@router.get("/")
async def get_rh():
    return {"message": "client RH opérationnel"}