import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_calcul_parametres_usinage():
    payload = {
        "longueur": 100,
        "largeur": 50,
        "hauteur": 20,
        "materiau": "acier",
        "operations": ["fraisage", "perçage"]
    }
    response = client.post("/usinage/calcul-parametres", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "brut" in data["data"]
    assert "passes" in data["data"]
    assert "vitesse_coupe" in data["data"]
    assert "temps_usinage" in data["data"]