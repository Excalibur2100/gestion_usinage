from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from db.models.base import Base

class Droit(Base):
    __tablename__ = "droits"

    id = Column(Integer, primary_key=True)
    module = Column(String(100), nullable=False, comment="Nom du module ou action concernée (ex: planning, stock)")
    autorisation = Column(Boolean, default=False, nullable=False, comment="Autorisation globale par défaut (utilisé en fallback)")

    # Relations
    droits_acces = relationship("DroitAcces", back_populates="droit", cascade="all, delete-orphan", lazy="joined")

    def __repr__(self):
        return f"<Droit module={self.module} autorisation={self.autorisation}>"
