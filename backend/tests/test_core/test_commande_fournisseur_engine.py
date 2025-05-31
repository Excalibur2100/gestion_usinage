import pytest
from datetime import datetime
from backend.core.ia.commande_fournisseur_engine import (
    generer_numero_commande,
    detecter_retard,
    statut_auto,
    suggere_commande_auto
)
from backend.db.schemas.achat.commande_fournisseur_schemas import StatutCommandeFournisseur


def test_generer_numero_commande():
    numero = generer_numero_commande(2024, 12)
    assert numero == "CMD-2024-0012"


def test_detecter_retard():
    assert detecter_retard(datetime(2024, 5, 1), datetime(2024, 5, 2)) is True
    assert detecter_retard(datetime(2024, 5, 1), datetime(2024, 4, 30)) is False


def test_statut_auto():
    assert statut_auto(False, False) == StatutCommandeFournisseur.envoyee
    assert statut_auto(True, False) == StatutCommandeFournisseur.partiellement_livree
    assert statut_auto(False, True) == StatutCommandeFournisseur.livree


def test_suggere_commande_auto():
    result = suggere_commande_auto(fournisseur_id=1, montant=450.0)
    assert result.numero_commande.startswith("AUTO-CMD-")
    assert result.montant_total == 450.0