from sqlalchemy import Column, Integer, String, ForeignKey, Text, CheckConstraint
from sqlalchemy.orm import relationship
from db.models.base import Base

class Poste(Base):
    __tablename__ = "postes"

    id = Column(Integer, primary_key=True, index=True)

    nom = Column(String(100), nullable=False, unique=True, comment="Nom du poste (ex: Usinage CN1)")
    type_poste = Column(String(50), nullable=False, comment="Usinage, assemblage, contrôle...")
    emplacement = Column(String(100), nullable=True, comment="Emplacement dans l'atelier")
    statut = Column(String(50), default="actif", nullable=False, comment="Statut du poste")
    description = Column(Text, nullable=True, comment="Remarques complémentaires")

    machine_id = Column(Integer, ForeignKey("machines.id", ondelete="SET NULL"), nullable=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id", ondelete="SET NULL"), nullable=True)

    machine = relationship("Machine", back_populates="postes", lazy="joined")
    utilisateur = relationship("Utilisateur", back_populates="poste", lazy="joined")
    ordres = relationship("OrdreFabrication", back_populates="poste", cascade="all, delete-orphan", lazy="joined")

    __table_args__ = (
        CheckConstraint("statut IN ('actif', 'inactif', 'en panne')", name="check_statut_poste"),
    )

    def __repr__(self):
        return f"<Poste nom='{self.nom}' type='{self.type_poste}' statut={self.statut}>"
