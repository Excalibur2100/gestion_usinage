from fastapi import APIRouter

router = APIRouter()

@router.get("/machine/test")
def test_rh():
    return {"message": "MACHINE OK"}