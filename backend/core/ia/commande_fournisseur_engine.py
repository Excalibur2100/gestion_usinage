from datetime import datetime
from backend.db.schemas.achat.commande_fournisseur_schemas import (
    CommandeFournisseurCreate,
    StatutCommandeFournisseur
)

def generer_numero_commande(annee: int, compteur: int) -> str:
    """
    Génère un numéro de commande unique basé sur l'année et un compteur.
    """
    return f"CMD-{annee}-{str(compteur).zfill(4)}"


def detecter_retard(date_prevue: datetime, date_effective: datetime) -> bool:
    """
    Retourne True si la livraison est en retard.
    """
    return date_effective > date_prevue


def statut_auto(depuis_livraison: bool, livree: bool) -> StatutCommandeFournisseur:
    """
    Détermine le statut automatiquement selon livraison.
    """
    if livree:
        return StatutCommandeFournisseur.livree
    if depuis_livraison:
        return StatutCommandeFournisseur.partiellement_livree
    return StatutCommandeFournisseur.envoyee


def suggere_commande_auto(fournisseur_id: int, montant: float) -> CommandeFournisseurCreate:
    """
    Simule la génération automatique d'une commande.
    """
    return CommandeFournisseurCreate(
        numero_commande="AUTO-CMD-0001",
        fournisseur_id=fournisseur_id,
        montant_total=montant,
        devise="EUR"
    )