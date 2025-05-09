from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from db.models.database import Base

class Poste(Base):
    __tablename__ = "postes"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String(100), nullable=False, unique=True, comment="Nom du poste de travail")
    type_poste = Column(String(50), nullable=False, comment="Type : usinage, assemblage, contrôle...")
    emplacement = Column(String(100), nullable=True, comment="Localisation physique dans l’atelier")
    statut = Column(String(50), default="actif", comment="Statut du poste : actif, en panne, inactif")
    description = Column(Text, nullable=True, comment="Description complémentaire")

    machine_id = Column(Integer, ForeignKey("machines.id"), nullable=True)
    utilisateur_id = Column(Integer, ForeignKey("utilisateurs.id"), nullable=True)

    machine = relationship("Machine", back_populates="postes", lazy="joined")
    utilisateur = relationship("Utilisateur", back_populates="poste", lazy="joined")
    ordres = relationship("OrdreFabrication", back_populates="poste", cascade="all, delete")
    


    def __repr__(self):
        return f"<Poste nom={self.nom} type={self.type_poste}>"
