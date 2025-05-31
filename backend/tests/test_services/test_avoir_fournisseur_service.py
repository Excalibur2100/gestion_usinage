import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.db.models.base import Base
from backend.services.achat import avoir_fournisseur_service
from backend.db.schemas.achat.avoir_fournisseur_schemas import AvoirFournisseurCreate

@pytest.fixture
def db():
    engine = create_engine("sqlite:///:memory:")
    TestingSessionLocal = sessionmaker(bind=engine)
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    yield session
    session.close()

def test_create_avoir_service(db):
    data = AvoirFournisseurCreate(
        reference="AVF-100",
        reference_externe=None,
        fournisseur_id=1,
        montant_ht=100.0,
        taux_tva=20.0,
        montant_ttc=120.0,
        motif=None
    )
    avoir = avoir_fournisseur_service.creer_avoir(db, data)
    db.refresh(avoir)
    assert avoir.id is not None

def test_delete_avoir_service(db):
    data = AvoirFournisseurCreate(
        reference="AVF-101",
        reference_externe=None,
        fournisseur_id=1,
        montant_ht=50.0,
        taux_tva=20.0,
        montant_ttc=60.0,
        motif=None
    )
    avoir = avoir_fournisseur_service.creer_avoir(db, data)
    db.refresh(avoir)
    result = avoir_fournisseur_service.delete_avoir(db, getattr(avoir, "id"))
    assert "succès" in result["detail"]

def test_bulk_create_delete_service(db):
    data = [
        AvoirFournisseurCreate(
            reference=f"AVF-BULK-{i}",
            reference_externe=None,
            fournisseur_id=1,
            montant_ht=10*i,
            taux_tva=10.0,
            montant_ttc=11*i,
            motif=None
        )
        for i in range(3)
    ]
    objets = avoir_fournisseur_service.bulk_create_avoirs(db, data)
    ids = [getattr(a, "id") for a in objets]
    count = avoir_fournisseur_service.bulk_delete_avoirs(db, ids)
    assert count == 3