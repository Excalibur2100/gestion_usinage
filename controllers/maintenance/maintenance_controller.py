from fastapi import APIRouter

router = APIRouter()

@router.get("/maintenance")
async def get_utilisateurs():
    return {"message": "Liste des maintenance"}