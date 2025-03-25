from fastapi import APIRouter

router = APIRouter()

@router.get("/rh/test")
def test_rh():
    return {"message": "RH OK"}