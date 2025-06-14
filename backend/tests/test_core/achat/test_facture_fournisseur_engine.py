import pytest
from datetime import datetime, timedelta

from backend.core.ia.achat.facture_fournisseur_engine import (
    calcul_montant_ttc,
    generer_numero_facture_auto,
    statut_automatique,
    suggere_facture_auto
)

from backend.db.schemas.achat.facture_fournisseur_schemas import (
    FactureFournisseurCreate,
    StatutFactureFournisseur
)


def test_calcul_montant_ttc():
    ht = 100.0
    tva = 20.0
    ttc = calcul_montant_ttc(ht, tva)
    assert ttc == 120.0


def test_generer_numero_facture_auto_unique():
    n1 = generer_numero_facture_auto()
    n2 = generer_numero_facture_auto()
    assert n1.startswith("FACT-AUTO-")
    assert n2.startswith("FACT-AUTO-")
    assert n1 != n2


def test_statut_automatique_en_retard():
    past_date = datetime.utcnow() - timedelta(days=5)
    assert statut_automatique(past_date) == StatutFactureFournisseur.en_retard


def test_statut_automatique_brouillon():
    future_date = datetime.utcnow() + timedelta(days=5)
    assert statut_automatique(future_date) == StatutFactureFournisseur.brouillon

    assert statut_automatique(None) == StatutFactureFournisseur.brouillon


def test_suggere_facture_auto():
    suggestion = suggere_facture_auto(
        fournisseur_id=1,
        montant_ht=100.0,
        taux_tva=20.0,
        devise="EUR",
        reference="AUTO-TEST"
    )

    assert isinstance(suggestion, FactureFournisseurCreate)
    assert suggestion.fournisseur_id == 1
    assert suggestion.montant_ht == 100.0
    assert suggestion.taux_tva == 20.0
    assert suggestion.montant_ttc == 120.0
    assert suggestion.devise == "EUR"
    assert suggestion.reference_externe == "AUTO-TEST"
    assert suggestion.numero_facture.startswith("FACT-AUTO-")
    assert suggestion.statut in [StatutFactureFournisseur.brouillon, StatutFactureFournisseur.en_retard]
    assert isinstance(suggestion.date_facture, datetime)
    assert isinstance(suggestion.date_echeance, datetime)