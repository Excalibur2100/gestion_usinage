from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Boolean,
    ForeignKey,
    DateTime,
    Text,
)
from sqlalchemy.orm import relationship
from db.models.base import Base


class RH(Base):
    __tablename__ = "rh"
    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    poste = Column(String(100))
    contrat = Column(String(100))
    temps_travail = Column(Float)
    est_cadre = Column(Boolean)
    date_debut = Column(DateTime)
    salaire_brut = Column(Float)
    statut_administratif = Column(String(100))
    remarques = Column(Text)

    # Relations
    utilisateur = relationship("Utilisateur", back_populates="rh")
