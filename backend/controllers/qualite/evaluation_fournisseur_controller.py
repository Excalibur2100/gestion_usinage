from fastapi import APIRouter

router = APIRouter(prefix="/evaluation_fournisseur", tags=["evaluation_fournisseur"])

@router.get("/")
async def get_documentevaluation_fournisseur():
    return {"message": "Document évaluation fournisseur opérationnel"}