from sqlalchemy import (
    Column, Integer, String, Float, DateTime, ForeignKey, Boolean, CheckConstraint, UniqueConstraint, func
)
from sqlalchemy.orm import relationship, declarative_base
from uuid import uuid4
from datetime import datetime

Base = declarative_base()

class LigneReception(Base):
    """
    Modèle SQLAlchemy pour une ligne de réception.
    Anticipe toutes les relations, contraintes, et inclut tous les champs ERP universels.
    """
    __tablename__ = "lignes_reception"
    __table_args__ = (
        UniqueConstraint("uuid", name="uq_ligne_reception_uuid"),
        CheckConstraint("quantite_commandee >= 0", name="check_quantite_commandee_positive"),
        CheckConstraint("quantite_recue >= 0", name="check_quantite_recue_positive"),
        CheckConstraint("quantite_recue <= quantite_commandee", name="check_quantite_recue_max"),
    )

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String(64), unique=True, default=lambda: str(uuid4()), nullable=False, index=True, comment="Identifiant universel unique")
    reception_id = Column(Integer, ForeignKey("receptions.id", ondelete="CASCADE"), nullable=False, index=True)
    designation = Column(String(255), nullable=False, comment="Désignation de la pièce ou du produit")
    quantite_commandee = Column(Float, nullable=False, default=0.0, comment="Quantité commandée")
    quantite_recue = Column(Float, nullable=False, default=0.0, comment="Quantité effectivement reçue")
    unite = Column(String(20), nullable=True, comment="Unité de mesure")
    commentaire = Column(String(255), nullable=True, comment="Commentaire libre")
    statut = Column(String(50), default="brouillon", nullable=False, comment="Statut de la ligne")
    etat = Column(String(50), default="non_conforme", nullable=False, comment="Etat métier de la ligne")
    devise = Column(String(10), default="EUR", nullable=False, comment="Devise")
    is_archived = Column(Boolean, default=False, nullable=False, comment="Archive logique")
    cree_par = Column(Integer, ForeignKey("utilisateurs.id"), nullable=True, comment="Utilisateur ayant créé la ligne")
    modifie_par = Column(Integer, ForeignKey("utilisateurs.id"), nullable=True, comment="Dernier utilisateur ayant modifié la ligne")
    version = Column(Integer, default=1, nullable=False, comment="Version de la ligne")
    etat_synchronisation = Column(String(50), default="non_synchro", nullable=False, comment="Etat de synchronisation")
    timestamp_creation = Column(DateTime, server_default=func.now(), nullable=False, comment="Date de création")
    timestamp_modification = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False, comment="Date de modification")

    # Relations ORM
    reception = relationship("Reception", back_populates="lignes_reception", lazy="joined")
    utilisateur_creation = relationship("Utilisateur", foreign_keys=[cree_par], lazy="joined")
    utilisateur_modification = relationship("Utilisateur", foreign_keys=[modifie_par], lazy="joined")

    def __repr__(self):
        return (
            f"<LigneReception(id={self.id}, uuid={self.uuid}, designation='{self.designation}', "
            f"quantite_commandee={self.quantite_commandee}, quantite_recue={self.quantite_recue}, "
            f"statut='{self.statut}', etat='{self.etat}')>"
        )