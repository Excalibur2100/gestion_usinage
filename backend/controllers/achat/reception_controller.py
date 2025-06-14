from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from fastapi.responses import StreamingResponse

from backend.dependencies import get_db
from backend.services.achat import reception_service
from backend.db.schemas.achat.reception_schemas import (
    ReceptionCreate,
    ReceptionRead,
    ReceptionUpdate,
    ReceptionSearch,
    ReceptionSearchResults,
    ReceptionBulkCreate,
    ReceptionResponse
)

import csv
import io


router = APIRouter(
    prefix="/api/v1/receptions",
    tags=["Receptions"]
)


@router.post("", response_model=ReceptionRead, summary="Créer une réception", description="Créer une nouvelle réception fournisseur")
def create_reception(reception_in: ReceptionCreate, db: Session = Depends(get_db)):
    return reception_service.create_reception(db, reception_in)


@router.get("/{reception_id}", response_model=ReceptionRead, summary="Lire une réception", description="Lire une réception à partir de son ID")
def read_reception(reception_id: int, db: Session = Depends(get_db)):
    reception = reception_service.get_reception_by_id(db, reception_id)
    if not reception:
        raise HTTPException(status_code=404, detail="Réception non trouvée")
    return reception


@router.get("", response_model=list[ReceptionRead], summary="Lister toutes les réceptions", description="Lister toutes les réceptions, avec pagination")
def list_receptions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return reception_service.get_all_receptions(db, skip, limit)


@router.put("/{reception_id}", response_model=ReceptionRead, summary="Mettre à jour une réception", description="Met à jour une réception existante")
def update_reception(reception_id: int, reception_in: ReceptionUpdate, db: Session = Depends(get_db)):
    updated = reception_service.update_reception(db, reception_id, reception_in)
    if not updated:
        raise HTTPException(status_code=404, detail="Réception non trouvée")
    return updated


@router.delete("/{reception_id}", response_model=dict, summary="Supprimer une réception", description="Supprimer une réception fournisseur par ID")
def delete_reception(reception_id: int, db: Session = Depends(get_db)):
    success = reception_service.delete_reception(db, reception_id)
    if not success:
        raise HTTPException(status_code=404, detail="Réception non trouvée")
    return {"message": "Réception supprimée avec succès."}


@router.post("/search", response_model=ReceptionSearchResults, summary="Rechercher des réceptions", description="Recherche multi-critères dans les réceptions")
def search_receptions(search: ReceptionSearch, db: Session = Depends(get_db)):
    results = reception_service.search_receptions(db, search)
    results_read = [ReceptionRead.from_orm(r) for r in results]
    return ReceptionSearchResults(total=len(results_read), results=results_read)


@router.post("/bulk", response_model=list[ReceptionRead], summary="Créer plusieurs réceptions", description="Créer plusieurs réceptions en une seule requête")
def bulk_create_receptions(receptions: ReceptionBulkCreate, db: Session = Depends(get_db)):
    return reception_service.bulk_create_receptions(db, receptions.receptions)


@router.get("/detail/{reception_id}", response_model=ReceptionRead, summary="Détail d'une réception", description="Accéder au détail complet d'une réception")
def detail_reception(reception_id: int, db: Session = Depends(get_db)):
    reception = reception_service.get_reception_by_id(db, reception_id)
    if not reception:
        raise HTTPException(status_code=404, detail="Réception non trouvée")
    return reception


@router.get("/export", response_class=StreamingResponse, summary="Exporter les réceptions", description="Exporter les réceptions au format CSV")
def export_receptions(db: Session = Depends(get_db)):
    receptions = reception_service.get_all_receptions(db)
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["ID", "Numéro", "Date", "Statut", "Commande ID"])
    for r in receptions:
        writer.writerow([r.id, r.numero_reception, r.date_reception, r.statut.value, r.commande_id])
    output.seek(0)
    return StreamingResponse(output, media_type="text/csv", headers={"Content-Disposition": "attachment; filename=receptions.csv"})