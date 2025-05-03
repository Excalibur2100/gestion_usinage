from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
    Text,
)
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime


# ========================= PIECES =========================
class Piece(Base):
    __tablename__ = "pieces"

    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False, comment="Nom de la pièce (max 100 caractères)")
    description = Column(Text, nullable=True, comment="Description de la pièce (optionnelle)")
    date_creation = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
        comment="Date de création de la pièce",
    )
    client_id = Column(
        Integer, ForeignKey("clients.id"), nullable=True, index=True, comment="ID du client associé"
    )

    # Relations
    client = relationship("Client", back_populates="pieces")
    programmes = relationship(
        "ProgrammePiece", back_populates="piece", cascade="all, delete-orphan"
    )
    non_conformites = relationship(
        "NonConformite", back_populates="piece", cascade="all, delete-orphan"
    )
    gammes = relationship(
        "GammeProduction", back_populates="piece", cascade="all, delete-orphan"
    )
    commandes = relationship(
        "CommandePiece", back_populates="piece", cascade="all, delete-orphan"
    )
    productions = relationship("Production", back_populates="piece")

    # Méthodes utilitaires
    def __repr__(self):
        return f"<Piece(id={self.id}, nom='{self.nom}', client_id={self.client_id})>"

    def get_programmes(self):
        return [programme.nom for programme in self.programmes]
    