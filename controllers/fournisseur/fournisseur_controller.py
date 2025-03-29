from fastapi import APIRouter

router = APIRouter(prefix="/fournisseur", tags=["RH"])

@router.get("/")
async def get_rh():
    return {"message": "Endpoint fournisseur opérationnel"}