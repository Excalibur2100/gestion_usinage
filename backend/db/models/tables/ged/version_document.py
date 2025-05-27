from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.models.base import Base

class VersionDocument(Base):
    __tablename__ = "versions_documents"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)

    document_id = Column(Integer, ForeignKey("documents_qualite.id", ondelete="CASCADE"), nullable=False)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="SET NULL"), nullable=True)

    numero_version = Column(String(50), nullable=False)
    commentaire = Column(Text, nullable=True)
    chemin_fichier = Column(Text, nullable=False)
    date_version = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    document = relationship("DocumentQualite", back_populates="versions")
    utilisateur = relationship("Utilisateur", back_populates="versions_documents")

    def __repr__(self):
        return f"<VersionDocument(document={self.document_id}, version='{self.numero_version}')>"