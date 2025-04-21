from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base


class EPIUtilisateur(Base):
    __tablename__ = "epis_utilisateur"
    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    nom_epi = Column(String(150), nullable=False)
    date_attribution = Column(String(50))
    date_retour = Column(String(50), nullable=True)

    # Relations
    utilisateur = relationship("Utilisateur", back_populates="epis")
