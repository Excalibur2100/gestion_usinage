import pdfplumber
import ezdxf
from OCC.Core.STEPControl import STEPControl_Reader
from OCC.Core.IFSelect import IFSelect_RetDone

def analyser_fichier(fichier):
    extension = fichier.filename.split(".")[-1].lower()

    if extension == "pdf":
        return analyser_pdf(fichier)
    elif extension == "dxf":
        return analyser_dxf(fichier)
    elif extension in ["step", "stp"]:
        return analyser_step(fichier)
    else:
        raise ValueError(f"Format de fichier non supporté : {extension}")

def analyser_pdf(fichier):
    with pdfplumber.open(fichier.file) as pdf:
        texte = ""
        for page in pdf.pages:
            texte += page.extract_text()
        return {"type": "pdf", "contenu": texte}

def analyser_dxf(fichier):
    doc = ezdxf.readfile(fichier.file)
    entites = []
    for entity in doc.modelspace():
        entites.append({
            "type": entity.dxftype(),
            "layer": entity.dxf.layer,
            "points": getattr(entity, "points", None)
        })
    return {"type": "dxf", "entites": entites}

def analyser_step(fichier):
    reader = STEPControl_Reader()
    status = reader.ReadFile(fichier.file.name)
    if status != IFSelect_RetDone:
        raise ValueError("Erreur lors de la lecture du fichier STEP")

    reader.TransferRoots()
    shape = reader.OneShape()
    return {"type": "step", "shape": str(shape)}