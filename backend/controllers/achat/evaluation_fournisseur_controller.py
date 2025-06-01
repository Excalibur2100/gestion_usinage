from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from fastapi.responses import StreamingResponse

from backend.dependencies import get_db
from backend.db.schemas.achat.evaluation_fournisseur_schemas import (
    EvaluationFournisseurCreate,
    EvaluationFournisseurUpdate,
    EvaluationFournisseurRead,
    EvaluationFournisseurDetail,
    EvaluationFournisseurSearch,
    EvaluationFournisseurSearchResults,
    EvaluationFournisseurBulkCreate,
    EvaluationFournisseurBulkDelete
)
from backend.services.achat import evaluation_fournisseur_service

router = APIRouter(
    prefix="/api/v1/evaluations-fournisseur",
    tags=["Évaluations Fournisseur"]
)

@router.post("/", response_model=EvaluationFournisseurRead, summary="Créer une évaluation fournisseur")
def create_evaluation(evaluation: EvaluationFournisseurCreate, db: Session = Depends(get_db)):
    return evaluation_fournisseur_service.creer_evaluation(db, evaluation)


@router.get("/", response_model=List[EvaluationFournisseurRead], summary="Lister toutes les évaluations")
def list_evaluations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return evaluation_fournisseur_service.list_evaluations(db, skip, limit)


@router.get("/{evaluation_id}", response_model=EvaluationFournisseurDetail, summary="Obtenir une évaluation par ID")
def get_evaluation(evaluation_id: int, db: Session = Depends(get_db)):
    return evaluation_fournisseur_service.get_evaluation(db, evaluation_id)


@router.put("/{evaluation_id}", response_model=EvaluationFournisseurRead, summary="Mettre à jour une évaluation")
def update_evaluation(evaluation_id: int, update: EvaluationFournisseurUpdate, db: Session = Depends(get_db)):
    return evaluation_fournisseur_service.update_evaluation(db, evaluation_id, update)


@router.delete("/{evaluation_id}", response_model=dict, summary="Supprimer une évaluation fournisseur")
def delete_evaluation(evaluation_id: int, db: Session = Depends(get_db)):
    return evaluation_fournisseur_service.delete_evaluation(db, evaluation_id)


@router.post("/search", response_model=EvaluationFournisseurSearchResults, summary="Rechercher des évaluations")
def search_evaluations(filters: EvaluationFournisseurSearch, skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    return evaluation_fournisseur_service.search_evaluations(db, filters, skip, limit)


@router.get("/export", response_class=StreamingResponse, summary="Exporter les évaluations au format CSV")
def export_evaluations(db: Session = Depends(get_db)):
    buffer = evaluation_fournisseur_service.export_evaluations_csv(db)
    return StreamingResponse(
        buffer,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=evaluations_fournisseur.csv"}
    )


@router.post("/bulk", response_model=List[EvaluationFournisseurRead], summary="Créer plusieurs évaluations")
def bulk_create(payload: EvaluationFournisseurBulkCreate, db: Session = Depends(get_db)):
    return evaluation_fournisseur_service.bulk_create_evaluations(db, payload.evaluations)


@router.delete("/bulk", response_model=dict, summary="Supprimer plusieurs évaluations")
def bulk_delete(payload: EvaluationFournisseurBulkDelete, db: Session = Depends(get_db)):
    count = evaluation_fournisseur_service.bulk_delete_evaluations(db, payload.ids)
    return {"detail": f"{count} évaluations supprimées"}