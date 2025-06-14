# backend/core/ia/ligne_commande_fournisseur_engine.py

from typing import Optional
from backend.db.schemas.achat.ligne_commande_fournisseur_schemas import (
    LigneCommandeFournisseurCreate,
    StatutLigneCommande
)


def calcul_montant_ttc(qte: float, pu_ht: float, tva: float = 20.0) -> float:
    """
    Calcule le montant TTC d’une ligne de commande.
    """
    montant_ht = qte * pu_ht
    montant_ttc = round(montant_ht * (1 + tva / 100), 2)
    return montant_ttc


def statut_ligne_automatique(qte_commandee: float, qte_recue: Optional[float]) -> StatutLigneCommande:
    """
    Déduit automatiquement le statut d’une ligne de commande.
    """
    if qte_recue is None or qte_recue == 0:
        return StatutLigneCommande.non_recue
    elif qte_recue < qte_commandee:
        return StatutLigneCommande.partiellement_recue
    return StatutLigneCommande.recue


def enrichir_ligne_commande_fournisseur(data: LigneCommandeFournisseurCreate) -> LigneCommandeFournisseurCreate:
    """
    Applique des règles métier avant création : calcul montant, statut automatique.
    """
    data.montant_ttc = calcul_montant_ttc(data.quantite, data.prix_unitaire_ht, data.taux_tva or 20.0)
    data.statut = statut_ligne_automatique(data.quantite, getattr(data, "quantite_recue", 0))
    return data