from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.models.base import Base

class SignatureDocument(Base):
    __tablename__ = "signatures_documents"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)

    document_id = Column(Integer, ForeignKey("documents_qualite.id", ondelete="CASCADE"), nullable=False)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="CASCADE"), nullable=False)

    statut = Column(String(50), nullable=False, default="en attente", comment="en attente, signé, refusé")
    commentaire = Column(Text, nullable=True)
    signature_validee = Column(Boolean, default=False)
    date_signature = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    utilisateur = relationship("Utilisateur", back_populates="signatures_documents")
    document = relationship("DocumentQualite", back_populates="signatures")

    def __repr__(self):
        return f"<SignatureDocument(document={self.document_id}, utilisateur={self.utilisateur_id}, statut='{self.statut}')>"