from fastapi import APIRouter, Query
from typing import Annotated

from backend.db.schemas.achat.evaluation_fournisseur_schemas import (
    EvaluationFournisseurCreate,
    StatutEvaluation,
)
from backend.core.ia.achat.evaluation_fournisseur_engine import (
    calculer_note_globale_pondérée,
    statut_automatique,
    generer_recommandation,
    suggere_evaluation_auto,
)

router = APIRouter(
    prefix="/api/v1/metier/evaluations-fournisseur",
    tags=["Métier - Évaluations Fournisseur"]
)


@router.get("/calcul-note", summary="Calculer une note globale pondérée", description="Calcule une note globale à partir des composantes qualité, délai, et prix.")
def get_note_globale(
    qualite: Annotated[float, Query(ge=0, le=100)],
    delai: Annotated[float, Query(ge=0, le=100)],
    prix: Annotated[float, Query(ge=0, le=100)]
):
    score = calculer_note_globale_pondérée(qualite, delai, prix)
    return {"note_globale": score}


@router.get("/statut-auto", summary="Déterminer automatiquement un statut", description="Retourne un statut (excellent, bon...) basé sur une note globale.")
def get_statut_auto(note: Annotated[float, Query(ge=0, le=100)]):
    statut = statut_automatique(note)
    return {"statut": statut}


@router.get("/recommandation", summary="Générer une recommandation IA", description="Fournit un conseil ou une recommandation selon le statut d'évaluation.")
def get_recommandation(statut: StatutEvaluation):
    message = generer_recommandation(statut)
    return {"recommandation": message}


@router.post(
    "/suggestion-automatique",
    response_model=EvaluationFournisseurCreate,
    summary="Suggestion automatique complète",
    description="Génère une évaluation complète à partir des notes (qualité, délai, prix)."
)
def get_suggestion_auto(
    fournisseur_id: int,
    note_qualite: Annotated[float, Query(ge=0, le=100)],
    note_delai: Annotated[float, Query(ge=0, le=100)],
    note_prix: Annotated[float, Query(ge=0, le=100)],
):
    suggestion = suggere_evaluation_auto(fournisseur_id, note_qualite, note_delai, note_prix)
    return suggestion