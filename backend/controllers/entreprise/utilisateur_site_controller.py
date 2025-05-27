from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.entreprise.utilisateur_site_schemas import *
from services.entreprise.utilisateur_site_service import *

router = APIRouter(prefix="/utilisateurs-sites", tags=["Utilisateurs - Sites"])

@router.post("/", response_model=UtilisateurSiteRead)
def create(data: UtilisateurSiteCreate, db: Session = Depends(get_db)):
    return create_utilisateur_site(db, data)

@router.get("/", response_model=List[UtilisateurSiteRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_utilisateurs_sites(db)

@router.get("/{id_}", response_model=UtilisateurSiteRead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_utilisateur_site(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Association non trouvée")
    return obj

@router.put("/{id_}", response_model=UtilisateurSiteRead)
def update(id_: int, data: UtilisateurSiteUpdate, db: Session = Depends(get_db)):
    obj = update_utilisateur_site(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Association non trouvée")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_utilisateur_site(db, id_):
        raise HTTPException(status_code=404, detail="Association non trouvée")
    return {"ok": True}

@router.post("/search", response_model=UtilisateurSiteSearchResults)
def search(data: UtilisateurSiteSearch, db: Session = Depends(get_db)):
    return {"results": search_utilisateurs_sites(db, data)}