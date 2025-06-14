from sqlalchemy import (
    Column, Integer, String, Float, DateTime, Enum, Text,
    ForeignKey, CheckConstraint, func
)
from sqlalchemy.orm import relationship
from backend.db.models.base import Base
import enum


class StatutEvaluation(str, enum.Enum):
    excellent = "excellent"
    bon = "bon"
    moyen = "moyen"
    faible = "faible"
    critique = "critique"

class TypeEvaluation(str, enum.Enum):
    ponctuelle = "ponctuelle"
    periodique = "periodique"
    automatique = "automatique"
    audit = "audit"


class EvaluationFournisseur(Base):
    __tablename__ = "evaluations_fournisseur"
    __table_args__ = (
        CheckConstraint("note_globale >= 0", name="check_note_positive"),
        CheckConstraint("note_globale <= 100", name="check_note_maximale"),
    )

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String(64), unique=True, index=True, nullable=True)

    fournisseur_id = Column(Integer, ForeignKey("fournisseurs.id"), nullable=False)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"), nullable=True)
    evalue_par = Column(Integer, ForeignKey("utilisateurs.id"), nullable=True)

    commande_id = Column(Integer, ForeignKey("commandes_fournisseur.id"), nullable=True)
    facture_id = Column(Integer, ForeignKey("factures_fournisseur.id"), nullable=True)
    reception_id = Column(Integer, ForeignKey("receptions.id"), nullable=True)

    document_associe_id = Column(Integer, ForeignKey("documents_qhse.id"), nullable=True)

    date_evaluation = Column(DateTime, default=func.now())
    periode = Column(String(20), nullable=True)  # exemple : "T1-2024"

    note_qualite = Column(Float, nullable=True)
    note_delai = Column(Float, nullable=True)
    note_prix = Column(Float, nullable=True)
    note_globale = Column(Float, nullable=False)

    statut = Column(Enum(StatutEvaluation), nullable=False)
    type_evaluation = Column(Enum(TypeEvaluation), default=TypeEvaluation.ponctuelle)
    origine = Column(String(50), nullable=True)

    commentaire = Column(Text, nullable=True)
    recommandation = Column(Text, nullable=True)
    indice_confiance = Column(Float, nullable=True)

    cree_par = Column(Integer, ForeignKey("utilisateurs.id"), nullable=True)
    modifie_par = Column(Integer, ForeignKey("utilisateurs.id"), nullable=True)
    timestamp_creation = Column(DateTime, server_default=func.now())
    timestamp_modification = Column(DateTime, server_default=func.now(), onupdate=func.now())

    # Relations ORM
    fournisseur = relationship("Fournisseur", back_populates="evaluations_fournisseur", lazy="joined")
    utilisateur = relationship("Utilisateur", back_populates="evaluations_fournisseur", lazy="joined", foreign_keys=[utilisateur_id])
    auteur_evaluation = relationship("Utilisateur", foreign_keys=[evalue_par], lazy="joined")
    auteur_creation = relationship("Utilisateur", foreign_keys=[cree_par], lazy="joined")
    auteur_modification = relationship("Utilisateur", foreign_keys=[modifie_par], lazy="joined")
    document_associe = relationship("DocumentQHSE", back_populates="evaluations_fournisseur", lazy="joined", uselist=False)

    def __repr__(self):
        return f"<EvaluationFournisseur(id={self.id}, fournisseur={self.fournisseur_id}, note={self.note_globale}, statut={self.statut})>"