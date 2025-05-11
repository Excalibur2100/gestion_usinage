from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime

class Piece(Base):
    __tablename__ = "pieces"

    id = Column(Integer, primary_key=True)

    nom = Column(String(100), nullable=False, comment="Nom de la pièce")
    description = Column(Text, nullable=True, comment="Détail ou notes sur la pièce")
    date_creation = Column(DateTime, default=datetime.utcnow, nullable=False, comment="Date d'enregistrement")

    client_id = Column(Integer, ForeignKey("clients.id", ondelete="SET NULL"), nullable=True, index=True, comment="Client concerné")

    # Relations
    client = relationship("Client", back_populates="pieces", lazy="joined")

    programmes = relationship("ProgrammePiece", back_populates="piece", cascade="all, delete-orphan", lazy="joined")

    non_conformites = relationship("NonConformite", back_populates="piece", cascade="all, delete-orphan", lazy="joined")
    gammes = relationship("GammeProduction", back_populates="piece", cascade="all, delete-orphan", lazy="joined")
    commandes = relationship("CommandePiece", back_populates="piece", cascade="all, delete-orphan", lazy="joined")
    productions = relationship("Production", back_populates="piece", cascade="all, delete-orphan")
    tracabilites = relationship("Tracabilite", back_populates="piece", cascade="all, delete-orphan")




    def __repr__(self):
        return f"<Piece id={self.id} nom='{self.nom}' client_id={self.client_id}>"

    def get_programmes(self):
        return [programme.nom for programme in self.programmes]
