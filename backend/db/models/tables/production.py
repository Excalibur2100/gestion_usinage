from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    ForeignKey,
    CheckConstraint,
)
from sqlalchemy.orm import relationship
from datetime import datetime
from db.models.base import Base


# ========================= PRODUCTION =========================
class Production(Base):
    """
    Classe Production représentant une production dans le système.

    Attributs :
        - piece_id : ID de la pièce produite.
        - machine_id : ID de la machine utilisée pour la production.
        - employe_id : ID de l'employé responsable de la production.
        - date_debut : Date de début de la production.
        - date_fin : Date de fin de la production (optionnelle).
        - statut : Statut de la production (en cours, terminée, annulée).
        - description : Description de la production (optionnelle).
    """
    __tablename__ = "production"
    __table_args__ = (
        CheckConstraint(
            "statut IN ('en cours', 'terminée', 'annulée')",
            name="check_statut_production",
        ),
        {
            "comment": "Table des productions",
            "extend_existing": True,
        },
    )

    id = Column(Integer, primary_key=True)
    piece_id = Column(
        Integer,
        ForeignKey("pieces.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
        comment="ID de la pièce produite",
    )
    machine_id = Column(
        Integer,
        ForeignKey("machines.id", ondelete="SET NULL"),
        nullable=True,
        comment="ID de la machine utilisée pour la production",
    )
    id = Column(Integer, primary_key=True)
    employe_id = Column(
        Integer,
        ForeignKey("employes.id", ondelete="SET NULL"),  # Assure-toi que le nom de la table est correct
        nullable=True,
        comment="ID de l'employé responsable de la production",
    )
    date_debut = Column(
        DateTime,
        nullable=False,
        default=datetime.now,  # Définit la date actuelle par défaut
        comment="Date de début de la production",
    )
    date_fin = Column(DateTime, nullable=True, comment="Date de fin de la production")
    statut = Column(
        String(50),
        nullable=False,
        comment="Statut de la production (en cours, terminée, annulée)",
    )

    # Relations
    piece = relationship("Piece", back_populates="productions")
    machine = relationship("Machine", back_populates="productions")
    employe = relationship("Employe", back_populates="productions")

    # Méthodes utilitaires
    def __repr__(self):
        return f"<Production(id={self.id}, piece_id={self.piece_id}, statut='{self.statut}')>"

    def is_terminee(self):
        """Vérifie si la production est terminée."""
        return self.statut == "terminée"

    def is_annulee(self):
        """Vérifie si la production est annulée."""
        return self.statut == "annulée"

    def duree_production(self):
        """Calcule la durée de la production en heures."""
        if self.date_fin and self.date_debut:
            return (self.date_fin - self.date_debut).total_seconds() / 3600
        return None