from fastapi import APIRouter

router = APIRouter(prefix="/instrument_controle", tags=["instrument_controle"])

@router.get("/")
async def get_instrument_controle():
    return {"message": "Instrument Contrôle opérationnel"}