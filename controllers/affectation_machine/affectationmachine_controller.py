from fastapi import APIRouter

router = APIRouter(prefix="/affectation_machine", tags=["affectation_machine"])

@router.get("/details")
async def get_affectation_machine_details():
    return {"message": "Détails de l'affectation machine opérationnel"}