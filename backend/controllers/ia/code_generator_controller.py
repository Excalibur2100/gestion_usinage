from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.ia.code_generator_schemas import *
from services.ia.code_generator_service import *

router = APIRouter(prefix="/code-generator", tags=["Code Generator"])

@router.post("/", response_model=CodeGeneratorRead)
def create(data: CodeGeneratorCreate, db: Session = Depends(get_db)):
    return create_generation(db, data)

@router.get("/", response_model=List[CodeGeneratorRead])
def read_all(db: Session = Depends(get_db)):
    return get_all_generations(db)

@router.get("/{id_}", response_model=CodeGeneratorRead)
def read(id_: int, db: Session = Depends(get_db)):
    obj = get_generation(db, id_)
    if not obj:
        raise HTTPException(status_code=404, detail="Entrée non trouvée")
    return obj

@router.put("/{id_}", response_model=CodeGeneratorRead)
def update(id_: int, data: CodeGeneratorUpdate, db: Session = Depends(get_db)):
    obj = update_generation(db, id_, data)
    if not obj:
        raise HTTPException(status_code=404, detail="Entrée non trouvée")
    return obj

@router.delete("/{id_}")
def delete(id_: int, db: Session = Depends(get_db)):
    if not delete_generation(db, id_):
        raise HTTPException(status_code=404, detail="Entrée non trouvée")
    return {"ok": True}

@router.post("/search", response_model=CodeGeneratorSearchResults)
def search(data: CodeGeneratorSearch, db: Session = Depends(get_db)):
    return {"results": search_generations(db, data)}