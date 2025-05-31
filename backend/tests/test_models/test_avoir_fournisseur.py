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

def test_enum_statut(db):
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
    assert str(avoir.statut) == str(StatutAvoir.valide.value)

def test_constraint_montant_ht_negative(db):
    with pytest.raises(exc.IntegrityError):
        db.add(AvoirFournisseur(
            reference="AVF-BAD",
            reference_externe=None,
            fournisseur_id=1,
            montant_ht=-10,
            taux_tva=20.0,
            montant_ttc=12.0,
            statut=StatutAvoir.brouillon,
            motif=None
        ))
        db.commit()