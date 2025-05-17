from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.config.database import get_db
from db.schemas.crm.tag_schemas import TagCreate, TagRead
from db.services.crm.tag_service import create_tag, get_all_tags

router = APIRouter(prefix="/tags", tags=["Tag"])

@router.post("/", response_model=TagRead)
def create(tag: TagCreate, db: Session = Depends(get_db)):
    return create_tag(db, tag)

@router.get("/", response_model=list[TagRead])
def list_all(db: Session = Depends(get_db)):
    return get_all_tags(db)
