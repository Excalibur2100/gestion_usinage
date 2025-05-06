from fastapi import APIRouter

router = APIRouter(prefix="/document_qualite", tags=["document_qualite"])

@router.get("/")
async def get_document_qualite():
    return {"message": "Document Qualité opérationnel"}