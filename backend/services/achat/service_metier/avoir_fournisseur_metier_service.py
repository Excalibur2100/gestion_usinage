from backend.db.schemas.achat.avoir_fournisseur_schemas import (
    AvoirFournisseurCreate,
    StatutAvoir,
    TypeAvoir
)
from datetime import datetime


def statut_automatique_si_montant(montant: float) -> StatutAvoir:
    """
    Détermine automatiquement le statut d’un avoir en fonction de son montant.
    
    - Si montant > 0 → brouillon
    - Sinon → annulé (peut être utilisé pour les contrôles ou rejets auto)
    """
    return StatutAvoir.brouillon if montant > 0 else StatutAvoir.annule


def calcul_montant_ttc(montant_ht: float, taux_tva: float = 20.0) -> float:
    """
    Calcule le montant TTC à partir du montant HT et du taux de TVA.
    
    Args:
        montant_ht (float): Montant hors taxe.
        taux_tva (float): Taux de TVA applicable.

    Returns:
        float: Montant TTC arrondi à 2 décimales.
    """
    return round(montant_ht * (1 + taux_tva / 100), 2)


def suggere_avoir_auto(
    reference: str,
    fournisseur_id: int,
    montant_ht: float,
    taux_tva: float = 20.0
) -> AvoirFournisseurCreate:
    """
    Génère un schéma AvoirFournisseurCreate pré-rempli de façon automatique,
    à partir d’un montant HT et d’un taux de TVA.
    
    Utilisé dans des cas d’IA métier ou suggestions rapides pour les utilisateurs.

    Args:
        reference (str): Référence de l’avoir.
        fournisseur_id (int): ID du fournisseur.
        montant_ht (float): Montant hors taxe.
        taux_tva (float): Taux de TVA applicable.

    Returns:
        AvoirFournisseurCreate: Objet prêt à être inséré.
    """
    montant_ttc = calcul_montant_ttc(montant_ht, taux_tva)
    statut = statut_automatique_si_montant(montant_ttc)

    return AvoirFournisseurCreate(
        reference=reference,
        fournisseur_id=fournisseur_id,
        type_avoir=TypeAvoir.remise,
        motif="Avoir généré automatiquement",
        montant_ht=montant_ht,
        taux_tva=taux_tva,
        montant_ttc=montant_ttc,
        statut=statut,
        date_emission=datetime.utcnow()
    )