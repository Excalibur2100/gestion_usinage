import pytest
from fastapi.testclient import TestClient
from main import app
from fastapi import UploadFile
from services.ia.analyse_fichier_service import analyser_fichier

client = TestClient(app)

def test_analyser_pdf():
    with open("tests/samples/sample.pdf", "rb") as fichier:
        fichier_upload = UploadFile(filename="sample.pdf", file=fichier)
        resultat = analyser_fichier(fichier_upload)
        assert resultat["type"] == "pdf"
        assert "contenu" in resultat

# def test_analyser_dxf():
#     with open("tests/samples/sample.dxf", "rb") as fichier:
#         response = client.post("/analyse-fichier/", files={"fichier": ("sample.dxf", fichier, "application/dxf")})
#         assert response.status_code == 200
#         data = response.json()
#         assert data["data"]["type"] == "dxf"

# def test_analyser_step():
#     with open("tests/samples/sample.step", "rb") as fichier:
#         response = client.post("/analyse-fichier/", files={"fichier": ("sample.step", fichier, "application/step")})
#         assert response.status_code == 200
#         data = response.json()