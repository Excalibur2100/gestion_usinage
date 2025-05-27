from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.models.base import Base

class DocumentQualite(Base):
    __tablename__ = "documents_qualite"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)

    entreprise_id = Column(Integer, ForeignKey("entreprises.id", ondelete="CASCADE"), nullable=False)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="SET NULL"), nullable=True)

    titre = Column(String(255), nullable=False)
    type_document = Column(String(100), nullable=False, comment="ex: procédure, audit, contrôle, suivi")
    description = Column(Text, nullable=True)
    chemin_fichier = Column(Text, nullable=False)

    date_creation = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    entreprise = relationship("Entreprise", back_populates="documents_qualite")
    utilisateur = relationship("Utilisateur", back_populates="documents_qualite")
    autorisations = relationship("AutorisationDocument", back_populates="document", cascade="all, delete-orphan")
    signatures = relationship("SignatureDocument", back_populates="document", cascade="all, delete-orphan")
    versions = relationship("VersionDocument", back_populates="document", cascade="all, delete-orphan")
    workflow_associe = relationship("WorkflowDocument", back_populates="document", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<DocumentQualite(titre='{self.titre}', type='{self.type_document}')>"