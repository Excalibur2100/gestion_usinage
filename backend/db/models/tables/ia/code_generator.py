from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from db.models.base import Base

class CodeGenerator(Base):
    __tablename__ = "code_generator"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True)

    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="SET NULL"), nullable=True)
    entreprise_id = Column(Integer, ForeignKey("entreprises.id", ondelete="SET NULL"), nullable=True)

    nom_session = Column(String(100), nullable=False)
    langage = Column(String(50), nullable=False, default="python")
    prompt = Column(Text, nullable=False)
    code_genere = Column(Text, nullable=True)
    version_modele = Column(String(50), default="gpt-4")
    date_generation = Column(DateTime(timezone=True), server_default=func.now())

    utilisateur = relationship("Utilisateur", back_populates="code_generations")
    entreprise = relationship("Entreprise", back_populates="code_generations")

    def __repr__(self):
        return f"<CodeGenerator(session='{self.nom_session}', langage='{self.langage}')>"