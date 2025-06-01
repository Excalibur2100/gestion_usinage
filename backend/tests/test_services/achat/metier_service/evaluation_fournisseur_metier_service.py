from backend.core.ia.evaluation_fournisseur_engine import (
    calculer_note_globale_pondérée,
    statut_automatique,
    generer_recommandation,
    suggere_evaluation_auto
)
from backend.db.schemas.achat.evaluation_fournisseur_schemas import (
    EvaluationFournisseurCreate,
    StatutEvaluation
)
from datetime import datetime


def service_calcul_note(qualite: float, delai: float, prix: float) -> float:
    return calculer_note_globale_pondérée(qualite, delai, prix)


def service_statut(note: float) -> StatutEvaluation:
    return statut_automatique(note)


def service_recommandation(statut: StatutEvaluation) -> str:
    return generer_recommandation(statut)


def service_suggestion_auto(fournisseur_id: int, qualite: float, delai: float, prix: float) -> EvaluationFournisseurCreate:
    return suggere_evaluation_auto(fournisseur_id, qualite, delai, prix)