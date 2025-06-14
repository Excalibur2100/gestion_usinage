from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from db.models.base import Base

class TypeFournisseur(Base):
    __tablename__ = "types_fournisseur"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)
    nom = Column(String(100), unique=True, nullable=False, comment="Ex: matière, prestation, outillage")
    description = Column(String(255), nullable=True)

    fournisseurs = relationship("Fournisseur", back_populates="type_fournisseur")

    def __repr__(self):
        return f"<TypeFournisseur(nom='{self.nom}')>"
