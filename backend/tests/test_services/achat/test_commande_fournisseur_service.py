import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.db.models.base import Base
from backend.db.schemas.achat.commande_fournisseur_schemas import CommandeFournisseurCreate
from backend.services.achat import commande_fournisseur_service


@pytest.fixture
def db():
    engine = create_engine("sqlite:///:memory:")
    TestingSessionLocal = sessionmaker(bind=engine)
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    yield session
    session.close()


def test_create_commande(db):
    data = CommandeFournisseurCreate(
        numero_commande="CMD-TEST-001",
        reference_externe=None,
        fournisseur_id=1,
        montant_total=100.0
    )
    commande = commande_fournisseur_service.creer_commande(db, data)
    db.refresh(commande)

    assert commande.id is not None
    assert getattr(commande, "numero_commande") == "CMD-TEST-001"


def test_delete_commande(db):
    data = CommandeFournisseurCreate(
        numero_commande="CMD-TEST-002",
        reference_externe=None,
        fournisseur_id=1,
        montant_total=150.0
    )
    commande = commande_fournisseur_service.creer_commande(db, data)
    db.refresh(commande)

    result = commande_fournisseur_service.delete_commande(db, getattr(commande, "id"))
    assert "succès" in result["detail"]


def test_bulk_create_delete(db):
    data = [
        CommandeFournisseurCreate(
            numero_commande=f"CMD-BULK-{i}",
            reference_externe=None,
            fournisseur_id=1,
            montant_total=20.0 * i
        ) for i in range(1, 4)
    ]
    commandes = commande_fournisseur_service.bulk_create_commandes(db, data)

    # Recharger les objets pour obtenir les IDs
    ids = [getattr(db.merge(c), "id") for c in commandes]

    count = commande_fournisseur_service.bulk_delete_commandes(db, ids)
    assert count == 3