from sqlalchemy import Column, Integer, String, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from db.models.base import Base

class Site(Base):
    __tablename__ = "sites"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)

    entreprise_id = Column(Integer, ForeignKey("entreprises.id", ondelete="CASCADE"), nullable=False)

    nom = Column(String(100), nullable=False)
    adresse = Column(Text, nullable=True)
    code_postal = Column(String(20), nullable=True)
    ville = Column(String(100), nullable=True)
    pays = Column(String(100), nullable=False, default="France")
    actif = Column(Boolean, default=True)

    entreprise = relationship("Entreprise", back_populates="sites")
    utilisateurs = relationship("UtilisateurSite", back_populates="site", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Site(nom='{self.nom}', entreprise={self.entreprise_id})>"