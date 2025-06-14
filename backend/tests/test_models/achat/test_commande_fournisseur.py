import pytest
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker, clear_mappers
from backend.db.models.base import Base
from backend.db.models.tables.achat.commandes_fournisseur import CommandeFournisseur, StatutCommandeFournisseur


@pytest.fixture
def db():
    engine = create_engine("sqlite:///:memory:")
    TestingSessionLocal = sessionmaker(bind=engine)
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    yield session
    session.close()
    clear_mappers()


def test_create_valid_commande(db):
    commande = CommandeFournisseur(
        numero_commande="CMD-TEST-001",
        reference_externe=None,
        fournisseur_id=1,
        montant_total=500.0,
        statut=StatutCommandeFournisseur.brouillon
    )
    db.add(commande)
    db.commit()
    db.refresh(commande)

    assert commande.id is not None
    assert str(commande.numero_commande).startswith("CMD-")
    assert float(getattr(commande, "montant_total")) == 500.0
    assert str(commande.statut) == StatutCommandeFournisseur.brouillon.value


def test_enum_statut(db):
    commande = CommandeFournisseur(
        numero_commande="CMD-TEST-002",
        reference_externe=None,
        fournisseur_id=1,
        montant_total=300.0,
        statut=StatutCommandeFournisseur.envoyee
    )
    db.add(commande)
    db.commit()
    db.refresh(commande)

    assert commande.statut.value == StatutCommandeFournisseur.envoyee.value


def test_constraint_montant_total_negative(db):
    with pytest.raises(exc.IntegrityError):
        db.add(CommandeFournisseur(
            numero_commande="CMD-NEGATIVE",
            reference_externe=None,
            fournisseur_id=1,
            montant_total=-50.0,
            statut=StatutCommandeFournisseur.brouillon
        ))
        db.commit()


def test_repr_commande(db):
    commande = CommandeFournisseur(
        numero_commande="CMD-REPR-001",
        reference_externe=None,
        fournisseur_id=123,
        montant_total=200.0,
        statut=StatutCommandeFournisseur.brouillon
    )
    db.add(commande)
    db.commit()
    db.refresh(commande)

    assert repr(commande) == f"<CommandeFournisseur(id={commande.id}, numero='CMD-REPR-001', fournisseur_id=123)>"