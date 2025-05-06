from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime


# ========================= DOCUMENTS QHSE =========================
class DocumentsQHSE(Base):
    __tablename__ = "documents_qhse"

    id = Column(Integer, primary_key=True)
    nom = Column(String(150), nullable=False, comment="Nom du document QHSE")
    type_document = Column(
        String(100),
        nullable=False,
        comment="Type de document (ex: procédure, rapport, norme)",
    )
    chemin_fichier = Column(
        String(255), nullable=False, comment="Chemin du fichier sur le disque"
    )
    date_creation = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
        comment="Date de création du document",
    )
    description = Column(
        Text, nullable=True, comment="Description ou remarques sur le document"
    )
    actif = Column(
        String(50),
        default="actif",
        nullable=False,
        comment="Statut du document (actif, archivé)",
    )

    # Relations
    audits = relationship(
        "AuditQualite", back_populates="document_qhse", cascade="all, delete-orphan"
    )
