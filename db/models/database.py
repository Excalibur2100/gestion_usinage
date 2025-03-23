from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

# 🔗 Import de la base et des modèles
from db.models.models import Base

# Accès à la configuration Alembic
config = context.config

# Configuration du logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Définition de la metadata pour l'autogénération
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Exécution des migrations en mode offline."""
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
    """Exécution des migrations en mode online."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True  # ➕ Compare aussi les changements de type
        )
        with context.begin_transaction():
            context.run_migrations()

# Démarrage des migrations
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
