from backend.db.schemas.achat.commande_fournisseur_schemas import (
    CommandeFournisseurCreate,
    StatutCommandeFournisseur
)
from datetime import datetime


def statut_initial(livraison_prevue: bool) -> StatutCommandeFournisseur:
    return StatutCommandeFournisseur.envoyee if livraison_prevue else StatutCommandeFournisseur.brouillon


def suggere_commande_auto(numero: str, fournisseur_id: int, montant_total: float) -> CommandeFournisseurCreate:
    return CommandeFournisseurCreate(
        numero_commande=numero,
        fournisseur_id=fournisseur_id,
        montant_total=montant_total,
        statut=StatutCommandeFournisseur.brouillon,
        date_commande=datetime.utcnow()
    )