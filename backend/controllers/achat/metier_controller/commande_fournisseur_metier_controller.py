from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from fastapi.responses import StreamingResponse

from backend.dependencies import get_db
from backend.db.schemas.achat.commande_fournisseur_schemas import (
    CommandeFournisseurCreate,
    CommandeFournisseurUpdate,
    CommandeFournisseurRead,
    CommandeFournisseurDetail,
    CommandeFournisseurSearch,
    CommandeFournisseurSearchResults,
    CommandeFournisseurBulkCreate,
    CommandeFournisseurBulkDelete
)
from backend.services.achat import commande_fournisseur_service

router = APIRouter(
    prefix="/api/v1/achat/commandes-fournisseur",
    tags=["Commandes Fournisseur"]
)

@router.post("/", response_model=CommandeFournisseurRead, summary="Créer une commande fournisseur")
def create_commande(commande: CommandeFournisseurCreate, db: Session = Depends(get_db)):
    """
    Crée une commande fournisseur.
    """
    return commande_fournisseur_service.creer_commande(db, commande)

@router.get("/", response_model=List[CommandeFournisseurRead], summary="Lister les commandes fournisseur")
def list_commandes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Liste paginée des commandes fournisseur.
    """
    return commande_fournisseur_service.list_commandes(db, skip, limit)

@router.get("/{commande_id}", response_model=CommandeFournisseurDetail, summary="Récupérer une commande fournisseur")
def get_commande(commande_id: int, db: Session = Depends(get_db)):
    """
    Récupère une commande fournisseur par ID.
    """
    return commande_fournisseur_service.get_commande(db, commande_id)

@router.put("/{commande_id}", response_model=CommandeFournisseurRead, summary="Mettre à jour une commande fournisseur")
def update_commande(commande_id: int, update: CommandeFournisseurUpdate, db: Session = Depends(get_db)):
    """
    Met à jour une commande fournisseur si son statut est brouillon.
    """
    return commande_fournisseur_service.update_commande(db, commande_id, update)

@router.delete("/{commande_id}", response_model=dict, summary="Supprimer une commande fournisseur")
def delete_commande(commande_id: int, db: Session = Depends(get_db)):
    """
    Supprime une commande fournisseur si son statut est brouillon.
    """
    return commande_fournisseur_service.delete_commande(db, commande_id)

@router.post("/search", response_model=CommandeFournisseurSearchResults, summary="Rechercher des commandes fournisseur")
def search_commandes(filters: CommandeFournisseurSearch, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Recherche multi-critères sur les commandes fournisseur.
    """
    results = commande_fournisseur_service.search_commandes(db, filters, skip, limit)
    return {"total": len(results), "results": results}

@router.get("/export", response_class=StreamingResponse, summary="Exporter les commandes fournisseur (CSV)")
def export_csv(db: Session = Depends(get_db)):
    """
    Exporte toutes les commandes fournisseur en CSV.
    """
    buffer = commande_fournisseur_service.export_commandes_csv(db)
    return StreamingResponse(buffer, media_type="text/csv", headers={
        "Content-Disposition": "attachment; filename=commandes_fournisseur.csv"
    })

@router.post("/bulk", response_model=List[CommandeFournisseurRead], summary="Création en lot de commandes")
def bulk_create(payload: CommandeFournisseurBulkCreate, db: Session = Depends(get_db)):
    """
    Crée plusieurs commandes fournisseur en une seule requête.
    """
    return commande_fournisseur_service.bulk_create_commandes(db, payload.commandes)

@router.delete("/bulk", response_model=dict, summary="Suppression en lot de commandes")
def bulk_delete(payload: CommandeFournisseurBulkDelete, db: Session = Depends(get_db)):
    """
    Supprime plusieurs commandes fournisseur si leur statut est brouillon.
    """
    count = commande_fournisseur_service.bulk_delete_commandes(db, payload.ids)
    return {"detail": f"{count} commandes supprimées."}