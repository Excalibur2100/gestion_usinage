import pytest
from datetime import datetime

from backend.services.achat.service_metier.avoir_fournisseur_metier_service import (
    calcul_montant_ttc,
    statut_automatique_si_montant,
    suggere_avoir_auto
)

from backend.db.schemas.achat.avoir_fournisseur_schemas import (
    StatutAvoir,
    AvoirFournisseurCreate,
    TypeAvoir
)


def test_calcul_montant_ttc():
    ht = 100.0
    tva = 20.0
    ttc = calcul_montant_ttc(ht, tva)
    assert ttc == 120.0


def test_statut_automatique_si_montant():
    assert statut_automatique_si_montant(100.0) == StatutAvoir.brouillon
    assert statut_automatique_si_montant(0.0) == StatutAvoir.annule


def test_suggere_avoir_auto():
    reference = "AVF-SUGG-001"
    fournisseur_id = 1
    montant_ht = 200.0
    taux_tva = 10.0

    avoir = suggere_avoir_auto(
        reference=reference,
        fournisseur_id=fournisseur_id,
        montant_ht=montant_ht,
        taux_tva=taux_tva
    )

    assert isinstance(avoir, AvoirFournisseurCreate)
    assert avoir.reference == reference
    assert avoir.fournisseur_id == fournisseur_id
    assert avoir.montant_ht == montant_ht
    assert avoir.taux_tva == taux_tva
    assert avoir.montant_ttc == 220.0
    assert avoir.statut == StatutAvoir.brouillon
    assert avoir.type_avoir == TypeAvoir.remise
    assert isinstance(avoir.date_emission, datetime)