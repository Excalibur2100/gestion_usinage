from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Boolean
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime

# ========================= AUDIT QUALITE =========================
class AuditQualite(Base):
    __tablename__ = "audit_qualite"
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, default=datetime.utcnow, nullable=False)
    type_audit = Column(String(50), nullable=False)  # interne, externe, etc.
    responsable = Column(String(100), nullable=False)
    statut = Column(String(50), nullable=False)  # planifié, en cours, terminé
    remarques = Column(Text, nullable=True)

# ========================= NON CONFORMITE =========================
class NonConformite(Base):
    __tablename__ = "non_conformites"
    id = Column(Integer, primary_key=True)
    description = Column(Text, nullable=False)
    date_detection = Column(DateTime, default=datetime.utcnow, nullable=False)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    piece_id = Column(Integer, ForeignKey("pieces.id"))
    statut = Column(String(50), nullable=False)  # ouverte, en cours, résolue
    actions_correctives = Column(Text, nullable=True)

    utilisateur = relationship("Utilisateur", back_populates="non_conformites")
    piece = relationship("Piece", back_populates="non_conformites")

# ========================= DOCUMENT QUALITE =========================
class DocumentQualite(Base):
    __tablename__ = "documents_qualite"
    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    chemin_fichier = Column(String(255), nullable=False)
    date_creation = Column(DateTime, default=datetime.utcnow)
    type_document = Column(String(50), nullable=False)  # procédure, certificat, etc.

# ========================= INSTRUMENT CONTROLE =========================
class InstrumentControle(Base):
    __tablename__ = "instruments_controle"
    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    type_instrument = Column(String(50), nullable=False)  # pied à coulisse, micromètre, etc.
    date_calibration = Column(DateTime, nullable=False)
    date_prochaine_calibration = Column(DateTime, nullable=False)
    statut = Column(String(50), nullable=False)  # conforme, non conforme
    emplacement_id = Column(Integer, ForeignKey("emplacements.id"))

    emplacement = relationship("EmplacementStock", back_populates="instruments")