from backend.db.schemas.achat.evaluation_fournisseur_schemas import (
    EvaluationFournisseurCreate,
    StatutEvaluation,
    TypeEvaluation
)
from datetime import datetime


def calculer_note_globale_pondérée(qualite: float, delai: float, prix: float,
                                    poids_qualite: float = 0.5,
                                    poids_delai: float = 0.3,
                                    poids_prix: float = 0.2) -> float:
    """
    Calcule une note globale pondérée sur 100.
    """
    total = poids_qualite + poids_delai + poids_prix
    if total == 0:
        return 0
    score = (qualite * poids_qualite + delai * poids_delai + prix * poids_prix) / total
    return round(score, 2)


def statut_automatique(note: float) -> StatutEvaluation:
    """
    Attribue un statut automatique selon la note.
    """
    if note >= 90:
        return StatutEvaluation.excellent
    elif note >= 75:
        return StatutEvaluation.bon
    elif note >= 60:
        return StatutEvaluation.moyen
    elif note >= 40:
        return StatutEvaluation.faible
    else:
        return StatutEvaluation.critique


def generer_recommandation(statut: StatutEvaluation) -> str:
    """
    Génère une suggestion IA simple en fonction du statut.
    """
    messages = {
        StatutEvaluation.excellent: "Fournisseur exemplaire. À privilégier pour projets critiques.",
        StatutEvaluation.bon: "Fournisseur fiable. À maintenir dans le panel.",
        StatutEvaluation.moyen: "Fournisseur correct. Suivi recommandé.",
        StatutEvaluation.faible: "Fournisseur à surveiller. Prévoir actions correctives.",
        StatutEvaluation.critique: "Fournisseur non conforme. Blocage ou audit conseillé."
    }
    return messages.get(statut, "")


def suggere_evaluation_auto(fournisseur_id: int, note_qualite: float, note_delai: float, note_prix: float) -> EvaluationFournisseurCreate:
    """
    Génère automatiquement une évaluation pré-remplie pour un fournisseur.
    """
    note = calculer_note_globale_pondérée(note_qualite, note_delai, note_prix)
    statut = statut_automatique(note)
    recommandation = generer_recommandation(statut)

    return EvaluationFournisseurCreate(
        fournisseur_id=fournisseur_id,
        note_qualite=note_qualite,
        note_delai=note_delai,
        note_prix=note_prix,
        note_globale=note,
        statut=statut,
        type_evaluation=TypeEvaluation.automatique,
        origine="auto-system",
        date_evaluation=datetime.utcnow(),
        recommandation=recommandation
    )