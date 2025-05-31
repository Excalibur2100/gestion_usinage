from fastapi import APIRouter, Query
from datetime import datetime
from backend.core.ia.commande_fournisseur_engine import (
    generer_numero_commande,
    detecter_retard,
    statut_auto,
    suggere_commande_auto
)
from backend.db.schemas.achat.commande_fournisseur_schemas import (
    StatutCommandeFournisseur,
    CommandeFournisseurCreate
)

router = APIRouter(
    prefix="/api/v1/metier/commandes-fournisseur",
    tags=["Commandes Fournisseur - Métier"]
)

@router.get("/generer-numero", response_model=str)
def api_generer_numero(annee: int, compteur: int):
    return generer_numero_commande(annee, compteur)


@router.get("/detecter-retard", response_model=bool)
def api_detecter_retard(date_prevue: datetime, date_effective: datetime):
    return detecter_retard(date_prevue, date_effective)


@router.get("/statut-auto", response_model=StatutCommandeFournisseur)
def api_statut_auto(depuis_livraison: bool, livree: bool):
    return statut_auto(depuis_livraison, livree)


@router.get("/suggere-auto", response_model=CommandeFournisseurCreate)
def api_suggere_commande(fournisseur_id: int, montant: float):
    return suggere_commande_auto(fournisseur_id, montant)
