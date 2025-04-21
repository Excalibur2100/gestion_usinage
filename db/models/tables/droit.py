from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base


class Droit(Base):
    __tablename__ = "droits"
    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    module = Column(String(100))
    autorisation = Column(Boolean, default=False)

    # Relations
    utilisateur = relationship("Utilisateur", back_populates="droits")
