from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from db.models.base import Base

class EPI(Base):
    __tablename__ = "epi"

    id = Column(Integer, primary_key=True)

    code_epi = Column(String(50), unique=True, nullable=False, comment="Code ou référence unique de l'EPI")
    nom = Column(String(100), nullable=False, comment="Nom de l'EPI")
    description = Column(Text, nullable=True, comment="Détails ou caractéristiques")
    categorie = Column(String(50), nullable=False, comment="Catégorie (ex: tête, mains, yeux...)")

    # Relations
    utilisateurs = relationship("EPIUtilisateur", back_populates="epi", cascade="all, delete-orphan", lazy="joined")

    def __repr__(self):
        return f"<EPI code={self.code_epi} nom={self.nom} categorie={self.categorie}>"
