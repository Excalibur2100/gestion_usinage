from fastapi import APIRouter

router = APIRouter()

@router.get("/robotique/test")
def test_rh():
    return {"message": "ROBOTIQUE OK"}