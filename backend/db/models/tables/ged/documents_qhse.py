from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.models.base import Base

class DocumentQHSE(Base):
    __tablename__ = "documents_qhse"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)

    entreprise_id = Column(Integer, ForeignKey("entreprises.id", ondelete="CASCADE"), nullable=False)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="SET NULL"), nullable=True)

    titre = Column(String(255), nullable=False)
    categorie = Column(String(100), nullable=False, comment="sécurité, hygiène, environnement, etc.")
    chemin_fichier = Column(Text, nullable=False)
    description = Column(Text, nullable=True)

    date_ajout = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    entreprise = relationship("Entreprise", back_populates="documents_qhse")
    utilisateur = relationship("Utilisateur", back_populates="documents_qhse")

    def __repr__(self):
        return f"<DocumentQHSE(titre='{self.titre}', categorie='{self.categorie}')>"