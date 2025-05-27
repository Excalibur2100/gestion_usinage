from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base

class ChiffrageOperation(Base):
    __tablename__ = "chiffrage_operations"

    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    temps_minute = Column(Float, nullable=False)
    outil_utilise = Column(String(100), nullable=True)

    piece_id = Column(Integer, ForeignKey("chiffrage_pieces.id", ondelete="CASCADE"))
    machine_id = Column(Integer, ForeignKey("chiffrage_machines.id", ondelete="SET NULL"))

    piece = relationship("ChiffragePiece", back_populates="operations")
    machine = relationship("ChiffrageMachine", back_populates="operations", lazy="joined")

    def __repr__(self):
        return f"<ChiffrageOperation({self.nom} - {self.temps_minute}min)>"