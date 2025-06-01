import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.db.models.base import Base
from backend.db.models.tables.achat.avoir_fournisseur import AvoirFournisseur, StatutAvoir
from backend.services.achat import avoir_fournisseur_service
from backend.db.schemas.achat.avoir_fournisseur_schemas import AvoirFournisseurCreate, AvoirFournisseurBulkCreate, AvoirFournisseurBulkDelete


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
        motif="Création"
    )
    avoir = avoir_fournisseur_service.creer_avoir(db, data)
    db.refresh(avoir)
    assert avoir.id is not None
    assert float(getattr(avoir, "montant_ttc")) == 120.0


def test_delete_avoir_service(db):
    data = AvoirFournisseurCreate(
        reference="AVF-101",
        reference_externe=None,
        fournisseur_id=1,
        montant_ht=50.0,
        taux_tva=20.0,
        montant_ttc=60.0,
        motif="Suppression"
    )
    avoir = avoir_fournisseur_service.creer_avoir(db, data)
    db.refresh(avoir)
    result = avoir_fournisseur_service.delete_avoir(db, getattr(avoir, "id"))
    assert "succès" in result["detail"]


def test_update_avoir_service(db):
    from backend.db.schemas.achat.avoir_fournisseur_schemas import AvoirFournisseurUpdate

    data = AvoirFournisseurCreate(
        reference="AVF-102",
        reference_externe=None,
        fournisseur_id=1,
        montant_ht=80.0,
        taux_tva=20.0,
        montant_ttc=96.0,
        commentaire="Ancien",
        motif="Initial"
    )
    avoir = avoir_fournisseur_service.creer_avoir(db, data)
    db.refresh(avoir)

    # Crée un schéma d'update à partir d'un dict bien typé
    update_data = AvoirFournisseurUpdate(
        commentaire="Mis à jour",
        motif="Modifié",
        modifie_par=None,
        is_archived=None,
        statut=None,
        tag=None,
        categorie=None
    )

    updated = avoir_fournisseur_service.update_avoir(db, int(getattr(avoir, "id")), update_data)

    assert getattr(updated, "commentaire") == "Mis à jour"
    assert getattr(updated, "motif") == "Modifié"


def test_bulk_create_delete_service(db):
    data = [
        AvoirFournisseurCreate(
            reference=f"AVF-BULK-{i}",
            reference_externe=None,
            fournisseur_id=1,
            montant_ht=10 * i,
            taux_tva=20.0,
            montant_ttc=12 * i,
            motif="Bulk"
        )
        for i in range(1, 4)
    ]
    objets = avoir_fournisseur_service.bulk_create_avoirs(db, data)
    ids = [getattr(a, "id") for a in objets]
    count = avoir_fournisseur_service.bulk_delete_avoirs(db, ids)
    assert count == 3


def test_list_and_search_service(db):
    data = AvoirFournisseurCreate(
        reference="AVF-SEARCH-001",
        reference_externe=None,
        fournisseur_id=1,
        montant_ht=100.0,
        taux_tva=10.0,
        montant_ttc=110.0,
        motif="Recherche"
    )
    avoir_fournisseur_service.creer_avoir(db, data)
    from backend.db.schemas.achat.avoir_fournisseur_schemas import AvoirFournisseurSearch
    filters = AvoirFournisseurSearch(reference="SEARCH")
    results = avoir_fournisseur_service.search_avoirs(db, filters=filters, skip=0, limit=10)
    assert results["total"] >= 1
    assert isinstance(results["results"], list)