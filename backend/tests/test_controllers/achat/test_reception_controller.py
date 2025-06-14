# backend/tests/test_controllers/achat/test_reception_controller.py

import pytest
from fastapi.testclient import TestClient
from datetime import datetime
from main import app

client = TestClient(app)


@pytest.fixture
def reception_data():
    return {
        "numero_reception": "REC-CTRL-001",
        "commande_id": 1,
        "date_reception": datetime.utcnow().isoformat(),
        "statut": "en_attente",
        "commentaire": "Réception test contrôleur",
        "document_associe": None,
        "cree_par": 1,
        "modifie_par": 1
    }


def test_create_reception(client_auth, reception_data):
    response = client_auth.post("/api/v1/receptions", json=reception_data)
    assert response.status_code == 200
    assert response.json()["numero_reception"] == "REC-CTRL-001"


def test_read_reception(client_auth):
    # ID 1 supposé exister après création
    response = client_auth.get("/api/v1/receptions/1")
    assert response.status_code == 200
    assert "numero_reception" in response.json()


def test_list_receptions(client_auth):
    response = client_auth.get("/api/v1/receptions?skip=0&limit=10")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_update_reception(client_auth):
    update_data = {
        "commentaire": "Réception mise à jour",
        "modifie_par": 2
    }
    response = client_auth.put("/api/v1/receptions/1", json=update_data)
    assert response.status_code == 200
    assert response.json()["commentaire"] == "Réception mise à jour"


def test_delete_reception(client_auth):
    response = client_auth.delete("/api/v1/receptions/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Réception supprimée avec succès."


def test_search_receptions(client_auth):
    search_data = {
        "numero_reception": "REC-CTRL"
    }
    response = client_auth.post("/api/v1/receptions/search", json=search_data)
    assert response.status_code == 200
    assert "results" in response.json()


def test_bulk_create_receptions(client_auth):
    bulk_data = {
        "receptions": [
            {
                "numero_reception": "REC-BULK-101",
                "commande_id": 1,
                "date_reception": datetime.utcnow().isoformat(),
                "statut": "en_attente",
                "cree_par": 1,
                "modifie_par": 1
            },
            {
                "numero_reception": "REC-BULK-102",
                "commande_id": 1,
                "date_reception": datetime.utcnow().isoformat(),
                "statut": "en_attente",
                "cree_par": 1,
                "modifie_par": 1
            }
        ]
    }
    response = client_auth.post("/api/v1/receptions/bulk", json=bulk_data)
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_detail_reception(client_auth):
    response = client_auth.get("/api/v1/receptions/detail/1")
    assert response.status_code == 200
    assert "id" in response.json()


def test_export_receptions(client_auth):
    response = client_auth.get("/api/v1/receptions/export")
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/csv"