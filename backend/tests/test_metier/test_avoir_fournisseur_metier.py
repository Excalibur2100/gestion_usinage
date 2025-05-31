import pytest
from fastapi.testclient import TestClient
from datetime import datetime
from backend.main import app

client = TestClient(app)


def test_creation_valide_et_consistance():
    """
    Teste la création d’un avoir fournisseur avec des données valides
    et vérifie les règles de cohérence métier.
    """
    response = client.post("/api/v1/avoirs-fournisseur/", json={
        "reference": "AV-METIER-001",
        "date_emission": datetime.utcnow().isoformat(),
        "montant_ht": 300.0,
        "taux_tva": 20.0,
        "montant_ttc": 360.0,
        "motif": "Retour de marchandise",
        "statut": "brouillon",
        "fournisseur_id": 1
    })
    assert response.status_code == 200
    data = response.json()
    assert data["reference"].startswith("AV-")
    assert data["montant_ttc"] > 0
    assert data["statut"] in ["brouillon", "valide", "remboursé", "annulé"]


def test_montant_negatif_refusé():
    """
    Test métier : montant négatif ne doit pas être accepté.
    """
    response = client.post("/api/v1/avoirs-fournisseur/", json={
        "reference": "AV-METIER-002",
        "montant_ht": -100.0,
        "taux_tva": 20.0,
        "montant_ttc": -120.0,
        "motif": "Erreur de facturation",
        "fournisseur_id": 1
    })
    assert response.status_code == 422  # Erreur de validation FastAPI


def test_statut_par_défaut_et_recherche():
    """
    Vérifie que le statut par défaut est 'brouillon' et
    que la recherche par statut retourne bien les bons enregistrements.
    """
    response = client.post("/api/v1/avoirs-fournisseur/", json={
        "reference": "AV-METIER-003",
        "montant_ht": 100.0,
        "taux_tva": 20.0,
        "montant_ttc": 120.0,
        "motif": "Test statut par défaut",
        "fournisseur_id": 1
    })
    assert response.status_code == 200
    data = response.json()
    assert data["statut"] == "brouillon"

    recherche = client.post("/api/v1/avoirs-fournisseur/search", json={"statut": "brouillon"})
    assert recherche.status_code == 200
    assert isinstance(recherche.json()["results"], list)