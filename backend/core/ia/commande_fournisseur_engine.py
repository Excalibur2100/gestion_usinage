# backend/core/ia/commande_fournisseur_engine.py

from datetime import datetime
from typing import List, Tuple

from backend.db.schemas.achat.commande_fournisseur_schemas import (
    CommandeFournisseurCreate,
    StatutCommandeFournisseur
)


def calcul_montant_total_commande(lignes: List[Tuple[str, int, float]]) -> float:
    """
    Calcule le montant total à partir des lignes de commande :
    (reference_produit, quantité, prix_unitaire)
    """
    return round(sum(qte * prix for _, qte, prix in lignes), 2)


def generer_numero_commande_auto() -> str:
    """
    Génère un numéro de commande automatique unique.
    """
    return f"CMD-AUTO-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}"


def statut_auto_commande(date_livraison_prevue: datetime) -> StatutCommandeFournisseur:
    """
    Déduit un statut automatique en fonction de la date prévue de livraison.
    """
    if date_livraison_prevue < datetime.utcnow():
        return StatutCommandeFournisseur.livree
    return StatutCommandeFournisseur.envoyee


def suggestion_commande_auto(
    fournisseur_id: int,
    lignes: List[Tuple[str, int, float]],
    cree_par: int
) -> CommandeFournisseurCreate:
    """
    Génère automatiquement une commande fournisseur basée sur une suggestion simple.
    """
    montant = calcul_montant_total_commande(lignes)
    date_commande = datetime.utcnow()
    date_livraison = date_commande.replace(day=date_commande.day + 3)
    statut = statut_auto_commande(date_livraison)

    return CommandeFournisseurCreate(
        numero_commande=generer_numero_commande_auto(),
        reference_externe=None,
        fournisseur_id=fournisseur_id,
        utilisateur_id=None,
        commentaire="Commande générée automatiquement",
        statut=statut,
        date_commande=date_commande,
        date_livraison_prevue=date_livraison,
        montant_total=montant,
        devise="EUR",
        cree_par=cree_par
    )