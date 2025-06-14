import pytest

from backend.services.achat.service_metier.ligne_commande_fournisseur_metier_service import (
    calcul_montant_ttc,
    statut_ligne_automatique,
    enrichir_ligne_commande_fournisseur
)

from backend.db.schemas.achat.ligne_commande_fournisseur_schemas import (
    LigneCommandeFournisseurCreate,
    StatutLigneCommande
)


def test_calcul_montant_ttc():
    montant = calcul_montant_ttc(qte=5, pu_ht=20, tva=20)
    assert montant == 120.0


@pytest.mark.parametrize("quantite, quantite_recue, attendu", [
    (10, 0, StatutLigneCommande.non_recue),
    (10, 5, StatutLigneCommande.partiellement_recue),
    (10, 10, StatutLigneCommande.recue)
])
def test_statut_ligne_automatique(quantite, quantite_recue, attendu):
    assert statut_ligne_automatique(quantite, quantite_recue) == attendu


def test_enrichir_ligne_commande_fournisseur():
    ligne = LigneCommandeFournisseurCreate(
        commande_id=1,
        designation="Axe trempé Ø20",
        quantite=10,
        prix_unitaire_ht=15,
        taux_tva=20,
        montant_ht=150,
        montant_ttc=0,  # volontairement faux
        unite="pièce",
        article_id=None,
        description="Test",
        commentaire=None,
        cree_par=1
    )
    enrichi = enrichir_ligne_commande_fournisseur(ligne)

    assert enrichi.montant_ttc == 180.0
    assert enrichi.statut == StatutLigneCommande.recue or enrichi.statut == StatutLigneCommande.non_recue