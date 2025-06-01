import pytest
from datetime import datetime, timedelta
from time import sleep

from backend.services.achat.service_metier.commande_fournisseur_metier_service import (
    calcul_date_livraison_prevue,
    generer_numero_commande_automatique,
    statut_automatique_si_livraison,
    suggere_commande_auto,
    verifier_montant_total
)

from backend.db.schemas.achat.commande_fournisseur_schemas import (
    StatutCommandeFournisseur,
    CommandeFournisseurCreate
)


def test_calcul_date_livraison_par_defaut():
    base = datetime.utcnow()
    livraison = calcul_date_livraison_prevue(base)
    assert isinstance(livraison, datetime)
    assert livraison.date() == (base + timedelta(days=5)).date()


def test_calcul_date_livraison_personnalisee():
    base = datetime(2024, 1, 1)
    livraison = calcul_date_livraison_prevue(base, delai_jours=10)
    assert livraison == datetime(2024, 1, 11)


def test_statut_auto_si_livraison():
    assert statut_automatique_si_livraison(True) == StatutCommandeFournisseur.livree
    assert statut_automatique_si_livraison(False) == StatutCommandeFournisseur.envoyee


def test_verifier_montant_total():
    assert verifier_montant_total(0) is True
    assert verifier_montant_total(99.99) is True
    assert verifier_montant_total(-1.0) is False


def test_generer_numero_commande_auto_unique():
    n1 = generer_numero_commande_automatique()
    sleep(0.001)  # éviter timestamp identique
    n2 = generer_numero_commande_automatique()
    assert n1.startswith("CMD-AUTO-")
    assert n2.startswith("CMD-AUTO-")
    assert n1 != n2


def test_suggere_commande_auto_complet():
    commande = suggere_commande_auto(
        fournisseur_id=42,
        montant_total=500.0,
        devise="USD"
    )
    assert isinstance(commande, CommandeFournisseurCreate)
    assert commande.fournisseur_id == 42
    assert commande.montant_total == 500.0
    assert commande.devise == "USD"
    assert commande.numero_commande.startswith("CMD-AUTO-")
    assert commande.statut == StatutCommandeFournisseur.brouillon
    assert isinstance(commande.date_commande, datetime)
    assert commande.commentaire == "Commande générée automatiquement"