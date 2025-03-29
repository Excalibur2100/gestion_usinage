from fastapi import APIRouter

router = APIRouter(prefix="/piece", tags=["RH"])

@router.get("/")
async def get_rh():
    return {"message": "Endpoint pièce opérationnel"}