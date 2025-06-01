import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


def test_api_generer_numero():
    response = client.get("/api/v1/metier/commandes-fournisseur/generer-numero?annee=2024&compteur=7")
    assert response.status_code == 200
    assert response.json() == "CMD-2024-0007"


def test_api_detecter_retard():
    response = client.get("/api/v1/metier/commandes-fournisseur/detecter-retard?date_prevue=2024-05-01T00:00:00&date_effective=2024-05-02T00:00:00")
    assert response.status_code == 200
    assert response.json() is True


def test_api_statut_auto():
    response = client.get("/api/v1/metier/commandes-fournisseur/statut-auto?depuis_livraison=true&livree=false")
    assert response.status_code == 200
    assert response.json() == "partiellement_livree"


def test_api_suggere_commande():
    response = client.get("/api/v1/metier/commandes-fournisseur/suggere-auto?fournisseur_id=1&montant=1000")
    assert response.status_code == 200
    data = response.json()
    assert data["numero_commande"].startswith("AUTO-CMD-")
    assert data["montant_total"] == 1000