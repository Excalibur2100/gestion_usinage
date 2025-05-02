from fastapi import APIRouter

router = APIRouter(prefix="/historique_action", tags=["historique_action"])

@router.get("/details")
async def get_historique_action_details():
    return {"message": "Detailed information about Document historique action opérationnel"}