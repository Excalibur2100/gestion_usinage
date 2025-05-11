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

    temperature = Column(Float, nullable=True, comment="Température mesurée pendant la charge")
    vibration = Column(Float, nullable=True, comment="Vibration mesurée pendant la charge")
    commentaire = Column(Text, nullable=True, comment="Remarque opérateur ou responsable")

    machine = relationship("Machine", back_populates="charges", lazy="joined")
    gamme = relationship("GammeProduction", back_populates="charges", lazy="joined")

    def __repr__(self):
        return f"<ChargeMachine machine={self.machine_id} {self.date_debut} → {self.date_fin}>"
