from sqlalchemy import Column, Integer, String, ForeignKey,Float
from sqlalchemy.orm import relationship
from db.models.base import Base


# ========================= GAMME PRODUCTION =========================
class GammeProduction(Base):
    __tablename__ = "gammes_production"

    id = Column(Integer, primary_key=True)
    piece_id = Column(
        Integer,
        ForeignKey("pieces.id"),
        nullable=False,
        comment="ID de la pièce associée",
    )
    machine_id = Column(
        Integer,
        ForeignKey("machines.id"),
        nullable=True,
        comment="ID de la machine associée",
    )
    operation = Column(String(100), nullable=False, comment="Nom de l'opération")
    temps_estime = Column(
        Float, nullable=False, comment="Temps estimé pour l'opération (en heures)"
    )

    # Relations
    piece = relationship("Piece", back_populates="gammes")
    machine = relationship("Machine", back_populates="gammes")
