from sqlalchemy import Column, Integer, Float, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base

class ConditionsCoupe(Base):
    __tablename__ = "conditions_coupe"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)

    piece_id = Column(Integer, ForeignKey("pieces.id", ondelete="SET NULL"), nullable=True)
    outil_id = Column(Integer, ForeignKey("outils.id", ondelete="SET NULL"), nullable=True)
    materiau_id = Column(Integer, ForeignKey("materiaux.id", ondelete="SET NULL"), nullable=True)

    operation = Column(String(100), nullable=False, comment="perçage, fraisage, tournage...")
    vitesse_coupe = Column(Float, nullable=False, comment="Vc en m/min")
    avance = Column(Float, nullable=False, comment="Fz en mm/dent")
    profondeur_passage = Column(Float, nullable=False, comment="ap en mm")
    commentaire = Column(Text, nullable=True)

    piece = relationship("Piece", back_populates="conditions_coupe")
    outil = relationship("Outil", back_populates="conditions_coupe")
    materiau = relationship("Materiau", back_populates="conditions_coupe")

    def __repr__(self):
        return f"<ConditionsCoupe(operation='{self.operation}', Vc={self.vitesse_coupe}, Fz={self.avance})>"