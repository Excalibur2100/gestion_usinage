import pytest
from datetime import datetime
from backend.services.achat.service_metier.evaluation_fournisseur_metier_service import (
    calculer_note_globale_pondérée,
    statut_automatique,
    generer_recommandation,
    suggere_evaluation_auto
)
from backend.db.schemas.achat.evaluation_fournisseur_schemas import (
    EvaluationFournisseurCreate,
    StatutEvaluation
)


def test_calculer_note_globale_ponderee():
    result = calculer_note_globale_pondérée(80, 90, 70)
    assert isinstance(result, float)
    assert 0 <= result <= 100
    assert round(result, 2) == round((80 * 0.4 + 90 * 0.3 + 70 * 0.3), 2)


@pytest.mark.parametrize("note,expected", [
    (95, StatutEvaluation.excellent),
    (85, StatutEvaluation.bon),
    (65, StatutEvaluation.moyen),
    (45, StatutEvaluation.faible),
    (20, StatutEvaluation.critique),
])
def test_statut_automatique(note, expected):
    assert statut_automatique(note) == expected


@pytest.mark.parametrize("statut", list(StatutEvaluation))
def test_generer_recommandation(statut):
    message = generer_recommandation(statut)
    assert isinstance(message, str)
    assert len(message) > 0


def test_suggere_evaluation_auto():
    evaluation = suggere_evaluation_auto(
        fournisseur_id=1,
        note_qualite=80,
        note_delai=70,
        note_prix=90
    )
    assert isinstance(evaluation, EvaluationFournisseurCreate)
    assert evaluation.fournisseur_id == 1
    assert 0 <= evaluation.note_globale <= 100
    assert evaluation.statut in StatutEvaluation
    assert isinstance(evaluation.date_evaluation, datetime)