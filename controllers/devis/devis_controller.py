from fastapi import APIRouter

router = APIRouter()

@router.get("/devis/test")
def test_rh():
    return {"message": "DEVIS OK"}