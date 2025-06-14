from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from typing import List

from backend.dependencies import get_db
from backend.db.schemas.achat.ligne_commande_fournisseur_schemas import (
    LigneCommandeFournisseurCreate,
    LigneCommandeFournisseurUpdate,
    LigneCommandeFournisseurRead,
    LigneCommandeFournisseurDetail,
    LigneCommandeFournisseurSearch,
    LigneCommandeFournisseurSearchResults,
    LigneCommandeFournisseurBulkCreate,
    LigneCommandeFournisseurBulkDelete
)
from backend.services.achat import ligne_commande_fournisseur_service

router = APIRouter(
    prefix="/api/v1/lignes-commande-fournisseur",
    tags=["Lignes Commande Fournisseur"]
)


@router.post("/", response_model=LigneCommandeFournisseurRead, summary="Créer une ligne de commande fournisseur")
def create_ligne_commande(data: LigneCommandeFournisseurCreate, db: Session = Depends(get_db)):
    return ligne_commande_fournisseur_service.creer_ligne_commande(db, data)


@router.get("/", response_model=List[LigneCommandeFournisseurRead], summary="Lister les lignes de commande")
def list_lignes_commande(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return ligne_commande_fournisseur_service.list_lignes_commande(db, skip=skip, limit=limit)


@router.get("/{ligne_id}", response_model=LigneCommandeFournisseurDetail, summary="Récupérer une ligne par ID")
def get_ligne_commande(ligne_id: int, db: Session = Depends(get_db)):
    return ligne_commande_fournisseur_service.get_ligne_commande(db, ligne_id)


@router.put("/{ligne_id}", response_model=LigneCommandeFournisseurRead, summary="Mettre à jour une ligne")
def update_ligne_commande(ligne_id: int, data: LigneCommandeFournisseurUpdate, db: Session = Depends(get_db)):
    return ligne_commande_fournisseur_service.update_ligne_commande(db, ligne_id, data)


@router.delete("/{ligne_id}", response_model=dict, summary="Supprimer une ligne")
def delete_ligne_commande(ligne_id: int, db: Session = Depends(get_db)):
    return ligne_commande_fournisseur_service.delete_ligne_commande(db, ligne_id)


@router.post("/search", response_model=LigneCommandeFournisseurSearchResults, summary="Rechercher des lignes")
def search_lignes_commande(filters: LigneCommandeFournisseurSearch, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return ligne_commande_fournisseur_service.search_lignes_commande(db, filters, skip=skip, limit=limit)


@router.post("/bulk", response_model=List[LigneCommandeFournisseurRead], summary="Créer plusieurs lignes")
def bulk_create_lignes(payload: LigneCommandeFournisseurBulkCreate, db: Session = Depends(get_db)):
    return ligne_commande_fournisseur_service.bulk_create_lignes_commande(db, payload.lignes)


@router.delete("/bulk", response_model=dict, summary="Supprimer plusieurs lignes")
def bulk_delete_lignes(payload: LigneCommandeFournisseurBulkDelete, db: Session = Depends(get_db)):
    count = ligne_commande_fournisseur_service.bulk_delete_lignes_commande(db, payload.ids)
    return {"detail": f"{count} lignes supprimées."}


@router.get("/export", response_class=StreamingResponse, summary="Exporter les lignes en CSV")
def export_lignes_commande_csv(db: Session = Depends(get_db)):
    buffer = ligne_commande_fournisseur_service.export_lignes_commande_csv(db)
    return StreamingResponse(
        buffer,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=lignes_commande_fournisseur.csv"}
    )


@router.get("/detail/{ligne_id}", response_model=LigneCommandeFournisseurDetail, summary="Détail d’une ligne")
def get_ligne_commande_detail(ligne_id: int, db: Session = Depends(get_db)):
    return ligne_commande_fournisseur_service.get_ligne_commande(db, ligne_id)