import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.db.models.base import Base
from backend.db.schemas.achat.facture_fournisseur_schemas import FactureFournisseurCreate, StatutFactureFournisseur
from backend.services.achat.facture_fournisseur_service import (
    creer_facture,
    delete_facture,
    update_facture,
    list_factures
)

@pytest.fixture
def db():
    engine = create_engine("sqlite:///:memory:")
    TestingSessionLocal = sessionmaker(bind=engine)
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    yield session
    session.close()

def test_create_facture(db):
    data = FactureFournisseurCreate(
        numero_facture="FACT-001",
        fournisseur_id=1,
        montant_ht=100.0,
        taux_tva=20.0,
        montant_ttc=120.0,
        statut=StatutFactureFournisseur.brouillon,
        reference_externe="REF-001",
        utilisateur_id=1,
        commande_id=1
    )
    facture = creer_facture(db, data)
    db.refresh(facture)
    
    assert facture.id is not None
    assert str(facture.numero_facture) == "FACT-001"
    assert float(getattr(facture, "montant_ttc")) == 120.0
    assert str(facture.statut) == StatutFactureFournisseur.brouillon.value

def test_delete_facture(db):
    data = FactureFournisseurCreate(
        numero_facture="FACT-002",
        fournisseur_id=1,
        montant_ht=150.0,
        taux_tva=20.0,
        montant_ttc=180.0,
        statut=StatutFactureFournisseur.brouillon,
        reference_externe="REF-002",
        utilisateur_id=1,
        commande_id=1
    )
    facture = creer_facture(db, data)
    db.refresh(facture)
    
    result = delete_facture(db, getattr(facture, "id"))
    assert "succès" in result["detail"]

def test_update_facture(db):
    data = FactureFournisseurCreate(
        numero_facture="FACT-003",
        fournisseur_id=1,
        montant_ht=80.0,
        taux_tva=20.0,
        montant_ttc=96.0,
        statut=StatutFactureFournisseur.brouillon,
        reference_externe="REF-003",
        utilisateur_id=1,
        commande_id=1
    )
    facture = creer_facture(db, data)
    db.refresh(facture)
    
    update_data = {
        "montant_ttc": 100.0,
        "statut": "validee"
    }
    from backend.db.schemas.achat.facture_fournisseur_schemas import FactureFournisseurUpdate
    update_schema = FactureFournisseurUpdate(**update_data)
    updated_facture = update_facture(db, getattr(facture, "id"), update_schema)
    db.refresh(updated_facture)
    assert float(getattr(updated_facture, "montant_ttc")) == 100.0
    assert str(updated_facture.statut) == "validee"

def test_list_factures(db):
    data = FactureFournisseurCreate(
        numero_facture="FACT-004",
        fournisseur_id=1,
        montant_ht=200.0,
        taux_tva=20.0,
        montant_ttc=240.0,
        statut=StatutFactureFournisseur.brouillon,
        reference_externe="REF-004",
        utilisateur_id=1,
        commande_id=1
    )
    creer_facture(db, data)
    
    factures = list_factures(db, skip=0, limit=10)
    assert len(factures) > 0
    assert str(factures[0].numero_facture) == "FACT-004"