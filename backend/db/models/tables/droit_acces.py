from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base

class DroitAcces(Base):
    __tablename__ = "droits_acces"
    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    droit_id = Column(Integer, ForeignKey("droits.id"))

    # Relations
    utilisateur = relationship("Utilisateur", back_populates="droits_acces")
    droit = relationship("Droit", back_populates="droits_acces")