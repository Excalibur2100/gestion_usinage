from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.entreprise.site_schemas import *
from services.entreprise.site_service import *

router = APIRouter(prefix="/sites", tags=["Sites Entreprise"])

@router.post("/", response_model=SiteRead)
def create(data: SiteCreate, db: Session = Depends(get_db)):
    return create_site(db, data)

@router.get("/", response_model=List[SiteRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_sites(db)

@router.get("/{id_}", response_model=SiteRead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_site(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Site non trouvé")
    return obj

@router.put("/{id_}", response_model=SiteRead)
def update(id_: int, data: SiteUpdate, db: Session = Depends(get_db)):
    obj = update_site(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Site non trouvé")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_site(db, id_):
        raise HTTPException(status_code=404, detail="Site non trouvé")
    return {"ok": True}

@router.post("/search", response_model=SiteSearchResults)
def search(data: SiteSearch, db: Session = Depends(get_db)):
    return {"results": search_sites(db, data)}