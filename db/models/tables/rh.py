from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Float
from sqlalchemy.orm import relationship
from db.models.base import Base
from datetime import datetime

# ========================= RH =========================
class RH(Base):
    __tablename__ = "rh"
    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    poste = Column(String(100), nullable=False)
    date_embauche = Column(DateTime, nullable=False)
    salaire = Column(Float, nullable=False)

    utilisateur = relationship("Utilisateur", back_populates="rh")

# ========================= ABSENCE =========================
class Absence(Base):
    __tablename__ = "absences"
    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    date_debut = Column(DateTime, nullable=False)
    date_fin = Column(DateTime, nullable=False)
    motif = Column(String(255), nullable=True)

    utilisateur = relationship("Utilisateur", back_populates="absences")

# ========================= FORMATION =========================
class Formation(Base):
    __tablename__ = "formations"
    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    nom = Column(String(100), nullable=False)
    date_obtention = Column(DateTime, nullable=False)
    organisme = Column(String(100), nullable=True)

    utilisateur = relationship("Utilisateur", back_populates="formations")

# ========================= SANCTION =========================
class Sanction(Base):
    __tablename__ = "sanctions"
    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    type_sanction = Column(String(50), nullable=False)  # avertissement, blâme, etc.
    date = Column(DateTime, nullable=False)
    description = Column(Text, nullable=True)

    utilisateur = relationship("Utilisateur", back_populates="sanctions")

# ========================= ENTRETIEN =========================
class Entretien(Base):
    __tablename__ = "entretiens"
    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    date = Column(DateTime, nullable=False)
    type_entretien = Column(String(50), nullable=False)  # annuel, semestriel, etc.
    commentaires = Column(Text, nullable=True)

    utilisateur = relationship("Utilisateur", back_populates="entretiens")

# ========================= NOTATION RH =========================
class NotationRH(Base):
    __tablename__ = "notations_rh"
    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    date = Column(DateTime, nullable=False)
    note = Column(Integer, nullable=False)
    commentaires = Column(Text, nullable=True)

    utilisateur = relationship("Utilisateur", back_populates="notations")

# ========================= DOCUMENT RH =========================
class DocumentRH(Base):
    __tablename__ = "documents_rh"
    id = Column(Integer, primary_key=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"))
    nom = Column(String(100), nullable=False)
    chemin_fichier = Column(String(255), nullable=False)
    date_creation = Column(DateTime, default=datetime.utcnow)

    utilisateur = relationship("Utilisateur", back_populates="documents")