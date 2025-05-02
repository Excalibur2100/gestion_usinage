from fastapi import APIRouter, UploadFile, HTTPException
from services.ia.analyse_fichier_service import analyser_fichier

router = APIRouter(prefix="/analyse-fichier", tags=["Analyse Fichier"])

@router.post("/")
async def analyser_fichier_endpoint(fichier: UploadFile):
    try:
        resultat = analyser_fichier(fichier)
        return {"status": "success", "data": resultat}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.post("/", summary="Analyser un fichier", description="Analyse un fichier PDF ou DXF et retourne son contenu.")
async def analyser_fichier_endpoint(fichier: UploadFile):
    """
    Analyse un fichier PDF ou DXF et retourne son contenu.

    - **fichier** : Le fichier à analyser.
    """
    try:
        resultat = analyser_fichier(fichier)
        return {"status": "success", "data": resultat}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))