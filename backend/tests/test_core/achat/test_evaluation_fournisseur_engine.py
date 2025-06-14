import pytest
from datetime import datetime
from backend.core.ia.achat.evaluation_fournisseur_engine import (
    calculer_note_globale_pondérée,
    statut_automatique,
    generer_recommandation,
    suggere_evaluation_auto
)
from backend.db.schemas.achat.evaluation_fournisseur_schemas import StatutEvaluation, TypeEvaluation


def test_calcul_note_ponderee():
    note = calculer_note_globale_pondérée(80, 90, 70)
    assert 0 <= note <= 100
    assert round(note, 2) == round((80*0.5 + 90*0.3 + 70*0.2) / 1.0, 2)


@pytest.mark.parametrize("note,expected", [
    (95, StatutEvaluation.excellent),
    (80, StatutEvaluation.bon),
    (65, StatutEvaluation.moyen),
    (45, StatutEvaluation.faible),
    (30, StatutEvaluation.critique)
])
def test_statut_automatique(note, expected):
    assert statut_automatique(note) == expected


@pytest.mark.parametrize("statut", list(StatutEvaluation))
def test_recommandation(statut):
    message = generer_recommandation(statut)
    assert isinstance(message, str)
    assert len(message) > 5


def test_suggestion_auto():
    suggestion = suggere_evaluation_auto(fournisseur_id=1, note_qualite=80, note_delai=75, note_prix=70)
    assert suggestion.fournisseur_id == 1
    assert suggestion.type_evaluation == TypeEvaluation.automatique
    assert suggestion.statut == statut_automatique(suggestion.note_globale)
    assert suggestion.recommandation == generer_recommandation(suggestion.statut)
    assert isinstance(suggestion.date_evaluation, datetime)