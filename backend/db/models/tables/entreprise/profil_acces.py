from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base

class ProfilAcces(Base):
    __tablename__ = "profils_acces"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)

    entreprise_id = Column(Integer, ForeignKey("entreprises.id", ondelete="CASCADE"), nullable=False)

    nom = Column(String(100), nullable=False, unique=False)
    description = Column(Text, nullable=True)

    entreprise = relationship("Entreprise", back_populates="profils")

    def __repr__(self):
        return f"<ProfilAcces(nom='{self.nom}', entreprise={self.entreprise_id})>"