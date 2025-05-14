from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime

class DocumentRH(Base):
    __tablename__ = "documents_rh"

    id = Column(Integer, primary_key=True)

    utilisateur_id = Column(
        Integer,
        ForeignKey("utilisateurs.id", ondelete="CASCADE"),
        nullable=False,
        comment="Utilisateur concerné par ce document RH"
    )

    nom_document = Column(String(150), nullable=False, comment="Nom du document (ex : Contrat CDI)")
    type_document = Column(String(100), nullable=False, comment="Type : Contrat, Certificat, Attestation...")
    date_creation = Column(DateTime, default=datetime.utcnow, nullable=False, comment="Date d'ajout du document")
    date_expiration = Column(DateTime, nullable=True, comment="Date d'expiration si applicable")
    fichier = Column(String(255), nullable=True, comment="Chemin vers le fichier stocké ou URL")
    commentaire = Column(Text, nullable=True, comment="Observations, contexte RH")

    utilisateur = relationship("Utilisateur", back_populates="documents", lazy="joined")

    def __repr__(self):
        return f"<DocumentRH {self.nom_document} utilisateur={self.utilisateur_id}>"
