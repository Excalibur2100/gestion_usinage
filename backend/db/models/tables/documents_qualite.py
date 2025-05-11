from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime

class DocumentQualite(Base):
    __tablename__ = "documents_qualite"

    id = Column(Integer, primary_key=True)

    code_document = Column(String(50), unique=True, nullable=False, comment="Code unique du document (ex: DQ-2024-001)")
    titre = Column(String(255), nullable=False, comment="Titre du document")
    contenu = Column(Text, nullable=False, comment="Texte ou résumé du contenu qualité")
    date_creation = Column(DateTime, default=datetime.utcnow, nullable=False, comment="Date d’émission du document")
    
    auteur_utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="SET NULL"), nullable=True)
    auteur_utilisateur = relationship("Utilisateur", back_populates="documents_qualite", lazy="joined")

    statut = Column(String(50), default="actif", nullable=False, comment="Statut du document : actif, archivé, obsolète")
    auteur = Column(String(100), nullable=True, comment="Nom de l'auteur externe ou autre que utilisateur")

    __table_args__ = (
        CheckConstraint("statut IN ('actif', 'archivé', 'obsolète')", name="check_statut_document_qualite"),
    )

    def __repr__(self):
        return f"<DocumentQualite code={self.code_document} statut={self.statut}>"
