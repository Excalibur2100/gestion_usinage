import pytest
from datetime import datetime

from backend.services.achat import reception_service
from backend.db.models.tables.achat.receptions import Reception  # On ne récupère PAS StatutReception ici
from backend.db.schemas.achat.reception_schemas import (
    ReceptionCreate,
    ReceptionUpdate,
    ReceptionSearch,
    ReceptionBulkCreate,
    StatutReceptionEnum
)


def test_create_reception(db_session):
    data = ReceptionCreate(
        numero_reception="REC-TEST-001",
        commande_id=1,
        date_reception=datetime.utcnow(),
        statut=StatutReceptionEnum.en_attente,
        commentaire="Test",
        document_associe=None,
        cree_par=1,
        modifie_par=1
    )

    reception = reception_service.create_reception(db_session, data)
    assert reception.id is not None
    assert getattr(reception, "numero_reception", None) == "REC-TEST-001"


def test_get_reception_by_id(db_session):
    reception = reception_service.get_reception_by_id(db_session, 1)
    assert reception is not None
    assert getattr(reception, "id", None) == 1


def test_get_all_receptions(db_session):
    results = reception_service.get_all_receptions(db_session)
    assert isinstance(results, list)
    assert len(results) >= 0


def test_update_reception(db_session):
    update = ReceptionUpdate(
        numero_reception="REC-TEST-001",
        commande_id=1,
        date_reception=datetime.utcnow(),
        document_associe=None,
        modifie_par=1,
        commentaire="Réception modifiée",
        statut=StatutReceptionEnum.recue
    )
    updated = reception_service.update_reception(db_session, 1, update)
    assert updated is not None
    assert getattr(updated, "commentaire", None) == "Réception modifiée"
    assert getattr(updated, "statut", None) == StatutReceptionEnum.recue


def test_delete_reception(db_session):
    deleted = reception_service.delete_reception(db_session, 1)
    assert deleted is True


def test_search_receptions(db_session):
    search = ReceptionSearch(
        numero_reception="REC-TEST",
        commande_id=None,
        date_debut=None,
        date_fin=None
    )
    results = reception_service.search_receptions(db_session, search)
    assert isinstance(results, list)
    for r in results:
        assert "REC-TEST" in r.numero_reception


def test_bulk_create_receptions(db_session):
    data = ReceptionBulkCreate(
        receptions=[
            ReceptionCreate(
                numero_reception="REC-BULK-001",
                commande_id=1,
                date_reception=datetime.utcnow(),
                statut=StatutReceptionEnum.en_attente,
                commentaire="Bulk test 1",
                document_associe=None,
                cree_par=1,
                modifie_par=1
            ),
            ReceptionCreate(
                numero_reception="REC-BULK-002",
                commande_id=1,
                date_reception=datetime.utcnow(),
                statut=StatutReceptionEnum.en_attente,
                commentaire="Bulk test 2",
                document_associe=None,
                cree_par=1,
                modifie_par=1
            )
        ]
    )
    results = reception_service.bulk_create_receptions(db_session, data.receptions)
    assert len(results) == 2
    assert str(results[0].numero_reception).startswith("REC-BULK")
    assert str(results[1].numero_reception).startswith("REC-BULK")