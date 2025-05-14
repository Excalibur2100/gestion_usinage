from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from db.models.base import Base

class ChargeMachine(Base):
    __tablename__ = "charges_machine"

    id = Column(Integer, primary_key=True)

    machine_id = Column(
        Integer,
        ForeignKey("machines.id", ondelete="CASCADE"),
        nullable=False,
        comment="Machine affectée à cette charge"
    )
    gamme_id = Column(
        Integer,
        ForeignKey("gammes_production.id", ondelete="SET NULL"),
        nullable=True,
        comment="Gamme de production liée à la charge"
    )

    date_debut = Column(DateTime, nullable=False, comment="Début de la plage de charge")
    date_fin = Column(DateTime, nullable=False, comment="Fin de la plage de charge")

    statut = Column(
        String(50),
        default="planifié",
        nullable=False,
        comment="Statut de la charge (planifié, en cours, terminé)"
    )
    type_charge = Column(
        String(50),
        nullable=False,
        comment="Type de charge (production, maintenance, etc.)"
    )
    piece_id = Column(
        Integer,
        ForeignKey("pieces.id", ondelete="SET NULL"),
        nullable=True,
        comment="ID de la pièce associée à la charge"
    )
    piece = relationship("Piece", back_populates="charges", lazy="joined")
    date_ajout = Column(DateTime, nullable=False, comment="Date d'ajout de la charge")
    date_modif = Column(DateTime, nullable=True, comment="Date de dernière modification")
    date_realisation = Column(DateTime, nullable=True, comment="Date de réalisation de la charge")
    date_annulation = Column(DateTime, nullable=True, comment="Date d'annulation de la charge")
    date_validation = Column(DateTime, nullable=True, comment="Date de validation de la charge")
    date_fermeture = Column(DateTime, nullable=True, comment="Date de fermeture de la charge")

    temperature = Column(Float, nullable=True, comment="Température mesurée pendant la charge")
    vibration = Column(Float, nullable=True, comment="Vibration mesurée pendant la charge")
    commentaire = Column(Text, nullable=True, comment="Remarque opérateur ou responsable")
    utilisateur_id = Column(
        Integer,
        ForeignKey("utilisateurs.id", ondelete="SET NULL"),
        nullable=True,
        comment="Utilisateur responsable de la charge"
    )
    utilisateur = relationship("Utilisateur", back_populates="charges", lazy="joined")

    machine = relationship("Machine", back_populates="charges", lazy="joined")
    gamme = relationship("GammeProduction", back_populates="charges", lazy="joined")
    piece = relationship("Piece", back_populates="charges", lazy="joined")


    def __repr__(self):
        return f"<ChargeMachine machine={self.machine_id} {self.date_debut} → {self.date_fin}>"
    def __init__(self, machine_id, date_debut, date_fin):
        self.machine_id = machine_id
        self.date_debut = date_debut
        self.date_fin = date_fin
