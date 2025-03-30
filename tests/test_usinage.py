import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# filepath: /home/excalibur/gestion_usinage/services/usinage_service.py
client = TestClient(app)

def test_calcul_parametres_usinage():
    payload = {
        "longueur": 100.0,
        "largeur": 50.0,
        "hauteur": 20.0,
        "materiau": "acier",
        "operations": ["fraisage", "perçage", "tournage", "taraudage", "alésage"],
        "outils": ["fraise", "foret", "outil de tournage", "taraud", "alésoir"],
        "outils_disponibles": ["fraise", "foret", "outil de tournage", "taraud", "alésoir"],
        "machines_disponibles": ["fraiseuse", "tour", "perceuse"]
    }
    response = client.post("/usinage/calcul-parametres", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "data" in data