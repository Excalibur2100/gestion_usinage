from sqlalchemy import Table, Column, Integer, ForeignKey
from db.models.base import Base

# ========================= ASSOCIATION MACHINE ↔ OUTIL =========================
machine_outil = Table(
    'machine_outil', Base.metadata,
    Column('machine_id', ForeignKey('machines.id'), primary_key=True),
    Column('outil_id', ForeignKey('outils.id'), primary_key=True)
)