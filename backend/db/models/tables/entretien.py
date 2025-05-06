from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base


class Entretien(Base):
    __tablename__ = "entretiens"
    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    type_entretien = Column(String(100))
    date = Column(DateTime)
    resume = Column(Text)
    actions_prevues = Column(Text)

    # Relations
    utilisateur = relationship("Utilisateur", back_populates="entretiens")
