from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime

# ========================= PIECES =========================
class Piece(Base):
    __tablename__ = "pieces"
    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    date_creation = Column(DateTime, default=datetime.utcnow)
    client_id = Column(Integer, ForeignKey("clients.id"))

    client = relationship("Client", back_populates="pieces")
    programmes = relationship("ProgrammePiece", back_populates="piece")
    non_conformites = relationship("NonConformite", back_populates="piece")

# ========================= MACHINES =========================
class Machine(Base):
    __tablename__ = "machines"
    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    type_machine = Column(String(50), nullable=False)
    vitesse_max = Column(Float, nullable=True)
    puissance = Column(Float, nullable=True)
    nb_axes = Column(Integer, nullable=True)

    postprocesseurs = relationship("PostProcesseur", back_populates="machine")
    maintenances = relationship("Maintenance", back_populates="machine")
    gammes = relationship("GammeProduction", back_populates="machine")

# ========================= GAMME PRODUCTION =========================
class GammeProduction(Base):
    __tablename__ = "gammes_production"
    id = Column(Integer, primary_key=True)
    piece_id = Column(Integer, ForeignKey("pieces.id"))
    machine_id = Column(Integer, ForeignKey("machines.id"))
    operation = Column(String(100), nullable=False)
    temps_estime = Column(Float, nullable=False)

    piece = relationship("Piece", back_populates="gammes")
    machine = relationship("Machine", back_populates="gammes")

# ========================= TRACABILITE =========================
class Tracabilite(Base):
    __tablename__ = "tracabilite"
    id = Column(Integer, primary_key=True)
    piece_id = Column(Integer, ForeignKey("pieces.id"))
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    date_action = Column(DateTime, default=datetime.utcnow)
    action = Column(String(255), nullable=False)

    piece = relationship("Piece", back_populates="tracabilites")
    utilisateur = relationship("Utilisateur", back_populates="tracabilites")