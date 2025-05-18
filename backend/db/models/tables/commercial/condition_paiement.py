from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from db.models.base import Base

class ConditionPaiement(Base):
    __tablename__ = "conditions_paiement"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    libelle = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=True)

    commandes = relationship("Commande", back_populates="condition_paiement")

    def __repr__(self):
        return f"<ConditionPaiement(libelle='{self.libelle}')>"
