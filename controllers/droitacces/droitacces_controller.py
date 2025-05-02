from fastapi import APIRouter

router = APIRouter(prefix="/droitacces", tags=["droitacces"])

@router.get("/")
async def get_documentdroitacces():
    return {"message": "Document droit d'accès opérationnel"}