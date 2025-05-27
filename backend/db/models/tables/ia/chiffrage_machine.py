from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from db.models.base import Base

class ChiffrageMachine(Base):
    __tablename__ = "chiffrage_machines"

    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False, unique=True)
    type_machine = Column(String(100), nullable=True)
    cout_horaire = Column(Float, nullable=False, comment="Coût €/h machine")

    operations = relationship("ChiffrageOperation", back_populates="machine", cascade="all, delete")

    def __repr__(self):
        return f"<ChiffrageMachine({self.nom} @ {self.cout_horaire}€/h)>"