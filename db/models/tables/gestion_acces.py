from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base

class GestionAcces(Base):
    __tablename__ = "gestion_acces"
    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    niveau_acces = Column(String(50))

    # Relations
    utilisateur = relationship("Utilisateur", back_populates="gestion_acces")