from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from db.models.base import Base

class InstrumentControle(Base):
    __tablename__ = "instruments_controle"

    id = Column(Integer, primary_key=True)

    nom = Column(String(100), nullable=False, comment="Nom de l'instrument")
    type_instrument = Column(String(50), nullable=False, comment="Ex : pied à coulisse, micromètre")
    numero_serie = Column(String(100), unique=True, nullable=False, comment="Numéro de série unique")
    date_calibration = Column(DateTime, nullable=False, comment="Dernière date de calibration")
    date_prochaine_calibration = Column(DateTime, nullable=False, comment="Prochaine calibration prévue")
    statut = Column(String(50), nullable=False, default="conforme", comment="Statut : conforme ou non conforme")

    emplacement_id = Column(Integer, ForeignKey("emplacements.id", ondelete="SET NULL"), nullable=True)

    emplacement = relationship("EmplacementStock", back_populates="instruments", lazy="joined")
    controles = relationship("ControlePiece", back_populates="instrument", cascade="all, delete-orphan", lazy="joined")
    non_conformites = relationship("NonConformite", back_populates="machine/materiau/outil/instrument", cascade="all, delete-orphan")


    __table_args__ = (
        CheckConstraint("statut IN ('conforme', 'non conforme')", name="check_statut_instrument"),
    )

    def __repr__(self):
        return f"<InstrumentControle nom={self.nom} statut={self.statut} calibration={self.date_calibration}>"
