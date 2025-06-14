import pytest
from sqlalchemy.exc import IntegrityError
from backend.db.models.tables.achat.receptions import Reception, StatutReception
from backend.db.models.tables.securite.utilisateur import Utilisateur
from backend.db.models.tables.achat.commandes_fournisseur import CommandeFournisseur
from datetime import datetime
from uuid import uuid4


def test_create_valid_reception(db_session):
    commande = CommandeFournisseur(id=1, numero_commande="CMD-001")
    db_session.add(commande)

    utilisateur = Utilisateur(id=1, nom="Testeur")
    db_session.add(utilisateur)

    reception = Reception(
        numero_reception="REC-001",
        commande_id=1,
        date_reception=datetime.utcnow(),
        statut=StatutReception.en_attente,
        commentaire="RAS",
        cree_par=1,
        modifie_par=1,
        uuid=str(uuid4())
    )

    db_session.add(reception)
    db_session.commit()

    assert reception.id is not None
    assert getattr(reception, "numero_reception") == "REC-001"
    assert getattr(reception, "commande_id") == 1
    assert str(reception.statut) == str(StatutReception.en_attente)


def test_reception_statut_enum(db_session):
    reception = Reception(
        numero_reception="REC-002",
        commande_id=1,
        date_reception=datetime.utcnow(),
        statut=StatutReception.recue
    )
    db_session.add(reception)
    db_session.commit()
    assert reception.statut is StatutReception.recue


def test_reception_repr(db_session):
    reception = Reception(
        numero_reception="REC-003",
        commande_id=1,
        date_reception=datetime(2025, 6, 1),
        statut=StatutReception.partiellement_recue
    )
    db_session.add(reception)
    db_session.commit()

    output = repr(reception)
    assert "REC-003" in output
    assert "partiellement_recue" in output
    assert "2025-06-01" in output


def test_reception_missing_required_fields(db_session):
    with pytest.raises(IntegrityError):
        reception = Reception(
            numero_reception=None,
            commande_id=None,
            date_reception=None
        )
        db_session.add(reception)
        db_session.commit()