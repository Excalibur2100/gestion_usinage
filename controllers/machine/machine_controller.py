from fastapi import APIRouter

router = APIRouter(prefix="/machine", tags=["RH"])

@router.get("/")
async def get_rh():
    return {"message": "Endpoint machine opérationnel"}