from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base

class PreferenceEntreprise(Base):
    __tablename__ = "preferences_entreprise"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)

    entreprise_id = Column(Integer, ForeignKey("entreprises.id", ondelete="CASCADE"), nullable=False)

    langue = Column(String(10), nullable=False, default="fr")
    fuseau_horaire = Column(String(100), nullable=True, default="Europe/Paris")
    format_date = Column(String(20), default="DD/MM/YYYY")
    affichage_24h = Column(Boolean, default=True)
    theme = Column(String(50), default="clair")

    entreprise = relationship("Entreprise", back_populates="preferences")

    def __repr__(self):
        return f"<PreferenceEntreprise(entreprise={self.entreprise_id}, langue='{self.langue}')>"