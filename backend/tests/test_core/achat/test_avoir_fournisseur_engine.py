import pytest
from datetime import datetime

from backend.core.ia.achat.avoir_fournisseur_engine import (
    calculer_montant_ttc,
    detecter_type_avoir,
    statut_automatique_si_montant,
    suggere_avoir_auto
)

from backend.db.schemas.achat.avoir_fournisseur_schemas import StatutAvoir, TypeAvoir


def test_calculer_montant_ttc():
    ht = 100.0
    tva = 20.0
    ttc = calculer_montant_ttc(ht, tva)
    assert ttc == 120.0


@pytest.mark.parametrize("reference,motif,expected", [
    ("RET-001", "retour produit", TypeAvoir.retour),
    ("REM-2024", "remise exceptionnelle", TypeAvoir.remise),
    ("GESTE-01", "geste commercial", TypeAvoir.geste),
    ("AUTRE", "autre chose", TypeAvoir.autre),
])
def test_detecter_type_avoir(reference, motif, expected):
    assert detecter_type_avoir(reference, motif) == expected


def test_statut_automatique_si_montant():
    assert statut_automatique_si_montant(150.0) == StatutAvoir.brouillon
    assert statut_automatique_si_montant(0.0) == StatutAvoir.annule


def test_suggere_avoir_auto():
    avoir = suggere_avoir_auto(
        reference="AVF-AUTO-001",
        fournisseur_id=1,
        montant_ht=100.0,
        taux_tva=20.0
    )

    assert avoir.reference == "AVF-AUTO-001"
    assert avoir.fournisseur_id == 1
    assert avoir.montant_ht == 100.0
    assert avoir.taux_tva == 20.0
    assert avoir.montant_ttc == 120.0
    assert avoir.statut == StatutAvoir.brouillon
    assert isinstance(avoir.date_emission, datetime)