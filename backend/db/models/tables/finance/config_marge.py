from sqlalchemy import Column, Integer, Float, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base

class ConfigMarge(Base):
    __tablename__ = "config_marges"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)

    client_id = Column(Integer, ForeignKey("clients.id", ondelete="SET NULL"), nullable=True)
    entreprise_id = Column(Integer, ForeignKey("entreprises.id", ondelete="CASCADE"), nullable=False)

    type_marge = Column(String(50), default="globale", comment="globale, par famille, par produit...")
    valeur = Column(Float, nullable=False)
    unite = Column(String(10), default="%", comment="% ou EUR")
    commentaire = Column(Text, nullable=True)

    client = relationship("Client", back_populates="marges")
    entreprise = relationship("Entreprise", back_populates="marges")

    def __repr__(self):
        return f"<ConfigMarge(type={self.type_marge}, valeur={self.valeur}{self.unite})>"