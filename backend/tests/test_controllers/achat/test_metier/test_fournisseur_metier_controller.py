import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_api_code_fournisseur_auto():
    response = client.get("/api/v1/metier/fournisseurs/generer-code-auto")
    assert response.status_code == 200
    code = response.json()
    assert code.startswith("FRN-")
    assert isinstance(code, str)
    assert len(code) > 10


@pytest.mark.parametrize("description, attendu", [
    ("acier brut et inox", "fournisseur_matiere_premiere"),
    ("plaquettes carbure et outils HSS", "fournisseur_outillage"),
    ("centre usinage CNC", "machine_outil"),
    ("traitement thermique nitruration", "traitement_surface"),
    ("transport logistique", "transport"),
    ("certificat de contrôle dimensionnel", "controle_qualite"),
    ("logiciel erp cao cam", "logiciel_support"),
    ("atelier de décolletage", "sous_traitant_usinage"),
    ("soudure TIG inox", "sous_traitant_soudure"),
    ("gravure et peinture", "peinture_industrielle"),
    ("inconnu ou autre domaine", "autre"),
])
def test_detecter_type_metier(description, attendu):
    response = client.get("/api/v1/metier/fournisseurs/detect-type", params={"description": description})
    assert response.status_code == 200
    assert response.json() == attendu


@pytest.mark.parametrize("commentaire, attendu", [
    ("blacklist suite à fraude", "blacklisté"),
    ("entreprise fermée", "inactif"),
    ("bon fournisseur", "actif"),
    ("", "actif"),
])
def test_detection_statut(commentaire, attendu):
    response = client.get("/api/v1/metier/fournisseurs/detect-statut", params={"commentaire": commentaire})
    assert response.status_code == 200
    assert response.json() == attendu


def test_suggestion_creation_fournisseur():
    payload = {
        "nom": "Fournisseur IA",
        "description": "usinage centre cnc",
        "commentaire": "Partenaire technique",
        "email": "ai@example.com",
        "pays": "France",
        "adresse": "1 rue IA",
        "ville": "Metz",
        "code_postal": "57000",
        "telephone": "0102030405",
        "site_web": "https://ai-fournisseur.com",
        "contact_nom": "Jean IA",
        "contact_email": "contact@ai-fournisseur.com",
        "contact_telephone": "0607080910"
    }

    response = client.post("/api/v1/metier/fournisseurs/suggestion-auto", json=payload)
    assert response.status_code == 200

    data = response.json()
    assert data["nom"] == "Fournisseur IA"
    assert data["type"] == "sous_traitant_usinage"
    assert data["statut"] == "actif"
    assert data["pays"] == "France"
    assert data["code"].startswith("FRN-")


def test_suggestion_creation_manquante():
    response = client.post("/api/v1/metier/fournisseurs/suggestion-auto", json={})
    assert response.status_code == 422  # Validation manquante