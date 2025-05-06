from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from db.models.base import Base

class EmplacementStock(Base):
    __tablename__ = "emplacements"

    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False, comment="Nom de l'emplacement")
    type = Column(
        String(50),
        nullable=False,
        comment="Type d'emplacement (ex: armoire, rack, bac)",
    )
    capacite = Column(
        Float, nullable=False, comment="Capacité maximale de l'emplacement (en kg)"
    )
    occupation_actuelle = Column(
        Float,
        default=0.0,
        nullable=False,
        comment="Occupation actuelle de l'emplacement (en kg)",
    )

    # Relations
    outils = relationship("Outil", back_populates="emplacement")
    materiaux = relationship("Materiau", back_populates="emplacement")