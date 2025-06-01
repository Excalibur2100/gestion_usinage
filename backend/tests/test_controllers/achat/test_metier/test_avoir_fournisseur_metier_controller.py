import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_api_calcul_montant_ttc():
    response = client.get("/api/v1/metier/avoirs-fournisseur/calcul-montant-ttc", params={"ht": 100, "tva": 20})
    assert response.status_code == 200
    assert float(response.json()) == 120.0


def test_api_detect_type():
    response = client.get("/api/v1/metier/avoirs-fournisseur/detect-type", params={"reference": "RET-001", "motif": "retour de marchandise"})
    assert response.status_code == 200
    assert response.json() in ["retour_marchandise", "remise_commerciale", "geste_commercial", "autre"]


def test_api_suggere_avoir_auto():
    response = client.get(
        "/api/v1/metier/avoirs-fournisseur/suggere-auto",
        params={"reference": "AVF-AUTO-001", "fournisseur_id": 1, "montant_ht": 100, "taux_tva": 20}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["reference"] == "AVF-AUTO-001"
    assert data["fournisseur_id"] == 1
    assert float(data["montant_ht"]) == 100.0
    assert float(data["montant_ttc"]) == 120.0
    assert data["statut"] == "brouillon"