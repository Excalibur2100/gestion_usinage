import pytest
from datetime import datetime

from backend.services.achat import lignes_reception_service, reception_service
from backend.db.models.tables.achat.lignes_reception import LigneReception
from backend.db.schemas.achat.reception_schemas import ReceptionCreate, StatutReceptionEnum
from backend.db.schemas.achat.lignes_reception_schemas import (
    LigneReceptionCreate,
    LigneReceptionUpdate,
    LigneReceptionSearch,
    LigneReceptionBulkCreate
)


def create_dummy_reception(db_session):
    reception_data = ReceptionCreate(
        numero_reception="REC-LIGNE-001",
        commande_id=1,
        date_reception=datetime.utcnow(),
        statut=StatutReceptionEnum.en_attente,
        cree_par=1,
        modifie_par=1,
        commentaire="Test commentaire",
        document_associe=None
    )
    return reception_service.create_reception(db_session, reception_data)


def test_create_ligne_reception(db_session):
    reception = create_dummy_reception(db_session)

    data = LigneReceptionCreate(
        reception_id=reception.id,
        designation="Pièce A",
        quantite_commandee=50,
        quantite_recue=30
    )

    ligne = lignes_reception_service.create_ligne_reception(db_session, data)
    assert ligne.id is not None
    assert getattr(ligne, "designation") == "Pièce A"
    assert getattr(ligne, "quantite_recue") == 30


def test_update_ligne_reception(db_session):
    ligne = db_session.query(LigneReception).first()
    update = LigneReceptionUpdate(
        quantite_commandee=ligne.quantite_commandee,
        quantite_recue=50,
        designation="Pièce A modifiée"
    )
    updated = lignes_reception_service.update_ligne_reception(db_session, ligne.id, update)
    assert updated is not None, "LigneReception not found or not updated"
    assert getattr(updated, "quantite_recue", None) == 50
    assert getattr(updated, "designation", None) == "Pièce A modifiée"


def test_delete_ligne_reception(db_session):
    ligne = db_session.query(LigneReception).first()
    success = lignes_reception_service.delete_ligne_reception(db_session, ligne.id)
    assert success is True


def test_search_ligne_reception(db_session):
    # Assuming you want to search for all receptions, set reception_id=None or provide a valid id
    search = LigneReceptionSearch(reception_id=None, designation="modifiée")
    results = lignes_reception_service.search_lignes_reception(db_session, search)
    assert isinstance(results, list)
    assert any("modifiée" in r.designation for r in results)


def test_bulk_create_lignes_reception(db_session):
    reception = create_dummy_reception(db_session)

    data = LigneReceptionBulkCreate(
        lignes=[
            LigneReceptionCreate(
                reception_id=reception.id,
                designation="Lot A",
                quantite_commandee=10,
                quantite_recue=10
            ),
            LigneReceptionCreate(
                reception_id=reception.id,
                designation="Lot B",
                quantite_commandee=20,
                quantite_recue=5
            )
        ]
    )
    results = lignes_reception_service.bulk_create_lignes_reception(db_session, data.lignes)
    assert len(results) == 2
    assert getattr(results[0], "designation", "").startswith("Lot")
    assert getattr(results[1], "designation", "").startswith("Lot")