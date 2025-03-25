from fastapi import APIRouter

router = APIRouter()

@router.get("/fournisseur/test")
def test_rh():
    return {"message": "FOURNISSEUR OK"}