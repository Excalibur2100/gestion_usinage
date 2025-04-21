from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base


# ========================= INSTRUMENT CONTROLE =========================
class InstrumentControle(Base):
    __tablename__ = "instruments_controle"

    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False, comment="Nom de l'instrument")
    type_instrument = Column(
        String(50),
        nullable=False,
        comment="Type d'instrument (pied à coulisse, micromètre, etc.)",
    )
    numero_serie = Column(
        String(100),
        unique=True,
        nullable=False,
        comment="Numéro de série de l'instrument",
    )
    date_calibration = Column(DateTime, nullable=False, comment="Date de calibration")
    date_prochaine_calibration = Column(
        DateTime, nullable=False, comment="Date de la prochaine calibration"
    )
    statut = Column(
        String(50),
        nullable=False,
        comment="Statut de l'instrument (conforme, non conforme)",
    )
    emplacement_id = Column(
        Integer,
        ForeignKey("emplacements.id"),
        nullable=True,
        comment="ID de l'emplacement associé",
    )

    # Relations
    emplacement = relationship("EmplacementStock", back_populates="instruments")
    controles = relationship("ControlePiece", back_populates="instrument")
    non_conformites = relationship("NonConformite", back_populates="instrument")