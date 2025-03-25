from fastapi import APIRouter

router = APIRouter()

@router.get("/maintenance/test")
def test_rh():
    return {"message": "MAINTENANCE OK"}