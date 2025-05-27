from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base

class ParametrageInterne(Base):
    __tablename__ = "parametrages_internes"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)

    entreprise_id = Column(Integer, ForeignKey("entreprises.id", ondelete="CASCADE"), nullable=False)

    cle = Column(String(100), nullable=False, comment="Nom du paramètre")
    valeur = Column(String(255), nullable=False, comment="Valeur brute du paramètre")
    description = Column(Text, nullable=True)
    actif = Column(Boolean, default=True)

    entreprise = relationship("Entreprise", back_populates="parametres")

    def __repr__(self):
        return f"<ParametrageInterne(cle='{self.cle}', entreprise={self.entreprise_id})>"