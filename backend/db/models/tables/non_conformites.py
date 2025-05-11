from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime

class NonConformite(Base):
    __tablename__ = "non_conformites"

    id = Column(Integer, primary_key=True)

    origine = Column(String(100), nullable=False, comment="Origine : matière, machine, opérateur, etc.")
    description = Column(Text, nullable=False, comment="Détail de la non-conformité")
    action_corrective = Column(Text, nullable=True, comment="Mesure corrective mise en place")
    date_detection = Column(DateTime, default=datetime.utcnow, nullable=False, comment="Date de détection")
    date_resolution = Column(DateTime, nullable=True, comment="Date de résolution")
    statut = Column(String(50), default="Ouvert", nullable=False, comment="Statut : Ouvert, En cours, Clôturé")
    detecte_par_ia = Column(Boolean, default=False, comment="Détectée automatiquement ?")

    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="SET NULL"), nullable=True)
    machine_id = Column(Integer, ForeignKey("machines.id", ondelete="SET NULL"), nullable=True)
    materiau_id = Column(Integer, ForeignKey("materiaux.id", ondelete="SET NULL"), nullable=True)
    outil_id = Column(Integer, ForeignKey("outils.id", ondelete="SET NULL"), nullable=True)
    instrument_id = Column(Integer, ForeignKey("instruments_controle.id", ondelete="SET NULL"), nullable=True)
    piece_id = Column(Integer, ForeignKey("pieces.id", ondelete="SET NULL"), nullable=True)

    utilisateur = relationship("Utilisateur", back_populates="non_conformites", lazy="joined")
    machine = relationship("Machine", back_populates="non_conformites", lazy="joined")
    materiau = relationship("Materiau", back_populates="non_conformites", lazy="joined")
    outil = relationship("Outil", back_populates="non_conformites", lazy="joined")
    instrument = relationship("InstrumentControle", back_populates="non_conformites", lazy="joined")
    piece = relationship("Piece", back_populates="non_conformites", lazy="joined")

    __table_args__ = (
        CheckConstraint("statut IN ('Ouvert', 'En cours', 'Clôturé')", name="check_statut_non_conformite"),
    )

    def __repr__(self):
        return f"<NonConformite id={self.id} origine={self.origine} statut={self.statut} detecte_par_ia={self.detecte_par_ia}>"
