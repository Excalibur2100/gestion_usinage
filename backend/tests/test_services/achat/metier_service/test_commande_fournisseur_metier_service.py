from backend.services.achat.service_metier.commande_fournisseur_metier_service import (
    statut_initial,
    suggere_commande_auto
)
from backend.db.schemas.achat.commande_fournisseur_schemas import StatutCommandeFournisseur


def test_statut_initial():
    assert statut_initial(True) == StatutCommandeFournisseur.envoyee
    assert statut_initial(False) == StatutCommandeFournisseur.brouillon


def test_suggere_commande_auto():
    cmd = suggere_commande_auto("CMD-001", 1, 1000.0)
    assert cmd.numero_commande == "CMD-001"
    assert cmd.fournisseur_id == 1
    assert cmd.statut == StatutCommandeFournisseur.brouillon