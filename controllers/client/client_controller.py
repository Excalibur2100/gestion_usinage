from fastapi import APIRouter

router = APIRouter()

@router.get("/client/test")
def test_rh():
    return {"message": "CLIENT OK"}