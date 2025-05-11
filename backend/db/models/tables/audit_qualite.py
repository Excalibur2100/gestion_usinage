from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime

class AuditQualite(Base):
    __tablename__ = "audits_qualite"

    id = Column(Integer, primary_key=True)

    responsable_utilisateur_id = Column(
        Integer,
        ForeignKey("utilisateurs.id", ondelete="SET NULL"),
        nullable=True,
        comment="Responsable de l'audit"
    )

    document_qhse_id = Column(
        Integer,
        ForeignKey("documents_qhse.id", ondelete="SET NULL"),
        nullable=True,
        comment="Document QHSE de référence"
    )

    date_audit = Column(DateTime, default=datetime.utcnow, nullable=False, comment="Date de réalisation ou planification")
    type_audit = Column(String(100), nullable=False, comment="Type d'audit : Interne, Externe, Client, etc.")
    resultat = Column(String(50), nullable=False, comment="Résultat : Conforme, Non conforme, À revoir")
    statut = Column(String(50), default="planifié", nullable=False, comment="Statut de l'audit : planifié, terminé, annulé")
    commentaire = Column(Text, nullable=True, comment="Remarques ou conclusions de l'audit")

    document_reglementaire_id = Column(Integer, ForeignKey("documents_reglementaires.id", ondelete="SET NULL"), nullable=True)
    document_reglementaire = relationship("DocumentReglementaire", back_populates="audits", lazy="joined")

    responsable_utilisateur = relationship("Utilisateur", back_populates="audits_realises", lazy="joined")
    document_qhse = relationship("DocumentQHSE", back_populates="audits", lazy="joined")

    __table_args__ = (
        CheckConstraint(
            "statut IN ('planifié', 'terminé', 'annulé')",
            name="check_statut_audit"
        ),
        CheckConstraint(
            "resultat IN ('Conforme', 'Non conforme', 'À revoir')",
            name="check_resultat_audit"
        ),
    )

    def __repr__(self):
        return f"<AuditQualite id={self.id} type={self.type_audit} resultat={self.resultat}>"


