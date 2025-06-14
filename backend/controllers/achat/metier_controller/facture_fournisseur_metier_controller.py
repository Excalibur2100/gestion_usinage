from fastapi import APIRouter, Query
from typing import Annotated

from backend.db.schemas.achat.facture_fournisseur_schemas import FactureFournisseurCreate
from backend.core.ia.achat.facture_fournisseur_engine import (
    calcul_montant_ttc,
    statut_automatique,
    generer_numero_facture_auto,
    suggere_facture_auto
)

router = APIRouter(
    prefix="/api/v1/metier/factures-fournisseur",
    tags=["Métier - Factures Fournisseur"]
)


@router.get("/calcul-montant-ttc", summary="Calculer le montant TTC")
def api_calcul_ttc(
    ht: Annotated[float, Query(ge=0)],
    tva: Annotated[float, Query(ge=0)]
):
    """
    Calcule le montant TTC à partir du montant HT et du taux de TVA.
    """
    return calcul_montant_ttc(ht, tva)


@router.get("/statut-automatique", summary="Déterminer le statut automatique")
def api_statut_auto(date_echeance: Annotated[str, Query()]):
    """
    Retourne le statut automatique d'une facture en fonction de sa date d’échéance.
    """
    from datetime import datetime
    try:
        parsed_date = datetime.fromisoformat(date_echeance)
    except ValueError:
        raise ValueError("Format de date invalide. Utilisez ISO 8601.")
    return statut_automatique(parsed_date)


@router.get("/generer-numero", summary="Générer un numéro automatique")
def api_generer_numero():
    """
    Génère un numéro de facture automatique unique.
    """
    return generer_numero_facture_auto()


@router.post("/suggere-auto", response_model=FactureFournisseurCreate, summary="Suggestion IA de facture")
def api_suggestion_auto(
    fournisseur_id: int,
    montant_ht: Annotated[float, Query(ge=0)],
    taux_tva: Annotated[float, Query(ge=0)],
    devise: str = "EUR",
    reference: str = "FACT-AUTO-GENEREE"
):
    """
    Génère automatiquement une suggestion complète de facture fournisseur.
    """
    return suggere_facture_auto(fournisseur_id, montant_ht, taux_tva, devise, reference)