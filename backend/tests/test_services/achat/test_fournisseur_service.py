import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.db.models.base import Base
from backend.db.schemas.achat.fournisseur_schemas import (
    FournisseurCreate,
    FournisseurUpdate,
    FournisseurSearch,
    StatutFournisseur,
    TypeFournisseur
)
from backend.services.achat import fournisseur_services


@pytest.fixture
def db():
    engine = create_engine("sqlite:///:memory:")
    TestingSessionLocal = sessionmaker(bind=engine)
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    yield session
    session.close()


def test_create_fournisseur_service(db):
    data = FournisseurCreate(
        nom="Fournisseur Service",
        code="FRN-SVC-001",
        type=TypeFournisseur("fournisseur_outillage"),
        statut=StatutFournisseur.actif,
        pays="France",
        ville="Paris",
        code_postal="75000",
        adresse="12 rue des Tests",
        email="service@example.com",
        telephone="0123456789",
        site_web="https://fournisseur-service.com",
        contact_nom="Jean Dupont",
        contact_email="contact@fournisseur-service.com",
        contact_telephone="0987654321"
    )
    f = fournisseur_services.creer_fournisseur(db, data)
    assert getattr(f, "nom") == "Fournisseur Service"
    assert getattr(f, "code") == "FRN-SVC-001"


def test_update_fournisseur_service(db):
    data = FournisseurCreate(
        nom="Fournisseur Update",
        code="FRN-SVC-002",
        type=TypeFournisseur("metrologie"),
        statut=StatutFournisseur.actif,
        adresse="1 rue machine",
        ville="Nancy",
        code_postal="54000",
        pays="France",
        email="update@example.com",
        telephone=None,
        site_web=None,
        contact_nom=None,
        contact_email=None,
        contact_telephone=None
    )
    f = fournisseur_services.creer_fournisseur(db, data)
    db.refresh(f)

    update_data = FournisseurUpdate(
        commentaire="Mis à jour via test",
        statut=StatutFournisseur.inactif
    )
    updated = fournisseur_services.update_fournisseur(db, getattr(f, "id"), update_data)
    assert getattr(updated, "commentaire", None) == "Mis à jour via test"
    assert getattr(updated, "statut", None) == StatutFournisseur.inactif.value or getattr(updated, "statut", None) == StatutFournisseur.inactif


def test_list_fournisseurs_service(db):
    data = FournisseurCreate(
        nom="Fournisseur List",
        code="FRN-SVC-003",
        type=TypeFournisseur("fabricant_machines"),
        statut=StatutFournisseur.actif,
        adresse="2 zone industrielle",
        ville="Metz",
        code_postal="57000",
        pays="France",
        email=None,
        telephone=None,
        site_web=None,
        contact_nom=None,
        contact_email=None,
        contact_telephone=None
    )
    fournisseur_services.creer_fournisseur(db, data)
    results = fournisseur_services.list_fournisseurs(db, skip=0, limit=10)
    assert isinstance(results, list)
    assert len(results) >= 1


def test_delete_fournisseur_service(db):
    data = FournisseurCreate(
        nom="Fournisseur Delete",
        code="FRN-SVC-004",
        type=TypeFournisseur("sous_traitant_usinage"),
        adresse="1 rue machine",
        ville="Nancy",
        code_postal="54000",
        pays="France",
        email=None,
        telephone=None,
        site_web=None,
        contact_nom=None,
        contact_email=None,
        contact_telephone=None
    )
    f = fournisseur_services.creer_fournisseur(db, data)
    db.refresh(f)
    result = fournisseur_services.delete_fournisseur(db, getattr(f, "id"))
    assert "supprimé" in result["detail"]


def test_search_fournisseur_service(db):
    data = FournisseurCreate(
        nom="Fournisseur Search",
        code="FRN-SVC-005",
        type=TypeFournisseur("peinture_industrielle"),
        commentaire="fournisseur pour test",
        adresse="zone peinture",
        ville="Toul",
        code_postal="54200",
        pays="France",
        email=None,
        telephone=None,
        site_web=None,
        contact_nom=None,
        contact_email=None,
        contact_telephone=None
    )
    fournisseur_services.creer_fournisseur(db, data)

    filters = FournisseurSearch(nom="Search")
    result = fournisseur_services.search_fournisseurs(db, filters, skip=0, limit=10)
    assert result["total"] >= 1
    assert isinstance(result["results"], list)