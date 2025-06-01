import pytest
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker, clear_mappers
from backend.db.models.base import Base
from backend.db.models.tables.achat.avoir_fournisseur import AvoirFournisseur, StatutAvoir


@pytest.fixture
def db():
    engine = create_engine("sqlite:///:memory:")
    TestingSessionLocal = sessionmaker(bind=engine)
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    yield session
    session.close()
    clear_mappers()


def test_create_valid_avoir(db):
    """Créer un avoir fournisseur valide."""
    avoir = AvoirFournisseur(
        reference="AVF-001",
        reference_externe=None,
        fournisseur_id=1,
        montant_ht=100.0,
        taux_tva=20.0,
        montant_ttc=120.0,
        statut=StatutAvoir.brouillon,
        motif=None
    )
    db.add(avoir)
    db.commit()
    db.refresh(avoir)

    assert avoir.id is not None
    assert float(getattr(avoir, "montant_ttc")) == 120.0
    assert str(avoir.statut) == str(StatutAvoir.brouillon)


def test_enum_statut(db):
    """Test de validité du statut."""
    avoir = AvoirFournisseur(
        reference="AVF-002",
        reference_externe=None,
        fournisseur_id=1,
        montant_ht=50.0,
        taux_tva=10.0,
        montant_ttc=55.0,
        statut=StatutAvoir.valide,
        motif=None
    )
    db.add(avoir)
    db.commit()
    db.refresh(avoir)

    assert str(avoir.statut) == str(StatutAvoir.valide)


def test_constraint_montant_ht_negative(db):
    """Doit lever une exception si le montant HT est négatif."""
    with pytest.raises(exc.IntegrityError):
        avoir = AvoirFournisseur(
            reference="AVF-BAD",
            reference_externe=None,
            fournisseur_id=1,
            montant_ht=-10,
            taux_tva=20.0,
            montant_ttc=12.0,
            statut=StatutAvoir.brouillon,
            motif=None
        )
        db.add(avoir)
        db.commit()


def test_repr_affichage(db):
    """Test du __repr__ de l'objet."""
    avoir = AvoirFournisseur(
        reference="AVF-TEST",
        reference_externe=None,
        fournisseur_id=123,
        montant_ht=10.0,
        taux_tva=20.0,
        montant_ttc=12.0,
        statut=StatutAvoir.valide
    )
    db.add(avoir)
    db.commit()
    db.refresh(avoir)

    assert repr(avoir) == f"<AvoirFournisseur(id={avoir.id}, ref='AVF-TEST', fournisseur_id=123)>"