from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base


class Sanction(Base):
    __tablename__ = "sanctions"
    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    type_sanction = Column(String(150))
    date = Column(DateTime)
    motif = Column(Text)

    # Relations
    utilisateur = relationship("Utilisateur", back_populates="sanctions")
