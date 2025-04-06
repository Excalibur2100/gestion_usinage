from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime
import bcrypt

# ========================= UTILISATEUR =========================
class Utilisateur(Base):
    __tablename__ = 'utilisateurs'
    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
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
    audits_realises = relationship("AuditQualite", back_populates="responsable_utilisateur")
    non_conformites = relationship("NonConformite", back_populates="utilisateur")
    filtres = relationship("GestionFiltrage", back_populates="utilisateur")

    # Méthodes de sécurité
    def set_password(self, plain_password: str):
        hashed = bcrypt.hashpw(plain_password.encode('utf-8'), bcrypt.gensalt())
        self.mot_de_passe = hashed.decode('utf-8')

    def check_password(self, plain_password: str) -> bool:
        return bcrypt.checkpw(plain_password.encode('utf-8'), self.mot_de_passe.encode('utf-8'))

# ========================= DROIT =========================
class Droit(Base):
    __tablename__ = "droits"
    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    module = Column(String(100))
    autorisation = Column(Boolean, default=False)

    utilisateur = relationship("Utilisateur", back_populates="droits")

# ========================= DROIT DACCES =========================
class DroitAcces(Base):
    __tablename__ = "droits_acces"
    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    module = Column(String(100))  # Ex: 'devis', 'production', 'finance', etc.
    peut_lire = Column(Boolean, default=False)
    peut_creer = Column(Boolean, default=False)
    peut_modifier = Column(Boolean, default=False)
    peut_supprimer = Column(Boolean, default=False)
    acces_total = Column(Boolean, default=False)

    utilisateur = relationship("Utilisateur", backref="droits_acces")

# ========================= GESTION ACCES UTILISATEURS =========================
class GestionAcces(Base):
    __tablename__ = "gestion_acces"
    id = Column(Integer, primary_key=True)

# ========================= HISTORIQUE DACTION =========================
class HistoriqueAction(Base):
    __tablename__ = "historique_actions"
    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    action = Column(String(255), nullable=False)
    date_action = Column(DateTime, default=datetime.utcnow)

    utilisateur = relationship("Utilisateur", backref="historique_actions")