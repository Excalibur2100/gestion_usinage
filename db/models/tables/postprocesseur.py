from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime

# ========================= POST PROCESSEUR =========================
class PostProcesseur(Base):
    __tablename__ = "postprocesseurs"
    id = Column(Integer, primary_key=True)
    nom = Column(String(150), nullable=False)  # Nom lisible (ex: "FANUC - Tour CN XYZ")
    logiciel_fao = Column(String(100), nullable=False)  # SolidCAM, TopSolid, etc.
    extension_sortie = Column(String(20), default=".nc")  # ex: .nc, .txt
    configuration = Column(Text)  # JSON / texte de configuration brute
    machine_id = Column(Integer, ForeignKey("machines.id"))
    date_creation = Column(DateTime, default=datetime.utcnow)

    machine = relationship("Machine", back_populates="postprocesseurs")
    programmes = relationship("ProgrammePiece", back_populates="postprocesseur")