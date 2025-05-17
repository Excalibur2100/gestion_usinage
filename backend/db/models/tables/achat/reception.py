from sqlalchemy import Column, Integer, Float, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.models.base import Base

class Reception(Base):
    __tablename__ = "receptions"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)

    date_reception = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    quantite_recue = Column(Float, nullable=False)
    commentaire = Column(Text, nullable=True)
    statut = Column(Text, default="en attente", nullable=False)

    ligne_commande_id = Column(Integer, ForeignKey("lignes_commande_fournisseur.id", ondelete="CASCADE"), nullable=False)
    commande_id = Column(Integer, ForeignKey("commandes_fournisseur.id", ondelete="CASCADE"), nullable=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="SET NULL"), nullable=True)

    # Relations
    ligne_commande = relationship("LigneCommandeFournisseur", back_populates="receptions")
    commande = relationship("CommandeFournisseur", back_populates="receptions")
    utilisateur = relationship("Utilisateur", back_populates="receptions")  # ← à ajouter dans utilisateur.py

    def __repr__(self):
        return f"<Reception(id={self.id}, qty={self.quantite_recue}, statut='{self.statut}')>"
