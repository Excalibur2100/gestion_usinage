from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime


class NonConformite(Base):
    __tablename__ = "non_conformites"
    id = Column(Integer, primary_key=True)
    origine = Column(String(100), nullable=False)  # matière, machine, opérateur, etc.
    description = Column(Text, nullable=False)
    action_corrective = Column(Text)
    date_detection = Column(DateTime, default=datetime.utcnow, nullable=False)
    date_resolution = Column(DateTime)
    statut = Column(String(50), default="Ouvert", nullable=False)
    detecte_par_ia = Column(Boolean, default=False)

    # Relations clés
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"), nullable=False)
    machine_id = Column(Integer, ForeignKey("machines.id"), nullable=True)
    materiau_id = Column(Integer, ForeignKey("materiaux.id"), nullable=True)
    outil_id = Column(Integer, ForeignKey("outils.id"), nullable=True)
    instrument_id = Column(
        Integer, ForeignKey("instruments_controle.id"), nullable=True
    )

    # ORM relationships
    utilisateur = relationship("Utilisateur", back_populates="non_conformites")
    machine = relationship("Machine", back_populates="non_conformites")
    materiau = relationship("Materiau", back_populates="non_conformites")
    outil = relationship("Outil", back_populates="non_conformites")
    instrument = relationship("InstrumentControle", back_populates="non_conformites")
