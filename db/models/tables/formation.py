from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base


class Formation(Base):
    __tablename__ = "formations"
    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    nom = Column(String(150))
    organisme = Column(String(150))
    date_debut = Column(DateTime)
    date_fin = Column(DateTime)
    certification = Column(String(150))
    commentaire = Column(Text)

    # Relations
    utilisateur = relationship("Utilisateur", back_populates="formations")
