from sqlalchemy import (
    Column, Integer, String, DateTime, ForeignKey, Text, Float, Enum, func
)
from sqlalchemy.orm import relationship
from backend.db.models.base import Base
import enum


class StatutReception(str, enum.Enum):
    en_attente = "en_attente"
    partiellement_recue = "partiellement_recue"
    recue = "recue"
    refusee = "refusee"
    archivee = "archivee"


class Reception(Base):
    __tablename__ = "receptions"

    id = Column(Integer, primary_key=True, index=True)
    uuid = Column(String(64), unique=True, index=True, nullable=True)

    numero_reception = Column(String(100), unique=True, nullable=False)
    commande_id = Column(Integer, ForeignKey("commandes_fournisseur.id"), nullable=False)
    date_reception = Column(DateTime, nullable=False, server_default=func.now())

    statut = Column(Enum(StatutReception), default=StatutReception.en_attente)

    commentaire = Column(Text, nullable=True)
    document_associe = Column(String(255), nullable=True)

    cree_par = Column(Integer, ForeignKey("utilisateurs.id"), nullable=True)
    modifie_par = Column(Integer, ForeignKey("utilisateurs.id"), nullable=True)
    timestamp_creation = Column(DateTime, server_default=func.now())
    timestamp_modification = Column(DateTime, server_default=func.now(), onupdate=func.now())

    # Relations ORM
    auteur_creation = relationship("Utilisateur", foreign_keys=[cree_par], lazy="joined")
    auteur_modification = relationship("Utilisateur", foreign_keys=[modifie_par], lazy="joined")

    commande = relationship("CommandeFournisseur", back_populates="receptions", lazy="joined")

    lignes_reception = relationship(
        "LigneReception",
        back_populates="reception",
        cascade="all, delete-orphan",
        lazy="select"
    )

    def __repr__(self):
        return (
            f"<Reception(id={self.id}, numero='{self.numero_reception}', "
            f"statut={self.statut}, date={self.date_reception})>"
        )