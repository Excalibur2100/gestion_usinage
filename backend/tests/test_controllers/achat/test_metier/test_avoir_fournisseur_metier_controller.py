# backend/tests/test_metier/achat/test_avoir_fournisseur_metier_controller.py

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_api_calcul_montant_ttc():
    response = client.get("/api/v1/metier/avoirs-fournisseur/calcul-montant-ttc", params={"ht": 100, "tva": 20})
    assert response.status_code == 200
    assert float(response.json()) == 120.0


@pytest.mark.parametrize("reference,motif,expected_type", [
    ("RET-001", "retour produit", "retour_marchandise"),
    ("REM-2024", "remise exceptionnelle", "remise_commerciale"),
    ("GESTE-01", "geste client", "geste_commercial"),
    ("XXXX", "autre", "autre"),
])
def test_api_detect_type(reference, motif, expected_type):
    response = client.get("/api/v1/metier/avoirs-fournisseur/detect-type", params={"reference": reference, "motif": motif})
    assert response.status_code == 200
    assert response.json() == expected_type


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