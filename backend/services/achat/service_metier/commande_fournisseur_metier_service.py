from datetime import datetime, timedelta
from backend.db.schemas.achat.commande_fournisseur_schemas import (
    StatutCommandeFournisseur,
    CommandeFournisseurCreate
)


def calcul_date_livraison_prevue(date_commande: datetime, delai_jours: int = 5) -> datetime:
    """
    Calcule une date de livraison prévue par défaut à N jours après la commande.
    """
    return date_commande + timedelta(days=delai_jours)


def statut_automatique_si_livraison(livree: bool) -> StatutCommandeFournisseur:
    """
    Détermine le statut automatiquement selon la livraison.
    """
    return StatutCommandeFournisseur.livree if livree else StatutCommandeFournisseur.envoyee


def verifier_montant_total(montant: float) -> bool:
    """
    Vérifie que le montant est positif.
    """
    return montant >= 0


def generer_numero_commande_automatique(prefix: str = "CMD-AUTO") -> str:
    """
    Génère un numéro de commande automatiquement avec timestamp.
    """
    return f"{prefix}-{datetime.utcnow().strftime('%Y%m%d%H%M%S')}"


def suggere_commande_auto(
    fournisseur_id: int,
    montant_total: float,
    devise: str = "EUR"
) -> CommandeFournisseurCreate:
    """
    Génère automatiquement une commande fournisseur de brouillon.
    """
    numero_commande = generer_numero_commande_automatique()
    statut = StatutCommandeFournisseur.brouillon
    date_commande = datetime.utcnow()

    return CommandeFournisseurCreate(
        numero_commande=numero_commande,
        reference_externe=None,
        fournisseur_id=fournisseur_id,
        utilisateur_id=None,
        commentaire="Commande générée automatiquement",
        statut=statut,
        date_commande=date_commande,
        date_livraison_prevue=None,
        date_livraison_effective=None,
        montant_total=montant_total,
        devise=devise,
        cree_par=None,
        modifie_par=None,
        version=1,
        etat_synchronisation="non_synchro",
        is_archived=False,
        uuid=None
    )  # type: ignore