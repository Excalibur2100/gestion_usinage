import pytest
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker, clear_mappers

from backend.db.models.base import Base
from backend.db.models.tables.achat.evaluations_fournisseur import (
    EvaluationFournisseur,
    StatutEvaluation,
    TypeEvaluation,
)


@pytest.fixture
def db():
    engine = create_engine("sqlite:///:memory:")
    TestingSessionLocal = sessionmaker(bind=engine)
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    yield session
    session.close()
    clear_mappers()


def test_create_valid_evaluation(db):
    evaluation = EvaluationFournisseur(
        fournisseur_id=1,
        note_globale=85.0,
        statut=StatutEvaluation.bon,
        type_evaluation=TypeEvaluation.ponctuelle
    )
    db.add(evaluation)
    db.commit()
    db.refresh(evaluation)

    assert evaluation.id is not None
    assert float(getattr(evaluation, "note_globale")) == 85.0
    assert evaluation.statut.value == StatutEvaluation.bon.value


def test_enum_statut_type(db):
    evaluation = EvaluationFournisseur(
        fournisseur_id=1,
        note_globale=60.0,
        statut=StatutEvaluation.moyen,
        type_evaluation=TypeEvaluation.periodique
    )
    db.add(evaluation)
    db.commit()
    db.refresh(evaluation)

    assert evaluation.statut.value == "moyen"
    assert evaluation.type_evaluation.value == "periodique"


def test_constraint_note_globale_maximale(db):
    with pytest.raises(exc.IntegrityError):
        evaluation = EvaluationFournisseur(
            fournisseur_id=1,
            note_globale=150.0,  # invalide > 100
            statut=StatutEvaluation.excellent
        )
        db.add(evaluation)
        db.commit()


def test_constraint_note_globale_negative(db):
    with pytest.raises(exc.IntegrityError):
        evaluation = EvaluationFournisseur(
            fournisseur_id=1,
            note_globale=-10.0,  # invalide < 0
            statut=StatutEvaluation.critique
        )
        db.add(evaluation)
        db.commit()


def test_repr_evaluation(db):
    evaluation = EvaluationFournisseur(
        fournisseur_id=123,
        note_globale=77.5,
        statut=StatutEvaluation.bon
    )
    db.add(evaluation)
    db.commit()
    db.refresh(evaluation)

    assert repr(evaluation) == (
        f"<EvaluationFournisseur(id={evaluation.id}, "
        f"fournisseur={evaluation.fournisseur_id}, "
        f"note={evaluation.note_globale}, "
        f"statut={evaluation.statut})>"
    )