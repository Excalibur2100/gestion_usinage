from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime

# ========================= DEVIS =========================
class Devis(Base):
    __tablename__ = "devis"
    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey("clients.id"))
    montant_total = Column(Float, nullable=False)
    date_creation = Column(DateTime, default=datetime.utcnow)
    date_livraison_souhaitee = Column(DateTime, nullable=True)
    statut = Column(String(50), nullable=False)  # brouillon, validé, annulé

    client = relationship("Client", back_populates="devis")
    commandes = relationship("Commande", back_populates="devis")

# ========================= COMMANDES =========================
class Commande(Base):
    __tablename__ = "commandes"
    id = Column(Integer, primary_key=True)
    devis_id = Column(Integer, ForeignKey("devis.id"))
    date_validation = Column(DateTime, nullable=False)
    statut = Column(String(50), nullable=False)  # en cours, terminée, annulée

    devis = relationship("Devis", back_populates="commandes")
    pieces = relationship("CommandePiece", back_populates="commande")

# ========================= COMMANDE PIECE =========================
class CommandePiece(Base):
    __tablename__ = "commande_pieces"
    id = Column(Integer, primary_key=True)
    commande_id = Column(Integer, ForeignKey("commandes.id"))
    piece_id = Column(Integer, ForeignKey("pieces.id"))
    quantite = Column(Integer, nullable=False)
    prix_unitaire = Column(Float, nullable=False)

    commande = relationship("Commande", back_populates="pieces")
    piece = relationship("Piece", back_populates="commandes")

# ========================= FACTURES =========================
class Facture(Base):
    __tablename__ = "factures"
    id = Column(Integer, primary_key=True)
    commande_id = Column(Integer, ForeignKey("commandes.id"))
    montant_total = Column(Float, nullable=False)
    date_emission = Column(DateTime, nullable=False)
    statut = Column(String(50), nullable=False)  # payée, impayée, annulée

    commande = relationship("Commande", back_populates="factures")

# ========================= LIGNE FACTURE =========================
class LigneFacture(Base):
    __tablename__ = "ligne_factures"
    id = Column(Integer, primary_key=True)
    facture_id = Column(Integer, ForeignKey("factures.id"))
    description = Column(Text, nullable=False)
    quantite = Column(Integer, nullable=False)
    prix_unitaire = Column(Float, nullable=False)

    facture = relationship("Facture", back_populates="lignes")