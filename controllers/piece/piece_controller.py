from fastapi import APIRouter

router = APIRouter()

@router.get("/piece/test")
def test_rh():
    return {"message": "PIECE OK"}