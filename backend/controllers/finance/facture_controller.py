from fastapi import APIRouter

router = APIRouter(prefix="/facture", tags=["facture"])

@router.get("/")
async def get_document_facture():
    return {"message": "Document facture opérationnel"}