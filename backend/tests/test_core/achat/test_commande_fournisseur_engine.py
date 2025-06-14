import pytest
from datetime import datetime, timedelta

from backend.core.ia.achat.commande_fournisseur_engine import (
    calcul_montant_total_commande,
    generer_numero_commande_auto,
    statut_auto_commande,
    suggestion_commande_auto
)

from backend.db.schemas.achat.commande_fournisseur_schemas import (
    CommandeFournisseurCreate,
    StatutCommandeFournisseur
)


def test_calcul_montant_total_commande():
    lignes: list[tuple[str, int, float]] = [("Produit A", 2, 10.0), ("Produit B", 1, 25.0)]
    total = calcul_montant_total_commande(lignes)
    assert total == 45.0


def test_calcul_montant_total_commande_vide():
    assert calcul_montant_total_commande([]) == 0.0


def test_generer_numero_commande_auto():
    numero = generer_numero_commande_auto()
    assert numero.startswith("CMD-AUTO-")
    assert len(numero) > 10


def test_statut_auto_commande():
    future_date = datetime.utcnow() + timedelta(days=3)
    past_date = datetime.utcnow() - timedelta(days=3)

    assert statut_auto_commande(future_date) == StatutCommandeFournisseur.envoyee
    assert statut_auto_commande(past_date) == StatutCommandeFournisseur.livree


def test_suggestion_commande_auto():
    suggestion = suggestion_commande_auto(
        fournisseur_id=1,
        lignes=[("Ref1", 2, 10.0), ("Ref2", 1, 20.0)],
        cree_par=1
    )

    assert isinstance(suggestion, CommandeFournisseurCreate)
    assert suggestion.fournisseur_id == 1
    assert suggestion.montant_total == 40.0
    assert suggestion.numero_commande.startswith("CMD-AUTO-")
    assert suggestion.statut in [
        StatutCommandeFournisseur.envoyee,
        StatutCommandeFournisseur.livree
    ]