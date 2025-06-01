import pytest
from datetime import datetime

from backend.services.achat.service_metier.facture_fournisseur_metier_service import (
    calcul_montant_ttc,
    generer_numero_facture_auto,
    suggere_facture_auto,
    statut_auto_si_retard
)

from backend.db.schemas.achat.facture_fournisseur_schemas import (
    StatutFactureFournisseur,
    FactureFournisseurCreate
)


def test_calcul_montant_ttc():
    assert calcul_montant_ttc(100, 20) == 120.0
    assert calcul_montant_ttc(0, 20) == 0.0
    assert calcul_montant_ttc(50, 10) == 55.0


def test_generer_numero_facture_auto():
    numero = generer_numero_facture_auto()
    assert numero.startswith("FACT-AUTO-")
    assert len(numero) > 10


def test_statut_auto_si_retard():
    date_passee = datetime(2020, 1, 1)
    assert statut_auto_si_retard(date_passee) == StatutFactureFournisseur.en_retard

    aujourd_hui = datetime.utcnow()
    assert statut_auto_si_retard(aujourd_hui) == StatutFactureFournisseur.brouillon


def test_suggere_facture_auto():
    facture = suggere_facture_auto(
        fournisseur_id=1,
        montant_ht=100.0,
        taux_tva=20.0,
        devise="EUR",
        reference="TEST-REF-001"
    )

    assert isinstance(facture, FactureFournisseurCreate)
    assert facture.montant_ttc == 120.0
    assert facture.statut in [StatutFactureFournisseur.brouillon, StatutFactureFournisseur.en_retard]
    assert facture.fournisseur_id == 1
    assert facture.devise == "EUR"
    assert isinstance(facture.date_facture, datetime)