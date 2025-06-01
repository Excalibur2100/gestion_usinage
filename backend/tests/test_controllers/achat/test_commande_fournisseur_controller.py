# backend/tests/test_controllers/achat/test_commande_fournisseur_controller.py

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_commande():
    payload = {
        "numero_commande": "CMD-TEST-001",
        "reference_externe": "EXT-001",
        "fournisseur_id": 1,
        "montant_total": 100.0,
        "devise": "EUR"
    }
    response = client.post("/api/v1/achat/commandes-fournisseur/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["numero_commande"] == "CMD-TEST-001"
    assert data["fournisseur_id"] == 1
    assert float(data["montant_total"]) == 100.0


def test_get_commande_detail():
    creation = client.post("/api/v1/achat/commandes-fournisseur/", json={
        "numero_commande": "CMD-DETAIL-001",
        "fournisseur_id": 1,
        "montant_total": 200.0
    })
    id_ = creation.json()["id"]
    response = client.get(f"/api/v1/achat/commandes-fournisseur/{id_}")
    assert response.status_code == 200
    assert response.json()["id"] == id_
    assert response.json()["numero_commande"] == "CMD-DETAIL-001"


def test_list_commandes():
    response = client.get("/api/v1/achat/commandes-fournisseur/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_update_commande():
    creation = client.post("/api/v1/achat/commandes-fournisseur/", json={
        "numero_commande": "CMD-UPD-001",
        "fournisseur_id": 1,
        "montant_total": 300.0
    })
    id_ = creation.json()["id"]
    update = {"commentaire": "Test de mise à jour"}
    response = client.put(f"/api/v1/achat/commandes-fournisseur/{id_}", json=update)
    assert response.status_code == 200
    assert response.json()["commentaire"] == "Test de mise à jour"


def test_delete_commande():
    creation = client.post("/api/v1/achat/commandes-fournisseur/", json={
        "numero_commande": "CMD-DEL-001",
        "fournisseur_id": 1,
        "montant_total": 90.0
    })
    id_ = creation.json()["id"]
    response = client.delete(f"/api/v1/achat/commandes-fournisseur/{id_}")
    assert response.status_code == 200
    assert "supprimée" in response.json()["detail"]


def test_search_commandes():
    client.post("/api/v1/achat/commandes-fournisseur/", json={
        "numero_commande": "CMD-SEARCH-001",
        "fournisseur_id": 1,
        "montant_total": 100.0
    })
    payload = {"numero_commande": "CMD-SEARCH"}
    response = client.post("/api/v1/achat/commandes-fournisseur/search", json=payload)
    assert response.status_code == 200
    assert response.json()["total"] >= 1
    assert isinstance(response.json()["results"], list)


def test_export_commandes_csv():
    response = client.get("/api/v1/achat/commandes-fournisseur/export")
    assert response.status_code == 200
    assert "text/csv" in response.headers["content-type"]


def test_bulk_create_and_delete():
    payload = {
        "commandes": [
            {"numero_commande": f"CMD-BULK-{i}", "fournisseur_id": 1, "montant_total": 25.0 * i}
            for i in range(1, 4)
        ]
    }
    creation = client.post("/api/v1/achat/commandes-fournisseur/bulk", json=payload)
    assert creation.status_code == 200
    ids = [cmd["id"] for cmd in creation.json()]

    delete_payload = {"ids": ids}
    delete = client.request(
        "DELETE",
        "/api/v1/achat/commandes-fournisseur/bulk",
        json=delete_payload,
        headers={"Content-Type": "application/json"}
    )
    assert delete.status_code == 200
    assert "supprimées" in delete.json()["detail"]