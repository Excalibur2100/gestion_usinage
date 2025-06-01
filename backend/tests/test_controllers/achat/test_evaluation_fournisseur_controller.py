import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_evaluation():
    payload = {
        "fournisseur_id": 1,
        "note_globale": 85.0,
        "statut": "bon"
    }
    response = client.post("/api/v1/evaluations-fournisseur/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["fournisseur_id"] == 1
    assert float(data["note_globale"]) == 85.0


def test_get_evaluation_detail():
    payload = {
        "fournisseur_id": 1,
        "note_globale": 70.0,
        "statut": "moyen"
    }
    creation = client.post("/api/v1/evaluations-fournisseur/", json=payload)
    eval_id = creation.json()["id"]
    response = client.get(f"/api/v1/evaluations-fournisseur/{eval_id}")
    assert response.status_code == 200
    assert response.json()["id"] == eval_id


def test_list_evaluations():
    response = client.get("/api/v1/evaluations-fournisseur/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_update_evaluation():
    creation = client.post("/api/v1/evaluations-fournisseur/", json={
        "fournisseur_id": 1,
        "note_globale": 60.0,
        "statut": "moyen"
    })
    eval_id = creation.json()["id"]
    update_data = {
        "commentaire": "Mise à jour test",
        "statut": "bon"
    }
    response = client.put(f"/api/v1/evaluations-fournisseur/{eval_id}", json=update_data)
    assert response.status_code == 200
    assert response.json()["commentaire"] == "Mise à jour test"


def test_delete_evaluation():
    creation = client.post("/api/v1/evaluations-fournisseur/", json={
        "fournisseur_id": 1,
        "note_globale": 50.0,
        "statut": "faible"
    })
    eval_id = creation.json()["id"]
    response = client.delete(f"/api/v1/evaluations-fournisseur/{eval_id}")
    assert response.status_code == 200
    assert "supprimée" in response.json()["detail"]


def test_search_evaluations():
    client.post("/api/v1/evaluations-fournisseur/", json={
        "fournisseur_id": 2,
        "note_globale": 90.0,
        "statut": "excellent"
    })
    search_payload = {"statut": "excellent"}
    response = client.post("/api/v1/evaluations-fournisseur/search", json=search_payload)
    assert response.status_code == 200
    assert isinstance(response.json()["results"], list)


def test_export_evaluations_csv():
    response = client.get("/api/v1/evaluations-fournisseur/export")
    assert response.status_code == 200
    assert "text/csv" in response.headers["content-type"]


def test_bulk_create_and_delete():
    payload = {
        "evaluations": [
            {
                "fournisseur_id": 1,
                "note_globale": 80.0,
                "statut": "bon"
            },
            {
                "fournisseur_id": 2,
                "note_globale": 90.0,
                "statut": "excellent"
            }
        ]
    }
    creation = client.post("/api/v1/evaluations-fournisseur/bulk", json=payload)
    assert creation.status_code == 200
    ids = [e["id"] for e in creation.json()]
    delete_payload = {"ids": ids}
    delete = client.request(
        "DELETE",
        "/api/v1/evaluations-fournisseur/bulk",
        json=delete_payload,
        headers={"Content-Type": "application/json"}
    )
    assert delete.status_code == 200
    assert "supprimées" in delete.json()["detail"]