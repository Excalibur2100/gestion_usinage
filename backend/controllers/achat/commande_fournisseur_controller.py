from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from fastapi.responses import StreamingResponse

from backend.dependencies import get_db
from backend.db.schemas.achat.commande_fournisseur_schemas import (
    CommandeFournisseurCreate,
    CommandeFournisseurRead,
    CommandeFournisseurUpdate,
    CommandeFournisseurSearch,
    CommandeFournisseurSearchResults,
    CommandeFournisseurBulkCreate,
    CommandeFournisseurBulkDelete,
    CommandeFournisseurDetail
)
from backend.services.achat import commande_fournisseur_service

router = APIRouter(
    prefix="/api/v1/commandes-fournisseur",
    tags=["Commandes Fournisseur"]
)


@router.post("/", response_model=CommandeFournisseurRead, summary="Créer une commande fournisseur")
def create_commande(commande: CommandeFournisseurCreate, db: Session = Depends(get_db)):
    return commande_fournisseur_service.creer_commande(db, commande)


@router.get("/", response_model=List[CommandeFournisseurRead], summary="Lister les commandes fournisseur")
def list_commandes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return commande_fournisseur_service.list_commandes(db, skip, limit)


@router.get("/{commande_id}", response_model=CommandeFournisseurDetail, summary="Récupérer une commande fournisseur")
def get_commande(commande_id: int, db: Session = Depends(get_db)):
    return commande_fournisseur_service.get_commande(db, commande_id)


@router.put("/{commande_id}", response_model=CommandeFournisseurRead, summary="Modifier une commande fournisseur")
def update_commande(commande_id: int, update: CommandeFournisseurUpdate, db: Session = Depends(get_db)):
    return commande_fournisseur_service.update_commande(db, commande_id, update)


@router.delete("/{commande_id}", response_model=dict, summary="Supprimer une commande fournisseur")
def delete_commande(commande_id: int, db: Session = Depends(get_db)):
    return commande_fournisseur_service.delete_commande(db, commande_id)


@router.post("/search", response_model=CommandeFournisseurSearchResults, summary="Rechercher des commandes fournisseur")
def search_commandes(filters: CommandeFournisseurSearch, skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    return commande_fournisseur_service.search_commandes(db, filters, skip, limit)


@router.get("/export", response_class=StreamingResponse, summary="Exporter les commandes en CSV")
def export_commandes(db: Session = Depends(get_db)):
    buffer = commande_fournisseur_service.export_commandes_csv(db)
    return StreamingResponse(
        buffer,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=commandes_fournisseur.csv"}
    )


@router.post("/bulk", response_model=List[CommandeFournisseurRead], summary="Créer des commandes fournisseur en lot")
def bulk_create(payload: CommandeFournisseurBulkCreate, db: Session = Depends(get_db)):
    return commande_fournisseur_service.bulk_create_commandes(db, payload.commandes)


@router.delete("/bulk", response_model=dict, summary="Supprimer des commandes fournisseur en lot")
def bulk_delete(payload: CommandeFournisseurBulkDelete, db: Session = Depends(get_db)):
    count = commande_fournisseur_service.bulk_delete_commandes(db, payload.ids)
    return {"detail": f"{count} commandes supprimées"}