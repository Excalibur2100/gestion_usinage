from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base

class ChiffragePiece(Base):
    __tablename__ = "chiffrage_pieces"

    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    matière = Column(String(50), nullable=False)
    poids_kg = Column(Float, nullable=True)
    volume_cm3 = Column(Float, nullable=True)
    quantite = Column(Integer, default=1)
    client_id = Column(Integer, ForeignKey("clients.id", ondelete="SET NULL"))

    client = relationship("Client", back_populates="pieces_chiffrages", lazy="joined")
    operations = relationship("ChiffrageOperation", back_populates="piece", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<ChiffragePiece(nom='{self.nom}', matière='{self.matière}')>"