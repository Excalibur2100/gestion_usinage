import pytest
from fastapi.testclient import TestClient
from main import app
from datetime import datetime

client = TestClient(app)


def test_api_calcul_montant_ttc():
    response = client.get("/api/v1/metier/factures-fournisseur/calcul-montant-ttc", params={"ht": 100, "tva": 20})
    assert response.status_code == 200
    assert float(response.json()) == 120.0


def test_api_generer_numero_facture_auto():
    response = client.get("/api/v1/metier/factures-fournisseur/generer-numero")
    assert response.status_code == 200
    numero = response.json()
    assert numero.startswith("FACT-AUTO-")
    assert isinstance(numero, str)


def test_api_statut_auto_retard():
    date_passée = (datetime.utcnow().replace(microsecond=0)).isoformat()
    response = client.get("/api/v1/metier/factures-fournisseur/statut-auto", params={"date_echeance": date_passée})
    assert response.status_code == 200
    assert response.json()["statut"] in ["en_retard", "brouillon"]


def test_api_suggere_facture_auto():
    response = client.get(
        "/api/v1/metier/factures-fournisseur/suggere-auto",
        params={
            "fournisseur_id": 1,
            "montant_ht": 100.0,
            "taux_tva": 20.0,
            "devise": "EUR",
            "reference": "FACT-IA-TEST"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["fournisseur_id"] == 1
    assert float(data["montant_ht"]) == 100.0
    assert float(data["montant_ttc"]) == 120.0
    assert data["statut"] in ["en_retard", "brouillon"]
    assert data["devise"] == "EUR"
    assert data["numero_facture"].startswith("FACT-AUTO-")