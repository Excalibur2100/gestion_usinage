from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime


# ========================= FINANCE =========================
class Finance(Base):
    __tablename__ = "finance"

    id = Column(Integer, primary_key=True)
    type_transaction = Column(
        String(50), nullable=False, comment="Type de transaction (revenu, dépense)"
    )
    categorie = Column(
        String(100), nullable=True, comment="Catégorie de la transaction"
    )
    sous_categorie = Column(
        String(100), nullable=True, comment="Sous-catégorie de la transaction"
    )
    montant = Column(Float, nullable=False, comment="Montant de la transaction")
    devise = Column(
        String(10), default="EUR", nullable=False, comment="Devise utilisée"
    )
    date_transaction = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
        comment="Date de la transaction",
    )
    description = Column(Text, nullable=True, comment="Description de la transaction")
    statut = Column(
        String(50),
        default="Validé",
        nullable=False,
        comment="Statut de la transaction (validé, rejeté, etc.)",
    )
    moyen_paiement = Column(
        String(50), nullable=True, comment="Moyen de paiement utilisé"
    )
    reference_facture = Column(
        String(100), nullable=True, comment="Référence de la facture associée"
    )

    # Relations clés
    utilisateur_id = Column(
        Integer,
        ForeignKey("utilisateurs.id"),
        nullable=False,
        comment="ID de l'utilisateur associé",
    )
    fournisseur_id = Column(
        Integer,
        ForeignKey("fournisseurs.id"),
        nullable=True,
        comment="ID du fournisseur associé",
    )
    materiau_id = Column(
        Integer,
        ForeignKey("materiaux.id"),
        nullable=True,
        comment="ID du matériau associé",
    )
    piece_id = Column(
        Integer,
        ForeignKey("pieces.id"),
        nullable=True,
        comment="ID de la pièce associée",
    )
    instrument_id = Column(
        Integer,
        ForeignKey("instruments_controle.id"),
        nullable=True,
        comment="ID de l'instrument de contrôle associé",
    )
    outil_id = Column(
        Integer, ForeignKey("outils.id"), nullable=True, comment="ID de l'outil associé"
    )
    machine_id = Column(
        Integer,
        ForeignKey("machines.id"),
        nullable=True,
        comment="ID de la machine associée",
    )
    facture_id = Column(
        Integer,
        ForeignKey("factures.id"),
        nullable=True,
        comment="ID de la facture associée",
    )

    # Timestamps
    created_at = Column(
        DateTime, default=datetime.utcnow, nullable=False, comment="Date de création"
    )
    updated_at = Column(
        DateTime, onupdate=datetime.utcnow, comment="Date de dernière mise à jour"
    )

    # ORM relationships
    utilisateur = relationship("Utilisateur", back_populates="finances")
    fournisseur = relationship("Fournisseur", back_populates="finances")
    materiau = relationship("Materiau", back_populates="finance")
    instrument = relationship("InstrumentControle", back_populates="finances")
    outil = relationship("Outil", back_populates="finances")
    piece = relationship("Piece", back_populates="finances")
    machine = relationship("Machine", back_populates="finances")
    facture = relationship("Facture", back_populates="finances")
