# backend/tests/test_services/achat/metier_service/test_fournisseur_metier_service.py

import pytest

from backend.services.achat.service_metier.fournisseur_metier_service import (
    verifier_domaine_usinage,
    suggestion_statut_automatique,
    enrichir_creation_fournisseur
)

from backend.db.schemas.achat.fournisseur_schemas import (
    FournisseurCreate,
    TypeFournisseur,
    StatutFournisseur
)


def test_verifier_domaine_usinage_reconnu():
    assert verifier_domaine_usinage(TypeFournisseur.sous_traitant_usinage)
    assert verifier_domaine_usinage(TypeFournisseur.traitement_surface)
    assert verifier_domaine_usinage(TypeFournisseur.logiciel_support)
    assert verifier_domaine_usinage(TypeFournisseur.machine_outil)
    assert verifier_domaine_usinage(TypeFournisseur.metrologie)


def test_verifier_domaine_usinage_non_reconnu():
    assert not verifier_domaine_usinage(TypeFournisseur.autre)
    assert not verifier_domaine_usinage(TypeFournisseur.grossiste)
    assert not verifier_domaine_usinage(TypeFournisseur.fournisseur_generaliste)


@pytest.mark.parametrize("commentaire, attendu", [
    ("Ce fournisseur est blacklist pour fraude", StatutFournisseur.blacklisté),
    ("Entreprise fermée depuis 2022", StatutFournisseur.inactif),
    ("Bon fournisseur, rien à signaler", StatutFournisseur.actif),
    ("", StatutFournisseur.actif),
    (None, StatutFournisseur.actif)
])
def test_suggestion_statut_automatique(commentaire, attendu):
    assert suggestion_statut_automatique(commentaire) == attendu


def test_enrichir_creation_fournisseur_defaults():
    data = FournisseurCreate(
        nom="Fournisseur Test",
        code="FTEST001",
        pays=None,
        commentaire="Fermé temporairement",
        type=TypeFournisseur.prestataire,
        adresse="1 rue du test",
        ville="Metz",
        code_postal="57000",
        email="test@exemple.com",
        telephone="0102030405",
        site_web="https://fournisseur-test.com",
        contact_nom="Jean Dupont",
        contact_email="contact@fournisseur-test.com",
        contact_telephone="0607080910"
    )

    enrichi = enrichir_creation_fournisseur(data)
    assert enrichi.pays == "France"
    assert enrichi.statut == StatutFournisseur.inactif.value or enrichi.statut == StatutFournisseur.inactif