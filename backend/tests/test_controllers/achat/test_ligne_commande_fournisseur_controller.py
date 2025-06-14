import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_ligne_commande():
    payload = {
        "commande_id": 1,
        "designation": "Acier XC48 Ø50",
        "description": "Barre acier pour tournage",
        "quantite": 10,
        "prix_unitaire_ht": 12.5,
        "taux_tva": 20.0,
        "montant_ht": 125.0,
        "montant_ttc": 150.0,
        "unite": "pièce",
        "statut": "en_attente",
        "commentaire": "Commande test création"
    }
    response = client.post("/api/v1/lignes-commande-fournisseur/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["designation"] == "Acier XC48 Ø50"
    assert float(data["montant_ttc"]) == 150.0


def test_get_ligne_commande_detail():
    creation = client.post("/api/v1/lignes-commande-fournisseur/", json={
        "commande_id": 1,
        "designation": "Rond alu Ø80",
        "quantite": 5,
        "prix_unitaire_ht": 20.0,
        "montant_ht": 100.0,
        "montant_ttc": 120.0
    })
    ligne_id = creation.json()["id"]

    response = client.get(f"/api/v1/lignes-commande-fournisseur/{ligne_id}")
    assert response.status_code == 200
    assert response.json()["designation"] == "Rond alu Ø80"


def test_update_ligne_commande():
    creation = client.post("/api/v1/lignes-commande-fournisseur/", json={
        "commande_id": 2,
        "designation": "Brut de forge",
        "quantite": 3,
        "prix_unitaire_ht": 50.0,
        "montant_ht": 150.0,
        "montant_ttc": 180.0
    })
    ligne_id = creation.json()["id"]

    response = client.put(f"/api/v1/lignes-commande-fournisseur/{ligne_id}", json={
        "commentaire": "Ajout commentaire test"
    })
    assert response.status_code == 200
    assert response.json()["commentaire"] == "Ajout commentaire test"


def test_delete_ligne_commande():
    creation = client.post("/api/v1/lignes-commande-fournisseur/", json={
        "commande_id": 3,
        "designation": "Tube acier",
        "quantite": 2,
        "prix_unitaire_ht": 40.0,
        "montant_ht": 80.0,
        "montant_ttc": 96.0
    })
    ligne_id = creation.json()["id"]

    response = client.delete(f"/api/v1/lignes-commande-fournisseur/{ligne_id}")
    assert response.status_code == 200
    assert "supprimée" in response.json()["detail"].lower()


def test_search_lignes_commande():
    client.post("/api/v1/lignes-commande-fournisseur/", json={
        "commande_id": 4,
        "designation": "Barre inox Ø20",
        "quantite": 6,
        "prix_unitaire_ht": 25.0,
        "montant_ht": 150.0,
        "montant_ttc": 180.0
    })

    response = client.post("/api/v1/lignes-commande-fournisseur/search", json={
        "designation": "inox"
    })
    assert response.status_code == 200
    assert isinstance(response.json()["results"], list)


def test_bulk_create_and_delete_lignes_commande():
    lignes = [{
        "commande_id": 5,
        "designation": f"Pièce {i}",
        "quantite": i,
        "prix_unitaire_ht": 10.0,
        "montant_ht": i * 10.0,
        "montant_ttc": i * 12.0
    } for i in range(1, 4)]

    creation = client.post("/api/v1/lignes-commande-fournisseur/bulk", json={"lignes": lignes})
    assert creation.status_code == 200
    ids = [l["id"] for l in creation.json()]

    suppression = client.request("DELETE", "/api/v1/lignes-commande-fournisseur/bulk", json={"ids": ids})
    assert suppression.status_code == 200
    assert "supprimées" in suppression.json()["detail"]


def test_export_lignes_commande_csv():
    response = client.get("/api/v1/lignes-commande-fournisseur/export")
    assert response.status_code == 200
    assert "text/csv" in response.headers["content-type"]