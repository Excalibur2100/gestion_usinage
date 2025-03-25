from fastapi import APIRouter

router = APIRouter()

@router.get("/epi/test")
def test_rh():
    return {"message": "EPI OK"}