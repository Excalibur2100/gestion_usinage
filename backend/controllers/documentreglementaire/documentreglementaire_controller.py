from fastapi import APIRouter

router = APIRouter(prefix="/documentreglementaire", tags=["documentreglementaire"])

@router.get("/")
async def get_documentreglementaire():
    return {"message": "Document réglementaire opérationnel"}