import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers
from backend.db.models.base import Base
from backend.services.achat import evaluation_fournisseur_service
from backend.db.schemas.achat.evaluation_fournisseur_schemas import (
    EvaluationFournisseurCreate,
    EvaluationFournisseurUpdate,
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

def test_create_evaluation_service(db):
    data = EvaluationFournisseurCreate(
        fournisseur_id=1,
        note_globale=90.0,
        statut=StatutEvaluation.excellent,
        type_evaluation=TypeEvaluation.ponctuelle
    )
    evaluation = evaluation_fournisseur_service.creer_evaluation(db, data)
    db.refresh(evaluation)

    assert getattr(evaluation, "id") is not None
    assert float(getattr(evaluation, "note_globale")) == 90.0
    assert getattr(evaluation, "statut") == StatutEvaluation.excellent

def test_update_evaluation_service(db):
    data = EvaluationFournisseurCreate(
        fournisseur_id=2,
        note_globale=70.0,
        statut=StatutEvaluation.bon,
        type_evaluation=TypeEvaluation.periodique
    )
    evaluation = evaluation_fournisseur_service.creer_evaluation(db, data)
    db.refresh(evaluation)

    update_data = {
        "note_globale": 75.0,
        "commentaire": "Amélioration notée"
    }

    update_schema = EvaluationFournisseurUpdate(**update_data)
    updated = evaluation_fournisseur_service.update_evaluation(db, getattr(evaluation, "id"), update_schema)

    assert float(getattr(updated, "note_globale")) == 75.0
    assert getattr(updated, "commentaire") == "Amélioration notée"

def test_delete_evaluation_service(db):
    data = EvaluationFournisseurCreate(
        fournisseur_id=3,
        note_globale=60.0,
        statut=StatutEvaluation.moyen,
        type_evaluation=TypeEvaluation.audit
    )
    evaluation = evaluation_fournisseur_service.creer_evaluation(db, data)
    db.refresh(evaluation)

    result = evaluation_fournisseur_service.delete_evaluation(db, getattr(evaluation, "id"))
    assert "succès" in result["detail"]

def test_bulk_create_and_delete_service(db):
    data = [
        EvaluationFournisseurCreate(
            fournisseur_id=i,
            note_globale=50.0 + i,
            statut=StatutEvaluation.faible,
            type_evaluation=TypeEvaluation.ponctuelle
        )
        for i in range(1, 4)
    ]
    objets = evaluation_fournisseur_service.bulk_create_evaluations(db, data)
    ids = [getattr(e, "id") for e in objets]

    count = evaluation_fournisseur_service.bulk_delete_evaluations(db, ids)
    assert count == 3