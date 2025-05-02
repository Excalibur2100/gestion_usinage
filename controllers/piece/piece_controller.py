from fastapi import APIRouter

router = APIRouter(prefix="/piece", tags=["piece"])

@router.get("/details")
async def get_piece_details():
    return {"message": "Endpoint pièce opérationnel"}