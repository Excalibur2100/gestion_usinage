from sqlalchemy import Column, Integer, Float, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.models.base import Base

class EvaluationFournisseur(Base):
    __tablename__ = "evaluations_fournisseur"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)

    date_evaluation = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    qualite = Column(Float, nullable=False)
    delai = Column(Float, nullable=False)
    communication = Column(Float, nullable=False)
    conformite = Column(Float, nullable=False)

    commentaire = Column(Text, nullable=True)

    commande_id = Column(Integer, ForeignKey("commandes_fournisseur.id", ondelete="SET NULL"), nullable=True)
    fournisseur_id = Column(Integer, ForeignKey("fournisseurs.id", ondelete="CASCADE"), nullable=False)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="SET NULL"), nullable=True)

    # Relations
    commande = relationship("CommandeFournisseur", back_populates="evaluations")  # ← à ajouter dans commande_fournisseur.py
    fournisseur = relationship("Fournisseur", back_populates="evaluations")
    utilisateur = relationship("Utilisateur", back_populates="evaluations_fournisseur")  # ← à ajouter dans utilisateur.py

    def __repr__(self):
        return f"<EvaluationFournisseur(fournisseur={self.fournisseur_id}, note={self.qualite})>"
