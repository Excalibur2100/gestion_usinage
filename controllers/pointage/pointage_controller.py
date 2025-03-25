from fastapi import APIRouter

router = APIRouter()

@router.get("/pointage/test")
def test_rh():
    return {"message": "POINTAGE OK"}