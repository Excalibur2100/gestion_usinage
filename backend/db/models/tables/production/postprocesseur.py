from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, CheckConstraint
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime

class PostProcesseur(Base):
    __tablename__ = "postprocesseurs"

    id = Column(Integer, primary_key=True)

    nom = Column(String(100), nullable=False, comment="Nom du post-processeur")
    description = Column(Text, nullable=True, comment="Notes ou résumé")
    version = Column(String(50), nullable=True, comment="Version logicielle")
    logiciel_fao = Column(String(100), nullable=False, comment="FAO utilisée (SolidCAM, TopSolid...)")
    extension_sortie = Column(String(20), default=".nc", nullable=False, comment="Extension fichier (.nc, .txt...)")
    configuration = Column(Text, nullable=True, comment="Paramètres JSON ou code postpro")

    machine_id = Column(Integer, ForeignKey("machines.id", ondelete="CASCADE"), nullable=False)
    date_creation = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)

    machine = relationship("Machine", back_populates="postprocesseurs", lazy="joined")
    programmes = relationship("ProgrammePiece", back_populates="postprocesseur", cascade="all, delete-orphan", lazy="joined")

    __table_args__ = (
        CheckConstraint(
            "extension_sortie IN ('.nc', '.txt', '.tap', '.gcode')",
            name="check_extension_sortie"
        ),
    )

    def __repr__(self):
        return f"<PostProcesseur nom={self.nom} logiciel={self.logiciel_fao} machine={self.machine_id}>"
