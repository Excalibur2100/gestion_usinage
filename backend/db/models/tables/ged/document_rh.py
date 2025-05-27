from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.models.base import Base

class DocumentRH(Base):
    __tablename__ = "documents_rh"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)

    employe_id = Column(Integer, ForeignKey("employes.id", ondelete="CASCADE"), nullable=False)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="SET NULL"), nullable=True)
    entreprise_id = Column(Integer, ForeignKey("entreprises.id", ondelete="SET NULL"), nullable=True)

    type_document = Column(String(100), nullable=False, comment="contrat, entretien, certificat…")
    titre = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    chemin_fichier = Column(Text, nullable=False)

    date_creation = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    employe = relationship("Employe", back_populates="documents_rh")
    utilisateur = relationship("Utilisateur", back_populates="documents_rh")
    entreprise = relationship("Entreprise", back_populates="documents_rh")

    def __repr__(self):
        return f"<DocumentRH(employe={self.employe_id}, type='{self.type_document}')>"