from fastapi import APIRouter

router = APIRouter(prefix="/commande", tags=["RH"])

@router.get("/")
async def get_rh():
    return {"message": "Endpoint Commande opérationnel"}