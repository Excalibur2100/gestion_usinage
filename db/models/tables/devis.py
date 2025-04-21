from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime


# ========================= DEVIS =========================
class Devis(Base):
    __tablename__ = "devis"

    id = Column(Integer, primary_key=True)
    client_id = Column(
        Integer,
        ForeignKey("clients.id"),
        nullable=False,
        comment="ID du client associé",
    )
    montant_total = Column(Float, nullable=False, comment="Montant total du devis")
    date_creation = Column(
        DateTime, default=datetime.utcnow, comment="Date de création du devis"
    )
    date_livraison_souhaitee = Column(
        DateTime, nullable=True, comment="Date de livraison souhaitée"
    )
    statut = Column(
        String(50),
        nullable=False,
        comment="Statut du devis (brouillon, validé, annulé)",
    )

    # Relations
    client = relationship("Client", back_populates="devis")
    commandes = relationship(
        "Commande", back_populates="devis", cascade="all, delete-orphan"
    )
