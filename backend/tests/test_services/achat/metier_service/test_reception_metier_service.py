# backend/tests/test_services/achat/metier_service/test_reception_metier_service.py

import pytest
from sqlalchemy.orm import Session
from datetime import datetime

from backend.services.achat.service_metier import reception_metier_service
from backend.db.models.tables.achat.receptions import Reception, StatutReception
from backend.db.models.tables.achat.lignes_reception import LigneReception


@pytest.fixture
def reception_avec_lignes(db_session: Session):
    reception = Reception(
        numero_reception="REC-METIER-001",
        commande_id=1,
        date_reception=datetime.utcnow(),
        statut=StatutReception.en_attente,
        cree_par=1,
        modifie_par=1
    )
    db_session.add(reception)
    db_session.commit()

    ligne1 = LigneReception(
        reception_id=reception.id,
        quantite_commandee=10,
        quantite_recue=10,
        designation="Pièce A"
    )
    db_session.add(ligne1)
    db_session.commit()
    db_session.refresh(reception)
    return reception


def test_appliquer_statut_automatique(db_session: Session, reception_avec_lignes: Reception):
    reception = reception_metier_service.appliquer_statut_automatique(db_session, getattr(reception_avec_lignes, "id"))
    assert reception is not None
    assert getattr(reception, "statut", None) == StatutReception.recue


def test_valider_reception(db_session: Session, reception_avec_lignes: Reception):
    reception = reception_metier_service.valider_reception(db_session, getattr(reception_avec_lignes, "id"))
    assert reception is not None
    assert getattr(reception, "statut", None) == StatutReception.recue


def test_valider_reception_sans_lignes(db_session: Session):
    reception = Reception(
        numero_reception="REC-METIER-002",
        commande_id=1,
        date_reception=datetime.utcnow(),
        statut=StatutReception.en_attente,
        cree_par=1,
        modifie_par=1
    )
    db_session.add(reception)
    db_session.commit()

    with pytest.raises(ValueError):
        reception_metier_service.valider_reception(db_session, getattr(reception, "id"))


def test_archiver_reception(db_session: Session):
    reception = Reception(
        numero_reception="REC-METIER-003",
        commande_id=1,
        date_reception=datetime.utcnow(),
        statut=StatutReception.en_attente,
        cree_par=1,
        modifie_par=1
    )
    db_session.add(reception)
    db_session.commit()

    archived = reception_metier_service.archiver_reception(db_session, getattr(reception, "id"))
    assert archived is not None
    assert getattr(archived, "statut", None) == StatutReception.archivee