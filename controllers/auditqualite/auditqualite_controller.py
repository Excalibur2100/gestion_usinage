from fastapi import APIRouter

router = APIRouter(prefix="/audit_qualite", tags=["audit_qualite"])

@router.get("/details")
async def get_audit_qualite_details():
    return {"message": "Détails de l'audit qualité opérationnel"}