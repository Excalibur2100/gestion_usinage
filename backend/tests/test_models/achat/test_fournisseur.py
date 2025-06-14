# backend/tests/test_models/achat/test_fournisseur.py

import pytest
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker, clear_mappers

from backend.db.models.base import Base
from backend.db.models.tables.achat.fournisseurs import Fournisseur, StatutFournisseur, TypeFournisseur


@pytest.fixture
def db():
    engine = create_engine("sqlite:///:memory:")
    TestingSessionLocal = sessionmaker(bind=engine)
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    yield session
    session.close()
    clear_mappers()


def test_create_valid_fournisseur(db):
    fournisseur = Fournisseur(
        nom="ACME Industries",
        code="FRN-001",
        type=TypeFournisseur.fournisseur_outillage,
        statut=StatutFournisseur.actif,
        pays="France",
        adresse="1 rue test",
        ville="Paris",
        code_postal="75000",
        email="contact@acme.com",
        telephone="0123456789",
        site_web="https://acme.com",
        contact_nom="Jean Dupont",
        contact_email="contact@acme.com",
        contact_telephone="0607080910"
    )
    db.add(fournisseur)
    db.commit()
    db.refresh(fournisseur)

    assert fournisseur.id is not None
    assert getattr(fournisseur, "nom") == "ACME Industries"
    assert fournisseur.statut.value == StatutFournisseur.actif.value


def test_enum_statut(db):
    fournisseur = Fournisseur(
        nom="Test Fournisseur",
        code="FRN-002",
        type=TypeFournisseur.machine_outil,
        statut=StatutFournisseur.blacklisté,
        adresse="2 rue test",
        ville="Lyon",
        code_postal="69000"
    )
    db.add(fournisseur)
    db.commit()
    db.refresh(fournisseur)

    assert str(fournisseur.statut) == "blacklisté"


def test_unique_code_constraint(db):
    f1 = Fournisseur(
        nom="Fournisseur 1",
        code="FRN-DUPLICATE",
        type=TypeFournisseur.autre,
        statut=StatutFournisseur.actif,
        adresse="3 rue test",
        ville="Metz",
        code_postal="57000"
    )
    f2 = Fournisseur(
        nom="Fournisseur 2",
        code="FRN-DUPLICATE",
        type=TypeFournisseur.autre,
        statut=StatutFournisseur.actif,
        adresse="4 rue test",
        ville="Nancy",
        code_postal="54000"
    )
    db.add(f1)
    db.commit()
    db.add(f2)
    with pytest.raises(exc.IntegrityError):
        db.commit()


def test_repr_fournisseur(db):
    fournisseur = Fournisseur(
        nom="REPR Supplier",
        code="FRN-REPR",
        type=TypeFournisseur.controle_qualite,
        statut=StatutFournisseur.actif,
        adresse="5 rue test",
        ville="Strasbourg",
        code_postal="67000"
    )
    db.add(fournisseur)
    db.commit()
    db.refresh(fournisseur)

    attendu = (
        f"<Fournisseur(id={fournisseur.id}, nom='REPR Supplier', type={TypeFournisseur.controle_qualite}, statut={StatutFournisseur.actif})>"
    )
    assert repr(fournisseur) == attendu