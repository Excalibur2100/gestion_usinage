from sqlalchemy import Column, Integer, Float, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base


class NotationRH(Base):
    __tablename__ = "notations_rh"
    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    date_evaluation = Column(DateTime)
    note = Column(Float)
    commentaire = Column(Text)

    # Relations
    utilisateur = relationship("Utilisateur", back_populates="notations")
