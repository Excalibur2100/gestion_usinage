from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime

# ========================= FINANCE =========================
class Finance(Base):
    __tablename__ = "finance"
    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    type_transaction = Column(String(50), nullable=False)  # revenu, dépense
    montant = Column(Float, nullable=False)
    date_transaction = Column(DateTime, default=datetime.utcnow)
    description = Column(Text, nullable=True)

    utilisateur = relationship("Utilisateur", back_populates="finances")

# ========================= STAT FINANCE =========================
class StatFinance(Base):
    __tablename__ = "stat_finance"
    id = Column(Integer, primary_key=True)
    periode = Column(String(50), nullable=False)  # mensuel, annuel, etc.
    revenu_total = Column(Float, nullable=False)
    depense_totale = Column(Float, nullable=False)
    profit = Column(Float, nullable=False)
    date_calcul = Column(DateTime, default=datetime.utcnow)