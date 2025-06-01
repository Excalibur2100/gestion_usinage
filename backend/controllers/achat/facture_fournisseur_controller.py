from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from fastapi.responses import StreamingResponse

from backend.dependencies import get_db
from backend.db.schemas.achat.facture_fournisseur_schemas import (
    FactureFournisseurCreate,
    FactureFournisseurUpdate,
    FactureFournisseurRead,
    FactureFournisseurDetail,
    FactureFournisseurSearch,
    FactureFournisseurSearchResults,
    FactureFournisseurBulkCreate,
    FactureFournisseurBulkDelete
)
from backend.services.achat import facture_fournisseur_service

router = APIRouter(
    prefix="/api/v1/achat/factures-fournisseur",
    tags=["Factures Fournisseur"]
)


@router.post("/", response_model=FactureFournisseurRead, summary="Créer une facture fournisseur")
def create_facture(facture: FactureFournisseurCreate, db: Session = Depends(get_db)):
    return facture_fournisseur_service.creer_facture(db, facture)


@router.get("/", response_model=List[FactureFournisseurRead], summary="Lister les factures fournisseur")
def list_factures(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return facture_fournisseur_service.list_factures(db, skip=skip, limit=limit)


@router.get("/{facture_id}", response_model=FactureFournisseurDetail, summary="Obtenir une facture fournisseur par ID")
def get_facture_detail(facture_id: int, db: Session = Depends(get_db)):
    return facture_fournisseur_service.get_facture(db, facture_id)


@router.put("/{facture_id}", response_model=FactureFournisseurRead, summary="Mettre à jour une facture fournisseur")
def update_facture(facture_id: int, data: FactureFournisseurUpdate, db: Session = Depends(get_db)):
    return facture_fournisseur_service.update_facture(db, facture_id, data)


@router.delete("/{facture_id}", response_model=dict, summary="Supprimer une facture fournisseur")
def delete_facture(facture_id: int, db: Session = Depends(get_db)):
    return facture_fournisseur_service.delete_facture(db, facture_id)


@router.post("/search", response_model=FactureFournisseurSearchResults, summary="Rechercher des factures fournisseur")
def search_factures(filters: FactureFournisseurSearch, skip: int = 0, limit: int = 50, db: Session = Depends(get_db)):
    return facture_fournisseur_service.search_factures(db, filters, skip=skip, limit=limit)


@router.post("/bulk", response_model=List[FactureFournisseurRead], summary="Créer plusieurs factures fournisseur")
def bulk_create_factures(payload: FactureFournisseurBulkCreate, db: Session = Depends(get_db)):
    return facture_fournisseur_service.bulk_create_factures(db, payload.factures)


@router.delete("/bulk", response_model=dict, summary="Supprimer plusieurs factures fournisseur")
def bulk_delete_factures(payload: FactureFournisseurBulkDelete, db: Session = Depends(get_db)):
    count = facture_fournisseur_service.bulk_delete_factures(db, payload.ids)
    return {"detail": f"{count} factures supprimées"}


@router.get("/export", response_class=StreamingResponse, summary="Exporter les factures au format CSV")
def export_factures(db: Session = Depends(get_db)):
    buffer = facture_fournisseur_service.export_factures_csv(db)
    return StreamingResponse(
        buffer,
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=factures_fournisseur.csv"}
    )