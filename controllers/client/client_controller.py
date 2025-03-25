from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db.models.database import get_db
from db.schemas.schemas import ClientCreate, ClientRead
from services.client.client_services import (
    creer_client,
    get_tous_clients,
    get_client_par_id,
    update_client,
    supprimer_client
)

router = APIRouter(prefix="/clients", tags=["Clients"])

# ========== CRÉATION ==========
@router.post("/", response_model=ClientRead)
def creer(client_data: ClientCreate, db: Session = Depends(get_db)):
    return creer_client(db, client_data)

# ========== TOUS ==========
@router.get("/", response_model=list[ClientRead])
def lire_tous(db: Session = Depends(get_db)):
    return get_tous_clients(db)

# ========== PAR ID ==========
@router.get("/{id}", response_model=ClientRead)
def lire_un(id: int, db: Session = Depends(get_db)):
    client = get_client_par_id(db, id)
    if not client:
        raise HTTPException(status_code=404, detail="Client non trouvé")
    return client

# ========== MISE À JOUR ==========
@router.put("/{id}", response_model=ClientRead)
def maj_client(id: int, client_data: ClientCreate, db: Session = Depends(get_db)):
    client = update_client(db, id, client_data)
    if not client:
        raise HTTPException(status_code=404, detail="Client non trouvé pour mise à jour")
    return client

# ========== SUPPRESSION ==========
@router.delete("/{id}", status_code=204)
def supprimer(id: int, db: Session = Depends(get_db)):
    supprimer_client(db, id)
    return
