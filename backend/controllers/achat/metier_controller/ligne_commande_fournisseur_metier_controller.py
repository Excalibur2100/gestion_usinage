from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.dependencies import get_db
from backend.db.schemas.achat.ligne_commande_fournisseur_schemas import (
    LigneCommandeFournisseurCreate,
    LigneCommandeFournisseurRead
)
from backend.services.achat.service_metier.ligne_commande_fournisseur_metier_service import enrichir_ligne_commande_fournisseur
from backend.services.achat.ligne_commande_fournisseur_service import creer_ligne_commande

router = APIRouter(
    prefix="/api/v1/metier/ligne-commande-fournisseur",
    tags=["Métier - Ligne Commande Fournisseur"]
)


@router.post(
    "/creer-enrichie",
    response_model=LigneCommandeFournisseurRead,
    summary="Créer une ligne de commande fournisseur enrichie",
    description="Crée une ligne en appliquant les règles métier (calcul TTC, statut automatique)."
)
def creer_ligne_enrichie(
    data: LigneCommandeFournisseurCreate,
    db: Session = Depends(get_db)
):
    enrichie = enrichir_ligne_commande_fournisseur(data)
    return creer_ligne_commande(db, enrichie)
