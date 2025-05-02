from fastapi import APIRouter

router = APIRouter(prefix="/finance", tags=["finance"])

@router.get("/details")
async def get_finance_details():
    return {"message": "Detailed information about Finance opérationnel"}