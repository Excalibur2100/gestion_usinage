from sqlalchemy import Column, Integer, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from db.models.base import Base

class DroitAcces(Base):
    __tablename__ = "droits_acces"

    id = Column(Integer, primary_key=True)

    utilisateur_id = Column(
        Integer,
        ForeignKey("utilisateurs.id", ondelete="CASCADE"),
        nullable=False,
        comment="Utilisateur concerné par le droit"
    )
    droit_id = Column(
        Integer,
        ForeignKey("droits.id", ondelete="CASCADE"),
        nullable=False,
        comment="Droit attribué"
    )

    utilisateur = relationship("Utilisateur", back_populates="droits_acces", lazy="joined")
    droit = relationship("Droit", back_populates="droits_acces", lazy="joined")

    __table_args__ = (
        UniqueConstraint('utilisateur_id', 'droit_id', name='uq_utilisateur_droit'),
    )

    def __repr__(self):
        return f"<DroitAcces utilisateur={self.utilisateur_id} droit={self.droit_id}>"
