from fastapi import APIRouter

router = APIRouter()

@router.get("/materiau/test")
def test_rh():
    return {"message": "MATERIAU OK"}