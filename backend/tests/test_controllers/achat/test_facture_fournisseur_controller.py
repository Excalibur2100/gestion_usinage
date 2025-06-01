import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_facture():
    payload = {
        "numero_facture": "FACT-TEST-001",
        "reference_externe": None,
        "fournisseur_id": 1,
        "montant_ht": 100.0,
        "taux_tva": 20.0,
        "montant_ttc": 120.0,
        "statut": "brouillon",
        "devise": "EUR"
    }
    response = client.post("/api/v1/factures-fournisseur/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["numero_facture"] == "FACT-TEST-001"
    assert float(data["montant_ttc"]) == 120.0

def test_list_factures():
    response = client.get("/api/v1/factures-fournisseur/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_facture_detail():
    creation = client.post("/api/v1/factures-fournisseur/", json={
        "numero_facture": "FACT-DETAIL-001",
        "reference_externe": None,
        "fournisseur_id": 1,
        "montant_ht": 200.0,
        "taux_tva": 10.0,
        "montant_ttc": 220.0,
        "statut": "brouillon",
        "devise": "EUR"
    })
    facture_id = creation.json()["id"]
    response = client.get(f"/api/v1/factures-fournisseur/{facture_id}")
    assert response.status_code == 200
    assert response.json()["numero_facture"] == "FACT-DETAIL-001"

def test_update_facture():
    creation = client.post("/api/v1/factures-fournisseur/", json={
        "numero_facture": "FACT-UPDATE-001",
        "reference_externe": None,
        "fournisseur_id": 1,
        "montant_ht": 150.0,
        "taux_tva": 20.0,
        "montant_ttc": 180.0,
        "statut": "brouillon",
        "devise": "EUR"
    })
    facture_id = creation.json()["id"]
    update_data = {
        "commentaire": "Mise à jour",
        "statut": "validee"
    }
    response = client.put(f"/api/v1/factures-fournisseur/{facture_id}", json=update_data)
    assert response.status_code == 200
    assert response.json()["commentaire"] == "Mise à jour"

def test_delete_facture():
    creation = client.post("/api/v1/factures-fournisseur/", json={
        "numero_facture": "FACT-DELETE-001",
        "reference_externe": None,
        "fournisseur_id": 1,
        "montant_ht": 90.0,
        "taux_tva": 10.0,
        "montant_ttc": 99.0,
        "statut": "brouillon",
        "devise": "EUR"
    })
    facture_id = creation.json()["id"]
    response = client.delete(f"/api/v1/factures-fournisseur/{facture_id}")
    assert response.status_code == 200
    assert "supprimée" in response.json()["detail"]

def test_search_factures():
    client.post("/api/v1/factures-fournisseur/", json={
        "numero_facture": "FACT-SEARCH-001",
        "reference_externe": None,
        "fournisseur_id": 1,
        "montant_ht": 50.0,
        "taux_tva": 10.0,
        "montant_ttc": 55.0,
        "statut": "brouillon",
        "devise": "EUR"
    })
    response = client.post("/api/v1/factures-fournisseur/search", json={
        "numero_facture": "FACT-SEARCH"
    })
    assert response.status_code == 200
    assert response.json()["total"] >= 1
    assert isinstance(response.json()["results"], list)

def test_export_csv_factures():
    response = client.get("/api/v1/factures-fournisseur/export")
    assert response.status_code == 200
    assert "text/csv" in response.headers["content-type"]
    assert "attachment;" in response.headers["content-disposition"]

def test_bulk_create_and_delete_factures():
    payload = {
        "factures": [
            {
                "numero_facture": f"FACT-BULK-{i}",
                "reference_externe": None,
                "fournisseur_id": 1,
                "montant_ht": 10.0 * i,
                "taux_tva": 20.0,
                "montant_ttc": 12.0 * i,
                "statut": "brouillon",
                "devise": "EUR"
            }
            for i in range(1, 4)
        ]
    }
    create_response = client.post("/api/v1/factures-fournisseur/bulk", json=payload)
    assert create_response.status_code == 200
    ids = [f["id"] for f in create_response.json()]
    delete_payload = {"ids": ids}
    delete_response = client.request(
        "DELETE",
        "/api/v1/factures-fournisseur/bulk",
        json=delete_payload,
        headers={"Content-Type": "application/json"}
    )
    assert delete_response.status_code == 200
    assert "supprimées" in delete_response.json()["detail"]