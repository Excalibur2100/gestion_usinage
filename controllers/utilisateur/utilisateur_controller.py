from fastapi import APIRouter

router = APIRouter()

@router.get("/utilisateur/test")
def test_utilisateur():
    return {"message": "utilisateur ok"}