import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.models.tables import Utilisateur
from main import app

client = TestClient(app)

@pytest.fixture(autouse=True)
def cleanup_database():
    """Nettoie la base de données avant chaque test."""
    db: Session = next(get_db())
    db.query(Utilisateur).delete()
    db.commit()

def test_creer_utilisateur():
    payload = {
        "nom": "Test User",
        "email": "testuser@example.com",
        "role": "admin",
        "mot_de_passe": "password123"
    }
    response = client.post("/utilisateurs/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data

def test_lire_tous_utilisateurs():
    response = client.get("/utilisateurs/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_lire_un_utilisateur():
    payload = {
        "nom": "Test User",
        "email": "testuser2@example.com",
        "role": "user",
        "mot_de_passe": "password123"
    }
    create_response = client.post("/utilisateurs/", json=payload)
    utilisateur_id = create_response.json()["id"]

    response = client.get(f"/utilisateurs/{utilisateur_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == utilisateur_id

def test_mettre_a_jour_utilisateur():
    payload = {
        "nom": "Test User",
        "email": "testuser3@example.com",
        "role": "user",
        "mot_de_passe": "password123"
    }
    create_response = client.post("/utilisateurs/", json=payload)
    utilisateur_id = create_response.json()["id"]

    update_payload = {"nom": "Updated User"}
    response = client.put(f"/utilisateurs/{utilisateur_id}", json=update_payload)
    assert response.status_code == 200
    data = response.json()
    assert data["nom"] == "Updated User"

def test_supprimer_utilisateur():
    # Crée un utilisateur pour le test
    payload = {
        "nom": "Test User",
        "email": "testuser4@example.com",
        "role": "user",
        "mot_de_passe": "password123"
    }
    create_response = client.post("/utilisateurs/", json=payload)
    utilisateur_id = create_response.json()["id"]

    # Supprime l'utilisateur
    response = client.delete(f"/utilisateurs/{utilisateur_id}")
    assert response.status_code == 204

    # Vérifie que l'utilisateur n'existe plus
    get_response = client.get(f"/utilisateurs/{utilisateur_id}")
    assert get_response.status_code == 404