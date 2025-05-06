# services/ia/code_generator_service.py

from datetime import datetime, timezone
from pydantic import BaseModel


class CodeGenRequest(BaseModel):
    module_name: str
    entity_name: str  # ex: "Client"
    include_controller: bool = True
    include_service: bool = True


class CodeGenResponse(BaseModel):
    controller_code: str | None = None
    service_code: str | None = None
    message: str
    created_at: datetime = datetime.now(timezone.utc)


def generate_controller_code(entity_name: str) -> str:
    return f"""# controllers/{entity_name.lower()}_controller.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.models import {entity_name}
from db.schemas import {entity_name}Create, {entity_name}Read
from services.{entity_name.lower()}_service import (
    create_{entity_name.lower()},
    get_all_{entity_name.lower()}
)
from db.database import get_db

router = APIRouter(prefix="/{entity_name.lower()}s", tags=["{entity_name}"])

@router.post("/", response_model={entity_name}Read)
def create(item: {entity_name}Create, db: Session = Depends(get_db)):
    return create_{entity_name.lower()}(db, item)

@router.get("/", response_model=list[{entity_name}Read])
def read_all(db: Session = Depends(get_db)):
    return get_all_{entity_name.lower()}(db)
"""


def generate_service_code(entity_name: str) -> str:
    return f"""# services/{entity_name.lower()}_service.py

from sqlalchemy.orm import Session
from db.models import {entity_name}
from db.schemas import {entity_name}Create

def create_{entity_name.lower()}(db: Session, item: {entity_name}Create) -> {entity_name}:
    obj = {entity_name}(**item.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def get_all_{entity_name.lower()}(db: Session):
    return db.query({entity_name}).all()
"""


def generate_code(request: CodeGenRequest) -> CodeGenResponse:
    controller = generate_controller_code(request.entity_name) if request.include_controller else None
    service = generate_service_code(request.entity_name) if request.include_service else None

    return CodeGenResponse(
        controller_code=controller,
        service_code=service,
        message=f"Code généré avec succès pour le module '{request.entity_name}'."
    )