from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean
)
from sqlalchemy.orm import relationship
from db.models.base import Base
import bcrypt


# ========================= UTILISATEUR =========================
class Utilisateur(Base):
    __tablename__ = "utilisateurs"
    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False, index=True)
    mot_de_passe = Column(String(255), nullable=False)
    role = Column(String(50), nullable=False)
    actif = Column(Boolean, default=True, nullable=False)

    # Relations
    droits = relationship("Droit", back_populates="utilisateur")
    rh = relationship("RH", back_populates="utilisateur", uselist=False)
    absences = relationship("Absence", back_populates="utilisateur")
    formations = relationship("Formation", back_populates="utilisateur")
    sanctions = relationship("Sanction", back_populates="utilisateur")
    entretiens = relationship("Entretien", back_populates="utilisateur")
    notations = relationship("NotationRH", back_populates="utilisateur")
    epis = relationship("EPIUtilisateur", back_populates="utilisateur")
    affectations = relationship("AffectationMachine", back_populates="utilisateur")
    finances = relationship("Finance", back_populates="utilisateur")
    documents = relationship("DocumentRH", back_populates="utilisateur")
    audits_realises = relationship(
        "AuditQualite", back_populates="responsable_utilisateur"
    )
    non_conformites = relationship("NonConformite", back_populates="utilisateur")
    filtres = relationship("GestionFiltrage", back_populates="utilisateur")

    # Méthodes de sécurité
    def set_password(self, plain_password: str):
        hashed = bcrypt.hashpw(plain_password.encode("utf-8"), bcrypt.gensalt())
        self.mot_de_passe = hashed.decode("utf-8")

    def check_password(self, plain_password: str) -> bool:
        return bcrypt.checkpw(
            plain_password.encode("utf-8"), self.mot_de_passe.encode("utf-8")
        )  

    def get_email(self) -> str:
        return self.email
    
