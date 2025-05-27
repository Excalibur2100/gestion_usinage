from typing import List, Optional
from sqlalchemy.orm import Session
from db.models.tables.ia.code_generator import CodeGenerator
from db.schemas.ia.code_generator_schemas import *

def create_generation(db: Session, data: CodeGeneratorCreate) -> CodeGenerator:
    obj = CodeGenerator(**data.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_generation(db: Session, id_: int) -> Optional[CodeGenerator]:
    return db.query(CodeGenerator).filter(CodeGenerator.id == id_).first()

def get_all_generations(db: Session) -> List[CodeGenerator]:
    return db.query(CodeGenerator).all()

def update_generation(db: Session, id_: int, data: CodeGeneratorUpdate) -> Optional[CodeGenerator]:
    obj = get_generation(db, id_)
    if not obj:
        return None
    for key, value in data.dict(exclude_unset=True).items():
        setattr(obj, key, value)
    db.commit()
    db.refresh(obj)
    return obj

def delete_generation(db: Session, id_: int) -> bool:
    obj = get_generation(db, id_)
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def search_generations(db: Session, search_data: CodeGeneratorSearch) -> List[CodeGenerator]:
    query = db.query(CodeGenerator)
    if search_data.utilisateur_id:
        query = query.filter(CodeGenerator.utilisateur_id == search_data.utilisateur_id)
    if search_data.langage:
        query = query.filter(CodeGenerator.langage.ilike(f"%{search_data.langage}%"))
    if search_data.nom_session:
        query = query.filter(CodeGenerator.nom_session.ilike(f"%{search_data.nom_session}%"))
    return query.all()
