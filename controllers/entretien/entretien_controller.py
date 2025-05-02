from fastapi import APIRouter

router = APIRouter(prefix="/entretien", tags=["entretien"])

@router.get("/")
async def get_documententretien():
    return {"message": "Document entretien opérationnel"}