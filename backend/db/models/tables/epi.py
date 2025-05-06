from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from db.models.base import Base


# ========================= EPI =========================
class EPI(Base):
    __tablename__ = "epi"

    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False, comment="Nom de l'EPI")
    description = Column(Text, nullable=True, comment="Description de l'EPI")
    categorie = Column(String(50), nullable=False, comment="Catégorie de l'EPI")

    # Relations
    utilisateurs = relationship("EPIUtilisateur", back_populates="epi")
