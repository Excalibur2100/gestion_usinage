from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from fastapi.responses import StreamingResponse
from typing import List

from backend.dependencies import get_db
from backend.db.schemas.achat.fournisseur_schemas import (
    FournisseurCreate,
    FournisseurRead,
    FournisseurUpdate,
    FournisseurSearch,
    FournisseurSearchResults,
    FournisseurBulkCreate,
    FournisseurBulkDelete,
    FournisseurResponse,
    FournisseurDetail
)
from backend.services.achat import fournisseur_services

router = APIRouter(
    prefix="/api/v1/fournisseurs",
    tags=["Fournisseurs"]
)

@router.post("/", response_model=FournisseurRead, summary="Créer un fournisseur", description="Crée un nouveau fournisseur avec toutes ses informations.")
def create_fournisseur(fournisseur: FournisseurCreate, db: Session = Depends(get_db)):
    return fournisseur_services.creer_fournisseur(db, fournisseur)

@router.get("/", response_model=List[FournisseurRead], summary="Lister les fournisseurs", description="Retourne une liste paginée de tous les fournisseurs.")
def list_fournisseurs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return fournisseur_services.list_fournisseurs(db, skip=skip, limit=limit)

@router.get("/{fournisseur_id}", response_model=FournisseurDetail, summary="Obtenir un fournisseur par ID", description="Retourne tous les détails d’un fournisseur à partir de son identifiant.")
def get_fournisseur(fournisseur_id: int, db: Session = Depends(get_db)):
    return fournisseur_services.get_fournisseur(db, fournisseur_id)

@router.put("/{fournisseur_id}", response_model=FournisseurRead, summary="Mettre à jour un fournisseur", description="Met à jour les informations d’un fournisseur existant.")
def update_fournisseur(fournisseur_id: int, data: FournisseurUpdate, db: Session = Depends(get_db)):
    return fournisseur_services.update_fournisseur(db, fournisseur_id, data)

@router.delete("/{fournisseur_id}", response_model=dict, summary="Supprimer un fournisseur", description="Supprime définitivement un fournisseur à partir de son ID.")
def delete_fournisseur(fournisseur_id: int, db: Session = Depends(get_db)):
    return fournisseur_services.delete_fournisseur(db, fournisseur_id)

@router.post("/search", response_model=FournisseurSearchResults, summary="Rechercher des fournisseurs", description="Recherche multi-critères parmi les fournisseurs.")
def search_fournisseurs(filters: FournisseurSearch, skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    return fournisseur_services.search_fournisseurs(db, filters, skip=skip, limit=limit)

@router.post("/bulk", response_model=List[FournisseurRead], summary="Créer plusieurs fournisseurs", description="Création en masse de fournisseurs.")
def bulk_create_fournisseurs(payload: FournisseurBulkCreate, db: Session = Depends(get_db)):
    return fournisseur_services.bulk_create_fournisseurs(db, payload.fournisseurs)

@router.delete("/bulk", response_model=dict, summary="Supprimer plusieurs fournisseurs", description="Suppression groupée de fournisseurs à partir d’une liste d’IDs.")
def bulk_delete_fournisseurs(payload: FournisseurBulkDelete, db: Session = Depends(get_db)):
    count = fournisseur_services.bulk_delete_fournisseurs(db, payload.ids)
    return {"detail": f"{count} fournisseurs supprimés."}

@router.get("/export", response_class=StreamingResponse, summary="Exporter les fournisseurs", description="Export CSV des données fournisseurs.")
def export_fournisseurs(db: Session = Depends(get_db)):
    buffer = fournisseur_services.export_fournisseurs_csv(db)
    return StreamingResponse(
        buffer,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=fournisseurs.csv"}
    )

@router.get("/detail/{fournisseur_id}", response_model=FournisseurDetail, summary="Détail d’un fournisseur", description="Détail enrichi du fournisseur (noms des auteurs, commandes, etc.).")
def get_fournisseur_detail(fournisseur_id: int, db: Session = Depends(get_db)):
    return fournisseur_services.get_fournisseur(db, fournisseur_id)