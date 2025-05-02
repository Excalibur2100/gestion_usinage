from fastapi import APIRouter

router = APIRouter(prefix="/droit", tags=["droit"])

@router.get("/")
async def get_documentdroit():
    return {"message": "Document droit opérationnel"}