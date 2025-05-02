from fastapi import APIRouter

router = APIRouter(prefix="/documentrh", tags=["documentrh"])

@router.get("/details")
async def get_documentrh_details():
    return {"message": "Document RH opérationnel"}