from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.config.database import get_db
from db.schemas.crm.tag_client_schemas import TagClientCreate, TagClientRead
from db.services.crm.tag_client_service import assign_tag, remove_tag

router = APIRouter(prefix="/tag-client", tags=["Tag Client"])

@router.post("/", response_model=TagClientRead)
def assign(data: TagClientCreate, db: Session = Depends(get_db)):
    return assign_tag(db, data)

@router.delete("/{tag_client_id}")
def remove(tag_client_id: int, db: Session = Depends(get_db)):
    deleted = remove_tag(db, tag_client_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Association non trouvée")
    return {"message": "Tag dissocié du client"}
