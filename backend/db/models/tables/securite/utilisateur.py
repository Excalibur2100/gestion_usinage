from sqlalchemy import Column, Integer, String, Boolean, CheckConstraint
from sqlalchemy.orm import relationship
from db.models.base import Base
import bcrypt

class Utilisateur(Base):
    __tablename__ = "utilisateurs"

    id = Column(Integer, primary_key=True)

    nom = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False, index=True)
    mot_de_passe = Column(String(255), nullable=False)
    role = Column(String(50), nullable=False, comment="admin, operateur, manager, etc.")
    actif = Column(Boolean, default=True, nullable=False)

    # Relations
    droits = relationship("Droit", back_populates="utilisateur", cascade="all, delete-orphan")
    rh = relationship("RH", back_populates="utilisateur", uselist=False, cascade="all, delete-orphan")
    absences = relationship("Absence", back_populates="utilisateur", cascade="all, delete-orphan")
    formations = relationship("Formation", back_populates="utilisateur", cascade="all, delete-orphan")
    sanctions = relationship("Sanction", back_populates="utilisateur", cascade="all, delete-orphan")
    entretiens = relationship("Entretien", back_populates="utilisateur", cascade="all, delete-orphan")
    notations = relationship("NotationRH", back_populates="utilisateur", cascade="all, delete-orphan")
    epis = relationship("EPIUtilisateur", back_populates="utilisateur", cascade="all, delete-orphan")
    affectations = relationship("AffectationMachine", back_populates="utilisateur", cascade="all, delete-orphan")
    finances = relationship("Finance", back_populates="utilisateur", cascade="all, delete-orphan")
    poste = relationship("Poste", back_populates="utilisateur", uselist=False, cascade="all, delete-orphan")
    machine = relationship("Machine", back_populates="utilisateurs", uselist=False, cascade="all, delete-orphan")
    pointages = relationship("Pointage", back_populates="utilisateur", cascade="all, delete-orphan")
    ordres = relationship("OrdreFabrication", back_populates="utilisateur", cascade="all, delete-orphan")
    plannings = relationship("PlanningEmploye", back_populates="utilisateur", cascade="all, delete-orphan")
    documents = relationship("DocumentRH", back_populates="utilisateur", cascade="all, delete-orphan")
    audits_realises = relationship("AuditQualite", back_populates="responsable_utilisateur", cascade="all, delete-orphan")
    non_conformites = relationship("NonConformite", back_populates="utilisateur", cascade="all, delete-orphan")
    filtres = relationship("GestionFiltrage", back_populates="utilisateur", cascade="all, delete-orphan")
    tracabilites = relationship("Tracabilite", back_populates="utilisateur", cascade="all, delete-orphan")
    qr_codes = relationship("QrCodeObjet", back_populates="utilisateur", cascade="all, delete-orphan")
    statistiques = relationship("StatProduction", back_populates="utilisateur", cascade="all, delete-orphan")
    statistiques_rh = relationship("StatRH", back_populates="utilisateur", cascade="all, delete-orphan")

    # Méthodes de sécurité
    def set_password(self, plain_password: str):
        hashed = bcrypt.hashpw(plain_password.encode("utf-8"), bcrypt.gensalt())
        self.mot_de_passe = hashed.decode("utf-8")

    def check_password(self, plain_password: str) -> bool:
        return bcrypt.checkpw(plain_password.encode("utf-8"), self.mot_de_passe.encode("utf-8"))

    def get_email(self) -> str:
        return self.email

    def __repr__(self):
        return f"<Utilisateur {self.nom} ({self.role})>"

    __table_args__ = (
        CheckConstraint("role IN ('admin', 'operateur', 'manager', 'rh')", name="check_role_utilisateur"),
    )
