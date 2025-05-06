from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime


class DocumentRH(Base):
    __tablename__ = "documents_rh"
    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    nom_document = Column(String(150), nullable=False)
    type_document = Column(String(100), nullable=False)  # Ex: "Contrat", "Certificat"
    date_creation = Column(DateTime, default=datetime.utcnow, nullable=False)
    date_expiration = Column(DateTime, nullable=True)
    fichier = Column(String(255), nullable=True)  # Chemin vers le fichier stocké
    commentaire = Column(Text, nullable=True)

    # Relations
    utilisateur = relationship("Utilisateur", back_populates="documents")

