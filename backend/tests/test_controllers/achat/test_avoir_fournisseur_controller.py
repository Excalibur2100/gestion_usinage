import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_avoir():
    payload = {
        "reference": "AVF-TEST-001",
        "reference_externe": None,
        "fournisseur_id": 1,
        "montant_ht": 100.0,
        "taux_tva": 20.0,
        "montant_ttc": 120.0,
        "motif": "Test création"
    }
    response = client.post("/api/v1/avoirs-fournisseur/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["reference"] == "AVF-TEST-001"
    assert float(data["montant_ttc"]) == 120.0


def test_list_avoirs():
    response = client.get("/api/v1/avoirs-fournisseur/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_avoir_detail():
    payload = {
        "reference": "AVF-DETAIL-001",
        "reference_externe": None,
        "fournisseur_id": 1,
        "montant_ht": 200.0,
        "taux_tva": 10.0,
        "montant_ttc": 220.0,
        "motif": "Détail"
    }
    creation = client.post("/api/v1/avoirs-fournisseur/", json=payload)
    avoir_id = creation.json()["id"]

    response = client.get(f"/api/v1/avoirs-fournisseur/{avoir_id}")
    assert response.status_code == 200
    assert response.json()["reference"] == "AVF-DETAIL-001"


def test_update_avoir():
    payload = {
        "reference": "AVF-UPDATE-001",
        "reference_externe": None,
        "fournisseur_id": 1,
        "montant_ht": 150.0,
        "taux_tva": 20.0,
        "montant_ttc": 180.0,
        "motif": "À mettre à jour"
    }
    creation = client.post("/api/v1/avoirs-fournisseur/", json=payload)
    avoir_id = creation.json()["id"]

    update_data = {
        "commentaire": "Modifié via test",
        "motif": "Mis à jour"
    }
    response = client.put(f"/api/v1/avoirs-fournisseur/{avoir_id}", json=update_data)
    assert response.status_code == 200
    assert response.json()["commentaire"] == "Modifié via test"


def test_delete_avoir():
    payload = {
        "reference": "AVF-DELETE-001",
        "reference_externe": None,
        "fournisseur_id": 1,
        "montant_ht": 90.0,
        "taux_tva": 10.0,
        "montant_ttc": 99.0,
        "motif": "À supprimer"
    }
    creation = client.post("/api/v1/avoirs-fournisseur/", json=payload)
    avoir_id = creation.json()["id"]

    response = client.delete(f"/api/v1/avoirs-fournisseur/{avoir_id}")
    assert response.status_code == 200
    assert "supprimé" in response.json()["detail"]


def test_search_avoirs():
    payload = {
        "reference": "AVF-SEARCH-001",
        "reference_externe": None,
        "fournisseur_id": 1,
        "montant_ht": 50.0,
        "taux_tva": 10.0,
        "montant_ttc": 55.0,
        "motif": "Recherche"
    }
    client.post("/api/v1/avoirs-fournisseur/", json=payload)

    search = {"reference": "AVF-SEARCH"}
    response = client.post("/api/v1/avoirs-fournisseur/search", json=search)
    assert response.status_code == 200
    assert response.json()["total"] >= 1
    assert isinstance(response.json()["results"], list)


def test_export_csv():
    response = client.get("/api/v1/avoirs-fournisseur/export")
    assert response.status_code == 200
    assert "text/csv" in response.headers["content-type"]
    assert "attachment;" in response.headers["content-disposition"]


def test_bulk_create_and_delete():
    payload = {
        "avoirs": [
            {
                "reference": f"AVF-BULK-{i}",
                "reference_externe": None,
                "fournisseur_id": 1,
                "montant_ht": 10.0 * i,
                "taux_tva": 20.0,
                "montant_ttc": 12.0 * i,
                "motif": "Bulk test"
            }
            for i in range(1, 4)
        ]
    }
    create_response = client.post("/api/v1/avoirs-fournisseur/bulk", json=payload)
    assert create_response.status_code == 200
    ids = [a["id"] for a in create_response.json()]

    delete_payload = {"ids": ids}
    delete_response = client.request(
        method="DELETE",
        url="/api/v1/avoirs-fournisseur/bulk",
        json=delete_payload
    )
    assert delete_response.status_code == 200
    assert "supprimés" in delete_response.json()["detail"]