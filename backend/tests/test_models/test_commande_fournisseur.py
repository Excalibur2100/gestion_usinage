import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers
from backend.db.models.base import Base
from backend.db.models.tables.achat.commande_fournisseur import CommandeFournisseur, StatutCommandeFournisseur

@pytest.fixture
def db():
    engine = create_engine("sqlite:///:memory:")
    TestingSessionLocal = sessionmaker(bind=engine)
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    yield session
    session.close()
    clear_mappers()

def test_creation_commande_valide(db):
    commande = CommandeFournisseur(
        numero_commande="CMD-TEST-001",
        fournisseur_id=1,
        montant_total=500.0,
        statut=StatutCommandeFournisseur.brouillon,
        devise="EUR"
    )
    db.add(commande)
    db.commit()
    db.refresh(commande)
    assert commande.id is not None
    assert getattr(commande, "numero_commande") == "CMD-TEST-001"