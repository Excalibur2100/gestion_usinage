from sqlalchemy import Column, Integer, String, DateTime, Text, CheckConstraint
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime

class DocumentReglementaire(Base):
    __tablename__ = "documents_reglementaires"

    id = Column(Integer, primary_key=True)

    code_document = Column(String(50), unique=True, nullable=False, comment="Code document (ex: DR-2024-001)")
    nom = Column(String(150), nullable=False, comment="Nom du document réglementaire")
    type_document = Column(String(100), nullable=False, comment="Type : norme, certificat, procédure, etc.")
    chemin_fichier = Column(String(255), nullable=False, comment="Chemin local ou distant du fichier")
    date_creation = Column(DateTime, default=datetime.utcnow, nullable=False, comment="Date d’ajout")
    description = Column(Text, nullable=True, comment="Remarques et contexte")
    actif = Column(String(50), default="actif", nullable=False, comment="Statut : actif, archivé")

    # Relations
    audits = relationship("AuditQualite", back_populates="document_reglementaire", cascade="all, delete-orphan", lazy="joined")

    __table_args__ = (
        CheckConstraint("actif IN ('actif', 'archivé')", name="check_statut_document_reglementaire"),
    )

    def __repr__(self):
        return f"<DocumentReglementaire code={self.code_document} actif={self.actif}>"
