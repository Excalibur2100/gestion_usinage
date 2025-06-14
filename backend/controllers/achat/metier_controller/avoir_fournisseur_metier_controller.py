from fastapi import APIRouter, Query
from backend.core.ia.achat.avoir_fournisseur_engine import (
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
    description="Retourne le montant TTC à partir du montant HT et du taux de TVA."
)
def api_calcul_montant_ttc(
    ht: float = Query(..., description="Montant HT"),
    tva: float = Query(20.0, description="Taux de TVA (en %) par défaut à 20")
) -> float:
    return calculer_montant_ttc(ht, tva)

@router.get(
    "/detect-type",
    response_model=TypeAvoir,
    summary="Détecter le type d'avoir",
    description="Tente de déterminer automatiquement le type d'avoir à partir du motif ou de la référence."
)
def api_detect_type(
    reference: str = Query("", description="Référence (texte libre)"),
    motif: str = Query("", description="Motif (texte libre)")
) -> TypeAvoir:
    return detecter_type_avoir(reference, motif)

@router.get(
    "/suggere-auto",
    response_model=AvoirFournisseurCreate,
    summary="Générer un avoir automatiquement",
    description="Crée une suggestion d'avoir fournisseur à partir du montant HT et d'un fournisseur."
)
def api_suggere_avoir_auto(
    reference: str = Query(..., description="Référence à générer"),
    fournisseur_id: int = Query(..., description="ID du fournisseur concerné"),
    montant_ht: float = Query(..., description="Montant HT"),
    taux_tva: float = Query(20.0, description="Taux de TVA (en %) par défaut à 20")
) -> AvoirFournisseurCreate:
    return suggere_avoir_auto(
        reference=reference,
        fournisseur_id=fournisseur_id,
        montant_ht=montant_ht,
        taux_tva=taux_tva
    )