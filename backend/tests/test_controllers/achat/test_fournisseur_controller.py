# backend/tests/test_controllers/achat/test_fournisseur_controller.py

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_fournisseur():
    payload = {
        "nom": "Fournisseur Controller",
        "code": "FRN-CTRL-001",
        "type": "fournisseur_outillage",
        "statut": "actif",
        "adresse": "1 rue industrielle",
        "ville": "Thionville",
        "code_postal": "57100",
        "pays": "France",
        "email": "contact@ctrl.com",
        "telephone": "0123456789",
        "site_web": "https://ctrl.com",
        "contact_nom": "Michel Contrôle",
        "contact_email": "contact@ctrl.com",
        "contact_telephone": "0601020304"
    }

    response = client.post("/api/v1/fournisseurs/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["nom"] == "Fournisseur Controller"
    assert data["code"] == "FRN-CTRL-001"


def test_get_fournisseur_detail():
    create = client.post("/api/v1/fournisseurs/", json={
        "nom": "Fournisseur Detail",
        "code": "FRN-CTRL-002",
        "type": "prestataire",
        "statut": "actif",
        "adresse": "2 rue du test",
        "ville": "Nancy",
        "code_postal": "54000",
        "pays": "France"
    })
    id_ = create.json()["id"]

    response = client.get(f"/api/v1/fournisseurs/{id_}")
    assert response.status_code == 200
    assert response.json()["nom"] == "Fournisseur Detail"


def test_update_fournisseur():
    create = client.post("/api/v1/fournisseurs/", json={
        "nom": "Fournisseur Update",
        "code": "FRN-CTRL-003",
        "type": "metrologie",
        "statut": "actif",
        "adresse": "3 avenue du progrès",
        "ville": "Metz",
        "code_postal": "57000",
        "pays": "France"
    })
    id_ = create.json()["id"]

    response = client.put(f"/api/v1/fournisseurs/{id_}", json={
        "commentaire": "Mis à jour via test"
    })

    assert response.status_code == 200
    assert response.json()["commentaire"] == "Mis à jour via test"


def test_delete_fournisseur():
    create = client.post("/api/v1/fournisseurs/", json={
        "nom": "Fournisseur Delete",
        "code": "FRN-CTRL-004",
        "type": "fabricant_machines",
        "statut": "actif",
        "adresse": "Zone industrielle",
        "ville": "Forbach",
        "code_postal": "57600",
        "pays": "France"
    })
    id_ = create.json()["id"]

    response = client.delete(f"/api/v1/fournisseurs/{id_}")
    assert response.status_code == 200
    assert "supprimé" in response.json()["detail"].lower()


def test_search_fournisseur():
    client.post("/api/v1/fournisseurs/", json={
        "nom": "Fournisseur Search",
        "code": "FRN-CTRL-005",
        "type": "peinture_industrielle",
        "statut": "actif",
        "adresse": "Route nationale",
        "ville": "St Avold",
        "code_postal": "57500",
        "pays": "France"
    })

    response = client.post("/api/v1/fournisseurs/search", json={"nom": "Search"})
    assert response.status_code == 200
    assert isinstance(response.json()["results"], list)


def test_bulk_create_and_delete_fournisseurs():
    payload = {
        "fournisseurs": [
            {
                "nom": f"Bulk F{i}",
                "code": f"FRN-BULK-{i}",
                "type": "controle_qualite",
                "statut": "actif",
                "adresse": "ZAC Usinage",
                "ville": "Yutz",
                "code_postal": "57970",
                "pays": "France"
            } for i in range(1, 4)
        ]
    }

    creation = client.post("/api/v1/fournisseurs/bulk", json=payload)
    assert creation.status_code == 200
    ids = [f["id"] for f in creation.json()]

    delete = client.request("DELETE", "/api/v1/fournisseurs/bulk", json={"ids": ids})
    assert delete.status_code == 200
    assert "supprimés" in delete.json()["detail"]


def test_export_fournisseur_csv():
    response = client.get("/api/v1/fournisseurs/export")
    assert response.status_code == 200
    assert "text/csv" in response.headers["content-type"]
    assert "attachment;" in response.headers["content-disposition"]