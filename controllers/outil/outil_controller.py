from fastapi import APIRouter

router = APIRouter()

@router.get("/outil/test")
def test_rh():
    return {"message": "OUTIL OK"}