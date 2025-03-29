from fastapi import APIRouter

router = APIRouter(prefix="/finance", tags=["RH"])

@router.get("/")
async def get_rh():
    return {"message": "Endpoint Finance opérationnel"}