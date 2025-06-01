from datetime import datetime
from backend.db.schemas.achat.facture_fournisseur_schemas import (
    FactureFournisseurCreate,
    StatutFactureFournisseur
)


def calcul_montant_ttc(montant_ht: float, taux_tva: float = 20.0) -> float:
    """
    Calcule le montant TTC à partir du montant HT et du taux de TVA.
    """
    return round(montant_ht * (1 + taux_tva / 100), 2)


def generer_numero_facture_auto(prefix: str = "FACT-AUTO") -> str:
    """
    Génère automatiquement un numéro de facture basé sur la date UTC.
    """
    return f"{prefix}-{datetime.utcnow().strftime('%Y%m%d%H%M%S%f')}"


def statut_auto_si_retard(date_echeance: datetime) -> StatutFactureFournisseur:
    """
    Détermine automatiquement le statut de la facture en fonction de l’échéance.
    """
    if date_echeance < datetime.utcnow():
        return StatutFactureFournisseur.en_retard
    return StatutFactureFournisseur.brouillon


def suggere_facture_auto(
    fournisseur_id: int,
    montant_ht: float,
    taux_tva: float = 20.0,
    devise: str = "EUR",
    reference: str = "FACT-AUTO-GENEREE"
) -> FactureFournisseurCreate:
    """
    Crée automatiquement une suggestion de facture fournisseur.
    """
    montant_ttc = calcul_montant_ttc(montant_ht, taux_tva)
    statut = statut_auto_si_retard(datetime.utcnow())

    return FactureFournisseurCreate(
        numero_facture=generer_numero_facture_auto(),
        reference_externe=reference,
        fournisseur_id=fournisseur_id,
        montant_ht=montant_ht,
        taux_tva=taux_tva,
        montant_ttc=montant_ttc,
        devise=devise,
        statut=statut,
        date_facture=datetime.utcnow()
    )  # type: ignore