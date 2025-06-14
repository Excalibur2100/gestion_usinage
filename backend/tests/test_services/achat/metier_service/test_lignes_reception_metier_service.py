import pytest
from backend.services.achat.service_metier import lignes_reception_metier_service
from backend.db.models.tables.achat.lignes_reception import LigneReception


def test_recalcul_etat_ligne_conforme(db_session):
    ligne = LigneReception(
        reception_id=1,
        designation="Pièce conforme",
        quantite_commandee=100,
        quantite_recue=100
    )
    db_session.add(ligne)
    db_session.commit()
    db_session.refresh(ligne)

    updated = lignes_reception_metier_service.recalculer_etat_ligne(db_session, ligne.id)
    assert updated is not None
    assert updated.etat == "conforme"


def test_recalcul_etat_ligne_partielle(db_session):
    ligne = LigneReception(
        reception_id=1,
        designation="Pièce partielle",
        quantite_commandee=100,
        quantite_recue=40
    )
    db_session.add(ligne)
    db_session.commit()
    db_session.refresh(ligne)

    updated = lignes_reception_metier_service.recalculer_etat_ligne(db_session, ligne.id)
    assert updated is not None
    assert updated.etat == "partielle"


def test_recalcul_etat_ligne_non_conforme(db_session):
    ligne = LigneReception(
        reception_id=1,
        designation="Pièce absente",
        quantite_commandee=50,
        quantite_recue=0
    )
    db_session.add(ligne)
    db_session.commit()
    db_session.refresh(ligne)

    updated = lignes_reception_metier_service.recalculer_etat_ligne(db_session, ligne.id)
    assert updated is not None
    assert updated.etat == "non_conforme"


def test_recalcul_etat_ligne_surplus(db_session):
    ligne = LigneReception(
        reception_id=1,
        designation="Pièce en surplus",
        quantite_commandee=20,
        quantite_recue=25
    )
    db_session.add(ligne)
    db_session.commit()
    db_session.refresh(ligne)

    updated = lignes_reception_metier_service.recalculer_etat_ligne(db_session, ligne.id)
    assert updated is not None
    assert updated.etat == "surplus"