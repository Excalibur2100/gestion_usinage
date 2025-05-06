from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base


class Absence(Base):
    __tablename__ = "absences"
    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    date_debut = Column(DateTime)
    date_fin = Column(DateTime)
    type_absence = Column(String(100))
    commentaire = Column(Text)

    # Relations
    utilisateur = relationship("Utilisateur", back_populates="absences")
