from fastapi import APIRouter

router = APIRouter(prefix="/devis", tags=["RH"])

@router.get("/")
async def get_rh():
    return {"message": "Endpoint devis opérationnel"}