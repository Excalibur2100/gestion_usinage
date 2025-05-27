from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.models.base import Base

class ObjectifCommercial(Base):
    __tablename__ = "objectifs_commerciaux"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)

    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="CASCADE"), nullable=False)
    periode = Column(String(20), nullable=False, comment="Format AAAA-MM")
    objectif_chiffre = Column(Float, nullable=False)
    objectif_marge = Column(Float, nullable=True)
    objectif_clients = Column(Integer, nullable=True)

    date_creation = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    utilisateur = relationship("Utilisateur", back_populates="objectifs_commerciaux")

    def __repr__(self):
        return f"<ObjectifCommercial(user={self.utilisateur_id}, periode={self.periode})>"
