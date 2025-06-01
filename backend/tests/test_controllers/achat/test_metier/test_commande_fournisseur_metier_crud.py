import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_creation_valide_commande():
    response = client.post("/api/v1/commandes-fournisseur/", json={
        "numero_commande": "CMD-METIER-001",
        "fournisseur_id": 1,
        "montant_total": 1000.0,
        "devise": "EUR"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["statut"] == "brouillon"
    assert data["montant_total"] > 0

def test_commande_montant_negatif():
    response = client.post("/api/v1/commandes-fournisseur/", json={
        "numero_commande": "CMD-METIER-002",
        "fournisseur_id": 1,
        "montant_total": -50,
        "devise": "EUR"
    })
    assert response.status_code == 422  # Validateur Pydantic déclenché

def test_recherche_statut_commande():
    client.post("/api/v1/commandes-fournisseur/", json={
        "numero_commande": "CMD-METIER-003",
        "fournisseur_id": 1,
        "montant_total": 750,
        "devise": "EUR",
        "statut": "brouillon"
    })
    search = client.post("/api/v1/commandes-fournisseur/search", json={"statut": "brouillon"})
    assert search.status_code == 200
    assert isinstance(search.json()["results"], list)

def test_suppression_non_brouillon_interdite():
    creation = client.post("/api/v1/commandes-fournisseur/", json={
        "numero_commande": "CMD-METIER-004",
        "fournisseur_id": 1,
        "montant_total": 150,
        "statut": "envoyee",
        "devise": "EUR"
    })
    cmd_id = creation.json()["id"]
    deletion = client.delete(f"/api/v1/commandes-fournisseur/{cmd_id}")
    assert deletion.status_code == 400
    assert "brouillon" in deletion.json()["detail"]