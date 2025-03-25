from fastapi import APIRouter

router = APIRouter()

@router.get("/finance/test")
def test_rh():
    return {"message": "FINANCE OK"}