from datetime import datetime
from backend.db.schemas.achat.evaluation_fournisseur_schemas import (
    EvaluationFournisseurCreate,
    StatutEvaluation,
    TypeEvaluation
)


def calculer_note_globale_pondérée(
    note_qualite: float,
    note_delai: float,
    note_prix: float,
    poids_qualite: float = 0.4,
    poids_delai: float = 0.35,
    poids_prix: float = 0.25
) -> float:
    """
    Calcule une note globale pondérée basée sur les critères qualité, délai et prix.
    """
    return round(
        note_qualite * poids_qualite +
        note_delai * poids_delai +
        note_prix * poids_prix,
        2
    )


def statut_automatique(note_globale: float) -> StatutEvaluation:
    """
    Déduit un statut qualitatif basé sur la note globale.
    """
    if note_globale >= 90:
        return StatutEvaluation.excellent
    elif note_globale >= 75:
        return StatutEvaluation.bon
    elif note_globale >= 60:
        return StatutEvaluation.moyen
    elif note_globale >= 40:
        return StatutEvaluation.faible
    else:
        return StatutEvaluation.critique


def generer_recommandation(statut: StatutEvaluation) -> str:
    """
    Fournit une recommandation textuelle en fonction du statut d’évaluation.
    """
    recommandations = {
        StatutEvaluation.excellent: "Fournisseur à privilégier pour les projets critiques.",
        StatutEvaluation.bon: "Fournisseur fiable, à suivre régulièrement.",
        StatutEvaluation.moyen: "Fournisseur acceptable, à surveiller.",
        StatutEvaluation.faible: "Fournisseur à évaluer avant tout nouvel engagement.",
        StatutEvaluation.critique: "Fournisseur non recommandé, revoir la collaboration."
    }
    return recommandations.get(statut, "Statut inconnu.")


def suggere_evaluation_auto(
    fournisseur_id: int,
    note_qualite: float,
    note_delai: float,
    note_prix: float,
    origine: str = "auto"
) -> EvaluationFournisseurCreate:
    """
    Génère une suggestion d’évaluation fournisseur automatiquement.
    """
    note_globale = calculer_note_globale_pondérée(note_qualite, note_delai, note_prix)
    statut = statut_automatique(note_globale)

    return EvaluationFournisseurCreate(
        fournisseur_id=fournisseur_id,
        note_qualite=note_qualite,
        note_delai=note_delai,
        note_prix=note_prix,
        note_globale=note_globale,
        statut=statut,
        type_evaluation=TypeEvaluation.automatique,
        origine=origine,
        commentaire="Évaluation générée automatiquement",
        date_evaluation=datetime.utcnow()
    )