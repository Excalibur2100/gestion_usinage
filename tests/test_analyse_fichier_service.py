import pytest
from services.ia.analyse_fichier_service import analyser_fichier
from fastapi import UploadFile
from io import BytesIO

def test_analyser_pdf():
    with open("tests/samples/sample.pdf", "rb") as fichier:
        fichier_upload = UploadFile(filename="sample.pdf", file=fichier)
        resultat = analyser_fichier(fichier_upload)
        assert resultat["type"] == "pdf"
        assert "contenu" in resultat

#def test_analyser_dxf():
#    fichier = UploadFile(filename="test.dxf", file=BytesIO(b"Dummy DXF content"))
#    with pytest.raises(Exception):  # Si le contenu DXF est invalide
#        analyser_fichier(fichier)
