from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
from typing import List


class Settings(BaseSettings):
    """
    Configuration centrale de l'ERP Usinage.
    Toutes les valeurs peuvent être surchargées par un fichier .env.
    """

    # === ENVIRONNEMENT ===
    ENV: str = "development"  # dev, staging, production
    DEBUG: bool = True
    LOG_LEVEL: str = "INFO"
    PROJECT_NAME: str = "ERP Usinage"
    VERSION: str = "1.0.0"
    API_PREFIX: str = "/api/v1"
    ALLOWED_HOSTS: List[str] = ["localhost", "127.0.0.1"]
    CORS_ORIGINS: List[str] = ["http://localhost", "https://erp.monentreprise.fr"]

    # === BASE DE DONNÉES ===
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///./dev.db"
    TEST_DATABASE_URI: str = "sqlite:///./test.db"

    # === EMAIL ===
    SMTP_HOST: str = "smtp.example.com"
    SMTP_PORT: int = 587
    SMTP_USER: str = "admin@example.com"
    SMTP_PASSWORD: str = "secure-password"
    EMAIL_FROM: str = "erp@example.com"

    # === SÉCURITÉ ===
    SECRET_KEY: str = "super-secret-key"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    JWT_ALGORITHM: str = "HS256"

    # === EXPORT / EXTENSIONS ===
    EXPORT_FOLDER: str = "./exports"
    EXTERNAL_API_URL: str = "https://api.externe.com"
    IA_MODEL_PATH: str = "./models"

    # === IA / MÉTIER ===
    ENABLE_IA: bool = True
    OPTIMISATION_PAR_DEFAUT: str = "standard"

    # === PARAMÈTRES INTERNES ===
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


@lru_cache()
def get_settings():
    """
    Fournit une instance de configuration globale (avec cache).
    À utiliser partout via : `settings = get_settings()`
    """
    return Settings()


# Accès direct par import
settings = get_settings()