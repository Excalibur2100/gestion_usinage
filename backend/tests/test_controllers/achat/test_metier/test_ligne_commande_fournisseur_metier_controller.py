# backend/tests/test_controllers/achat/test_ligne_commande_fournisseur_metier_controller.py

import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_api_calcul_montant_ttc():
    response = client.get(
        "/api/v1/metier/lignes-commande-fournisseur/calcul-montant-ttc",
        params={"quantite": 5, "prix_unitaire_ht": 20, "taux_tva": 20}
    )
    assert response.status_code == 200
    assert response.json() == 120.0


@pytest.mark.parametrize("qte, qte_recue, attendu", [
    (10, 0, "non_recue"),
    (10, 5, "partiellement_recue"),
    (10, 10, "recue")
])
def test_api_statut_ligne_auto(qte, qte_recue, attendu):
    response = client.get(
        "/api/v1/metier/lignes-commande-fournisseur/statut-auto",
        params={"quantite": qte, "quantite_recue": qte_recue}
    )
    assert response.status_code == 200
    assert response.json() == attendu


def test_post_creer_ligne_enrichie():
    payload = {
        "commande_id": 99,
        "designation": "Rond brut Ø60 XC48",
        "quantite": 4,
        "prix_unitaire_ht": 30.0,
        "taux_tva": 20.0,
        "montant_ht": 120.0,
        "montant_ttc": 144.0  # volontairement faux, engine recalculera
    }

    response = client.post("/api/v1/metier/ligne-commande-fournisseur/creer-enrichie", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["commande_id"] == 99
    assert data["designation"] == "Rond brut Ø60 XC48"
    assert float(data["montant_ttc"]) == 144.0
    assert data["statut"] == "non_recue"