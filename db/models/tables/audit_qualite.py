from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime


class AuditQualite(Base):
    __tablename__ = "audits_qualite"
    id = Column(Integer, primary_key=True)
    responsable_utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    date_audit = Column(DateTime, default=datetime.utcnow, nullable=False)
    type_audit = Column(String(100), nullable=False)  # Ex: "Interne", "Externe"
    resultat = Column(String(50), nullable=False)  # Ex: "Conforme", "Non conforme"
    commentaire = Column(Text, nullable=True)

    # Relations
    responsable_utilisateur = relationship(
        "Utilisateur", back_populates="audits_realises"
    )
