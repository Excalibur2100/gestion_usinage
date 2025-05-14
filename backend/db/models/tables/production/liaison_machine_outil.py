from sqlalchemy import Table, Column, Integer, ForeignKey
from db.models.base import Base

# ========================= ASSOCIATION MACHINE ↔ OUTIL =========================
# Table d'association pour la relation many-to-many entre Machine et Outil
machine_outil = Table(
    "machine_outil",
    Base.metadata,
    Column(
        "machine_id",
        ForeignKey("machines.id", ondelete="CASCADE"),
        primary_key=True,
        comment="ID de la machine associée",
    ),
    Column(
        "outil_id",
        ForeignKey("outils.id", ondelete="CASCADE"),
        primary_key=True,
        comment="ID de l'outil associé",
    ),
)
