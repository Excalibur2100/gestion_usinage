from fastapi import APIRouter

router = APIRouter(prefix="/documentqhse", tags=["documentqhse"])

@router.get("/")
async def get_documentqhse():
    return {"message": "Document QHSE opérationnel"}