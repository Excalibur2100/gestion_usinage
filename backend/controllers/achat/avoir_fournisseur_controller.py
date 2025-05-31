from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from fastapi.responses import StreamingResponse
from typing import List

from backend.dependencies import get_db
from backend.db.schemas.achat.avoir_fournisseur_schemas import (
    AvoirFournisseurCreate,
    AvoirFournisseurRead,
    AvoirFournisseurUpdate,
    AvoirFournisseurSearch,
    AvoirFournisseurSearchResults,
    AvoirFournisseurBulkCreate,
    AvoirFournisseurBulkDelete,
    AvoirFournisseurResponse,
    AvoirFournisseurDetail
)
from backend.services.achat import avoir_fournisseur_service

router = APIRouter(
    prefix="/api/v1/avoirs-fournisseur",
    tags=["Avoirs Fournisseur"]
)

@router.post(
    "/",
    response_model=AvoirFournisseurRead,
    summary="Créer un avoir fournisseur",
    description="Crée un nouvel avoir fournisseur à partir des données fournies."
)
def create_avoir(avoir: AvoirFournisseurCreate, db: Session = Depends(get_db)):
    return avoir_fournisseur_service.creer_avoir(db, avoir)


@router.get(
    "/",
    response_model=List[AvoirFournisseurRead],
    summary="Lister les avoirs",
    description="Retourne une liste paginée de tous les avoirs fournisseur existants."
)
def get_avoirs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return avoir_fournisseur_service.list_avoirs(db, skip=skip, limit=limit)


@router.get(
    "/{avoir_id}",
    response_model=AvoirFournisseurDetail,
    summary="Récupérer un avoir par ID",
    description="Retourne les détails complets d’un avoir fournisseur en fonction de son ID."
)
def get_avoir(avoir_id: int, db: Session = Depends(get_db)):
    return avoir_fournisseur_service.get_avoir(db, avoir_id)


@router.put(
    "/{avoir_id}",
    response_model=AvoirFournisseurRead,
    summary="Mettre à jour un avoir",
    description="Met à jour un avoir fournisseur (seulement s’il est en statut brouillon)."
)
def update_avoir(avoir_id: int, data: AvoirFournisseurUpdate, db: Session = Depends(get_db)):
    return avoir_fournisseur_service.update_avoir(db, avoir_id, data)


@router.delete(
    "/{avoir_id}",
    response_model=dict,
    summary="Supprimer un avoir",
    description="Supprime un avoir fournisseur si son statut est brouillon."
)
def delete_avoir(avoir_id: int, db: Session = Depends(get_db)):
    return avoir_fournisseur_service.delete_avoir(db, avoir_id)


@router.post(
    "/search",
    response_model=AvoirFournisseurSearchResults,
    summary="Rechercher des avoirs",
    description="Recherche multi-critères sur les avoirs fournisseurs (référence, statut, dates, etc.)."
)
def search_avoirs(
    filters: AvoirFournisseurSearch,
    skip: int = 0,
    limit: int = 50,
    db: Session = Depends(get_db)
):
    return avoir_fournisseur_service.search_avoirs(db, filters, skip=skip, limit=limit)


@router.post(
    "/bulk",
    response_model=List[AvoirFournisseurRead],
    summary="Création en lot",
    description="Crée plusieurs avoirs fournisseurs d’un coup (bulk)."
)
def bulk_create(avoir_bulk: AvoirFournisseurBulkCreate, db: Session = Depends(get_db)):
    return avoir_fournisseur_service.bulk_create_avoirs(db, avoir_bulk.avoirs)


@router.delete(
    "/bulk",
    response_model=dict,
    summary="Suppression en lot",
    description="Supprime plusieurs avoirs en fonction d’une liste d’IDs (seuls les brouillons sont supprimés)."
)
def bulk_delete(payload: AvoirFournisseurBulkDelete, db: Session = Depends(get_db)):
    count = avoir_fournisseur_service.bulk_delete_avoirs(db, payload.ids)
    return {"detail": f"{count} avoirs supprimés."}


@router.get(
    "/export",
    response_class=StreamingResponse,
    summary="Exporter les avoirs (CSV)",
    description="Génère un fichier CSV contenant tous les avoirs fournisseurs."
)
def export_avoirs(db: Session = Depends(get_db)):
    buffer = avoir_fournisseur_service.export_avoirs_csv(db)
    return StreamingResponse(
        buffer,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=avoirs_fournisseur.csv"}
    )


@router.get(
    "/detail/{avoir_id}",
    response_model=AvoirFournisseurDetail,
    summary="Détail d’un avoir",
    description="Alias de /{id} pour des cas d’intégration frontend (ex: modale)."
)
def get_avoir_detail(avoir_id: int, db: Session = Depends(get_db)):
    return avoir_fournisseur_service.get_avoir(db, avoir_id)