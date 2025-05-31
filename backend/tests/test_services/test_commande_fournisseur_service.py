import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.db.models.base import Base
from backend.services.achat import commande_fournisseur_service
from backend.db.schemas.achat.commande_fournisseur_schemas import CommandeFournisseurCreate

@pytest.fixture
def db():
    engine = create_engine("sqlite:///:memory:")
    TestingSessionLocal = sessionmaker(bind=engine)
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    yield session
    session.close()

def test_creer_commande(db):
    data = CommandeFournisseurCreate(
        numero_commande="CMD-UNIT-001",
        fournisseur_id=1,
        montant_total=1000.0,
        devise="EUR"
    )
    commande = commande_fournisseur_service.creer_commande(db, data)
    assert commande.id is not None
    assert getattr(commande, "numero_commande", None) == "CMD-UNIT-001"

def test_delete_commande(db):
    data = CommandeFournisseurCreate(
        numero_commande="CMD-DEL-001",
        fournisseur_id=1,
        montant_total=300.0,
        devise="EUR"
    )
    commande = commande_fournisseur_service.creer_commande(db, data)
    result = commande_fournisseur_service.delete_commande(db, getattr(commande, "id"))
    assert "succès" in result["detail"]
