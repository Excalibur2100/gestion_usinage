# backend/tests/test_metier/achat/test_reception_metier_controller.py

import pytest
from fastapi.testclient import TestClient
from main import app
from datetime import datetime

client = TestClient(app)


@pytest.fixture
def reception_test_data(db_session):
    """
    Prépare une réception avec lignes fictives si besoin.
    """
    from backend.db.models.tables.achat.receptions import Reception
    from backend.db.models.tables.achat.lignes_reception import LigneReception

    reception = Reception(
        numero_reception="REC-METIER-001",
        commande_id=1,
        date_reception=datetime.utcnow(),
        statut="en_attente",
        cree_par=1,
        modifie_par=1
    )
    db_session.add(reception)
    db_session.commit()
    db_session.refresh(reception)

    ligne = LigneReception(
        reception_id=reception.id,
        designation="Pièce test",
        quantite_commandee=10,
        quantite_recue=5
    )
    db_session.add(ligne)
    db_session.commit()

    return reception.id


def test_appliquer_statut_automatique(client_auth, reception_test_data):
    response = client_auth.post(f"/api/v1/metier/receptions/statut-automatique/{reception_test_data}")
    assert response.status_code == 200
    assert response.json()["statut"] in ["en_attente", "partiellement_recue", "recue"]


def test_valider_reception(client_auth, reception_test_data):
    response = client_auth.post(f"/api/v1/metier/receptions/valider/{reception_test_data}")
    assert response.status_code == 200
    assert response.json()["statut"] == "recue"


def test_archiver_reception(client_auth, reception_test_data):
    response = client_auth.post(f"/api/v1/metier/receptions/archiver/{reception_test_data}")
    assert response.status_code == 200
    assert response.json()["statut"] == "archivee"