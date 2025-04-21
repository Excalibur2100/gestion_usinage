from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
    DateTime,
    CheckConstraint,
)
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime


# ========================= POST PROCESSEUR =========================
class PostProcesseur(Base):
    __tablename__ = "postprocesseurs"

    id = Column(Integer, primary_key=True)
    nom = Column(
        String(100),
        nullable=False,
        comment="Nom du postprocesseur",
    )
    description = Column(
        Text,
        nullable=True,
        comment="Description du postprocesseur",
    )
    version = Column(
        String(50),
        nullable=True,
        comment="Version du postprocesseur",
    )
    logiciel_fao = Column(
        String(100),
        nullable=False,
        comment="Logiciel FAO associé (ex: SolidCAM, TopSolid)",
    )
    extension_sortie = Column(
        String(20),
        default=".nc",
        nullable=False,
        comment="Extension de fichier générée (ex: .nc, .txt)",
    )
    configuration = Column(
        Text,
        nullable=True,
        comment="Configuration brute du post-processeur (JSON ou texte)",
    )
    machine_id = Column(
        Integer,
        ForeignKey("machines.id", ondelete="CASCADE"),
        nullable=False,
        comment="ID de la machine associée",
    )
    date_creation = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
        comment="Date de création du post-processeur",
    )
    updated_at = Column(
        DateTime,
        onupdate=datetime.utcnow,
        comment="Date de dernière mise à jour du post-processeur",
    )

    # Relations
    machine = relationship("Machine", back_populates="postprocesseurs")
    programmes = relationship(
        "ProgrammePiece", back_populates="postprocesseur", cascade="all, delete-orphan"
    )

    __table_args__ = (
        CheckConstraint(
            "extension_sortie IN ('.nc', '.txt', '.tap', '.gcode')",
            name="check_extension_sortie",
        ),
    )
