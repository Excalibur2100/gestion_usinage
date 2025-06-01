import pytest
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker, clear_mappers

from backend.db.models.base import Base
from backend.db.models.tables.achat.facture_fournisseur import (
    FactureFournisseur,
    StatutFactureFournisseur
)


@pytest.fixture
def db():
    engine = create_engine("sqlite:///:memory:")
    TestingSessionLocal = sessionmaker(bind=engine)
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    yield session
    session.close()
    clear_mappers()


def test_create_valid_facture(db):
    facture = FactureFournisseur(
        numero_facture="FACT-001",
        fournisseur_id=1,
        montant_ht=100.0,
        taux_tva=20.0,
        montant_ttc=120.0,
        statut=StatutFactureFournisseur.brouillon
    )
    db.add(facture)
    db.commit()
    db.refresh(facture)

    assert facture.id is not None
    assert str(facture.numero_facture) == "FACT-001"
    assert float(getattr(facture, "montant_ttc")) == 120.0
    assert facture.statut.value == StatutFactureFournisseur.brouillon.value


def test_enum_statut_facture(db):
    facture = FactureFournisseur(
        numero_facture="FACT-002",
        fournisseur_id=1,
        montant_ht=50.0,
        taux_tva=10.0,
        montant_ttc=55.0,
        statut=StatutFactureFournisseur.validee
    )
    db.add(facture)
    db.commit()
    db.refresh(facture)

    assert facture.statut.value == "validee"


def test_constraint_montant_negatif(db):
    with pytest.raises(exc.IntegrityError):
        db.add(FactureFournisseur(
            numero_facture="FACT-NEG",
            fournisseur_id=1,
            montant_ht=-10.0,
            taux_tva=20.0,
            montant_ttc=12.0,
            statut=StatutFactureFournisseur.brouillon
        ))
        db.commit()


def test_repr_facture(db):
    facture = FactureFournisseur(
        numero_facture="FACT-REPR",
        fournisseur_id=42,
        montant_ht=100.0,
        taux_tva=20.0,
        montant_ttc=120.0,
        statut=StatutFactureFournisseur.payee
    )
    db.add(facture)
    db.commit()
    db.refresh(facture)

    assert repr(facture) == f"<FactureFournisseur(id={facture.id}, numero='FACT-REPR', fournisseur_id=42)>"