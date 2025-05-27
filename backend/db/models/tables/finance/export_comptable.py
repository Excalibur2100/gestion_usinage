from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.models.base import Base

class ExportComptable(Base):
    __tablename__ = "exports_comptables"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)

    entreprise_id = Column(Integer, ForeignKey("entreprises.id", ondelete="CASCADE"), nullable=False)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="SET NULL"), nullable=True)

    type_export = Column(String(100), nullable=False, comment="journal, bilan, grand livre...")
    format_export = Column(String(50), nullable=False, default="CSV")
    chemin_fichier = Column(Text, nullable=False)
    commentaire = Column(Text, nullable=True)

    date_export = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    entreprise = relationship("Entreprise", back_populates="exports_comptables")
    utilisateur = relationship("Utilisateur", back_populates="exports_comptables")

    def __repr__(self):
        return f"<ExportComptable(type='{self.type_export}', entreprise={self.entreprise_id})>"