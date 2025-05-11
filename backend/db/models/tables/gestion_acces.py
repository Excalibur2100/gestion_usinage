from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base

class GestionAcces(Base):
    __tablename__ = "gestion_acces"

    id = Column(Integer, primary_key=True)

    utilisateur_id = Column(
        Integer,
        ForeignKey("utilisateurs.id", ondelete="CASCADE"),
        nullable=False,
        comment="Utilisateur concerné"
    )

    niveau_acces = Column(
        String(50),
        nullable=False,
        comment="Niveau : admin, manager, lecture seule, etc."
    )

    utilisateur = relationship("Utilisateur", back_populates="gestion_acces", lazy="joined")

    def __repr__(self):
        return f"<GestionAcces utilisateur={self.utilisateur_id} niveau={self.niveau_acces}>"
