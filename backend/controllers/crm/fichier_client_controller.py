from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from schemas.crm.fichier_client_schemas import (
    FichierClientCreate, FichierClientRead, FichierClientUpdate,
    FichierClientDelete, FichierClientList
)
from services.crm.fichier_client_service import (
    create_fichier, get_fichiers_by_client, get_all_fichiers,
    get_fichier_by_id, update_fichier, delete_fichier
)

router = APIRouter(prefix="/fichiers-client", tags=["Fichier Client"])

@router.post("/", response_model=FichierClientRead)
def create(fichier: FichierClientCreate, db: Session = Depends(get_db)):
    return create_fichier(db, fichier)

@router.get("/", response_model=FichierClientList)
def list_all(db: Session = Depends(get_db)):
    fichiers = get_all_fichiers(db)
    return {"fichiers": fichiers}

@router.get("/client/{client_id}", response_model=list[FichierClientRead])
def list_by_client(client_id: int, db: Session = Depends(get_db)):
    return get_fichiers_by_client(db, client_id)

@router.get("/{fichier_id}", response_model=FichierClientRead)
def get_one(fichier_id: int, db: Session = Depends(get_db)):
    fichier = get_fichier_by_id(db, fichier_id)
    if not fichier:
        raise HTTPException(status_code=404, detail="Fichier non trouvé")
    return fichier

@router.put("/{fichier_id}", response_model=FichierClientRead)
def update(fichier_id: int, data: FichierClientUpdate, db: Session = Depends(get_db)):
    updated = update_fichier(db, fichier_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Fichier non trouvé")
    return updated

@router.delete("/{fichier_id}", response_model=FichierClientDelete)
def delete(fichier_id: int, db: Session = Depends(get_db)):
    deleted = delete_fichier(db, fichier_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Fichier non trouvé")
    return {"id": fichier_id}
