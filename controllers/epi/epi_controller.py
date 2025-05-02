from fastapi import APIRouter

router = APIRouter(prefix="/epi", tags=["epi"])

@router.get("/")
async def get_documentepi():
    return {"message": "Document epi opérationnel"}