from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from fastapi.responses import StreamingResponse
from typing import List, Optional

from backend.dependencies import get_db
from backend.db.schemas.achat.avoir_fournisseur_schemas import (
    AvoirFournisseurCreate,
    AvoirFournisseurRead,
    AvoirFournisseurUpdate,
    AvoirFournisseurSearch,
    AvoirFournisseurSearchResults,
    AvoirFournisseurBulkCreate,
    AvoirFournisseurBulkDelete,
    AvoirFournisseurDetail,
)

from backend.services.achat import avoir_fournisseur_service

router = APIRouter(
    prefix="/api/v1/achat/avoirs-fournisseur",
    tags=["Avoirs Fournisseur"]
)


@router.post("/", response_model=AvoirFournisseurRead, summary="Créer un avoir fournisseur")
def create_avoir(data: AvoirFournisseurCreate, db: Session = Depends(get_db)):
    """Crée un nouvel avoir fournisseur à partir des données fournies."""
    return avoir_fournisseur_service.creer_avoir(db, data)


from backend.db.schemas.achat.avoir_fournisseur_schemas import AvoirFournisseurSearch, StatutAvoir

...

@router.get("/", response_model=List[AvoirFournisseurRead], summary="Lister les avoirs")
def get_avoirs(
    numero_avoir: Optional[str] = Query(None, alias="reference"),
    statut: Optional[str] = Query(None),
    fournisseur_id: Optional[int] = None,
    is_archived: Optional[bool] = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    Liste paginée et filtrée des avoirs fournisseur.
    """
    filters = AvoirFournisseurSearch(
        reference=numero_avoir,
        statut=StatutAvoir(statut) if statut else None,
        fournisseur_id=fournisseur_id,
        is_archived=is_archived
    )
    return avoir_fournisseur_service.search_avoirs(db, filters, skip=skip, limit=limit)


@router.get("/{avoir_id}", response_model=AvoirFournisseurDetail, summary="Récupérer un avoir par ID")
def get_avoir(avoir_id: int, db: Session = Depends(get_db)):
    """Retourne les détails d’un avoir fournisseur via son ID."""
    return avoir_fournisseur_service.get_avoir(db, avoir_id)


@router.put("/{avoir_id}", response_model=AvoirFournisseurRead, summary="Mettre à jour un avoir fournisseur")
def update_avoir(avoir_id: int, data: AvoirFournisseurUpdate, db: Session = Depends(get_db)):
    """Met à jour un avoir fournisseur (seulement s’il est en statut brouillon)."""
    return avoir_fournisseur_service.update_avoir(db, avoir_id, data)


@router.delete("/{avoir_id}", response_model=dict, summary="Supprimer un avoir fournisseur")
def delete_avoir(avoir_id: int, db: Session = Depends(get_db)):
    """Supprime un avoir fournisseur si son statut est brouillon."""
    return avoir_fournisseur_service.delete_avoir(db, avoir_id)


@router.post("/search", response_model=AvoirFournisseurSearchResults, summary="Rechercher des avoirs fournisseur")
def search_avoirs(
    filters: AvoirFournisseurSearch,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """Recherche multi-critères sur les avoirs fournisseur (numéro, statut, dates, etc.)."""
    results = avoir_fournisseur_service.search_avoirs(db, filters, skip, limit)
    return {"total": len(results), "results": results}


@router.get("/export", response_class=StreamingResponse, summary="Exporter les avoirs (CSV)")
def export_avoirs(db: Session = Depends(get_db)):
    """Génère un fichier CSV contenant tous les avoirs fournisseurs."""
    buffer = avoir_fournisseur_service.export_avoirs_csv(db)
    return StreamingResponse(
        buffer,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=avoirs_fournisseur.csv"}
    )


@router.post("/bulk", response_model=List[AvoirFournisseurRead], summary="Créer plusieurs avoirs fournisseur")
def bulk_create(payload: AvoirFournisseurBulkCreate, db: Session = Depends(get_db)):
    """Crée plusieurs avoirs fournisseurs d’un coup (bulk)."""
    return avoir_fournisseur_service.bulk_create_avoirs(db, payload.avoirs)


@router.delete("/bulk", response_model=dict, summary="Supprimer plusieurs avoirs fournisseur")
def bulk_delete(payload: AvoirFournisseurBulkDelete, db: Session = Depends(get_db)):
    """Supprime plusieurs avoirs (seuls les brouillons sont supprimés)."""
    count = avoir_fournisseur_service.bulk_delete_avoirs(db, payload.ids)
    return {"detail": f"{count} avoirs supprimés."}


@router.get("/detail/{avoir_id}", response_model=AvoirFournisseurDetail, summary="Détail d’un avoir fournisseur")
def get_avoir_detail(avoir_id: int, db: Session = Depends(get_db)):
    """Alias de /{id} pour intégration frontend (ex: modale, preview, etc.)."""
    return avoir_fournisseur_service.get_avoir(db, avoir_id)