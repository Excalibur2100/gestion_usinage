from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import os
import sys
from dotenv import load_dotenv

# Charger les variables d'environnement depuis config.env
load_dotenv(dotenv_path="config.env")

# Ajouter le chemin du projet pour permettre l'import des modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Importer la base et les modèles
from db.models.base import Base

# Configuration Alembic
config = context.config

# Charger DATABASE_URL depuis les variables d'environnement
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL n'est pas configurée dans config.env")

# Configurer l'URL de la base de données pour Alembic
config.set_main_option("sqlalchemy.url", DATABASE_URL)

# Configurer le logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Cible pour l'autogénération des migrations
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Exécuter les migrations en mode hors-ligne."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Exécuter les migrations en mode en-ligne."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True  # Compare aussi les types de colonnes
        )

        with context.begin_transaction():
            context.run_migrations()

# Déterminer le mode d'exécution (hors-ligne ou en-ligne)
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()