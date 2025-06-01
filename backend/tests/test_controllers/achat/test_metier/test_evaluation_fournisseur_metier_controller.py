import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_note_globale():
    response = client.get(
        "/api/v1/metier/evaluations-fournisseur/calcul-note",
        params={"qualite": 80.0, "delai": 70.0, "prix": 90.0}
    )
    assert response.status_code == 200
    note = response.json()["note_globale"]
    assert isinstance(note, float)
    assert round(note, 2) == round(0.4 * 80 + 0.4 * 70 + 0.2 * 90, 2)


def test_get_statut_auto():
    response = client.get("/api/v1/metier/evaluations-fournisseur/statut-auto", params={"note": 75.0})
    assert response.status_code == 200
    assert response.json()["statut"] in ["excellent", "bon", "moyen", "faible", "critique"]


def test_get_recommandation():
    response = client.get("/api/v1/metier/evaluations-fournisseur/recommandation", params={"statut": "bon"})
    assert response.status_code == 200
    assert isinstance(response.json()["recommandation"], str)


def test_get_suggestion_auto():
    response = client.post(
        "/api/v1/metier/evaluations-fournisseur/suggestion-automatique",
        params={
            "fournisseur_id": 1,
            "note_qualite": 85.0,
            "note_delai": 80.0,
            "note_prix": 90.0
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["fournisseur_id"] == 1
    assert float(data["note_globale"]) > 0
    assert data["statut"] in ["excellent", "bon", "moyen", "faible", "critique"]