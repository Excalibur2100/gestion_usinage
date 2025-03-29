import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_analyser_pdf():
    with open("tests/samples/sample.pdf", "rb") as fichier:
        response = client.post("/analyse-fichier/", files={"fichier": ("sample.pdf", fichier, "application/pdf")})
        assert response.status_code == 200
        data = response.json()
        assert data["data"]["type"] == "pdf"

def test_analyser_dxf():
    with open("tests/samples/sample.dxf", "rb") as fichier:
        response = client.post("/analyse-fichier/", files={"fichier": ("sample.dxf", fichier, "application/dxf")})
        assert response.status_code == 200
        data = response.json()
        assert data["data"]["type"] == "dxf"

def test_analyser_step():
    with open("tests/samples/sample.step", "rb") as fichier:
        response = client.post("/analyse-fichier/", files={"fichier": ("sample.step", fichier, "application/step")})
        assert response.status_code == 200
        data = response.json()
        assert data["data"]["type"] == "step"