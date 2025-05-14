from sqlalchemy import Column, Integer, String, Float, CheckConstraint
from sqlalchemy.orm import relationship
from db.models.base import Base

class EmplacementStock(Base):
    __tablename__ = "emplacements"

    id = Column(Integer, primary_key=True)

    code_emplacement = Column(String(50), unique=True, nullable=False, comment="Code interne ou code-barres de l'emplacement")
    nom = Column(String(100), nullable=False, comment="Nom visible de l'emplacement")
    type = Column(String(50), nullable=False, comment="Type : rack, armoire, bac, palette")
    capacite = Column(Float, nullable=False, comment="Capacité max (en kg)")
    occupation_actuelle = Column(Float, default=0.0, nullable=False, comment="Occupation actuelle (en kg)")

    # Relations
    outils = relationship("Outil", back_populates="emplacement", cascade="all, delete-orphan", lazy="joined")
    materiaux = relationship("Materiau", back_populates="emplacement", cascade="all, delete-orphan", lazy="joined")
    instruments = relationship("InstrumentControle", back_populates="emplacement", cascade="all, delete-orphan")


    __table_args__ = (
        CheckConstraint("occupation_actuelle <= capacite", name="check_occupation_max"),
    )

    def __repr__(self):
        return f"<EmplacementStock {self.code_emplacement} type={self.type} {self.occupation_actuelle}/{self.capacite}kg>"
