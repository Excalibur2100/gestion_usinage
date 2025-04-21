from sqlalchemy import Column, Integer, String, Text, DateTime
from db.models.base import Base
from datetime import datetime


# ========================= DOCUMENT QUALITE =========================
class DocumentQualite(Base):
    __tablename__ = "documents_qualite"

    id = Column(Integer, primary_key=True)
    titre = Column(String(255), nullable=False, comment="Titre du document")
    contenu = Column(Text, nullable=False, comment="Contenu du document")
    date_creation = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
        comment="Date de création du document",
    )
    auteur = Column(String(100), nullable=True, comment="Auteur du document")
