from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db.models.base import Base

class HistoriqueChiffrage(Base):
    __tablename__ = "historiques_chiffrage"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)

    chiffrage_id = Column(Integer, ForeignKey("chiffrages.id", ondelete="CASCADE"), nullable=False)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="SET NULL"), nullable=True)

    version = Column(String(50), nullable=False)
    commentaire = Column(Text, nullable=True)

    duree_estimee = Column(Float, nullable=False)
    cout_estime = Column(Float, nullable=False)
    taux_marge = Column(Float, default=0.0)

    date_version = Column(DateTime(timezone=True), server_default=func.now())

    chiffrage = relationship("Chiffrage", back_populates="historiques")
    utilisateur = relationship("Utilisateur", back_populates="historiques_chiffrage")

    def __repr__(self):
        return f"<HistoriqueChiffrage(chiffrage={self.chiffrage_id}, version='{self.version}')>"