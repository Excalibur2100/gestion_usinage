from fastapi import APIRouter

router = APIRouter(prefix="/ligne_facture", tags=["ligne_facture"])

@router.get("/")
async def get_ligne_facture():
    return {"message": "Ligne Facture opérationnelle"}