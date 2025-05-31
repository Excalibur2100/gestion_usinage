import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_api_calcul_montant_ttc():
    response = client.get("/api/v1/metier/avoirs-fournisseur/calcul-montant-ttc?ht=100&tva=20")
    assert response.status_code == 200
    assert response.json() == 120.0

def test_api_detect_type():
    response = client.get("/api/v1/metier/avoirs-fournisseur/detect-type?motif=geste commercial")
    assert response.status_code == 200
    assert response.json() == "geste"

def test_api_suggere_auto():
    response = client.get("/api/v1/metier/avoirs-fournisseur/suggere-auto?facture_id=456&montant=240&raison=remise")
    assert response.status_code == 200
    data = response.json()
    assert data["montant_ttc"] == 240
    assert data["type_avoir"] == "remise"