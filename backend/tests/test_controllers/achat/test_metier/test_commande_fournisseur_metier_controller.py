# backend/tests/test_metier/achat/test_commande_fournisseur_metier_controller.py

import pytest
from fastapi.testclient import TestClient
from main import app
from datetime import datetime

client = TestClient(app)


def test_calcul_montant_total_commande():
    response = client.get(
        "/api/v1/metier/commandes-fournisseur/calcul-montant-total",
        params={
            "references": ["P001", "P002"],
            "quantites": [2, 3],
            "prix_unitaires": [10.0, 5.0]
        }
    )
    assert response.status_code == 200
    assert response.json() == 35.0


def test_generer_numero_commande_auto():
    response = client.get("/api/v1/metier/commandes-fournisseur/generer-numero")
    assert response.status_code == 200
    numero = response.json()
    assert numero.startswith("CMD-AUTO-")
    assert isinstance(numero, str)


def test_statut_auto_commande():
    date_livraison = datetime.utcnow().isoformat()
    response = client.get("/api/v1/metier/commandes-fournisseur/statut-auto", params={
        "date_livraison_prevue": date_livraison
    })
    assert response.status_code == 200
    assert response.json() in ["envoyee", "livree"]


def test_suggestion_commande_auto():
    payload = {
        "fournisseur_id": 1,
        "lignes": [
            ["PRD-001", 2, 50.0],
            ["PRD-002", 1, 30.0]
        ],
        "cree_par": 1
    }

    response = client.post("/api/v1/metier/commandes-fournisseur/suggestion-auto", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert data["numero_commande"].startswith("CMD-AUTO-")
    assert data["fournisseur_id"] == 1
    assert float(data["montant_total"]) == 130.0


def test_suggestion_commande_auto_erreur_format():
    response = client.post("/api/v1/metier/commandes-fournisseur/suggestion-auto", json={})
    assert response.status_code == 422  # Erreur validation FastAPI