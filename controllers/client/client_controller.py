from fastapi import APIRouter

router = APIRouter(
    prefix="/clients",  # Utilisation du pluriel pour refléter les bonnes pratiques REST
    tags=["Clients"]    # Correction du tag pour une meilleure catégorisation
)

@router.get("/")
async def get_clients():
    """
    Endpoint pour récupérer tous les clients.
    """
    return {"message": "Liste des clients récupérée avec succès"}

@router.get("/{client_id}")
async def get_client(client_id: int):
    """
    Endpoint pour récupérer un client spécifique par son ID.
    """
    return {"message": f"Client avec l'ID {client_id} récupéré avec succès"}

@router.post("/")
async def create_client(client: dict):
    """
    Endpoint pour créer un nouveau client.
    """
    return {"message": "Client créé avec succès", "client": client}

@router.put("/{client_id}")
async def update_client(client_id: int, client: dict):
    """
    Endpoint pour mettre à jour un client existant.
    """
    return {"message": f"Client avec l'ID {client_id} mis à jour avec succès", "client": client}

@router.delete("/{client_id}")
async def delete_client(client_id: int):
    """
    Endpoint pour supprimer un client par son ID.
    """
    return {"message": f"Client avec l'ID {client_id} supprimé avec succès"}