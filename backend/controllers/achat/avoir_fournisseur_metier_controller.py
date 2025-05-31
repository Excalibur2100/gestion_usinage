from fastapi import APIRouter, Depends, Query
from backend.core.ia.avoir_fournisseur_engine import (
    calculer_montant_ttc,
    detecter_type_avoir,
    suggere_avoir_auto
)
from backend.db.schemas.achat.avoir_fournisseur_schemas import (
    AvoirFournisseurCreate,
    TypeAvoir
)

router = APIRouter(
    prefix="/api/v1/metier/avoirs-fournisseur",
    tags=["Avoirs Fournisseur - Métier"]
)

@router.get(
    "/calcul-montant-ttc",
    response_model=float,
    summary="Calculer le montant TTC",
    description="Retourne le montant TTC calculé à partir du montant HT et du taux de TVA."
)
def api_calcul_montant_ttc(
    ht: float = Query(..., description="Montant HT"),
    tva: float = Query(..., description="Taux de TVA")
):
    return calculer_montant_ttc(ht, tva)


@router.get(
    "/detect-type",
    response_model=TypeAvoir,
    summary="Détecter le type d'avoir",
    description="Tente de déterminer automatiquement le type d'avoir à partir du motif ou de la référence."
)
def api_detect_type(
    reference: str = "",
    motif: str = ""
):
    return detecter_type_avoir(reference, motif)


@router.get(
    "/suggere-auto",
    response_model=AvoirFournisseurCreate,
    summary="Générer un avoir automatiquement",
    description="Crée une suggestion d'avoir fournisseur à partir d'une facture et d'un montant à rembourser."
)
def api_suggere_avoir_auto(
    facture_id: int = Query(..., description="ID de la facture concernée"),
    montant: float = Query(..., description="Montant total à rembourser (TTC)"),
    raison: str = Query("", description="Raison du remboursement (motif libre)")
):
    return suggere_avoir_auto(facture_id=facture_id, total_rembourse=montant, raison=raison)