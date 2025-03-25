from fastapi import APIRouter

router = APIRouter()

@router.get("/commande/test")
def test_rh():
    return {"message": "COMMANDE OK"}