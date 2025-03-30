from db.models.database import SessionLocal
from db.models import AnalyseFichier
import pdfplumber
import ezdxf
from fastapi import UploadFile
#from OCC.Core.STEPControl import STEPControl_Reader
#from OCC.Core.IFSelect import IFSelect_RetDone


def sauvegarder_resultat(type_fichier, contenu):
    db = SessionLocal()
    resultat = AnalyseFichier(type_fichier=type_fichier, contenu=contenu)
    db.add(resultat)
    db.commit()
    db.refresh(resultat)
    return resultat

def analyser_fichier(fichier):
    extension = fichier.filename.split(".")[-1].lower()

    if extension == "pdf":
        return analyser_pdf(fichier)
#    elif extension == "dxf":
#        return analyser_dxf(fichier)
    elif extension in ["step", "stp"]:
        raise ValueError("Les fichiers STEP ne sont pas encore pris en charge")
#    elif extension in ["step", "stp"]:
#        return analyser_step(fichier)
    else:
        raise ValueError(f"Format de fichier non supporté : {extension}")

def analyser_pdf(fichier: UploadFile) -> dict:
    try:
        with pdfplumber.open(fichier.file) as pdf:
            contenu = ""
            for page in pdf.pages:
                contenu += page.extract_text() or ""
            return {"type": "pdf", "contenu": contenu.strip()}
    except Exception as e:
        raise ValueError(f"Erreur lors de l'analyse du fichier PDF : {str(e)}")

#def analyser_fichier(fichier):
#    extension = fichier.filename.split(".")[-1].lower()
#
#    if extension not in ["pdf", "dxf"]:
#        raise ValueError(f"Format de fichier non supporté : {extension}")
#
#    if extension == "pdf":
#        return analyser_pdf(fichier)
#    elif extension == "dxf":
#        return analyser_dxf(fichier)

#def analyser_step(fichier):
#    reader = STEPControl_Reader()
#    status = reader.ReadFile(fichier.file.name)
#    if status != IFSelect_RetDone:
#        raise ValueError("Erreur lors de la lecture du fichier STEP")
#
#    reader.TransferRoots()
#    shape = reader.OneShape()
#    return {"type": "step", "shape": str(shape)}
