from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.models.base import Base

class CampagneCommerciale(Base):
    __tablename__ = "campagnes_commerciales"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    nom = Column(String(100), unique=True, nullable=False)
    objectif = Column(Text, nullable=True)
    date_debut = Column(DateTime(timezone=True), nullable=True)
    date_fin = Column(DateTime(timezone=True), nullable=True)
    statut = Column(String(50), default="planifiée")

    # Relations
    actions = relationship("ActionCommerciale", back_populates="campagne", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<CampagneCommerciale(nom='{self.nom}', statut='{self.statut}')>"
