from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from backend.dependencies import get_db
from backend.db.schemas.achat.fournisseur_schemas import (
    FournisseurCreate,
    StatutFournisseur
)
from backend.services.achat.service_metier.fournisseur_metier_service import (
    verifier_domaine_usinage,
    enrichir_creation_fournisseur,
    suggestion_statut_automatique
)

router = APIRouter(
    prefix="/api/v1/metier/fournisseurs",
    tags=["Fournisseurs - Métier"]
)

@router.get("/verifier-usinage", response_model=bool, summary="Fournisseur usinage/soudure ?")
def verifier_usinage(type_fournisseur: str):
    """
    Vérifie si le fournisseur appartient au domaine de l'usinage, soudure ou services associés.
    """
    try:
        from backend.db.schemas.achat.fournisseur_schemas import TypeFournisseur
        type_enum = TypeFournisseur(type_fournisseur)
    except ValueError:
        return False
    return verifier_domaine_usinage(type_enum)


@router.post("/enrichir", response_model=FournisseurCreate, summary="Préparer données fournisseur")
def enrichir_fournisseur(data: FournisseurCreate):
    """
    Applique les règles métier sur un fournisseur avant création :
    - Pays par défaut
    - Statut automatique si commentaire douteux
    """
    return enrichir_creation_fournisseur(data)


@router.get("/statut-auto", response_model=StatutFournisseur, summary="Statut auto selon commentaire")
def get_statut_auto(commentaire: str = Query(..., description="Commentaire ou note libre du fournisseur")):
    """
    Retourne un statut fournisseur automatiquement déduit du commentaire.
    """
    return suggestion_statut_automatique(commentaire)