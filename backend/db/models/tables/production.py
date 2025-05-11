from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from datetime import datetime
from db.models.base import Base

class Production(Base):
    """
    Table des cycles de production sur pièce par opérateur et machine.
    """
    __tablename__ = "production"
    __table_args__ = (
        CheckConstraint(
            "statut IN ('en cours', 'terminée', 'annulée')",
            name="check_statut_production"
        ),
        {"comment": "Table des productions"},
    )

    id = Column(Integer, primary_key=True)

    piece_id = Column(
        Integer,
        ForeignKey("pieces.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
        comment="Pièce produite"
    )

    machine_id = Column(
        Integer,
        ForeignKey("machines.id", ondelete="SET NULL"),
        nullable=True,
        comment="Machine de production"
    )

    employe_id = Column(
        Integer,
        ForeignKey("employes.id", ondelete="SET NULL"),
        nullable=True,
        comment="Opérateur affecté"
    )

    date_debut = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
        comment="Début de production"
    )

    date_fin = Column(DateTime, nullable=True, comment="Fin de production")
    statut = Column(String(50), nullable=False, default="en cours", comment="Statut : en cours, terminée, annulée")

    # Relations
    piece = relationship("Piece", back_populates="productions", lazy="joined")
    machine = relationship("Machine", back_populates="productions", lazy="joined")
    employe = relationship("Employe", back_populates="productions", lazy="joined")

    def __repr__(self):
        return f"<Production id={self.id} piece={self.piece_id} statut={self.statut}>"

    def is_terminee(self):
        return self.statut == "terminée"

    def is_annulee(self):
        return self.statut == "annulée"

    def duree_production(self):
        if self.date_debut and self.date_fin:
            return (self.date_fin - self.date_debut).total_seconds() / 3600
        return None
