from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.entreprise.parametrage_interne_schemas import *
from services.entreprise.parametrage_interne_service import *

router = APIRouter(prefix="/parametrages-internes", tags=["Paramétrage Interne"])

@router.post("/", response_model=ParametrageInterneRead)
def create(data: ParametrageInterneCreate, db: Session = Depends(get_db)):
    return create_parametre(db, data)

@router.get("/", response_model=List[ParametrageInterneRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_parametres(db)

@router.get("/{id_}", response_model=ParametrageInterneRead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_parametre(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Paramètre non trouvé")
    return obj

@router.put("/{id_}", response_model=ParametrageInterneRead)
def update(id_: int, data: ParametrageInterneUpdate, db: Session = Depends(get_db)):
    obj = update_parametre(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Paramètre non trouvé")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_parametre(db, id_):
        raise HTTPException(status_code=404, detail="Paramètre non trouvé")
    return {"ok": True}

@router.post("/search", response_model=ParametrageInterneSearchResults)
def search(data: ParametrageInterneSearch, db: Session = Depends(get_db)):
    return {"results": search_parametres(db, data)}