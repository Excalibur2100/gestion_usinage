from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text, CheckConstraint
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime

class Finance(Base):
    __tablename__ = "finance"

    id = Column(Integer, primary_key=True)

    type_transaction = Column(String(50), nullable=False, comment="Type : revenu ou dépense")
    categorie = Column(String(100), nullable=True, comment="Catégorie (salaire, achat, etc.)")
    sous_categorie = Column(String(100), nullable=True, comment="Sous-catégorie plus précise")
    montant = Column(Float, nullable=False, comment="Montant de la transaction")
    devise = Column(String(10), default="EUR", nullable=False, comment="Devise utilisée")
    date_transaction = Column(DateTime, default=datetime.utcnow, nullable=False, comment="Date réelle de la transaction")
    description = Column(Text, nullable=True, comment="Remarques, contexte")
    statut = Column(String(50), default="Validé", nullable=False, comment="Statut : Validé, Rejeté, En attente")
    moyen_paiement = Column(String(50), nullable=True, comment="Carte, virement, etc.")
    reference_facture = Column(String(100), nullable=True, comment="Référence externe ou interne")

    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="SET NULL"), nullable=True)
    fournisseur_id = Column(Integer, ForeignKey("fournisseurs.id", ondelete="SET NULL"), nullable=True)
    materiau_id = Column(Integer, ForeignKey("materiaux.id", ondelete="SET NULL"), nullable=True)
    piece_id = Column(Integer, ForeignKey("pieces.id", ondelete="SET NULL"), nullable=True)
    instrument_id = Column(Integer, ForeignKey("instruments_controle.id", ondelete="SET NULL"), nullable=True)
    outil_id = Column(Integer, ForeignKey("outils.id", ondelete="SET NULL"), nullable=True)
    machine_id = Column(Integer, ForeignKey("machines.id", ondelete="SET NULL"), nullable=True)
    facture_id = Column(Integer, ForeignKey("factures.id", ondelete="SET NULL"), nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow, nullable=False, comment="Date de création")
    updated_at = Column(DateTime, onupdate=datetime.utcnow, comment="Dernière mise à jour")

    # Relations
    utilisateur = relationship("Utilisateur", back_populates="finances", lazy="joined")
    fournisseur = relationship("Fournisseur", back_populates="finances", lazy="joined")
    materiau = relationship("Materiau", back_populates="finance", lazy="joined")
    instrument = relationship("InstrumentControle", back_populates="finances", lazy="joined")
    outil = relationship("Outil", back_populates="finances", lazy="joined")
    piece = relationship("Piece", back_populates="finances", lazy="joined")
    machine = relationship("Machine", back_populates="finances", lazy="joined")
    facture = relationship("Facture", back_populates="finances", lazy="joined")

    __table_args__ = (
        CheckConstraint("montant >= 0", name="check_montant_positif"),
        CheckConstraint("type_transaction IN ('revenu', 'dépense')", name="check_type_transaction"),
        CheckConstraint("statut IN ('Validé', 'Rejeté', 'En attente')", name="check_statut_transaction"),
    )

    def __repr__(self):
        return f"<Finance id={self.id} type={self.type_transaction} montant={self.montant} statut={self.statut}>"
