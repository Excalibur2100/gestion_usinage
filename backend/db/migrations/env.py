from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import os
import sys
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv(dotenv_path="config.env")

# Ajouter le dossier racine du projet
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Importer Base et tous les modèles
from db.models.base import Base
import importlib
import pkgutil
import db.models.table

# Import dynamique de tous les fichiers de db.models.tables
for _, module_name, _ in pkgutil.iter_modules(db.models.table.__path__):
    importlib.import_module(f"db.models.tables.{module_name}")

# Configuration Alembic
config = context.config

# URL de la base de données
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL n'est pas définie dans config.env")

config.set_main_option("sqlalchemy.url", DATABASE_URL)

# Logging
if config.config_file_name:
    fileConfig(config.config_file_name)

# Cible de migration
target_metadata = Base.metadata

def run_migrations_offline() -> None:
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
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )
        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
