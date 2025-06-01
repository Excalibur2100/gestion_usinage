from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
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
    CommandeFournisseurBulkDelete,
)

from backend.services.achat import commande_fournisseur_service

router = APIRouter(
    prefix="/api/v1/achat/commandes-fournisseur",
    tags=["Commandes Fournisseur"]
)


@router.post("/", response_model=CommandeFournisseurRead, summary="Créer une commande fournisseur")
def create_commande(commande: CommandeFournisseurCreate, db: Session = Depends(get_db)):
    """
    Crée une commande fournisseur sans logique métier.  
    Utilise uniquement le service CRUD standard.
    """
    return commande_fournisseur_service.creer_commande(db, commande)


@router.get("/", response_model=List[CommandeFournisseurRead], summary="Lister toutes les commandes fournisseur")
def list_commandes(
    skip: int = 0,
    limit: int = 100,
    numero_commande: Optional[str] = Query(None),
    statut: Optional[str] = Query(None),
    fournisseur_id: Optional[int] = Query(None),
    date_min: Optional[str] = Query(None),
    date_max: Optional[str] = Query(None),
    is_archived: Optional[bool] = Query(None),
    db: Session = Depends(get_db)
):
    """
    Liste paginée et filtrée des commandes fournisseur.
    """
    from datetime import datetime

    date_min_dt = datetime.fromisoformat(date_min) if date_min else None
    date_max_dt = datetime.fromisoformat(date_max) if date_max else None

    from backend.db.schemas.achat.commande_fournisseur_schemas import StatutCommandeFournisseur

    statut_enum = None
    if statut is not None:
        try:
            statut_enum = StatutCommandeFournisseur(statut)
        except ValueError:
            raise HTTPException(status_code=400, detail=f"Statut '{statut}' invalide.")

    filters = CommandeFournisseurSearch(
        numero_commande=numero_commande,
        statut=statut_enum,
        fournisseur_id=fournisseur_id,
        date_min=date_min_dt,
        date_max=date_max_dt,
        is_archived=is_archived
    )
    return commande_fournisseur_service.search_commandes(db, filters, skip, limit)


@router.get("/{commande_id}", response_model=CommandeFournisseurDetail, summary="Récupérer une commande fournisseur")
def get_commande(commande_id: int, db: Session = Depends(get_db)):
    """
    Récupère une commande fournisseur par ID.
    """
    return commande_fournisseur_service.get_commande(db, commande_id)


@router.put("/{commande_id}", response_model=CommandeFournisseurRead, summary="Mettre à jour une commande fournisseur")
def update_commande(commande_id: int, update: CommandeFournisseurUpdate, db: Session = Depends(get_db)):
    """
    Met à jour une commande fournisseur (aucune règle de statut ici).
    """
    return commande_fournisseur_service.update_commande(db, commande_id, update)


@router.delete("/{commande_id}", response_model=dict, summary="Supprimer une commande fournisseur")
def delete_commande(commande_id: int, db: Session = Depends(get_db)):
    """
    Supprime une commande fournisseur (peu importe son statut).
    """
    return commande_fournisseur_service.delete_commande(db, commande_id)


@router.post("/search", response_model=CommandeFournisseurSearchResults, summary="Rechercher des commandes fournisseur")
def search_commandes(filters: CommandeFournisseurSearch, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Recherche filtrée des commandes fournisseur par numéro, statut, dates, etc.
    """
    results = commande_fournisseur_service.search_commandes(db, filters, skip, limit)
    return {"total": len(results), "results": results}


@router.get("/export", response_class=StreamingResponse, summary="Exporter les commandes fournisseur en CSV")
def export_csv(db: Session = Depends(get_db)):
    """
    Exporte toutes les commandes fournisseur au format CSV.
    """
    return commande_fournisseur_service.export_commandes_csv(db)


@router.post("/bulk", response_model=List[CommandeFournisseurRead], summary="Création en masse de commandes")
def bulk_create(payload: CommandeFournisseurBulkCreate, db: Session = Depends(get_db)):
    """
    Crée plusieurs commandes en une seule requête.
    """
    return commande_fournisseur_service.bulk_create_commandes(db, payload.commandes)


@router.delete("/bulk", response_model=dict, summary="Suppression en masse de commandes")
def bulk_delete(payload: CommandeFournisseurBulkDelete, db: Session = Depends(get_db)):
    """
    Supprime plusieurs commandes en une seule requête.
    """
    return commande_fournisseur_service.bulk_delete_commandes(db, payload.ids)