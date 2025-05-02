from fastapi import APIRouter

router = APIRouter(prefix="/epi_utilisateur", tags=["epi_utilisateur"])

@router.get("/")
async def get_documentepi_utilisateur():
    return {"message": "Document utilisateur opérationnel"}