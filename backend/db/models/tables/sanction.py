from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from db.models.base import Base

class Sanction(Base):
    __tablename__ = "sanctions"

    id = Column(Integer, primary_key=True)

    utilisateur_id = Column(
        Integer,
        ForeignKey("utilisateurs.id", ondelete="CASCADE"),
        nullable=False,
        comment="ID de l'utilisateur sanctionné"
    )

    type_sanction = Column(String(150), nullable=False, comment="Type : avertissement, blâme, exclusion...")
    date = Column(DateTime, nullable=False, comment="Date d'application de la sanction")
    motif = Column(Text, nullable=False, comment="Motif détaillé de la sanction")

    utilisateur = relationship("Utilisateur", back_populates="sanctions", lazy="joined")

    def __repr__(self):
        return f"<Sanction utilisateur={self.utilisateur_id} type='{self.type_sanction}' date={self.date}>"
