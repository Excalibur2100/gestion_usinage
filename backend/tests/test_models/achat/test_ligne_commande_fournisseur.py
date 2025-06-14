import pytest
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker, clear_mappers

from backend.db.models.base import Base
from backend.db.models.tables.achat.lignes_commande_fournisseur import (
    LigneCommandeFournisseur,
    StatutLigneCommande
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


def test_create_valid_ligne_commande(db):
    ligne = LigneCommandeFournisseur(
        commande_id=1,
        article_id=None,
        designation="Pièce test",
        description="Test unité",
        quantite=10,
        prix_unitaire_ht=15.0,
        taux_tva=20.0,
        montant_ht=150.0,
        montant_ttc=180.0,
        unite="pièce",
        statut=StatutLigneCommande.recue
    )
    db.add(ligne)
    db.commit()
    db.refresh(ligne)

    assert ligne.id is not None
    assert getattr(ligne, "designation") == "Pièce test"
    assert ligne.statut.value == StatutLigneCommande.recue.value
    assert float(getattr(ligne, "montant_ttc")) == 180.0


def test_enum_statut(db):
    ligne = LigneCommandeFournisseur(
        commande_id=2,
        designation="Autre test",
        quantite=5,
        prix_unitaire_ht=10.0,
        taux_tva=20.0,
        montant_ht=50.0,
        montant_ttc=60.0,
        statut=StatutLigneCommande.non_recue
    )
    db.add(ligne)
    db.commit()
    db.refresh(ligne)

    assert ligne.statut.value == StatutLigneCommande.non_recue.value
    assert ligne.statut.value == "non_recue"


def test_unique_constraint_fails(db):
    ligne1 = LigneCommandeFournisseur(
        commande_id=1,
        designation="Test Duplication",
        quantite=2,
        prix_unitaire_ht=20.0,
        taux_tva=20.0,
        montant_ht=40.0,
        montant_ttc=48.0
    )
    ligne2 = LigneCommandeFournisseur(
        commande_id=1,
        designation="Test Duplication",
        quantite=2,
        prix_unitaire_ht=20.0,
        taux_tva=20.0,
        montant_ht=40.0,
        montant_ttc=48.0
    )
    db.add(ligne1)
    db.commit()
    db.add(ligne2)
    try:
        db.commit()
    except exc.IntegrityError:
        db.rollback()
        assert True
    else:
        assert False, "La contrainte d'intégrité aurait dû échouer"


def test_repr_ligne_commande(db):
    ligne = LigneCommandeFournisseur(
        commande_id=99,
        designation="Repr Ligne",
        quantite=1,
        prix_unitaire_ht=100.0,
        taux_tva=20.0,
        montant_ht=100.0,
        montant_ttc=120.0,
        statut=StatutLigneCommande.annulee
    )
    db.add(ligne)
    db.commit()
    db.refresh(ligne)

    assert repr(ligne) == (
        f"<LigneCommandeFournisseur(id={ligne.id}, designation='Repr Ligne', statut=StatutLigneCommande.annulee)>"
    )