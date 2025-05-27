from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.models.base import Base

class FichierClient(Base):
    __tablename__ = "fichiers_client"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)

    client_id = Column(Integer, ForeignKey("clients.id", ondelete="CASCADE"), nullable=False)
    nom_fichier = Column(String(255), nullable=False)
    chemin = Column(String(500), nullable=False, comment="Chemin ou URI de stockage")
    type_fichier = Column(String(100), nullable=True)
    commentaire = Column(Text, nullable=True)
    date_ajout = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    client = relationship("Client", back_populates="fichiers")

    def __repr__(self):
        return f"<FichierClient(nom='{self.nom_fichier}', client={self.client_id})>"