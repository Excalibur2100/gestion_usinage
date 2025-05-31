import pytest
from backend.core.ia.avoir_fournisseur_engine import (
    calculer_montant_ttc,
    detecter_type_avoir,
    suggere_avoir_auto
)
from backend.db.schemas.achat.avoir_fournisseur_schemas import TypeAvoir


def test_calcul_montant_ttc():
    assert calculer_montant_ttc(100, 20) == 120.0
    assert calculer_montant_ttc(0, 20) == 0.0
    assert calculer_montant_ttc(150, 10) == 165.0


@pytest.mark.parametrize("motif,expected", [
    ("retour marchandise", TypeAvoir.retour),
    ("geste commercial", TypeAvoir.geste),
    ("remise exceptionnelle", TypeAvoir.remise),
    ("autre cas inconnu", TypeAvoir.autre),
])
def test_detecter_type_avoir(motif, expected):
    assert detecter_type_avoir("", motif) == expected


def test_suggere_avoir_auto():
    avoir = suggere_avoir_auto(facture_id=123, total_rembourse=120.0, raison="retour produit")
    assert avoir.reference.startswith("SUGG-AVF-")
    assert avoir.montant_ttc == 120.0
    assert avoir.type_avoir == TypeAvoir.retour