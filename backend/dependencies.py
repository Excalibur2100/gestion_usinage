from typing import Generator
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status, Request
from backend.db.models.database import SessionLocal

import logging

logger = logging.getLogger(__name__)


# ▶️ Session DB avec log de cycle de vie
def get_db() -> Generator[Session, None, None]:
    """
    Fournit une session DB SQLAlchemy pour chaque requête FastAPI.
    Gère proprement le cycle (open → yield → close).
    Journalise l'ouverture et la fermeture si DEBUG activé.
    """
    db = SessionLocal()
    logger.debug("📂 [DB] Session ouverte")
    try:
        yield db
    finally:
        db.close()
        logger.debug("✅ [DB] Session fermée")


# ▶️ Placeholder futur pour auth : utilisateur connecté
def get_current_user(request: Request):
    """
    Récupère l'utilisateur connecté à partir du token, header ou session.
    À connecter avec le système de sécurité du projet (ex: JWT/OAuth2).
    """
    # Exemple future (à implémenter dans `auth/jwt.py`) :
    # token = request.headers.get("Authorization")
    # return decode_token(token)
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Authentification requise"
    )


# ▶️ Vérifie que l'utilisateur a un rôle admin
def get_admin_user(current_user=Depends(get_current_user)):
    """
    Vérifie que l'utilisateur est administrateur.
    À brancher sur `current_user.role`, `permissions`, etc.
    """
    # Exemple future :
    # if current_user.role != "admin":
    #     raise HTTPException(status_code=403, detail="Accès interdit (admin uniquement)")
    return current_user


# ▶️ Settings applicatifs centralisés (optionnel)
def get_settings():
    """
    Fonction pour injecter les paramètres globaux (env, config, secrets).
    Exemple : app name, email d’expédition, activation debug, etc.
    """
    from backend.core.config import settings  # ← à créer dans ton projet
    return settings