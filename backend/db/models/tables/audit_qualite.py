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
    date_ajout = Column(DateTime, default=datetime.utcnow, nullable=False, comment="Date d'ajout de l'audit")
    date_modif = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=True, comment="Date de dernière modification")
    date_realisation = Column(DateTime, nullable=True, comment="Date de réalisation de l'audit")
    date_planification = Column(DateTime, nullable=True, comment="Date de planification de l'audit")
    date_annulation = Column(DateTime, nullable=True, comment="Date d'annulation de l'audit")
    date_validation = Column(DateTime, nullable=True, comment="Date de validation de l'audit")
    date_fermeture = Column(DateTime, nullable=True, comment="Date de fermeture de l'audit")
    date_modification = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=True, comment="Date de dernière modification")
   



    date_audit = Column(DateTime, default=datetime.utcnow, nullable=False, comment="Date de réalisation ou planification")
    type_audit = Column(String(100), nullable=False, comment="Type d'audit : Interne, Externe, Client, etc.")
    resultat = Column(String(50), nullable=False, comment="Résultat : Conforme, Non conforme, À revoir")
    statut = Column(String(50), default="planifié", nullable=False, comment="Statut de l'audit : planifié, terminé, annulé")
    commentaire = Column(Text, nullable=True, comment="Remarques ou conclusions de l'audit")


    document_reglementaire_id = Column(Integer, ForeignKey("documents_reglementaires.id", ondelete="SET NULL"), nullable=True)
    document_reglementaire = relationship("DocumentReglementaire", back_populates="audits", lazy="joined")


    responsable_utilisateur = relationship("Utilisateur", back_populates="audits_realises", lazy="joined")
    document_qhse = relationship("DocumentQHSE", back_populates="audits", lazy="joined")
    programme = relationship("ProgrammePiece", back_populates="audits", lazy="joined")
    document_reglementaire = relationship("DocumentReglementaire", back_populates="audits", lazy="joined")
    piece = relationship("Piece", back_populates="audits", lazy="joined")
    machine = relationship("Machine", back_populates="audits", lazy="joined")
    analyse_fichier = relationship("AnalyseFichier", back_populates="audits", lazy="joined")
    analyse_fichier_id = Column(Integer, ForeignKey("analyses_fichiers.id", ondelete="SET NULL"), nullable=True)
    analyse_fichier = relationship("AnalyseFichier", back_populates="audits", lazy="joined")
    piece_id = Column(Integer, ForeignKey("pieces.id", ondelete="SET NULL"), nullable=True)
    machine_id = Column(Integer, ForeignKey("machines.id", ondelete="SET NULL"), nullable=True)

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
    def __init__(self, responsable_utilisateur_id, document_qhse_id, type_audit, resultat, statut, commentaire):
        self.responsable_utilisateur_id = responsable_utilisateur_id
        self.document_qhse_id = document_qhse_id
        self.type_audit = type_audit
        self.resultat = resultat
        self.statut = statut
        self.commentaire = commentaire
        self.date_ajout = datetime.utcnow()
        self.date_modification = datetime.utcnow()
        self.date_audit = datetime.utcnow()
        self.date_planification = datetime.utcnow()
        self.date_realisation = datetime.utcnow()
        self.date_fermeture = datetime.utcnow()
        self.date_validation = datetime.utcnow()
        self.date_annulation = datetime.utcnow()

    def __repr__(self):
        return f"<AuditQualite id={self.id} type={self.type_audit} resultat={self.resultat}>"
    


