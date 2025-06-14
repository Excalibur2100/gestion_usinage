from datetime import datetime
from backend.db.schemas.achat.facture_fournisseur_schemas import (
    FactureFournisseurCreate,
    StatutFactureFournisseur
)


def calcul_montant_ttc(montant_ht: float, taux_tva: float = 20.0) -> float:
    """
    Calcule le montant TTC à partir du HT et du taux de TVA.
    """
    return round(montant_ht * (1 + taux_tva / 100), 2)


def statut_automatique(date_echeance: datetime | None) -> StatutFactureFournisseur:
    """
    Détermine automatiquement le statut en fonction de la date d’échéance.
    """
    if date_echeance and date_echeance < datetime.utcnow():
        return StatutFactureFournisseur.en_retard
    return StatutFactureFournisseur.brouillon


def generer_numero_facture_auto(prefix: str = "FACT-AUTO") -> str:
    """
    Génère automatiquement un numéro de facture unique basé sur le timestamp UTC.
    """
    return f"{prefix}-{datetime.utcnow().strftime('%Y%m%d%H%M%S%f')}"


def suggere_facture_auto(
    fournisseur_id: int,
    montant_ht: float,
    taux_tva: float = 20.0,
    devise: str = "EUR",
    reference: str = "FACT-AUTO-GENEREE"
) -> FactureFournisseurCreate:
    """
    Génère une suggestion intelligente de facture fournisseur.
    """
    montant_ttc = calcul_montant_ttc(montant_ht, taux_tva)
    date_now = datetime.utcnow()

    return FactureFournisseurCreate(
        numero_facture=generer_numero_facture_auto(),
        reference_externe=reference,
        fournisseur_id=fournisseur_id,
        montant_ht=montant_ht,
        taux_tva=taux_tva,
        montant_ttc=montant_ttc,
        devise=devise,
        date_facture=date_now,
        date_echeance=date_now,
        statut=statut_automatique(date_now)
    )  # type: ignore