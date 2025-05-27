from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, UniqueConstraint
from sqlalchemy.orm import relationship
from db.models.base import Base

class AutorisationDocument(Base):
    __tablename__ = "autorisations_documents"
    __table_args__ = (
        UniqueConstraint("document_id", "utilisateur_id", name="uq_document_utilisateur"),
        {"extend_existing": True}
    )

    id = Column(Integer, primary_key=True)

    document_id = Column(Integer, ForeignKey("documents_qualite.id", ondelete="CASCADE"), nullable=False)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="CASCADE"), nullable=False)

    peut_lire = Column(Boolean, default=True)
    peut_modifier = Column(Boolean, default=False)
    peut_supprimer = Column(Boolean, default=False)
    peut_signer = Column(Boolean, default=False)

    utilisateur = relationship("Utilisateur", back_populates="autorisations_documents")
    document = relationship("DocumentQualite", back_populates="autorisations")

    def __repr__(self):
        return f"<AutorisationDocument(document={self.document_id}, utilisateur={self.utilisateur_id})>"